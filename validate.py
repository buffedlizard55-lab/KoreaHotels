#!/usr/bin/env python3
"""
validate.py — Data quality checker for Korea-hotels

Checks hotels.json, its arrival-night shortlist, and itinerary.json for required fields and common issues.
Run with: python3 validate.py
"""

import json
import sys

HOTELS_FILE = "data/hotels.json"
ITINERARY_FILE = "data/itinerary.json"

REQUIRED_HOTEL_FIELDS = [
    "id", "city", "name", "tier", "stars", "area", "neighborhood",
    "priceFrom", "priceTo", "currency", "checkIn", "checkOut",
    "policies", "rooms", "promos", "amenities", "hasOnSiteLaundry",
    "officialLabel", "compareUrl", "compareLabel", "why", "highlights",
    "fits", "fitReason", "lat", "lng"
]

REQUIRED_ROOM_FIELDS = [
    "name", "price", "note", "bed", "bedType", "bedSize",
    "oneBed", "oneBedOnly", "privateBathroom", "bedNote"
]

# The arrival-night block is intentionally strict: it is the only shortlist
# that makes a 24-hour-reception claim, so every candidate needs an auditable
# source link and a direct-booking link.
REQUIRED_ARRIVAL_FIELDS = [
    "title", "airport", "arrivalTime", "arrivalCity", "firstNightOnly",
    "lastVerified", "requirement", "definition", "recommendedId",
    "decision", "steps", "candidates"
]
REQUIRED_ARRIVAL_CANDIDATE_FIELDS = [
    "id", "rank", "label", "location", "tier", "checkIn", "checkOut",
    "frontDesk", "room", "privateBathroom", "station", "estimatedRate",
    "why", "tradeoff", "bookingNote", "officialUrl", "evidenceUrl",
    "evidenceLabel", "evidenceQuote"
]

def load_json(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Failed to load {path}: {e}")
        sys.exit(1)

def room_meets_queen_or_king_requirement(room):
    return (
        room.get("oneBedOnly") is True
        and room.get("privateBathroom") is True
        and str(room.get("bedType", "")).lower() in {"queen", "king"}
    )


def validate_hotels(data):
    print("=== Validating hotels.json ===")
    hotels = data.get("hotels", [])
    print(f"Total hotels: {len(hotels)}")

    errors = 0
    warnings = 0

    for h in hotels:
        # Check required fields
        for field in REQUIRED_HOTEL_FIELDS:
            if field not in h:
                print(f"  ❌ Missing field '{field}' in {h.get('name', h.get('id'))}")
                errors += 1

        # Check rooms
        for room in h.get("rooms", []):
            for rfield in REQUIRED_ROOM_FIELDS:
                if rfield not in room:
                    print(f"  ❌ Missing room field '{rfield}' in {h['name']}")
                    errors += 1

        # A green core-needs match has a stricter meaning than merely one bed:
        # it must have a private-bath queen or king room, not a 140cm double.
        if h.get("fits") and not any(room_meets_queen_or_king_requirement(room) for room in h.get("rooms", [])):
            print(f"  ❌ {h.get('name', h.get('id'))} is marked fits=true but has no private-bath queen/king room")
            errors += 1

        # Check officialUrl
        if not h.get("officialUrl"):
            print(f"  ⚠️  No officialUrl for {h['name']} (city: {h['city']})")
            warnings += 1

        # Check hasOnSiteLaundry
        if "hasOnSiteLaundry" not in h:
            print(f"  ❌ Missing hasOnSiteLaundry in {h['name']}")
            errors += 1

    if errors == 0:
        print("✅ No critical errors in hotels.json")
    else:
        print(f"❌ Found {errors} critical errors")

    if warnings > 0:
        print(f"⚠️  {warnings} warnings (mostly missing officialUrl)")

    return errors


def valid_http_url(value):
    return isinstance(value, str) and value.startswith(("https://", "http://"))


def validate_arrival_night(data):
    print("\n=== Validating arrival-night shortlist ===")
    arrival = data.get("arrivalNight")
    if not isinstance(arrival, dict):
        print("❌ Missing 'arrivalNight' in hotels.json")
        return 1

    errors = 0
    for field in REQUIRED_ARRIVAL_FIELDS:
        if field not in arrival:
            print(f"  ❌ Missing arrival-night field '{field}'")
            errors += 1

    candidates = arrival.get("candidates", [])
    if not candidates:
        print("  ❌ Arrival-night shortlist has no candidates")
        errors += 1
        return errors

    ids = set()
    hotel_ids = {hotel.get("id") for hotel in data.get("hotels", [])}
    for candidate in candidates:
        name = candidate.get("id", "unnamed arrival candidate")
        for field in REQUIRED_ARRIVAL_CANDIDATE_FIELDS:
            if field not in candidate:
                print(f"  ❌ Missing arrival candidate field '{field}' in {name}")
                errors += 1

        if candidate.get("id") in ids:
            print(f"  ❌ Duplicate arrival candidate id '{candidate.get('id')}'")
            errors += 1
        ids.add(candidate.get("id"))

        for url_field in ("officialUrl", "evidenceUrl"):
            if url_field in candidate and not valid_http_url(candidate[url_field]):
                print(f"  ❌ Invalid {url_field} in {name}")
                errors += 1

        if candidate.get("hotelId") is not None and candidate.get("hotelId") not in hotel_ids:
            print(f"  ❌ hotelId '{candidate.get('hotelId')}' in {name} is not in hotels[]")
            errors += 1

        if "24" not in str(candidate.get("frontDesk", "")) and "anytime" not in str(candidate.get("frontDesk", "")).lower():
            print(f"  ❌ {name} does not state a 24-hour/front-desk signal")
            errors += 1

    if arrival.get("recommendedId") not in ids:
        print("  ❌ recommendedId does not point to an arrival-night candidate")
        errors += 1

    if errors == 0:
        print(f"✅ {len(candidates)} arrival-night candidates have booking + evidence links")
    else:
        print(f"❌ Found {errors} arrival-night shortlist issues")
    return errors


def validate_itinerary(data):
    print("\n=== Validating itinerary.json ===")
    if "legs" not in data:
        print("❌ Missing 'legs' in itinerary.json")
        return 1

    print(f"Legs: {len(data['legs'])}")
    print("✅ itinerary.json looks valid")
    return 0

def main():
    print("🔍 Running Korea-hotels data validator...\n")

    hotels_data = load_json(HOTELS_FILE)
    itinerary_data = load_json(ITINERARY_FILE)

    hotel_errors = validate_hotels(hotels_data)
    arrival_errors = validate_arrival_night(hotels_data)
    itinerary_errors = validate_itinerary(itinerary_data)

    total_errors = hotel_errors + arrival_errors + itinerary_errors

    print("\n=== Summary ===")
    if total_errors == 0:
        print("✅ All checks passed!")
    else:
        print(f"❌ {total_errors} issues found")

    sys.exit(total_errors)

if __name__ == "__main__":
    main()
