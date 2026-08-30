#!/usr/bin/env python3
"""
validate.py — Data quality checker for Korea-hotels

Checks hotels.json, its arrival-night shortlist, and itinerary.json for required fields and common issues.
Run with: python3 validate.py
"""

import difflib
import json
import re
import sys
import unicodedata
from collections import defaultdict

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

REQUIRED_VERIFICATION_FIELDS = [
    "lastChecked", "sourceType", "sourceUrl", "canonicalName",
    "existenceStatus", "note"
]

MIN_PRIMARY_CITY_HOTELS = {
    "Seoul": 20,
    "Gyeongju": 15,
    "Busan": 20,
}

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
    "evidenceType", "evidenceLabel", "evidenceQuote"
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


SECONDARY_PLATFORM = "Agoda"
SECONDARY_STATUSES = {"verified", "not-found", "unresolved"}
SECONDARY_CHECK_METHODS = {"property-page-fetched", "search-index"}
RATE_FIELDS = ("refundableRate", "refundableRateNov9", "refundableRateNov15")


def validate_secondary_source(hotel, agoda_urls):
    """Every record must state its secondary verified source (Agoda) outcome.

    A verified Agoda link needs a unique agoda.com URL and a recorded check date
    and method; a record without a listing must say so explicitly so a blank can
    never be misread as "not yet checked".
    """
    errors = 0
    name = hotel.get("name", hotel.get("id"))
    secondary = hotel.get("secondarySource")
    if not isinstance(secondary, dict):
        print(f"  ❌ Missing secondarySource (Agoda) block in {name}")
        return 1
    if secondary.get("platform") != SECONDARY_PLATFORM:
        print(f"  ❌ secondarySource.platform must be '{SECONDARY_PLATFORM}' in {name}")
        errors += 1
    status = secondary.get("status")
    if status not in SECONDARY_STATUSES:
        print(f"  ❌ secondarySource.status '{status}' in {name} must be one of {sorted(SECONDARY_STATUSES)}")
        errors += 1
    if not secondary.get("note"):
        print(f"  ❌ secondarySource in {name} needs a note describing what was checked")
        errors += 1
    if not secondary.get("lastCheckedUtc"):
        print(f"  ❌ secondarySource in {name} needs a lastCheckedUtc date")
        errors += 1
    url = secondary.get("url")
    if status == "verified":
        if not isinstance(url, str) or not url.startswith("https://www.agoda.com/"):
            print(f"  ❌ Verified secondarySource in {name} needs an https://www.agoda.com/ URL")
            errors += 1
        else:
            key = url.strip().rstrip("/").lower()
            if key in agoda_urls:
                print(f"  ❌ Same Agoda URL used by {name} and {agoda_urls[key]} — duplicate identity")
                errors += 1
            agoda_urls[key] = name
        if secondary.get("checkMethod") not in SECONDARY_CHECK_METHODS:
            print(f"  ❌ secondarySource.checkMethod in {name} must be one of {sorted(SECONDARY_CHECK_METHODS)}")
            errors += 1
    elif url:
        print(f"  ❌ secondarySource.status '{status}' in {name} must not carry a URL")
        errors += 1
    if status in ("not-found", "unresolved") and not secondary.get("lastCheckedUtc"):
        print(f"  ❌ secondarySource '{status}' in {name} needs a date showing the blank is current")
        errors += 1
    return errors


def validate_rate_source_labels(hotel):
    """Rate rows and comparison links must state which site they belong to."""
    errors = 0
    name = hotel.get("name", hotel.get("id"))
    for field in RATE_FIELDS:
        rate = hotel.get(field)
        if not isinstance(rate, dict):
            continue
        source = str(rate.get("source", ""))
        if "Booking" not in source and "Agoda" not in source:
            print(f"  ❌ {name}.{field}: 'source' must name the platform (Booking.com or Agoda)")
            errors += 1
    if hotel.get("compareLabel") and hotel.get("compareUrl"):
        host = hotel["compareUrl"].split("/")[2].lower() if "://" in hotel["compareUrl"] else ""
        known = next((site for site in ("kayak", "google", "booking", "agoda", "trip") if site in host), None)
        if known and known not in hotel["compareLabel"].lower():
            print(f"  ❌ {name}: compareLabel '{hotel['compareLabel']}' does not name the site in compareUrl")
            errors += 1
    return errors


def normalize_identity_name(value):
    """Normalize a sourced hotel name for exact/fuzzy duplicate checks."""
    ascii_name = unicodedata.normalize("NFKD", str(value)).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "", ascii_name)


def canonical_url(value):
    """Normalize source URLs enough to catch the same property link twice."""
    return str(value or "").strip().rstrip("/").lower()


def validate_hotels(data):
    print("=== Validating hotels.json ===")
    hotels = data.get("hotels", [])
    print(f"Total hotels: {len(hotels)}")

    errors = 0
    verified = 0
    ids = set()
    canonical_names = defaultdict(list)
    official_urls = defaultdict(list)
    source_urls = defaultdict(list)
    coordinates = defaultdict(list)
    agoda_urls = {}

    for h in hotels:
        # Check required fields and stable unique IDs.
        for field in REQUIRED_HOTEL_FIELDS:
            if field not in h:
                print(f"  ❌ Missing field '{field}' in {h.get('name', h.get('id'))}")
                errors += 1

        if h.get("id") in ids:
            print(f"  ❌ Duplicate hotel id '{h.get('id')}'")
            errors += 1
        ids.add(h.get("id"))

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

        # An official property URL is preferred, but some independent hotels
        # have only a government-tourism or major-platform identity source.
        if h.get("officialUrl"):
            if not isinstance(h.get("officialUrl"), str) or not h["officialUrl"].startswith(("https://", "http://")):
                print(f"  ❌ Invalid officialUrl in {h['name']}")
                errors += 1
            else:
                official_urls[canonical_url(h["officialUrl"])].append(h["id"])

        # Check hasOnSiteLaundry
        if "hasOnSiteLaundry" not in h:
            print(f"  ❌ Missing hasOnSiteLaundry in {h['name']}")
            errors += 1

        # Every record must identify a real operating property through one
        # dated official, government-tourism, or major trusted source.
        verification = h.get("verification")
        if not isinstance(verification, dict):
            print(f"  ❌ Missing/invalid verification block in {h['name']}")
            errors += 1
        else:
            verified += 1
            for field in REQUIRED_VERIFICATION_FIELDS:
                if not verification.get(field):
                    print(f"  ❌ Missing verification field '{field}' in {h['name']}")
                    errors += 1

            source_url = verification.get("sourceUrl", "")
            if not isinstance(source_url, str) or not source_url.startswith(("https://", "http://")):
                print(f"  ❌ Invalid verification sourceUrl in {h['name']}")
                errors += 1
            else:
                source_urls[canonical_url(source_url)].append(h["id"])

            if verification.get("existenceStatus") != "Verified operating property":
                print(f"  ❌ Unverified existenceStatus in {h['name']}")
                errors += 1

            canonical_name = normalize_identity_name(verification.get("canonicalName", ""))
            if canonical_name:
                canonical_names[(h.get("city"), canonical_name)].append(h["id"])

        if isinstance(h.get("lat"), (int, float)) and isinstance(h.get("lng"), (int, float)):
            coordinates[(round(h["lat"], 6), round(h["lng"], 6))].append(h["id"])

        errors += validate_secondary_source(h, agoda_urls)
        errors += validate_rate_source_labels(h)

    # Identity-level duplicate detection: IDs alone are not enough because a
    # duplicate property could be entered under a new slug or spelling.
    for (city, canonical_name), matching_ids in canonical_names.items():
        if len(matching_ids) > 1:
            print(f"  ❌ Duplicate canonical hotel name in {city}: {matching_ids}")
            errors += 1

    for label, mapping in (("official URL", official_urls), ("verification source URL", source_urls)):
        for url, matching_ids in mapping.items():
            if len(matching_ids) > 1:
                print(f"  ❌ Duplicate {label} used by {matching_ids}: {url}")
                errors += 1

    for coordinate, matching_ids in coordinates.items():
        if len(matching_ids) > 1:
            print(f"  ❌ Exact duplicate coordinates {coordinate} used by {matching_ids}")
            errors += 1

    for index, first in enumerate(hotels):
        first_verification = first.get("verification") or {}
        first_name = normalize_identity_name(first_verification.get("canonicalName", first.get("name", "")))
        for second in hotels[index + 1:]:
            if first.get("city") != second.get("city"):
                continue
            second_verification = second.get("verification") or {}
            second_name = normalize_identity_name(second_verification.get("canonicalName", second.get("name", "")))
            similarity = difflib.SequenceMatcher(None, first_name, second_name).ratio()
            if similarity < 0.92:
                continue
            first_exceptions = set(first_verification.get("distinctFrom", []))
            second_exceptions = set(second_verification.get("distinctFrom", []))
            if second.get("id") not in first_exceptions or first.get("id") not in second_exceptions:
                print(f"  ❌ Possible fuzzy duplicate ({similarity:.0%}): {first['id']} / {second['id']}")
                errors += 1

    city_counts = {city: sum(h.get("city") == city for h in hotels) for city in MIN_PRIMARY_CITY_HOTELS}
    for city, minimum in MIN_PRIMARY_CITY_HOTELS.items():
        if city_counts[city] < minimum:
            print(f"  ❌ {city} has {city_counts[city]} hotels; expanded-list minimum is {minimum}")
            errors += 1

    print(f"Verified identities: {verified}/{len(hotels)}; planned-city coverage: " + ", ".join(f"{city} {count}" for city, count in city_counts.items()))

    secondary_verified = sum(1 for h in hotels if (h.get("secondarySource") or {}).get("status") == "verified")
    secondary_not_found = sum(1 for h in hotels if (h.get("secondarySource") or {}).get("status") == "not-found")
    print(f"Secondary source (Agoda): {secondary_verified} verified links, {secondary_not_found} explicit not-found")

    if errors == 0:
        print(f"✅ {len(hotels)} unique, source-verified hotel records; no duplicate IDs, names, URLs, or coordinates")
    else:
        print(f"❌ Found {errors} critical errors")

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
    ranks = set()
    hotel_ids = {hotel.get("id") for hotel in data.get("hotels", [])}
    allowed_evidence_types = {"Official hotel/brand page", "Government tourism authority", "Major trusted booking platform", "Official hotel/brand + major trusted booking platform"}
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

        if candidate.get("rank") in ranks:
            print(f"  ❌ Duplicate arrival candidate rank '{candidate.get('rank')}'")
            errors += 1
        ranks.add(candidate.get("rank"))

        if candidate.get("evidenceType") not in allowed_evidence_types:
            print(f"  ❌ Unrecognized evidenceType in {name}")
            errors += 1

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
    else:
        recommended = next(candidate for candidate in candidates if candidate.get("id") == arrival.get("recommendedId"))
        if recommended.get("evidenceType") != "Official hotel/brand page":
            print("  ❌ Recommended arrival hotel must use direct official hotel/brand evidence")
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
