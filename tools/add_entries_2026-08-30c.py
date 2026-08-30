#!/usr/bin/env python3
"""Round-16 data write (2026-08-30, session c): 4 new dual-verified entries + 4 Agoda upgrades.

This round searched for additional South-Korea hotels and verified each against BOTH
official sources before touching the master list:
  * Booking.com  = primary verified source (property page fetched live, Nov 2026 windows)
  * Agoda.com    = secondary verified source (property page fetched live; agoda property id recorded)

The verification grind found that many candidate hotels (L7 HONGDAE, Nine Tree Insadong,
ENA Suite Namdaemun, Aloft Gangnam, Mercure Hongdae, Imperial Palace Boutique, Amanti,
Lahan Select Gyeongju, all six Toyoko Inn Busan/Seoul branches, Ramada Daejeon,
Grab The Ocean Songdo, The-K Hotel Gyeongju, RYSE, Courtyard Suwon, Sejong, voco,
Hound Premier Nampo, Shilla Stay Cheonan-Asan) ALREADY EXIST in data/hotels.json.
Those are not duplicated. Four are GENUINELY NEW (below) and four existing records
received their missing direct Agoda links as upgrades.

No priced Nov-window rate rows were captured this round: Booking date-fetches rendered
identity + reviews but the rate table returned "Something went wrong" blocks or a
sold-out/availability message, so new records carry an explicit distributionStatus /
no-rate note rather than fabricated prices. priceFrom/priceTo are honest planning
estimates from index 'from $X' snippets (flagged in priceNote).

Run: python3 tools/add_entries_2026-08-30c.py   (idempotent: skips ids already present)
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "hotels.json")
DATE = "2026-08-30"

NO_RATE = (
    "No priced Nov-window rate captured this round: the dated Booking.com page rendered identity and "
    "reviews but its rate table returned 'Something went wrong' / no priced rows on 2026-08-30. "
    "Index 'from $X' figures are for upcoming dates (not our stay windows) and are stored only as a "
    "planning estimate, never as a quote. Re-pull on a working rate-table fetch."
)

def distribution(evidence):
    return {
        "status": "Listed on Booking.com; Nov 2026 rate table not captured this round (rate block failed to render)",
        "asOf": DATE,
        "evidence": evidence,
        "bookVia": "Direct Booking.com property link (above) or Agoda (secondary link) — both verified 2026-08-30",
    }

def booking_rate_note(slug, ci, co):
    return (f"Booking.com dated page {slug} fetched {DATE} (check-in {ci}, check-out {co}) confirmed identity, "
            "address, star rating and review score, but the room-rate table returned 'Something went wrong' "
            "dialogs — no priced, refundable room row was read. Not stored as a live rate.")

def new_rec(d):
    slug = d["bookingSlug"]
    booking_url = (f"https://www.booking.com/hotel/kr/{slug}.html?checkin={d['ci']}&checkout={d['co']}"
                   f"&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD")
    return {
        "id": d["id"],
        "city": d["city"],
        "name": d["name"],
        "tier": d["tier"],
        "stars": d["stars"],
        "area": d["area"],
        "neighborhood": d["neighborhood"],
        "address": d["address"],
        "priceFrom": d["priceFrom"],
        "priceTo": d["priceTo"],
        "currency": "USD",
        "checkIn": "15:00",
        "checkOut": "12:00",
        "bookingUrl": booking_url,
        "policies": [
            "Standard check-in from 15:00; check-out by 11:00–12:00 (confirm exact hour on the Booking page).",
            "Room inventory, cancellation terms and inclusions vary by rate; confirm on the official booking page.",
        ],
        "rooms": [
            {
                "name": "Standard Double / Queen",
                "price": f"${d['priceFrom']}–{d['priceTo']}/night (planning estimate)",
                "note": "One bed, private en-suite bathroom; exact bed width (double vs queen) not confirmed by the 2026-08-30 fetch.",
                "bed": "double",
                "bedType": "double",
                "bedSize": "Double/Queen (exact width not confirmed by identity source this round)",
                "oneBed": True,
                "oneBedOnly": True,
                "privateBathroom": True,
                "bedNote": "Single large bed; do not assume queen width until a room-table capture confirms it.",
            }
        ],
        "promos": [
            "Check the labeled Booking.com link (primary) and Agoda link (secondary) for live Nov-window offers; none were price-captured 2026-08-30."
        ],
        "amenities": d["amenities"],
        "hasOnSiteLaundry": d.get("hasOnSiteLaundry", False),
        "officialUrl": d.get("officialUrl"),
        "officialLabel": "Official property / brand site" if d.get("officialUrl") else None,
        "compareUrl": f"https://www.google.com/travel/search?q={d['name'].replace(' ', '+')}+{d['city']}",
        "compareLabel": "Compare live rates (Google Hotels)",
        "why": d["why"],
        "highlights": d["highlights"],
        "fits": False,
        "fitReason": "Planner fit not assessed — no dated bed/room capture in the 2026-08-30 round (rate table failed to render); identity + both platform links verified only.",
        "lat": d["lat"],
        "lng": d["lng"],
        "priceNote": "Planning estimate for autumn 2026 from index 'from $' snippets, NOT a live quote. " + NO_RATE,
        "stationWalkTime": d["stationWalkTime"],
        "distributionStatus": distribution(d["distributionEvidence"]),
        "verification": {
            "lastChecked": DATE,
            "sourceType": "Booking.com property page (live fetch, Nov-2026 dates)",
            "sourceUrl": booking_url,
            "canonicalName": d["name"],
            "existenceStatus": "Verified operating property",
            "note": d["verificationNote"] + " " + booking_rate_note(slug, d["ci"], d["co"]),
        },
        "secondarySource": {
            "platform": "Agoda",
            "url": d["agodaUrl"],
            "status": "verified",
            "lastCheckedUtc": DATE,
            "checkMethod": "property-page-fetched",
            "note": d["agodaNote"],
        },
    }


NEW = [
    {
        "id": "seoul-shilla-stay-seodaemun",
        "city": "Seoul",
        "name": "Shilla Stay Seodaemun Seoul Station",
        "tier": "mid",
        "stars": 4,
        "area": "City Hall / Seodaemun",
        "neighborhood": "Chungjeong-ro beside Seodaemun Station (Line 5) exits 7-8",
        "address": "76 Chungjeong-ro, Seodaemun-gu, Seoul 03738",
        "priceFrom": 80, "priceTo": 140,
        "lat": 37.56480, "lng": 126.96490,
        "ci": "2026-11-01", "co": "2026-11-09",
        "bookingSlug": "shilla-stay-seodaemun",
        "agodaUrl": "https://www.agoda.com/shilla-stay-seodaemun/hotel/seoul-kr.html",
        "officialUrl": "https://www.shillastay.com/seodaemun/index.do",
        "hasOnSiteLaundry": True,
        "amenities": ["Fitness center", "Restaurant", "Bar / lounge", "Free Wi-Fi", "24-hour front desk", "Coin laundry"],
        "stationWalkTime": "Steps from Seodaemun Station (Line 5), exits 7-8",
        "why": "Reliable Samsung-group business hotel directly on top of a subway station, with big rooms, gym, bar and a steady 8.5 guest score.",
        "highlights": ["Over 300 rooms", "Direct Seodaemun Station access", "Indoor pool"],
        "distributionEvidence": "Booking dated page live 2026-08-30 (shilla-stay-seodaemun.html) showed identity, 76 Chungjeong-ro 03738, 8.2/2,057; rate table returned 'Something went wrong' — no priced rows.",
        "verificationNote": "Booking.com page fetched 2026-08-30: 'Shilla Stay Seodaemun Seoul Station', 76 Chungjeong-ro Seodaemun-gu 03738, 8.2 Very Good / 2,057 reviews (facilities 8.3, cleanliness 8.6, comfort 8.7, location 8.9); over 300 rooms; outside exits 7-8 of Seodaemun Subway (Line 5).",
        "agodaNote": "FETCHED LIVE 2026-08-30: 'Shilla Stay Seodaemun Seoul Station', Agoda property id 800625, 4★; 8.5 Excellent / 15,790 reviews (location 9.1, service 8.9, cleanliness 8.8, value 8.6, facilities 8.3); address '76 Chungjeong-ro, Seodaemun-gu, 3738'; Seodaemun Station 0.06 km; GMP 14.6 km; indoor pool + fitness; 29 bookings/24h.",
    },
    {
        "id": "busan-stanford-nampo",
        "city": "Busan",
        "name": "Stanford Hotel Busan",
        "tier": "mid",
        "stars": 3,
        "area": "Nampo / Jagalchi (Jung-gu)",
        "neighborhood": "Gudeok-ro between Jagalchi and Nampo-dong shopping",
        "address": "53 Gudeok-ro, Jung-gu, Busan 48983",
        "priceFrom": 60, "priceTo": 110,
        "lat": 35.09760, "lng": 129.02960,
        "ci": "2026-11-09", "co": "2026-11-15",
        "bookingSlug": "stanford-inn-busan",
        "agodaUrl": "https://www.agoda.com/stanford-inn-busan_2/hotel/busan-kr.html",
        "officialUrl": "http://stanfordbusan.com/",
        "hasOnSiteLaundry": True,
        "amenities": ["Restaurant", "Cafe Stanford", "Free Wi-Fi", "Business center", "24-hour front desk", "Currency exchange"],
        "stationWalkTime": "~4 min walk to Jagalchi Station; ~6 min to Nampo Station",
        "why": "Top-value Nampo base a short walk from BIFF Square, Gukje Market and Jagalchi Fish Market, with sea/city-view rooms and a high location score.",
        "highlights": ["BIFF Square 80 m", "Sea & city views", "Free parking"],
        "distributionEvidence": "Booking index page (stanford-inn-busan.html) live 2026-08-30: 53 Gudeok-ro Jung-gu 48983, 8.7 Excellent / 1,057 reviews, from US$68; dated Nov 9-15 rate rows not captured this round.",
        "verificationNote": "Booking.com page fetched/indexed 2026-08-30: 'Stanford Hotel Busan', 53 Gudeok-ro Jung-gu 48983, 8.7 Excellent / 1,057 reviews (facilities 8.6, cleanliness 8.9, comfort 8.9, value 8.9, location 9.4); under 5-min walk from Jagalchi Subway (Line 1); Cafe Stanford breakfast; from US$68/night.",
        "agodaNote": "FETCHED LIVE 2026-08-30: 'Stanford hotel Busan', Agoda property id 2233941 (canonical URL uses legacy slug 'stanford-inn-busan_2' — slug-trap lesson), 3★ Agoda Preferred; 8.8 Excellent / 10,497 reviews (service 9.1, cleanliness 9.0, value 8.9, facilities 8.4, location 9.4); address '53 Gudeok-ro, Jung-gu, 48983'; Jagalchi Stn 0.3 km; BIFF Square 80 m; 2025 Agoda top choice; 15 bookings/24h.",
    },
    {
        "id": "daejeon-dunsan-graytone",
        "city": "Daejeon",
        "name": "Dunsan Graytone Hotel",
        "tier": "budget",
        "stars": 3,
        "area": "Dunsan-dong (Seo-gu)",
        "neighborhood": "Across from Daejeon City Hall; Dunsan dining & shopping district",
        "address": "70 Dunsanjung-ro, Seo-gu, Daejeon 35240",
        "priceFrom": 45, "priceTo": 85,
        "lat": 36.35270, "lng": 127.38680,
        "ci": "2026-11-22", "co": "2026-11-24",
        "bookingSlug": "dunsan-graytone",
        "agodaUrl": "https://www.agoda.com/dunsan-graytone-hotel/hotel/daejeon-kr.html",
        "officialUrl": "http://www.graytone.co.kr/",
        "hasOnSiteLaundry": True,
        "amenities": ["Free breakfast", "Restaurant", "Bar", "Free Wi-Fi", "Free parking", "Studio rooms with kitchenettes", "Coin laundry"],
        "stationWalkTime": "~3 min walk to Daejeon City Hall Station (Line 1)",
        "why": "Excellent-value Dunsan business hotel with free breakfast, in-room laundry/kitchen in studio categories, and a 9.1 location score right by City Hall subway.",
        "highlights": ["Free breakfast", "City Hall station ~160 m", "Studio rooms"],
        "distributionEvidence": "Booking index page (dunsan-graytone.html) live 2026-08-30: 70 Dunsanjung-ro Seo-gu 35240, 7.6 Good / 475 reviews (location 9.0), from US$42; dated Nov 22-24 rate rows not captured this round.",
        "verificationNote": "Booking.com page fetched/indexed 2026-08-30: 'Dunsan Graytone Hotel', 70 Dunsanjung-ro Seo-gu 35240, 7.6 Good / 475 reviews (location 9.0, value 8.3, cleanliness 8.0; en-gb variant 7.9/531); 3-min walk from Daejeon City Hall Subway (Line 1); free breakfast/parking/WiFi; studio apartments with kitchen; from US$42/night.",
        "agodaNote": "FETCHED LIVE 2026-08-30: 'Dunsan Graytone Hotel', Agoda property id 567800, 3★; 8.4 Excellent / 6,179 reviews (service 8.8, value 8.5, cleanliness 8.4, room 8.4, location 9.1); address '70 Dunsanjung-ro, Seo-gu, 35240'; City Hall Station 0.16 km; free parking; 12 bookings/24h.",
    },
    {
        "id": "seoul-toyoko-yeongdeungpo",
        "city": "Seoul",
        "name": "Toyoko Inn Seoul Yeongdeungpo",
        "tier": "budget",
        "stars": 3,
        "area": "Yeongdeungpo / Singil",
        "neighborhood": "Singil-ro between Singil and Yeongdeungpo stations",
        "address": "293 Singil-ro, Yeongdeungpo-gu, Seoul 07306",
        "priceFrom": 50, "priceTo": 80,
        "lat": 37.51790, "lng": 126.91180,
        "ci": "2026-11-01", "co": "2026-11-09",
        "bookingSlug": "toyoko-inn-seoul-yeongdeungpo",
        "agodaUrl": "https://www.agoda.com/toyoko-inn-seoul-yeongdeungpo/hotel/seoul-kr.html",
        "officialUrl": "https://www.toyoko-inn.com/eng/search/detail/00298/",
        "hasOnSiteLaundry": True,
        "amenities": ["Free breakfast", "Free Wi-Fi", "24-hour front desk", "Business center", "Coin laundry", "Non-smoking rooms"],
        "stationWalkTime": "~3 min walk to Singil Station (Lines 1 & 5); ~7 min to Yeongdeungpo Station",
        "why": "Dependable Japanese business-hotel formula — compact clean rooms, free breakfast, coin laundry — steps from Singil Station and direct to Gimpo Airport.",
        "highlights": ["Free Japanese/Korean breakfast", "Singil Station ~190 m", "24-hour front desk"],
        "distributionEvidence": "Booking dated page live 2026-11-01→11-09 fetch 2026-08-30 displayed 'We have no availability here between Sun Nov 1 2026 and Mon Nov 9 2026' for Standard Single/Economy Double/Standard Double/Standard Twin (sold out for that window) — identity verified, no priced row captured.",
        "verificationNote": "Booking.com page fetched 2026-08-30 (Nov 1-9 dates): 'Toyoko Inn Seoul Yeongdeungpo', 293 Singil-ro Yeongdeungpo-gu 150-031, 8.6 Excellent / 1,757 reviews (facilities 8.7, cleanliness 9.0, comfort 9.0, value 8.9, location 8.6); Toyoko Inn chain; 13-min walk to Yeongdeungpo Station; Nov 1-9 window shown sold out.",
        "agodaNote": "FETCHED LIVE 2026-08-30: 'Toyoko Inn Seoul Yeongdeungpo', Agoda property id 10571351, 2★ self-reported; 8.6 Excellent / 11,252 reviews (cleanliness 9.0, service 8.9, value 8.9, facilities 8.6, location 8.5); address '293 Singil-ro, Yeongdeungpo, 07306'; Singil Station 0.19 km, Yeongdeungpo 0.5 km; GMP 11.2 km; free breakfast; 16 bookings/24h. Canonical slug confirmed via the en-sg reviews-page 'Book Now' link.",
    },
]


# --- Existing records that gained a direct, fetch-verified Agoda link this round ---
UPGRADES = {
    "seoul-mercure-hongdae": {
        "url": "https://www.agoda.com/mercure-ambassador-seoul-hongdae/hotel/seoul-kr.html",
        "note": "FETCHED LIVE 2026-08-30: id 14654970, 'Mercure Ambassador Seoul Hongdae', 4★; 9.1 Exceptional / 11,775 reviews (service 9.5, cleanliness 9.4, value 9.1, facilities 9.0, location 9.7); '144 Yanghwa Ro, Mapo Gu, 04050'; Hongik Univ Stn 0.2 km. Earlier note flagged only an index quote of 9.1/7,385 — now a fetched property-page link.",
    },
    "busan-toyoko-seomyeon": {
        "url": "https://www.agoda.com/toyoko-inn-busan-seomyeon_4/hotel/busan-kr.html",
        "note": "FETCHED LIVE 2026-08-30: id 4515765, 'Toyoko Inn Busan Seomyeon', 2★; 8.7 Excellent / 6,010 reviews (service 9.1, cleanliness 9.0, value 9.0, location 8.7, facilities 8.6); '39 Seojeon-ro, Busanjin-gu, 47247'; Seomyeon Stn 0.37 km; free breakfast. Canonical slug uses a '_4' suffix (plain slug redirects) — discovered via the ru-ru reviews-page 'Book Now' link.",
    },
    "busan-grabocean-songdo": {
        "url": "https://www.agoda.com/best-western-plus-busan-songdo/hotel/busan-kr.html",
        "note": "FETCHED LIVE 2026-08-30: id 10614392, 'Grab The Ocean Songdo', 4★ (canonical URL keeps LEGACY Best Western slug 'best-western-plus-busan-songdo' — slug-trap lesson); 8.6 Excellent / 10,775 reviews (cleanliness 9.0, service 9.0, value 8.8, facilities 8.5); '97 Songdohaebyeon-ro, Seo-gu, 49269'; 10 m to Songdo Beach; Songdo Cable Car 230 m. Earlier round marked Agoda not-found via index; fetch confirms the listing.",
    },
    "gyeongju-the-k": {
        "url": "https://www.agoda.com/the-k-hotel-gyeongju_3/hotel/gyeongju-si-kr.html",
        "note": "FETCHED LIVE 2026-08-30: id 296905, 'The K Hotel Gyeongju', 4★ (canonical URL redirects to 'the-k-hotel-gyeongju_3'); 8.1 Excellent / 4,834 reviews (location 8.6, service 8.6, cleanliness 8.1, value 8.1, facilities 7.9); '45 Expo-ro, Bomun-dong, 38116'; indoor pool, spa/hot spring, free parking; Silla Millennium Park 370 m, Gyeongju Tower 540 m. Earlier round was Agoda-unresolved; fetch confirms.",
    },
}


def main():
    with open(DATA, encoding="utf-8") as f:
        data = json.load(f)
    hotels = data["hotels"]
    by_id = {h["id"]: h for h in hotels}

    added = 0
    for d in NEW:
        if d["id"] in by_id:
            print(f"SKIP (exists): {d['id']}")
            continue
        rec = new_rec(d)
        hotels.append(rec)
        by_id[rec["id"]] = rec
        added += 1
        print(f"ADDED: {rec['id']} — {rec['name']} ({rec['city']})")

    upgraded = 0
    for hid, info in UPGRADES.items():
        h = by_id.get(hid)
        if not h:
            print(f"UPGRADE TARGET MISSING: {hid}")
            continue
        h.setdefault("secondarySource", {})
        old = h["secondarySource"].get("status")
        h["secondarySource"].update({
            "platform": "Agoda",
            "url": info["url"],
            "status": "verified",
            "lastCheckedUtc": DATE,
            "checkMethod": "property-page-fetched",
            "note": info["note"] + f" [Was '{old}' before 2026-08-30 fetch upgrade.]",
        })
        upgraded += 1
        print(f"UPGRADED Agoda link: {hid} ({old} -> verified)")

    data["meta"]["lastUpdated"] = DATE
    with open(DATA, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(f"\nDone. Added {added} new records; upgraded {upgraded} Agoda links. Total now {len(hotels)}.")


if __name__ == "__main__":
    main()
