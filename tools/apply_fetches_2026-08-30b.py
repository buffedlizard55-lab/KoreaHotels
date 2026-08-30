#!/usr/bin/env python3
"""Round-15b: apply the live dated-fetch findings to data/hotels.json.

Every fact written here was read verbatim off a page fetched in the
2026-08-30 01:30-01:48 UTC session (Booking.com dated property pages and
Agoda property pages). Nothing is estimated: where a fetch proved absence
(no availability / 404 / redirect), the record now says so with the date.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "hotels.json")

BOOKING_DATED = ("https://www.booking.com/hotel/kr/{slug}.html?checkin={ci}&checkout={co}"
                 "&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD")

def dated(slug, ci, co):
    return BOOKING_DATED.format(slug=slug, ci=ci, co=co)

data = json.load(open(DATA, encoding="utf-8"))
by_id = {h["id"]: h for h in data["hotels"]}
W = "2026-08-30 live dated fetch (session 01:30-01:48 UTC)"

# ---------------------------------------------------------------- 1. Tmark -> voco (rebrand + rates)
h = by_id["seoul-tmark-myeongdong"]
h["name"] = "voco Seoul Myeongdong by IHG (former Tmark Grand)"
h["address"] = "52 Toegye-ro, Jung-gu, Seoul (Booking 2026-08-30: 04625; Agoda page prints 'Taegye-ro ... 04634' — conflict FLAGGED, both kept)"
h["compareUrl"] = "https://www.booking.com/hotel/kr/voco-seoul-myeongdong.html"
h["compareLabel"] = "Open property page (Booking.com — 301 from old tmark slug, verified live)"
h["checkIn"] = "Not shown in the captured chunks of the dated page (2026-08-30) — confirm on the dated page before booking"
h["checkOut"] = "Not shown in the captured chunks of the dated page (2026-08-30) — confirm on the dated page before booking"
h["priceFrom"], h["priceTo"] = 330, 401
h["priceNote"] = ("Range = spread of the four plans captured 2026-08-30 for 2026-11-01 to 11-09, 2 adults, USD; "
                  "not a year-round estimate. Refundable king from $340/night; the non-refundable pay-online plan was $10/night cheaper.")
h["promos"] = ["No promo copy captured on the dated page (2026-08-30); the 'pay online' non-refundable plan was the only discount-style row."]
h["amenities"] = [
    "576 rooms; 2 pools (indoor heated + kids pool) — Booking dated page + Agoda facilities, both fetched 2026-08-30",
    "Restaurants, fitness centre, free Wi-Fi, car park, 24-h front desk, luggage storage (Agoda facilities copy, fetched 2026-08-30)",
    "Free Wi-Fi, A/C, attached bathroom in the captured Deluxe King room row (Booking dated page, 2026-08-30)",
]
h["rooms"] = [{
    "name": "Deluxe King Room with Mountain View",
    "price": "$330-401/night (plan-dependent)",
    "note": "8-night total $2,637-3,212 excl 10% TAX as captured 2026-08-30; other same-table rows ($365/$376/$401) had their room names truncated at capture — likely a Superior tier, unattributed on purpose",
    "bed": "king",
    "bedType": "king",
    "bedSize": "1 king bed (width not published on the Booking row)",
    "oneBed": True, "oneBedOnly": True, "privateBathroom": True,
    "bedNote": "Attached bathroom stated on the row; king bed width not stated",
}]
h["fits"] = True
h["fitReason"] = ("Core needs (1 room, 1 large bed, private bath): captured Booking row 'Deluxe King Room with Mountain View' = "
                  "1 king bed + attached bathroom, sleeps 2 (fetched 2026-08-30). Bed width not published — confirm at booking if critical.")
h["refundableRate"] = {
    "capturedAtUtc": "2026-08-30T01:40:00Z",
    "source": "Booking.com property page (dated rate table, live fetch 2026-08-30; timestamp approximated to session window 01:30-01:48Z)",
    "sourceUrl": dated("voco-seoul-myeongdong", "2026-11-01", "2026-11-09"),
    "stayCheckIn": "2026-11-01", "stayCheckOut": "2026-11-09", "nights": 8,
    "available": True,
    "room": "Deluxe King Room with Mountain View",
    "beds": "1 king bed (258 feet², sleeps 2, attached bathroom)",
    "pricePerNight": 340,
    "totalStay": 2719,
    "currency": "USD (Excluded: 10% TAX; 10% service charge line not shown for this plan)",
    "breakfastIncluded": False,
    "freeCancellation": "Free cancellation before 2026-10-02 (30 days pre-arrival). Cancel inside the window: fee = cost of the FIRST night (page wording); no-show fee = same as cancellation fee.",
    "prepayment": "No prepayment needed — pay at the property",
    "note": ("Cheaper sibling plan in the same row: NON-REFUNDABLE, pay online at booking — $330/night, $2,637 total (the full total is charged at booking, no refund). "
              "Breakfast-included plans of $376 ($3,007) and $401 ($3,212) appeared on same-table rows whose room names were truncated at capture (see priceNote). "
              "Page also showed the marketing chip 'Perfect for an 8-night stay'."),
}
h["verification"] = {
    "lastChecked": "2026-08-30",
    "sourceType": "Booking.com dated property page (LIVE FETCH 2026-08-30, rate grid captured) + Agoda property page (LIVE FETCH 2026-08-30)",
    "sourceUrl": dated("voco-seoul-myeongdong", "2026-11-01", "2026-11-09"),
    "canonicalName": "voco Seoul Myeongdong by IHG",
    "existenceStatus": "Verified operating and bookable (2026-08-30); rebrand from Tmark Grand Hotel Myeongdong live-confirmed",
    "note": ("REBRAND LIVE-CONFIRMED 2026-08-30: https://www.booking.com/hotel/kr/tmark-grand-myeongdong.html 301-redirects to /hotel/kr/voco-seoul-myeongdong.html. "
             "STALE-INDEX IRREGULARITY FLAGGED: the 2026-08-30 search-index copy still titled the property 'Tmark Grand' and said it was NOT taking reservations; "
             "the live dated page minutes later showed it fully bookable — index snapshots cannot be trusted for sale-status or scores; a live dated fetch must gate any 'verified'. "
             "Booking live page (2026-08-30): 8.7/10 from 442 reviews, location 9.3/432, breakfast 9.3/14 (prior index snapshot said 8.6/839 — both recorded, no overwrite; "
             "review-base change on rebrand is the likely cause, unproven). "
             "ADDRESS CONFLICT FLAGGED: Booking prints '52, Toegye-ro, Jung-gu, Seoul 04625'; the fetched Agoda page prints '52, Taegye-ro, Jung-gu, Seoul 04634' — "
             "spelling and postal code differ between the two official sites; kept as-is. "
             "Coordinates 37.5625/126.9925613 unchanged and consistent with Agoda distances (Hoehyeon Stn 0.05 km, Myeongdong Walking St 700 m, GMP 15.7 km). "
             "Do-not-confuse flag retained: 'Tmark Hotel Myeongdong' (43 Chungmuro 3-ga) is a different, smaller property."),
}
h["distributionStatus"] = {
    "status": "Bookable on Booking.com and on Agoda (both property pages fetched live 2026-08-30)",
    "asOf": "2026-08-30",
    "evidence": ("Booking dated page returned a full rate grid with Select-Rooms controls (voco slug, redirected from the old tmark slug); "
                 "Agoda property page LIVE and self-described 'Newly renovated 2025'. The prior 'not taking reservations' index copy (2026-08-30 earlier round) is superseded — "
                 "kept here as the staleness exhibit."),
}
h["highlights"] = [
    "Rebrand Tmark Grand → voco (IHG) live-confirmed 2026-08-30 (Booking 301 + both site titles)",
    "Refundable Deluxe King $340/n · $2,719 for 8 nights captured live (Nov 1–9 window)",
    "Hoehyeon Stn exit at the door; airport-bus stop out front (pre-existing map data)",
]
h["secondarySource"] = {
    "platform": "Agoda",
    "url": "https://www.agoda.com/tmark-grand-hotel-myeongdong_12/hotel/seoul-kr.html",
    "status": "verified",
    "lastCheckedUtc": "2026-08-30",
    "checkMethod": "property-page-fetched",
    "note": ("FETCHED LIVE 2026-08-30 (a voco-guess Agoda URL 301'd onto this canonical tmark-grand slug; page title reads 'voco Seoul Myeongdong By IHG'). "
             "Agoda score 8.9/10 from 2,582 reviews (location 9.4, clean 9.3, service 9.1, facilities 8.9, value 8.9); 4.5-star self-reported; "
             "'Newly renovated 2025'; 'Booked 10 times in the last 24h'; value-for-money 8.9; city centre 0.6 km; GMP 15.7 km. "
             "Agoda prints the address as '52, Taegye-ro … 04634' vs Booking's 'Toegye-ro … 04625' — conflict flagged, neither corrected."),
}

# ---------------------------------------------------------------- 2. Signiel (dated suite capture + Agoda fetched)
h = by_id["seoul-signiel"]
h["checkIn"] = "From 15:00 — Booking house rules, fetched live 2026-08-30 (formerly only a KAYAK-sourced guess)"
h["checkOut"] = "Until 11:00 — Booking house rules, fetched live 2026-08-30"
h["policies"] = (h.get("policies") or []) + [
    "Booking house rules (fetched 2026-08-30): extra bed KRW 60,500/night (children 0–2 and 3+); cribs free; children 13+ are charged as adults.",
]
h["amenities"] = (h.get("amenities") or []) + [
    "2 restaurants on site per the fetched Booking page (STAY — French/European; BICENA — Korean); top amenities incl. indoor pool, spa & wellness, airport shuttle, fitness, bar (fetched 2026-08-30)",
]
h["priceFrom"], h["priceTo"] = 1162, 1162
h["priceNote"] = ("Single dated capture 2026-08-30 for 2026-11-15 to 11-22 (7 nights, 2 adults, USD): Premier Suite Double Scenic Bath $1,162/night → $9,026 total. "
                  "A cheaper row ($8,743 total, free cancellation before 2026-11-13, no meal) existed above the capture cut-off with no recoverable room name — NOT attributed; "
                  "treat $1,162 as a suite-floor capture, not the property floor.")
h["refundableRate"] = {
    "capturedAtUtc": "2026-08-30T01:40:00Z",
    "source": "Booking.com property page (dated rate table, live fetch 2026-08-30; timestamp approximated to session window 01:30-01:48Z)",
    "sourceUrl": dated("signiel-seoul", "2026-11-15", "2026-11-22"),
    "stayCheckIn": "2026-11-15", "stayCheckOut": "2026-11-22", "nights": 7,
    "available": True,
    "room": "Premier Suite Double Scenic Bath",
    "beds": "1 queen bed (private suite, 729 feet², spa tub/hot tub, city view, private bathroom with walk-in shower + bath + bidet)",
    "pricePerNight": 1162,
    "totalStay": 9026,
    "currency": "USD (Included: 10% service charge; Excluded: 10% TAX)",
    "breakfastIncluded": True,
    "freeCancellation": "Free cancellation before 2026-11-13 (2 days pre-arrival). Cancel inside the window: fee = cost of the FIRST night; no-show fee = same. 'We have 3 left' shown.",
    "prepayment": "No prepayment needed — pay at the property",
    "note": "Buffet breakfast included (the page rates the breakfast itself 7.4/10 from 17 reviews); minibar, coffee machine, flat-screen cable TV, A/C, free Wi-Fi on the room row.",
}
h["verification"]["lastChecked"] = "2026-08-30"
h["verification"]["note"] = (h["verification"].get("note", "") +
    " | UPDATE 2026-08-30 (live dated fetch): Booking page now shows 9.3/10 from 753 reviews (staff 9.4, facilities 9.5, cleanliness 9.6, comfort 9.7, value 8.6, location 9.2, wifi 9.7). "
    "The stored aggregator-era figure 9.3/6,360 and Agoda's 9.2/7,615 differ in review counts — all three recorded, no overwrite; Booking count likely covers the main profile only. "
    "Check-in 15:00 / check-out 11:00 upgraded from KAYAK-sourced to Booking-confirmed. Full dated rate grid captured (see refundableRate).")
h["secondarySource"] = {
    "platform": "Agoda",
    "url": "https://www.agoda.com/signiel-seoul/hotel/seoul-kr.html",
    "status": "verified",
    "lastCheckedUtc": "2026-08-30",
    "checkMethod": "property-page-fetched",
    "note": ("FETCHED LIVE 2026-08-30 (canonical agoda.com property page): 5-star (government-verified label), Agoda score 9.2/10 'Exceptional' from 7,615 reviews "
             "(clean 9.7, service 9.7, facilities 9.5, value 9.1, location 9.6); address 300 Olympic-ro, Yeongdong-gun… 05551 shown as '300 Olympic-ro, Songpa-gu, Seoul, 05551'; "
             "Jamsil Station 0.24 km; '2024 top choice' badge copy. Diverges from the earlier index-era note (9.3/6,360 via search index): both kept, page fetch authoritative for page content."),
}
h["highlights"] = (h.get("highlights") or [])[:2] + ["Suite rate captured live 2026-08-30: $1,162/n · $9,026/7n refundable, breakfast included"]

# ---------------------------------------------------------------- 3. Lotte Hotel World (name fix + rates)
h = by_id["seoul-lotte-world"]
h["name"] = "Lotte Hotel World"
h["priceFrom"], h["priceTo"] = 258, 347
h["priceNote"] = ("Range from the single room family captured 2026-08-30 for 2026-11-01 to 11-09 (8 nights, 2 adults, USD): "
                  "no-meal plan $258/n avg → $2,294 (7% 'Bonus savings' off $2,467) and breakfast-included $347/n → $3,082; other room families had a row above the capture cut-off. "
                  "Not a year-round estimate.")
h["refundableRate"] = {
    "capturedAtUtc": "2026-08-30T01:45:02Z",
    "source": "Booking.com property page (dated rate table, live fetch 2026-08-30)",
    "sourceUrl": dated("lotte-world", "2026-11-01", "2026-11-09"),
    "stayCheckIn": "2026-11-01", "stayCheckOut": "2026-11-09", "nights": 8,
    "available": True,
    "room": "Deluxe Double Room with Lake View",
    "beds": "1 queen bed (301 feet², sleeps 2 adults; 'The unit has 1 bed'; bathroom type not restated on the captured row)",
    "pricePerNight": 258,
    "totalStay": 2294,
    "currency": "USD (total before taxes $2,294.16; Included: 10% service charge; Excluded: 10% TAX)",
    "breakfastIncluded": False,
    "freeCancellation": "Free cancellation before 2026-10-30 (2 days pre-arrival). Inside the window: fee = cost of the FIRST night; no-show = same.",
    "prepayment": "No prepayment needed — pay at the property",
    "note": ("Original price $2,467, 7% 'Bonus savings' discount → $2,294. Buffet breakfast $45/person/night not included (breakfast rated 8.5/10 from 10 reviews). "
              "Second plan on the same room: $347/n → $3,082 with breakfast INCLUDED (same free-cancel terms). Multi-room ladder shown (2 rooms $4,588 … 10 rooms $22,940 at the no-meal rate). "
              "Booking page title: 'Lotte Hotel World' — record name corrected from the legacy display 'Lotte Hotel Seoul'; canonicalName was already 'Lotte Hotel World'."),
}
h["verification"]["lastChecked"] = "2026-08-30"
h["verification"]["note"] = (h["verification"].get("note", "") +
    " | UPDATE 2026-08-30: Booking dated page fetched LIVE (full rate grid captured); display name on the official page is 'Lotte Hotel World' (Jamsil/Lotte World complex), "
    "not the legacy 'Lotte Hotel Seoul' this record previously displayed — name corrected; the flagship 'LOTTE HOTEL SEOUL' (id seoul-lotte-hotel, Myeongdong) is a different property and remains separate.")
h["secondarySource"]["note"] = (h["secondarySource"].get("note", "") +
    " | 2026-08-30: no Agoda URL surfaced yet (status stays unresolved); the Booking side is now fully fetched with a dated rate table.")

# ---------------------------------------------------------------- 4. Hound Premier Nampo (rates + fits upgrade)
h = by_id["busan-hound-premier-nampo"]
h["priceFrom"], h["priceTo"] = 68, 92
h["priceNote"] = ("Range from rows captured live 2026-08-30 for 2026-11-09 to 11-15 (6 nights, 2 adults, USD): Deluxe Double $68/n → $409 (9% off $449), "
                  "Double with Balcony $92/n → $551 (was $606). An unnamed cheaper row ($66/n → $394, identical amenity list, 323 feet²) sits above the capture cut-off — NOT attributed. "
                  "Prices are the discounted 'pay online' figures; totals are before the excluded 10% TAX.")
h["refundableRate"] = {
    "capturedAtUtc": "2026-08-30T01:45:07Z",
    "source": "Booking.com property page (dated rate table, live fetch 2026-08-30)",
    "sourceUrl": dated("hound-bupyeong", "2026-11-09", "2026-11-15"),
    "stayCheckIn": "2026-11-09", "stayCheckOut": "2026-11-15", "nights": 6,
    "available": True,
    "room": "Deluxe Double Room with City View",
    "beds": "1 queen bed (323 feet², city view, PRIVATE BATHROOM stated, soundproofing, flat-screen TV, free Wi-Fi)",
    "pricePerNight": 68,
    "totalStay": 409,
    "currency": "USD (Excluded: 10% TAX; 'Booking.com pays $40.43' discount from $449 applied)",
    "breakfastIncluded": False,
    "freeCancellation": "Free cancellation before 2026-11-08 (1 day pre-arrival). ⚠️ Inside the window the fee is the TOTAL reservation price (not the first night), and no-show = total price.",
    "prepayment": "⚠️ 'Pay nothing until November 6, 2026' — payment is due 3 days BEFORE check-in (auto-charge or pay at booking). Not pay-at-property.",
    "note": ("Same property also sold a Double with Balcony, 1 king bed, 371 feet², landmark+city view, $92/n → $551 (no meal, same cancellation ladder). "
              "No meal included on any captured row. Harsh ladder (total-price fee 1 day out) recorded as an irregularity flag for this otherwise-cheap option."),
}
h["fits"] = True
h["fitReason"] = ("Captured Booking row (fetched 2026-08-30) 'Deluxe Double Room with City View' = 1 queen bed + private bathroom stated, sleeps 2 — core fit met. "
                  "Bed width not published beyond 'queen'.")
h["distributionStatus"]["status"] = "Bookable on Booking.com with dated rates captured (live fetch 2026-08-30)"
h["distributionStatus"]["asOf"] = "2026-08-30"
h["distributionStatus"]["evidence"] = ("Dated Booking page returned a full rate grid (hound-bupyeong slug); 'We have N left' ladders shown. "
                                       "Agoda side unchanged: KAYAK-quoted provider score 8.9/337 and momondo deal lines $36–43 — still no direct agoda.com URL (unresolved).")
h["secondarySource"]["note"] = (h["secondarySource"].get("note", "") + " | 2026-08-30: Agoda URL still unresolved; Booking side fetched live with full dated capture.")

# ---------------------------------------------------------------- 5. Benikea Haeundae
h = by_id["busan-benikea-haeundae"]
h["priceFrom"], h["priceTo"] = 77, 77
h["priceNote"] = ("Captured live 2026-08-30 for 2026-11-09 to 11-15 (6 nights, 2 adults, USD): Staycation-Offer Standard Double $77/n → $464 (10% TAX excluded). "
                  "An unattributed $71/n → $427 row (spa tub/jacuzzi, ground floor, wheelchair-accessible — amenities visible, room name above the cut-off) and a Standard Twin row exist but "
                  "were truncated; only the named Double row is used as the floor. NOT pay-at-property — see refund terms.")
h["refundableRate"] = {
    "capturedAtUtc": "2026-08-30T01:45:49Z",
    "source": "Booking.com property page (dated rate table, live fetch 2026-08-30)",
    "sourceUrl": dated("benikea-haeundae", "2026-11-09", "2026-11-15"),
    "stayCheckIn": "2026-11-09", "stayCheckOut": "2026-11-15", "nights": 6,
    "available": True,
    "room": "Staycation Offer- Standard Double Room (check-in at 3pm - check-out at 3pm)",
    "beds": "1 full bed (258 feet², mountain view, ATTACHED bathroom stated)",
    "pricePerNight": 77,
    "totalStay": 464,
    "currency": "USD (Excluded: 10% TAX)",
    "breakfastIncluded": False,
    "freeCancellation": "Free cancellation before 2026-11-06 (3 days pre-arrival); cancel inside the window = TOTAL reservation price; no-show = same. 'Fully refundable during free cancellation' stated.",
    "prepayment": "⚠️ 'Pay the property before arrival' — charged the TOTAL price within 3 days of arrival (not pay-at-property). 'We have 3 left'.",
    "note": ("Staycation plan uses 15:00 check-in / 15:00 check-out (per plan name). Buffet breakfast $11/person/night (rated 7.5/2 reviews). "
              "Core-fit caveat: the named cheap room is '1 FULL bed' — not a queen/king — so fits stays false pending a wider-bed row."),
}
h["fitReason"] = ("Not a fit on the captured evidence alone: cheapest fully-named room (fetched 2026-08-30) is '1 full bed' — the planner requires a queen/king; "
                  "the unattributed cheaper row and the twin row don't change that. Re-check a Deluxe/king row on the dated page.")
h["distributionStatus"]["status"] = "Bookable on Booking.com with dated rates captured (live fetch 2026-08-30)"
h["distributionStatus"]["asOf"] = "2026-08-30"
h["distributionStatus"]["evidence"] = "Dated Booking page returned a live rate grid with Select-Rooms ladders (3 left on captured plans). Agoda URL still unresolved."
h["secondarySource"]["note"] = (h["secondarySource"].get("note", "") + " | 2026-08-30: Booking dated page fetched live (rates captured); Agoda URL still unresolved.")

# ---------------------------------------------------------------- 6. Toyoko Inn Seoul Gangnam (live page, no availability)
h = by_id["seoul-toyoko-gangnam"]
h["checkIn"] = "From 15:00 — and guests must advise arrival time in advance (Booking house rules, fetched live 2026-08-30)"
h["checkOut"] = "Until 10:00 — Booking house rules, fetched live 2026-08-30"
h["policies"] = (h.get("policies") or []) + [
    "No cribs and no extra beds at this property (Booking house rules, fetched 2026-08-30); children of all ages welcome.",
    "Pets not allowed. Payments: Visa/Mastercard/Diners/JCB/UnionPay/cash. License number 8698500804 (fetched 2026-08-30).",
]
h["amenities"] = (h.get("amenities") or []) + [
    "Booking 'Most popular amenities' (fetched 2026-08-30): private parking, free Wi-Fi, 24-hour front desk, elevator, daily housekeeping, luggage storage, non-smoking rooms, accessible facilities, breakfast (guests: buffet, included at the price point)",
]
h["priceNote"] = ("Still not captured — and now with a proven reason: the dated Booking page (Nov 1–9) was FETCHED LIVE 2026-08-30 and is a short 3-chunk page "
                  "listing no rooms ('See availability' placeholders only), i.e. no availability for our window rather than a dead link. Check a different window or Toyoko's own site.")
h["distributionStatus"]["status"] = "Property page LIVE on Booking (fetched 2026-08-30) but no rooms shown for 2026-11-01→09"
h["distributionStatus"]["asOf"] = "2026-08-30"
h["distributionStatus"]["evidence"] = ("Live dated fetch 2026-08-30: /hotel/kr/toyoko-inn-seoul-gangnam.html resolves (title 'Toyoko Inn Seoul Gangnam, Seoul (updated prices 2026)'), "
                                       "reviews and house rules render, but the availability table is empty for our dates. Guest quotes describe included buffet breakfast. "
                                       "Booking sub-scores captured: cleanliness 8.7, comfort 8.7, value 8.8, location 8.8, wifi 9.0, facilities review 8.4 (overall score sits above the captured chunk — not recorded).")
h["verification"]["lastChecked"] = "2026-08-30"
h["verification"]["note"] = (h["verification"].get("note", "") +
    " | UPDATE 2026-08-30: Booking property page fetched live — operating status, check-in/out, amenities, payment and license 8698500804 now Booking-confirmed. No dated rates (no availability shown).")
h["secondarySource"]["note"] = (h["secondarySource"].get("note", "") +
    " | 2026-08-30: Booking side now fetched live (page up, zero availability for our window). Agoda URL still unresolved (KAYAK-quoted 8.8/129 stand-off unchanged).")

# ---------------------------------------------------------------- 7. J-TOP Cheonan (fetched Agoda page + laundry + drift)
h = by_id["cheonan-jtop"]
h["hasOnSiteLaundry"] = True
h["amenities"] = (h.get("amenities") or []) + [
    "Laundry service (Agoda facilities, fetched live 2026-08-30)",
    "Free parking, 24-hour front desk (24-h check-in), bar, coffee shop, elevator, daily housekeeping (Agoda facilities copy, fetched 2026-08-30)",
]
h["verification"]["lastChecked"] = "2026-08-30"
h["verification"]["note"] = (h["verification"].get("note", "") +
    " | UPDATE 2026-08-30: the Agoda property page was fetched LIVE — address 19 Geomeundeul 3-gil, Cheonan 31163 confirmed ✓; 3-star self-reported; "
    "1.76 km from city centre, Asan Station 1.97 km, Cheonan-Jang Kee? (CJJ airport) 35.7 km, location subscore 8.8. "
    "STALE-INDEX FLAG ×2: the page shows 8.7/10 from 862 reviews while yesterday's index copy said 8.2/451 — both recorded (page authoritative for page content), reinforcing the round's lesson that scores drift between snapshots.")
h["secondarySource"] = {
    "platform": h["secondarySource"].get("platform", "Agoda"),
    "url": "https://www.agoda.com/hotel-j-top-cheonan_2/hotel/cheonan-kr.html",
    "status": "verified",
    "lastCheckedUtc": "2026-08-30",
    "checkMethod": "property-page-fetched",
    "note": ("FETCHED LIVE 2026-08-30 (agoda.com/hotel-j-top-cheonan_2): 3★ self-reported; 8.7/10 from 862 reviews, location 8.8; free Wi-Fi, free parking, "
             "24-hour front desk, bar, coffee shop, elevator, daily housekeeping, LAUNDRY SERVICE. Agoda's static copy carries NO dated USD rate rows, so pricing stays a Booking-window question mark. "
             "Index-era score 8.2/451 recorded in verification.note as the staleness exhibit."),
}

# ---------------------------------------------------------------- 8. Hotel Biz Suwon
h = by_id["suwon-hotel-biz"]
h["verification"]["lastChecked"] = "2026-08-30"
h["verification"]["note"] = (h["verification"].get("note", "") +
    " | UPDATE 2026-08-30: Agoda property page FETCHED LIVE — 2★, 8.5/10 from 11 reviews (matches the stored index figure ✓), address confirmed 16565, "
    "Suwon City Hall Station 980 m. ODDITY FLAGGED: Agoda's facilities list includes a 'Swimming pool' for this small business hotel (travelmyth copy agreed); "
    "not corroborated anywhere else — flagged only, not promoted to the amenities list.")
h["secondarySource"] = {
    "platform": h["secondarySource"].get("platform", "Agoda"),
    "url": "https://www.agoda.com/hotel-biz-suwon/hotel/suwon-kr.html",
    "status": "verified",
    "lastCheckedUtc": "2026-08-30",
    "checkMethod": "property-page-fetched",
    "note": ("FETCHED LIVE 2026-08-30: 2★, 8.5/11 ✓ (index figure agreed), address ✓ 16565; City Hall Stn 980 m. "
             "Flagged: 'Swimming pool' appears in Agoda facilities — single-source, unverified elsewhere, treated as suspicious for a 2★. No dated USD rates on the page."),
}

# ---------------------------------------------------------------- 9. BW Premier Gangnam — downgrade (dead stored URL)
h = by_id["seoul-bw-premier-gangnam"]
h["secondarySource"] = {
    "platform": h["secondarySource"].get("platform", "Agoda"),
    "url": None,
    "status": "unresolved",
    "lastCheckedUtc": "2026-08-30",
    "checkMethod": "search-index",
    "note": ("DOWNGRADED from 'verified' 2026-08-30: the previously stored URL "
             "https://www.agoda.com/best-western-premier-gangnam/reviews-page-24/seoul-kr.html (a search-index-era deep link) now 302s to Agoda's pagenotfound — "
             "the saved URL is DEAD even though the listing itself demonstrably exists (KAYAK quotes Agoda 8.3/71; Agoda deal rows surface via index). "
             "Repo rule: 'verified' requires the STORED URL to fetch live — a stale deep-link cannot carry verified status. URL removed per schema (non-verified statuses must not carry URLs); "
             "resolve to the canonical /hotel/kr page manually and re-verify."),
}

# ---------------------------------------------------------------- 10. The Coolest Songjeong — not-on-sale PROVEN
h = by_id["busan-coolest-songjeong"]
h["distributionStatus"]["status"] = "Not bookable on Booking.com (PROVEN by live fetch 2026-08-30)"
h["distributionStatus"]["asOf"] = "2026-08-30"
h["distributionStatus"]["evidence"] = ("2026-08-30 dated fetch: the Booking property URL redirects to the Busan city searchresults page (486 properties listed for Nov 9–15) "
                                       "instead of a property page — live confirmation of the prior index-copy 'not on sale' status (no longer just suspected). "
                                       "Property identity remains verified via Google/Tripadvisor copies; Booking/Agoda sellability: Booking NO (proven).")
h["verification"]["lastChecked"] = "2026-08-30"
h["verification"]["note"] = (h["verification"].get("note", "") +
    " | 2026-08-30: dated-URL redirect to search results live-confirmed the not-on-sale status (evidence class upgrade: suspicion → proof).")

# ---------------------------------------------------------------- 11. Toyoko Busan Seomyeon — Booking page LIVE, sold out
h = by_id["busan-toyoko-seomyeon"]
h["checkIn"] = "From 15:00 to 24:00; photo ID + credit card required at check-in; advise arrival time in advance (Booking house rules, fetched live 2026-08-30)"
h["checkOut"] = "Until 10:00 — Booking house rules, fetched live 2026-08-30"
h["hasOnSiteLaundry"] = True
h["amenities"] = (h.get("amenities") or []) + [
    "Laundry listed in Booking 'Most popular amenities' (fetched 2026-08-30); guests mention coin washer/dryer for a small fee",
    "Non-smoking rooms, accessible facilities, free Wi-Fi, 24-hour front desk, breakfast (guests: buffet, varies daily) — Booking amenities, fetched 2026-08-30",
]
h["policies"] = (h.get("policies") or []) + [
    "No cribs / no extra beds; children 13+ charged as adults; guests under 19 need a legal guardian (Booking house rules + fine print, fetched 2026-08-30).",
    "Pets not allowed. Parking available but limited ('subject to availability', fine print). License 6058536106. Payment: AmEx/Visa/MC/JCB/Maestro/BC/cash.",
]
h["priceNote"] = ("Still not captured with a proven reason: the dated Booking page (Nov 9–15) was FETCHED LIVE 2026-08-30 — every room row reads "
                  "'Not available on our site for your dates' + 'Limited supply in Busan for your dates: 21 hotels like this are already unavailable' — "
                  "sold out for our window, not a dead link. Try other dates or Toyoko's own site.")
h["refundableRate"] = {
    "capturedAtUtc": "2026-08-30T01:48:30Z",
    "source": "Booking.com property page (dated availability check, live fetch 2026-08-30)",
    "sourceUrl": dated("toyoko-inn-seomyeon", "2026-11-09", "2026-11-15"),
    "stayCheckIn": "2026-11-09", "stayCheckOut": "2026-11-15", "nights": 6,
    "available": False,
    "finding": "Property page LIVE but every captured room row reads 'Not available on our site for your dates' (Deluxe Twin, Standard Twin etc. enumerated); zero rates shown for Nov 9–15.",
}
h["fits"] = False
h["fitReason"] = ("Core needs (1 room, 1 large bed, private bath) plausibly met by the chain's usual layout, and the live page enumerates 'Deluxe Twin Room — 1 full bed + 1 queen bed' "
                  "(queen ✓, two-bed ✗), but with zero rates/availability for our window the fit stays unconfirmed; do not treat as bookable.")
h["distributionStatus"]["status"] = "On Booking (page live, SOLD OUT for our window 2026-11-09→15) — fetched 2026-08-30"
h["distributionStatus"]["asOf"] = "2026-08-30"
h["distributionStatus"]["evidence"] = ("Live dated fetch 2026-08-30 of the record's own compareUrl: full property page renders (8.3/10 from 2,237 reviews; staff 8.9, facilities 8.4, clean 8.7, "
                                       "comfort 8.6, value 8.8, location 8.7, wifi 8.8; facilities score 8.4) but no rooms available. Correction to the earlier round: a DIFFERENT guessed slug "
                                       "(toyoko-inn-busan-seomyeon) 404s — the correct slug is toyoko-inn-seomyeon as stored.")
h["verification"]["lastChecked"] = "2026-08-30"
h["verification"]["note"] = (h["verification"].get("note", "") +
    " | UPDATE 2026-08-30: Booking page fetched live at the stored URL → operating & bookable in principle, score 8.3/2,237 captured with all sub-scores; "
    "house rules confirm 15:00–24:00 check-in (ID+card), 10:00 check-out, laundry, limited parking, license 6058536106. Sold out for Nov 9–15 (no rates). "
    "Lesson noted: probing near-miss slug 'toyoko-inn-busan-seomyeon' 404s — slug traps cut both ways.")
h["secondarySource"]["note"] = (h["secondarySource"].get("note", "") +
    " | 2026-08-30: Booking side fetched live (page up, sold out for window). Agoda URL still unresolved (deal lines via momondo unchanged).")

# ---------------------------------------------------------------- 12. Crown Park Seoul Myeongdong — guessed-slug redirect, status stays unresolved
h = by_id["seoul-crown-park-myeongdong"]
h["distributionStatus"]["status"] = (h.get("distributionStatus") or {}).get("status", "Agoda/Booking sellability unresolved")
h["distributionStatus"]["asOf"] = "2026-08-30"
h["distributionStatus"]["evidence"] = ((h.get("distributionStatus") or {}).get("evidence", "") +
    " | 2026-08-30 probe: a GUESSED Booking slug /hotel/kr/crown-park-seoul.html 301-redirects to Booking's Seoul searchresults with a 'closed_msg' parameter. "
    "That is Booking's generic redirect for an unmatched/unavailable hotel slug — it does NOT prove closure (the stored property URL was never such a Booking page) and was explicitly not treated as closure evidence. "
    "KAYAK remains the only linked source; direct Booking presence: unknown (do not re-probe guessed slugs).")
h["secondarySource"]["note"] = (h["secondarySource"].get("note", "") +
    " | 2026-08-30: no new Agoda URL surfaced; the guessed-Booking-slug redirect was logged as inconclusive (see distributionStatus.evidence). Status stays unresolved honestly.")

json.dump(data, open(DATA, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("patched", len(by_id), "records; data file rewritten")
