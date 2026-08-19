#!/usr/bin/env python3
"""Derive display-only findings from hotels.json. No invented prices."""

from __future__ import annotations

import re
from typing import Any


CITY_ORDER = ["Seoul", "Gyeongju", "Busan", "Cheonan", "Daejeon", "Suwon"]

PLANNED = {"Seoul", "Gyeongju", "Busan"}


def _rr(hotel: dict) -> dict:
    return hotel.get("refundableRate") or {}


def _text(*parts: Any) -> str:
    return " ".join(str(part or "") for part in parts)


def bed_class_for_rate(rr: dict) -> str:
    """Classify one captured rate row only — never the hotel room catalog."""
    beds = str(rr.get("beds") or "")
    room = str(rr.get("room") or "")
    # Classify the captured row only. Do not read `note` — it often mentions other rooms.
    blob = f"{beds} {room}".lower()

    if re.search(r"\bor\b.*\btwin\b|\btwin\b.*\bor\b", blob) and "full bed or" in blob:
        return "mixed"
    if any(
        token in blob
        for token in (
            "2 beds",
            "2 full",
            "2 twin",
            "2 queen",
            "4 futon",
            "futon beds",
            "+ 2 futon",
            "+ 1 twin",
            "+ 1 full",
            "1 twin +",
            "1 king bed +",
            "1 queen bed +",
        )
    ):
        return "multi"
    if "hollywood" in blob:
        return "hollywood"
    if "booking label" in blob and "unpublished" in blob:
        return "queen_unconfirmed"
    if re.search(r"1[,\s]?600|160\s*[×x]\s*190|1600\s*[×x]", beds):
        return "queen"
    head = beds.split("—")[0].split("/")[0]
    if re.search(r"\b1\s+king\b", head, re.I) and "+" not in head:
        return "king"
    if re.search(r"\b1\s+queen\b", beds, re.I) and "+" not in beds.split("—")[0]:
        return "queen"
    if re.search(r"\b1\s+(full|double)\b", beds, re.I) and "+" not in beds.split("—")[0]:
        return "full"
    if re.search(r"1\s+x\s+king", beds, re.I):
        return "king"
    if re.search(r"1\s+x\s+queen", beds, re.I):
        return "queen"
    if re.search(r"1\s+x\s+double", beds, re.I):
        return "full"
    return "unknown"


def bed_class(hotel: dict) -> str:
    """Backward-compatible primary-window classification."""
    return bed_class_for_rate(_rr(hotel))


def has_live_rate(rr: dict) -> bool:
    return bool(
        rr.get("available") is True
        and isinstance(rr.get("pricePerNight"), (int, float))
        and isinstance(rr.get("totalStay"), (int, float))
        and rr.get("capturedAtUtc")
    )


def has_live_quote(hotel: dict) -> bool:
    return has_live_rate(_rr(hotel))


def is_one_bed(kind: str) -> bool:
    return kind in {"king", "queen", "full", "queen_unconfirmed"}


def is_confirmed_queen_king(kind: str) -> bool:
    return kind in {"king", "queen"}


def quote_row(hotel: dict, rate: dict | None = None, window_key: str = "nov1") -> dict[str, Any]:
    rr = rate if isinstance(rate, dict) else _rr(hotel)
    kind = bed_class_for_rate(rr)
    window = {
        "nov1": "Nov 1–9, 2026 (8 nights)",
        "nov15": "Nov 15–22, 2026 (7 nights)",
    }.get(window_key, "Captured stay window")
    return {
        "id": hotel.get("id"),
        "name": hotel.get("name"),
        "city": hotel.get("city"),
        "area": hotel.get("area") or "",
        "neighborhood": hotel.get("neighborhood") or "",
        "fits": bool(hotel.get("fits")),
        "room": rr.get("room"),
        "beds": rr.get("beds"),
        "bedClass": kind,
        "pricePerNight": rr.get("pricePerNight") if has_live_rate(rr) else None,
        "totalStay": rr.get("totalStay") if has_live_rate(rr) else None,
        "nights": rr.get("nights"),
        "stayCheckIn": rr.get("stayCheckIn"),
        "stayCheckOut": rr.get("stayCheckOut"),
        "freeCancellation": rr.get("freeCancellation"),
        "breakfastIncluded": bool(rr.get("breakfastIncluded")),
        "sourceUrl": rr.get("sourceUrl") or hotel.get("officialUrl"),
        "officialUrl": hotel.get("officialUrl"),
        "capturedAtUtc": rr.get("capturedAtUtc"),
        "available": rr.get("available"),
        "finding": rr.get("finding"),
        "note": rr.get("note"),
        "fitReason": hotel.get("fitReason"),
        "windowKey": window_key,
        "windowLabel": window,
    }


def _cheapest(rows: list[dict], predicate) -> dict | None:
    eligible = [
        row
        for row in rows
        if predicate(row) and isinstance(row.get("totalStay"), (int, float))
    ]
    if not eligible:
        return None
    return min(eligible, key=lambda row: (row["totalStay"], row.get("pricePerNight") or 0))


def _flag_rows(hotels: list[dict]) -> list[dict]:
    flags = []
    for hotel in hotels:
        rr = _rr(hotel)
        kind = bed_class(hotel)
        city = hotel.get("city")
        name = hotel.get("name")
        if rr.get("available") and not rr.get("capturedAtUtc"):
            flags.append(
                {
                    "city": city,
                    "name": name,
                    "text": "Stored price has no UTC capture — not treated as a live quote on this page.",
                }
            )
        if kind == "hollywood":
            flags.append(
                {
                    "city": city,
                    "name": name,
                    "text": "Captured row is a Hollywood / joined-mattress room.",
                }
            )
        if kind == "queen_unconfirmed":
            flags.append(
                {
                    "city": city,
                    "name": name,
                    "text": "Booking says queen; official millimetres unpublished.",
                }
            )
        beds = str(rr.get("beds") or "")
        if "despite" in beds.lower():
            flags.append(
                {
                    "city": city,
                    "name": name,
                    "text": f"Name/size mismatch on the captured row: {beds}",
                }
            )
        note = str(rr.get("note") or "").lower()
        cancel = str(rr.get("freeCancellation") or "")
        if "pet hotel" in note or "pet-focused" in note:
            flags.append({"city": city, "name": name, "text": "Pet hotel."})
        if "adults-only" in note or "adults only" in note:
            flags.append({"city": city, "name": name, "text": "Adults-only rooms."})
        if "TOTAL" in cancel or "total stay" in cancel.lower() or "total price" in cancel.lower():
            flags.append(
                {
                    "city": city,
                    "name": name,
                    "text": "Inside the free-cancel window the fee can be the total stay.",
                }
            )
        if hotel.get("id") == "cheonan-brown-dot":
            flags.append(
                {
                    "city": city,
                    "name": name,
                    "text": "No Booking.com Dongnam page. Do not use Brown Dot Buldang prices.",
                }
            )
        if hotel.get("id") == "suwon-novotel-ambassador":
            flags.append(
                {
                    "city": city,
                    "name": name,
                    "text": "Only Suwon core-needs match. Booking sold out Nov 1–9 — book Accor.",
                }
            )
    # de-dupe exact lines
    seen = set()
    unique = []
    for flag in flags:
        key = (flag["city"], flag["name"], flag["text"])
        if key in seen:
            continue
        seen.add(key)
        unique.append(flag)
    return unique


def build_findings(hotels_data: dict, itinerary: dict) -> dict:
    hotels = hotels_data.get("hotels") or []
    # Primary-city statistics retain the itinerary's original window. Seoul's
    # alternate window is deliberately added only to the quote display below,
    # never combined with Nov 1–9 totals or recommendations.
    rows = [quote_row(hotel) for hotel in hotels]
    live_rows = [row for row in rows if row["pricePerNight"] is not None]
    quote_rows = list(live_rows)
    quote_rows.extend(
        quote_row(hotel, hotel.get("refundableRateNov15"), "nov15")
        for hotel in hotels
        if hotel.get("city") == "Seoul" and isinstance(hotel.get("refundableRateNov15"), dict)
        and has_live_rate(hotel.get("refundableRateNov15"))
    )
    unsourced = [
        hotel
        for hotel in hotels
        if (_rr(hotel).get("available") is True and not _rr(hotel).get("capturedAtUtc"))
    ]

    captures = [
        str(_rr(hotel).get("capturedAtUtc"))
        for hotel in hotels
        if _rr(hotel).get("capturedAtUtc")
    ]
    last_capture = max(captures) if captures else None

    legs = {leg["city"]: leg for leg in (itinerary.get("legs") or [])}
    alts = {leg["city"]: leg for leg in (itinerary.get("alternatives") or [])}

    cities = []
    for city in CITY_ORDER:
        subset = [row for row in rows if row["city"] == city]
        live = [row for row in subset if row["pricePerNight"] is not None]
        info = legs.get(city) or alts.get(city) or {}
        cities.append(
            {
                "city": city,
                "role": "Planned stop" if city in PLANNED else "Alternative stop",
                "dates": info.get("dates"),
                "nights": info.get("nights"),
                "hotels": len(subset),
                "coreMatches": sum(1 for row in subset if row["fits"]),
                "liveQuotes": len(live),
                "soldOut": sum(1 for row in subset if row.get("available") is False),
                "cheapestOneBed": _cheapest(live, lambda row: is_one_bed(row["bedClass"])),
                "cheapestQueenKing": _cheapest(
                    live, lambda row: is_confirmed_queen_king(row["bedClass"])
                ),
                "cheapestCoreQueenKing": _cheapest(
                    live,
                    lambda row: row["fits"] and is_confirmed_queen_king(row["bedClass"]),
                ),
            }
        )

    def city_pick(city: str, field: str) -> dict | None:
        block = next((item for item in cities if item["city"] == city), None)
        return (block or {}).get(field)

    seoul_qk = city_pick("Seoul", "cheapestCoreQueenKing") or city_pick(
        "Seoul", "cheapestQueenKing"
    )
    gyeongju_qk = city_pick("Gyeongju", "cheapestQueenKing")
    gyeongju_king = _cheapest(
        [row for row in live_rows if row["city"] == "Gyeongju"],
        lambda row: row["bedClass"] == "king",
    )
    busan_qk = city_pick("Busan", "cheapestCoreQueenKing") or city_pick(
        "Busan", "cheapestQueenKing"
    )
    seoul_one = city_pick("Seoul", "cheapestOneBed")
    gyeongju_one = city_pick("Gyeongju", "cheapestOneBed")
    busan_one = city_pick("Busan", "cheapestOneBed")
    cheonan_one = city_pick("Cheonan", "cheapestOneBed")
    daejeon_one = city_pick("Daejeon", "cheapestOneBed")

    def trip(title: str, note: str, picks: list[dict | None]) -> dict:
        present = [pick for pick in picks if pick]
        total = sum(int(pick["totalStay"]) for pick in present)
        return {
            "title": title,
            "note": note,
            "legs": present,
            "total": total,
            "complete": len(present) == len(picks) and len(picks) > 0,
        }

    sample_trips = [
        trip(
            "Planned route · cheapest isolated queen/king live quotes",
            "Uses only timestamped Booking rows whose captured bed is one queen or one king. Gyeongju has no walkable KTX, so that leg is not a core-needs match. If the Gyeongju pick is KINOCK, it is a pet hotel. Totals are USD display snapshots, usually before 10% tax.",
            [seoul_qk, gyeongju_qk, busan_qk],
        ),
        trip(
            "Planned route · cheapest isolated one-bed live quotes",
            "Any isolated one-bed (full, queen, or king) with a UTC-stamped quote. A full/double is often below the 150 cm preference. Not a core-needs itinerary.",
            [seoul_one, gyeongju_one, busan_one],
        ),
        trip(
            "If Gyeongju is swapped for Cheonan · cheapest one-bed live quotes",
            "Alternative middle-leg only. No Cheonan hotel currently has both a confirmed queen/king width and walkable KTX.",
            [seoul_one, cheonan_one, busan_one],
        ),
        trip(
            "If Gyeongju is swapped for Daejeon · cheapest one-bed live quotes",
            "Alternative middle-leg only. No Daejeon hotel currently has both a confirmed queen/king width and walkable KTX.",
            [seoul_one, daejeon_one, busan_one],
        ),
    ]

    recommendations = []

    def add_rec(title: str, pick: dict | None, why: str, caveat: str | None = None) -> None:
        if not pick:
            recommendations.append(
                {"title": title, "missing": True, "why": why, "caveat": caveat}
            )
            return
        recommendations.append(
            {
                "title": title,
                "missing": False,
                "why": why,
                "caveat": caveat,
                **pick,
            }
        )

    add_rec(
        "Night one · official 24-hour desk",
        {
            "id": "seoul-somerset-palace",
            "name": "Somerset Palace Seoul",
            "city": "Seoul",
            "room": "Studio Executive / Executive One-Bedroom",
            "beds": "Official Ascott: 1 queen. Live Booking capture also isolated 1 queen.",
            "pricePerNight": next(
                (row["pricePerNight"] for row in live_rows if row["id"] == "seoul-somerset-palace"),
                None,
            ),
            "totalStay": next(
                (row["totalStay"] for row in live_rows if row["id"] == "seoul-somerset-palace"),
                None,
            ),
            "nights": 8,
            "sourceUrl": next(
                (row["sourceUrl"] for row in rows if row["id"] == "seoul-somerset-palace"),
                None,
            ),
            "officialUrl": "https://www.discoverasr.com/en/somerset-serviced-residence/korea-south/somerset-palace-seoul",
            "bedClass": "queen",
            "fits": True,
        },
        "Strongest official 24-hour reception source on the arrival-night shortlist.",
        "Send the flight number. A 24-hour desk is not a no-show waiver.",
    )
    add_rec(
        "Seoul 8 nights · cheapest confirmed queen/king live quote",
        seoul_qk,
        "Cheapest UTC-stamped Booking row whose captured bed is one queen or one king, on a core-needs hotel when one exists.",
        "Book that named room. Other rooms at the same hotel may be twins or fulls.",
    )
    add_rec(
        "Gyeongju 6 nights · strongest isolated king live quote",
        gyeongju_king or gyeongju_qk,
        "Gyeongju has no walkable KTX. This is the cheapest isolated king (or queen if no king) on Booking for Nov 9–15.",
        "Not a green core-needs match.",
    )
    add_rec(
        "Busan 7 nights · cheapest confirmed queen/king live quote on a core-needs hotel",
        busan_qk,
        "Cheapest UTC-stamped one-queen or one-king row among Busan hotels already marked as core-needs matches.",
        "Avani and some 'King' names are labeled queen on Booking — the captured bed text is what counts.",
    )
    add_rec(
        "Suwon · only green core-needs match",
        {
            "id": "suwon-novotel-ambassador",
            "name": "Novotel Ambassador Suwon",
            "city": "Suwon",
            "room": "Superior 1 King (Accor /8748)",
            "beds": "1 x King size bed",
            "pricePerNight": None,
            "totalStay": None,
            "nights": 8,
            "sourceUrl": "https://all.accor.com/hotel/8748/index.en.shtml",
            "officialUrl": "https://all.accor.com/hotel/8748/index.en.shtml",
            "bedClass": "king",
            "fits": True,
            "available": False,
        },
        "Official Accor king room with direct Suwon Station (KTX + subway) access.",
        "Booking.com is sold out for Nov 1–9. Book Accor.",
    )

    return {
        "asOf": "2026-08-18",
        "lastCaptureUtc": last_capture,
        "method": (
            "Identity: every hotel has a unique official, government-tourism, or exact-property source. "
            "Live prices: only Booking.com dated tables with a UTC timestamp are treated as quotes. "
            "Bed class is read from the captured row, not guessed from the hotel name. "
            "USD snapshots usually exclude 10% tax."
        ),
        "totals": {
            "hotels": len(hotels),
            "identityVerified": sum(
                1
                for hotel in hotels
                if (hotel.get("verification") or {}).get("existenceStatus")
                == "Verified operating property"
            ),
            "coreMatches": sum(1 for hotel in hotels if hotel.get("fits")),
            "liveQuotes": len(live_rows),
            "soldOut": sum(1 for hotel in hotels if _rr(hotel).get("available") is False),
            "unsourcedPrices": len(unsourced),
        },
        "cities": cities,
        "recommendations": recommendations,
        "sampleTrips": sample_trips,
        "quotes": sorted(
            quote_rows,
            key=lambda row: (
                row.get("windowKey", "nov1"),
                CITY_ORDER.index(row["city"]) if row["city"] in CITY_ORDER else 99,
                row["totalStay"],
            ),
        ),
        "flags": _flag_rows(hotels),
        "guides": {
            "fourCity": "guide/verification-suwon-gyeongju-cheonan-daejeon-2026-08-18.md",
            "lineByLine": "guide/verification-checklist-2026-08-18-line-by-line.md",
            "seoulDualWindow": "guide/verification-seoul-dual-window-nov1-and-nov15-2026.md",
            "audit": "guide/verification-audit.md",
        },
    }
