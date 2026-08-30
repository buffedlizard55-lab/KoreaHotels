#!/usr/bin/env python3
"""Round-15 data write (2026-08-30): dual-source expansion + 20 new entries.

Two steps, one shot:
  1. Apply the reviewed Agoda secondarySource table (tools/secondary_sources_2026-08-30.json)
     to the 26 Busan records checked this round.
  2. Append 20 new hotel records. Every identity fact below was read from a
     Booking.com / Agoda.com / official-site page that the search layer returned
     in the 2026-08-30 round (index copy incl. JSON-LD address blocks and hasMap
     coordinates). No dated rates were captured because the page-fetch tool was
     down all session; those records say so explicitly and priceFrom/priceTo stay null.

Run: python3 tools/add_entries_2026-08-30.py
Idempotent: re-running skips records that already exist.
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "hotels.json")
SRC = os.path.join(ROOT, "tools", "secondary_sources_2026-08-30.json")
DATE = "2026-08-30"
NO_RATE = "No dated capture in this round — the page-fetch tool was down on 2026-08-30, so no Nov window rates were read. Index 'from $X' figures seen in search results are for upcoming dates (not our stay windows) and are deliberately NOT stored as plan pricing."

def dist(evidence):
    return {"status": "Listed on Booking.com, no dated capture in this round", "asOf": DATE, "evidence": evidence}

def secondary(status, note, url=None):
    s = {"platform": "Agoda", "status": status, "lastCheckedUtc": DATE, "checkMethod": "search-index", "note": note}
    if url:
        s = {"platform": "Agoda", "url": url, "status": status, "lastCheckedUtc": DATE, "checkMethod": "search-index", "note": note}
    return s

def rec(**k):
    h = {
        "id": k["id"], "city": k["city"], "name": k["name"], "tier": k["tier"], "stars": k.get("stars"),
        "area": k["area"], "neighborhood": k["neighborhood"], "address": k["address"],
        "priceFrom": k.get("priceFrom"), "priceTo": k.get("priceTo"), "currency": "USD",
        "checkIn": k.get("checkIn", "Not captured in the 2026-08-30 round — confirm on the dated page"),
        "checkOut": k.get("checkOut", "Not captured in the 2026-08-30 round — confirm on the dated page"),
        "policies": k.get("policies", ["Room inventory, cancellation terms, and inclusions vary by rate; confirm them on the official booking page."]),
        "rooms": k.get("rooms", []),
        "promos": k.get("promos", ["Check the dated Booking.com page (and the Agoda page where linked) for live offers in this round; none were captured 2026-08-30."]),
        "amenities": k.get("amenities", []),
        "hasOnSiteLaundry": k.get("hasOnSiteLaundry", False),
        "officialUrl": k.get("officialUrl"), "officialLabel": k.get("officialLabel"),
        "compareUrl": k["compareUrl"], "compareLabel": k["compareLabel"],
        "why": k["why"], "highlights": k["highlights"],
        "fits": False,
        "fitReason": k.get("fitReason", "Planner fit not assessed — no dated room/bed capture in the 2026-08-30 round (fetch tool down); identity verified only."),
        "lat": k["lat"], "lng": k["lng"],
        "priceNote": k.get("priceNote", NO_RATE + (" Booking.com index copy (2026-08-30): " + k["idxPrice"] if k.get("idxPrice") else "")),
    }
    if k.get("stationWalkTime"): h["stationWalkTime"] = k["stationWalkTime"]
    if k.get("phone"): h["phone"] = k["phone"]
    if k.get("address"): h["address"] = k["address"]
    h["verification"] = {
        "lastChecked": DATE, "sourceType": k.get("sourceType", "Booking.com property index page (search-index capture)"),
        "sourceUrl": k["sourceUrl"], "canonicalName": k["canonicalName"],
        "existenceStatus": "Verified operating property",
        "note": k["vnote"],
    }
    h["distributionStatus"] = k.get("distributionStatus", dist(k.get("distEvidence", "Booking.com property page located in the 2026-08-30 search index; page not re-fetched (fetch tool down), so no window rates stored.")))
    h["secondarySource"] = k["secondary"]
    return h

# ---------------------------------------------------------------- 20 new records
R = []

R.append(rec(
    id="seoul-signiel", city="Seoul", name="Signiel Seoul", tier="luxury", stars=5,
    area="Jamsil / Songpa (Lotte World Tower)", neighborhood="Floors 76–101 of Lotte World Tower",
    address="300 Olympic-ro, Songpa-gu, Seoul 05551", lat=37.512573, lng=127.102608,
    idxPrice="from US$469/night for upcoming dates (2 adults), review snapshot 9.2/928",
    compareUrl="https://www.booking.com/hotel/kr/signiel-seoul.html", compareLabel="Open property page (Booking.com)",
    sourceUrl="https://www.booking.com/hotel/kr/signiel-seoul.html",
    canonicalName="Signiel Seoul",
    amenities=["Indoor pool (KAYAK snapshot of the Booking listing — not reconfirmed this round)"],
    why="Seoul's skyline-floor luxury pick, attached to Lotte World Tower and Jamsil; the only record whose Agoda page was found at property level in the Seoul pass.",
    highlights=["Floors 76–101, 235 rooms", "Direct Lotte World Mall access", "Agoda property page located"],
    vnote="Booking.com index page (title, 5-star class, 'from $469 upcoming') + Agoda's own property page (address 300 Olympic-ro 05551, 235 rooms floors 76–101) cross-match exactly; coordinates from Agoda map data. FLAGGED: an aggregator (momondo) shows a landmark-side pin 37.5684/127.00864 for a related listing — NOT used here. Check-in 15:00 / check-out 11:00 only seen via KAYAK (unconfirmed).",
    secondary=secondary("verified", "Agoda property page surfaced in search index via its es-mx locale variant; canonical locale-less URL stored. Agoda 9.3/10 from 6,360 reviews quoted on the indexed page. Canonical URL still needs a direct fetch-confirm (fetch tool down 2026-08-30).", url="https://www.agoda.com/signiel-seoul/hotel/seoul-kr.html")))

R.append(rec(
    id="seoul-lotte-world", city="Seoul", name="Lotte Hotel Seoul", tier="luxury", stars=5,
    area="Jamsil / Songpa", neighborhood="Atop Jamsil Station, beside Lotte World",
    address="240 Olympic-ro, Songpa-gu, Seoul 05554", lat=37.5114833, lng=127.1001810,
    idxPrice="from US$220–229/night for upcoming dates",
    compareUrl="https://www.booking.com/hotel/kr/lotte-world.html", compareLabel="Open property page (Booking.com)",
    sourceUrl="https://www.booking.com/hotel/kr/lotte-world.html",
    canonicalName="Lotte Hotel World",
    amenities=["Indoor pool", "Free parking (Booking.com index copy)"],
    why="The landmark five-star on the Han River east side; family-friendly, directly above Jamsil Station.",
    highlights="Flagged index copy shows a 'Family 2 Beds' room name (guestreservations mirror)".split("|") if False else ["Above Jamsil Station", "Indoor pool & free parking per index copy", "Score snapshot drift recorded"],
    vnote="Booking index JSON-LD gives address 240 Olympic-ro 05554 and hasMap coordinates 37.5114833/127.1001810. FLAGGED: review-score snapshots disagree across locale pages captured the same day (8.8/1,352 vs 8.5/760) — recorded, not overwritten. guestreservations mirror lists a 'Family 2 Beds' room (bed evidence pending a dated capture).",
    secondary=secondary("unresolved", "KAYAK cites 'Agoda 9.3/10 · 306 reviews' and shows Agoda deal lines, so an Agoda listing is known to exist; no agoda.com URL was surfaced by the 2026-08-30 index searches. Resolve manually from within agoda.com.")))

R.append(rec(
    id="seoul-classic500", city="Seoul", name="The Classic 500 Pentaz Executive Residence", tier="premium", stars=None,
    area="Gwangjin-gu (Konkuk Univ.)", neighborhood="Sky residence floors in Pentaz complex",
    address="90 Neungdong-ro, Gwangjin-gu, Seoul 05065", lat=37.5384012, lng=127.0707276,
    idxPrice="from US$116–171/night for upcoming dates; index copy says breakfast unavailable since 2023-03-01 (temporary)",
    compareUrl="https://www.booking.com/hotel/kr/the-classic-500.html", compareLabel="Open property page (Booking.com)",
    sourceUrl="https://www.booking.com/hotel/kr/the-classic-500.html",
    canonicalName="The Classic 500 Pentaz Executive Residence",
    amenities=["Suites with washer (Booking index rows)"],
    why="Apartment-style suites with washing machines near Seoul Forest / Konkuk Univ. — useful for laundry on a 22-night trip.",
    highlights=["Suites include in-unit washer", "8.6–8.7 snapshot across 506–651 reviews", "Not the Yeouido listing earlier queues guessed"],
    vnote="Booking index page + HotelsCombined/OTA mirrors confirm the property at 90 Neungdong-ro, Gwangjin-gu (NOT Yeouido as an earlier held-out note guessed). Score snapshots 8.6–8.7 across 506–651 reviews. FLAGGED: Booking index copy carries a standing notice that breakfast is unavailable since 2023-03-01 (temporary) — recheck at booking time.",
    secondary=secondary("unresolved", "Agoda listing exists (HotelsCombined shows an Agoda.com deal line at $140/night); no agoda.com URL surfaced by 2026-08-30 index searches. Resolve manually.")))

R.append(rec(
    id="seoul-tmark-myeongdong", city="Seoul", name="Tmark Grand Hotel Myeongdong", tier="upper", stars=4,
    area="Myeongdong / Hoehyeon", neighborhood="Opposite Namdaemun Market, Hoehyeon Stn exit 3 at the door",
    address="52 Toegye-ro, Jung-gu, Seoul 04634", lat=37.5625, lng=126.9925613,
    idxPrice="from US$150–258/night for upcoming dates — but the index copy states the property is not taking reservations right now",
    compareUrl="https://www.booking.com/hotel/kr/tmark-grand-myeongdong.html", compareLabel="Open property page (Booking.com)",
    sourceUrl="https://www.booking.com/hotel/kr/tmark-grand-myeongdong.html",
    canonicalName="Tmark Grand Hotel Myeongdong",
    distributionStatus={"status": "On Booking but not taking reservations (index 2026-08-30)", "asOf": DATE,
                        "evidence": "Booking.com index copy states: 'This property isn't taking reservations on our site right now.' No dates, rates or room claims recorded from Booking until it reopens for sale."},
    sourceType="Booking.com property index page (search-index capture) + Agoda cross-check",
    amenities=["2 restaurants & café, indoor pool & gym (Google Hotels copy — NOT reconfirmed on a fetched Booking page)"],
    why="Prime Myeongdong/Namdaemun location kept out of the sold column: listed on Booking but currently not sellable there — recorded honestly instead of guessed.",
    highlights=["Airport bus stop at the front door", "8.6/839 snapshot when bookable", "Not-taking-reservations status captured"],
    vnote="Booking index page gives 52 Toegye-ro 04634 + 'not taking reservations right now' + snapshot 8.6/839; coordinates from the Booking map data mirrored by Trivago (37.5625/126.9925613). FLAGGED: do not confuse with 'Tmark Hotel Myeongdong' (43 Chungmuro 3-ga / 15 Chungmu-ro), a different, smaller property. Google's entity uses the lot address '194-15 Hoehyeon-dong 1(il)-ga' for the same building.",
    secondary=secondary("not-found", "Two Agoda index queries (2026-08-30) surfaced no agoda.com property page for the Grand; only third-party mirrors (trivago, traveloka, seoul-hotels-kr). Existence on Agoda is NOT confirmed — blank, not a verified absence. Also unverified: 4-star class (Trivago mirror only).")))

R.append(rec(
    id="seoul-crown-park-myeongdong", city="Seoul", name="Crown Park Hotel Seoul Myeongdong", tier="upper", stars=None,
    area="Namdaemun / Hoehyeon", neighborhood="7-gil off Namdaemun-ro, convenience stores downstairs",
    address="19 Namdaemun-ro 7-gil, Jung-gu, Seoul 04568 (old-format 10456 in Booking copy)", lat=37.5638278, lng=126.9808978,
    idxPrice="from US$143–171/night for upcoming dates",
    compareUrl="https://www.kayak.com/Seoul-Hotels-Crown-Park-Hotel-Seoul-Myeongdong.2042753.ksp", compareLabel="Compare rates (KAYAK)",
    sourceUrl="https://www.booking.com/hotel/kr/crown-park.html",
    canonicalName="Crown Park Hotel Seoul Myeongdong",
    amenities=[],
    why="Large 204-room Myeongdong-edge hotel; guest reports of on-site laundry floors fit the laundry priority — pending confirmation from a fetched facilities list.",
    highlights=["204 rooms, opened Oct 2015 (Tripadvisor structured copy)", "Laundry reportedly on floor 7 (guest text, unconfirmed)", "Score snapshots 8.3/4,264–8.5/3,976"],
    vnote="Booking index JSON-LD: address 19 Namdaemun-ro 7-gil, hasMap 37.5638278/126.9808978, snapshots 8.3/4,264 vs 8.5/3,976 (flagged drift, both kept). Tripadvisor structured copy adds 204 rooms / Oct-2015 opening. FLAGGED: the floor-7 laundry claim comes from a guest review, not a facilities list — hasOnSiteLaundry deliberately stays false until confirmed; phone +82 2-750-5900 seen on Google's entity.",
    secondary=secondary("unresolved", "Agoda listing exists (Google Hotels shows an 'Agoda $139' line and Tripadvisor shows 'Agoda.com $161–203' deal rows); no agoda.com URL surfaced in the 2026-08-30 index round. Resolve manually.")))

R.append(rec(
    id="seoul-toyoko-gangnam", city="Seoul", name="Toyoko Inn Seoul Gangnam", tier="budget", stars=None,
    area="Gangnam / Seocho (Gangnam Stn)", neighborhood="On Gangnam-daero by the airport-bus 6009 stop",
    address="323 Gangnam-daero, Seocho-gu, Seoul 06627", lat=37.491822, lng=127.0299,
    idxPrice="from US$64/night for upcoming dates",
    compareUrl="https://www.kayak.com/Seoul-Hotels-Toyoko-Inn-Seoul-Gangnam.4079576.ksp", compareLabel="Compare rates (KAYAK)",
    sourceUrl="https://www.booking.com/hotel/kr/toyoko-inn-seoul-gangnam.html",
    canonicalName="Toyoko Inn Seoul Gangnam",
    amenities=["Free breakfast (chain standard + guest quotes — NOT confirmed on a fetched page this round)"],
    why="Reliable Toyoko pricing one metro stop from Gangnam Station; the index shows a two-beds room photo (twin layout available).",
    highlights=["1–2 min to airport bus 6009 stop", "8.3/2,923–8.4/2,360 snapshot drift", "Chain-standard breakfast on request — unconfirmed"],
    vnote="Booking index page: 323 Gangnam-daero 06627, hasMap 37.491822/127.0299, 'from $64', score snapshots 8.3/2,923 and 8.4/2,360 (drift recorded). KAYAK shows an Agoda line 8.8/129. FLAGGED: the free-breakfast claim is chain policy + guest quotes, not a captured Booking rate row.",
    secondary=secondary("unresolved", "Agoda listing exists (KAYAK provider scores 'Agoda.com 8.8/10 · 129 reviews'); no agoda.com URL in the 2026-08-30 index round. Resolve manually.")))

R.append(rec(
    id="seoul-bw-premier-gangnam", city="Seoul", name="Best Western Premier Gangnam Hotel", tier="mid", stars=None,
    area="Gangnam (Shinnonhyeon)", neighborhood="5-min walk to Shinnonhyeon Stn (Line 9)",
    address="139 Bongeunsa-ro, Gangnam-gu, Seoul 06122", lat=37.5063002, lng=127.0298910,
    idxPrice="from US$103–108/night for upcoming dates",
    officialUrl="https://en.bestwesterngangnam.com/", officialLabel="Official property site (bestwesterngangnam.com)",
    compareUrl="https://www.kayak.com/Seoul-Hotels-Best-Western-Premier-Gangnam.88441.ksp", compareLabel="Compare rates (KAYAK)",
    sourceUrl="https://www.booking.com/hotel/kr/bestwestern-premier-gangnam.html",
    canonicalName="Best Western Premier Gangnam Hotel",
    phone="+82 2-6474-2000",
    amenities=["Free parking (Booking index copy)", "5-min walk to Shinnonhyeon Stn"],
    why="Gangnam business hotel with an index copy photo of a two-beds room; the official site confirms address and phone, and its Agoda review page was found at URL level.",
    highlights=["Official site + Booking + Agoda pages all agree on 139 Bongeunsa-ro", "8.1/2,111 Booking snapshot", "Single rooms sell as '1 Single Bed, Standard'"],
    vnote="Booking index: address + hasMap 37.5063002/127.0298910 + 'from $103' + 8.1/2,111 (other locale snapshot 8.1/1,568, KAYAK 8.2/867 — drift recorded). Official site (en.bestwesterngangnam.com) confirms the same address, phone +82 2-6474-2000, business no. 229-81-07409. Agoda reviews page title matches.",
    secondary=secondary("verified", "Agoda reviews page surfaced in index: 8.2/10, 3,233 reviews, 'recommended by 88%'; URL stored exactly as indexed (paginated variant). Agoda also shows the same 139 Bongeunsa-ro address block.", url="https://www.agoda.com/best-western-premier-gangnam/reviews-page-24/seoul-kr.html")))

R.append(rec(
    id="seoul-muststay-myeongdong", city="Seoul", name="Must Stay Hotel Myeongdong", tier="budget", stars=None,
    area="Myeongdong / Namdaemun", neighborhood="5-min walk to Namdaemun Market",
    address="15-3 Toegye-ro 2-gil, Jung-gu, Seoul 04635", lat=37.5569046, lng=126.9775906,
    idxPrice="from US$40/night for upcoming dates",
    compareUrl="https://www.kayak.com/Seoul-Hotels-Must-Stay-Hotel-Myeongdong.3527515.ksp", compareLabel="Compare rates (KAYAK)",
    sourceUrl="https://www.booking.com/hotel/kr/seoul-backpackers.html",
    canonicalName="Must Stay Hotel Myeongdong",
    amenities=["Free WiFi throughout (Booking index copy)", "Family rooms"],
    why="Cheap Myeongdong-edge base — kept visible but marked low-fit: its Booking review snapshots are the weakest on this list (4.5/10), which the plan should weigh honestly.",
    highlights=["$40 upcoming-date floor is the lowest in the Myeongdong cluster", "FLAGGED: 4.5/49–25 review snapshot", "Legacy slug 'seoul-backpackers' under current name"],
    vnote="Booking index JSON-LD: 15-3 Toegye-ro 2-gil 04635, hasMap 37.5569046/126.9775906, 'from $40', score 4.5/25 (KAYAK's Booking column shows 4.5/49; momondo blended 6.2/409) — all recorded. FLAGGED: the URL slug is legacy 'seoul-backpackers' while the title is Must Stay Hotel Myeongdong — confirm same building before booking. No bed data captured; fits=false.",
    secondary=secondary("unresolved", "Agoda listing exists (KAYAK 'Agoda.com 6.4/10 · 171 reviews'; HotelsCombined shows Agoda $38–42 deal lines); no agoda.com URL surfaced 2026-08-30. Resolve manually.")))

R.append(rec(
    id="busan-hound-premier-nampo", city="Busan", name="Nampo Hound Hotel Premier", tier="mid", stars=3,
    area="Nampo / Jung-gu", neighborhood="Bosu-daero, short walk to Nampo-dong streets",
    address="24 Bosu-daero, Jung-gu, Busan 48980", lat=35.0991293, lng=129.0253633,
    checkIn="15:00 (Booking index copy: 15:00–23:59)", checkOut="12:00 (Booking index copy)",
    idxPrice="from US$52–66/night for upcoming dates",
    compareUrl="https://www.booking.com/hotel/kr/hound-bupyeong.html", compareLabel="Open property page (Booking.com)",
    sourceUrl="https://www.booking.com/hotel/kr/hound-bupyeong.html",
    canonicalName="Nampo Hound Hotel Premier",
    amenities=["87 rooms (Booking index copy)"],
    phone="+82 51-254-0702",
    why="New-build-feel business hotel in the Nampo/Gwangbok corridor — the old held-out identity blocker is now resolved against Booking's own index data.",
    highlights=["Booking 8.4–8.6 across 613–1,353 reviews", "Phone +82 51 254 0702 from the Booking index block", "FLAGGED: slug says 'bupyeong', address is Jung-gu"],
    vnote="Booking index: title 'Nampo Hound Hotel Premier', 3★, address 24 Bosu-daero 48980, hasMap 35.0991293/129.0253633, check-in 15:00–23:59/out 12:00, 87 rooms, tel +82 51 254 0702; score snapshots 8.4–8.6 across 613–1,353 reviews (drift recorded). FLAGGED: the URL slug 'hound-bupyeong' references a different district than the page address — likely a listing migration; resolve which building the slug's photos show before booking. An HotelsCombined page calls a sister listing 'Hound Premier Nampo' at $37+.",
    secondary=secondary("unresolved", "Agoda listing exists (KAYAK provider score 'Agoda.com 8.9/10 · 337 reviews'; momondo shows Agoda deal lines $36–43); no agoda.com URL in the 2026-08-30 index round. Resolve manually.")))

R.append(rec(
    id="busan-toyoko-seomyeon", city="Busan", name="Toyoko Inn Busan Seomyeon", tier="budget", stars=None,
    area="Seomyeon / Busanjin-gu", neighborhood="6-min walk to Seomyeon Stn exit 8",
    address="39 Seojeon-ro, Busanjin-gu, Busan 47247", lat=35.1579202, lng=129.0640998,
    idxPrice="from US$52/night for upcoming dates",
    compareUrl="https://www.booking.com/hotel/kr/toyoko-inn-seomyeon.html", compareLabel="Open property page (Booking.com)",
    sourceUrl="https://www.booking.com/hotel/kr/toyoko-inn-seomyeon.html",
    canonicalName="Toyoko Inn Busan Seomyeon",
    amenities=["Free breakfast (chain standard + aggregator copy — not confirmed on a fetched page this round)"],
    stationWalkTime="6 min walk to Seomyeon Station exit 8 (aggregator copy)",
    why="Central Seomyeon base connecting lines 1+2, at Toyoko pricing; useful for the Gyeongju-line trips via Bujeon.",
    highlights=["8.4/2,394 Booking snapshot", "Two-branch Busan Toyoko family (this one is Seomyeon; the Station branch is busan-toyoko-station1)", "Free breakfast reported, unconfirmed"],
    vnote="Booking index: 39 Seojeon-ro 47247, hasMap 35.1579202/129.0640998, 8.4/2,394, 'from $52'. southkrhotel aggregator adds the 6-min exit-8 walk + free breakfast (recorded as unconfirmed). Distinct from 'Toyoko Inn Busan Station' (busan-toyoko-station1) — same chain, different building; canonical names differ enough that the validator's fuzzy rule passes, but a human should keep them apart.",
    secondary=secondary("unresolved", "Agoda deal lines seen via momondo ('from $46 Agoda'); no agoda.com URL surfaced 2026-08-30. Resolve manually.")))

R.append(rec(
    id="busan-shilla-seobusan", city="Busan", name="Shilla Stay Seobusan - Gimhae Airport", tier="mid", stars=None,
    area="Gangseo-gu (west Busan / airport side)", neighborhood="Myeongji international-district side, 15 km from Haeundae",
    address="38 Myeongjigukje 7-ro, Gangseo-gu, Busan 46726", lat=35.097057, lng=128.905060,
    idxPrice="8.5/351 Booking snapshot (en-gb page); no dollar floor shown in the captured copy",
    officialUrl="https://www.shillahotels.com/en/shillastay/seobusan", officialLabel="Official site (shillahotels.com)",
    phone="+82-51-661-9000",
    compareUrl="https://www.booking.com/hotel/kr/shillastay-seobusan.en-gb.html", compareLabel="Open property page (Booking.com)",
    sourceUrl="https://www.booking.com/hotel/kr/shillastay-seobusan.en-gb.html",
    canonicalName="Shilla Stay Seobusan - Gimhae Airport",
    amenities=["295 rooms on floors 6–25 (official site)", "Outdoor pool (official site)", "Fitness centre (hotel.com.au copy)"],
    why="The Shilla-quality anchor for airport-side stays and the 2025 held-out 'Seobusan' blocker, now identity-resolved — with a rename chain documented.",
    highlights=["Opened 2021-04-16 (official site)", "295 rooms, floors 6–25", "FLAGGED: multi-platform rename chain — same building"],
    vnote="Official site confirms 295 rooms on floors 6–25, outdoor pool, opening 2021-04-16, phone +82-51-661-9000, address 38 Myeongjigukje 7-ro 46726 (Booking title adds '- Gimhae Airport'). FLAGGED (rename chain): hotel.com.au documents 'Shilla Stay Busan Gimhae Airport - Noksan' as formerly '...Seobusan Gimhae Airport - Noksan', formerly 'Shilla Stay Seobusan' — the '-Noksan' sibling in earlier notes is the SAME property under later names, not a second hotel; coordinates 35.097057/128.905060 come from OTA geo mirrors of the identical address (Booking hasMap not captured). Guest tip captured: check-in lobby on level 5.",
    secondary=secondary("not-found", "Agoda index queries (2026-08-30, incl. the -Noksan and 'Seobusan Gimhae Airport' name variants) surfaced only Trip.com/KAYAK/hotel.com.au copies — no agoda.com page found. Existence on Agoda NOT confirmed; blank means unverified.")))

R.append(rec(
    id="busan-benikea-haeundae", city="Busan", name="Benikea Hotel Haeundae", tier="budget", stars=None,
    area="Haeundae (beach)", neighborhood="Haeundae-haebyeon-ro, between station and beach",
    address="317 Haeundaehaebyeon-ro, Haeundae-gu, Busan 48095", lat=35.1622459, lng=129.1647488,
    idxPrice="7.7/686 Booking snapshot; no dollar floor in captured copy",
    compareUrl="https://www.booking.com/hotel/kr/benikea-haeundae.html", compareLabel="Open property page (Booking.com)",
    sourceUrl="https://www.booking.com/hotel/kr/benikea-haeundae.html",
    canonicalName="Benikea Hotel Haeundae",
    rooms=[
        {"name": "Premium Standard Double", "price": "not captured (no dated capture 2026-08-30)", "note": "Bed label from Booking room rows mirrored on KAYAK", "bed": "queen", "bedType": "queen", "bedSize": None, "oneBed": True, "oneBedOnly": None, "privateBathroom": None, "bedNote": "Booking label '1 queen bed'; physical width never published by a source checked; bath/attic unverified"},
        {"name": "Standard Twin", "price": "not captured (no dated capture 2026-08-30)", "note": "Bed label from Booking room rows mirrored on KAYAK", "bed": "twin", "bedType": "twin", "bedSize": "2 twin beds", "oneBed": False, "oneBedOnly": None, "privateBathroom": None, "bedNote": "Two beds — does not meet the one-bed preference"},
        {"name": "Family Twin", "price": "not captured (no dated capture 2026-08-30)", "note": "Bed label from Booking room rows mirrored on KAYAK", "bed": "double", "bedType": "double", "bedSize": "2 double beds", "oneBed": False, "oneBedOnly": None, "privateBathroom": None, "bedNote": "Two double beds — does not meet the one-bed preference"},
    ],
    amenities=["Room rows seen: Std Twin 2 twins; Deluxe Twin 1 twin + 1 double; Suite Ocean 2 doubles (KAYAK mirror of Booking rows)"],
    why="Beachside-corridor budget option with real bed labels captured (rare for this cluster at this price); the 2025 queue's 'Benikea Premier' name was a misnomer and is corrected here.",
    highlights=["FLAGGED: 'Benikea Premier Haeundae' in older queue notes is wrong — Booking lists 'Benikea Hotel Haeundae'", "Not the repo's Benikea Bay 7 Busan", "Agoda 8.5/156 via KAYAK (URL unresolved)"],
    vnote="Booking index: 317 Haeundaehaebyeon-ro 48095, hasMap 35.1622459/129.1647488, 7.7/686. Room/bed rows come from the KAYAK mirror of this property's Booking listing (row names + bed labels) — recorded, not enriched. FLAGGED: distinct property from 'Benikea Bay 7 Busan' (existing record) despite chain-name similarity; the earlier held-out note calling it 'Premier' matches no current page.",
    secondary=secondary("unresolved", "Agoda listing exists (KAYAK provider line 'Agoda.com 8.5/10 · 156 reviews'); no agoda.com URL in the 2026-08-30 index round. Resolve manually.")))

R.append(rec(
    id="busan-havenue-gwangalli", city="Busan", name="H Avenue Hotel Gwangalli branch", tier="mid", stars=3,
    area="Gwangalli (Millak)", neighborhood="2-min walk to Gwangalli Beach (Booking index copy)",
    address="29 Millaksubyeon-ro, Suyeong-gu, Busan 48283", lat=35.1532487, lng=129.1246539,
    idxPrice="from US$100/night for upcoming dates",
    compareUrl="https://www.booking.com/hotel/kr/h-avnue.html", compareLabel="Open property page (Booking.com)",
    sourceUrl="https://www.booking.com/hotel/kr/h-avnue.html",
    canonicalName="H Avenue Hotel Gwangalli branch",
    amenities=[],
    why="Gwangalli-bridge-view budget mid-range — added with the identity minefield spelled out: this record covers ONLY the Booking 'Gwangalli branch' building at 29 Millaksubyeon-ro.",
    highlights=["FLAGGED: typo'd slug 'h-avnue'", "FLAGGED: three H-Avenue-style listings around Gwangalli — read the identity note before booking", "8.5/263 vs 7.7/368 snapshot drift"],
    vnote="Booking index: title 'H Avenue Hotel Gwangalli branch', 29 Millaksubyeon-ro 48283, hasMap 35.1532487/129.1246539, snapshots 8.5/263 and 7.7/368 (drift recorded). IDENTITY MINEFIELD (why the 2025 round held this out): the same Booking landmark page also lists 'H Avenue Gwanganri Beach' and 'H-Avenue Hotel Haeundae'; Agoda lists 'Busan Gwangalli Beach H Avenue' at a different address (42 Gwanganhaebyeon-ro 278beon-gil, ~90 m away, geo 35.1539726/129.1245422); Expedia shows 'H Avenue Gwangalli Beach' h35795203 (80 rooms). Whether those are separate buildings or listing drift is UNRESOLVED — a human must confirm on-site. This record makes no claim about the other listings.",
    secondary=secondary("unresolved", "An Agoda property page exists under a different address ('Busan Gwangalli Beach H Avenue', 42 Gwanganhaebyeon-ro 278beon-gil) and is NOT asserted to be the same building as this record — the address conflict is the very reason this link stays unresolved. Manual review required; no URL copied across identities.")))

R.append(rec(
    id="busan-coolest-songjeong", city="Busan", name="The Coolest Hotel", tier="mid", stars=3,
    area="Songjeong (Haeundae east)", neighborhood="2–3-min walk to Songjeong Beach",
    address="11 Songjeonggwangeogol-ro, Haeundae-gu, Busan 48073", lat=35.1798800, lng=129.1987930,
    idxPrice="from US$92/night for upcoming dates",
    distributionStatus={"status": "On Booking but not taking reservations (index 2026-08-30)", "asOf": DATE,
                        "evidence": "Booking.com index copy states: 'This property isn't taking reservations on our site right now.' Snapshot scores/addresses are valid but no dated rate may be attributed to Booking."},
    compareUrl="https://www.booking.com/hotel/kr/the-coolest.html", compareLabel="Open property page (Booking.com)",
    sourceUrl="https://www.booking.com/hotel/kr/the-coolest.html",
    canonicalName="The Coolest Hotel",
    amenities=["Outdoor swimming pool", "Free private parking", "Fitness centre", "Bar (all from Booking index copy)"],
    why="Design-forward Songjeong pick opening a new beach district to the plan — but Booking currently can't sell it, and that status is on the card.",
    highlights=["First Songjeong entry in the dataset", "53 rooms, some with private pools (Expedia copy, unconfirmed)", "Score snapshots 8.2/207 · 8.5/174 · 8.6/121"],
    vnote="Booking index: 11 Songjeonggwangeogol-ro 48073, hasMap 35.1798800/129.1987930, 3★, outdoor pool/free parking/gym, snapshots 8.2/207 (en), 8.5/174 (nl), 8.6/121 (en-gb) — drift recorded, all three kept. Expedia copy says 53 individually decorated rooms with private pools — third-party, unconfirmed. Check-in 15:00–23:59 / 11:00 from two aggregator mirrors — left as unconfirmed.",
    secondary=secondary("not-found", "Agoda index query (2026-08-30) returned only third-party mirrors (busanhotelsweb, Expedia h96904083, busanhotels.net) — no agoda.com page found. Existence on Agoda NOT confirmed.")))

R.append(rec(
    id="busan-grabocean-songdo", city="Busan", name="Grab The Ocean Songdo", tier="mid", stars=4,
    area="Songdo (Seo-gu)", neighborhood="Beachfront, steps from Songdo Beach",
    address="97 Songdohaebyeon-ro, Seo-gu, Busan 49269", lat=35.0772420, lng=129.0178550,
    idxPrice="from US$49–55/night for upcoming dates",
    compareUrl="https://www.booking.com/hotel/kr/busan-songdo-hotel.html", compareLabel="Open property page (Booking.com)",
    sourceUrl="https://www.booking.com/hotel/kr/busan-songdo-hotel.html",
    canonicalName="Grab The Ocean Songdo",
    amenities=["Fitness centre", "Restaurant", "Terrace", "Beachfront", "24-hour front desk", "Private parking KRW 3,000/day (all from Booking index copy)"],
    why="Beachfront 4-star on the Songdo strip at mid-strip prices — opens the third beach district (Songdo) the plan lacked.",
    highlights=["FLAGGED: Booking slug still 'busan-songdo-hotel' from the pre-rebrand name", "Parking costs KRW 3,000/day (Booking copy)", "8.8/692 down to 8.1/828 across snapshots"],
    vnote="Booking index: 'Grab The Ocean Songdo' served at the legacy URL slug 'busan-songdo-hotel' — the same URL showed the old title 'Busan Songdo Hotel' in other index copies the same day. FLAGGED: rebrand-in-progress; some aggregators (southkrhotel mirror) still brand it 'Best Western Plus Busan Songdo'. Address/coords from Booking JSON-LD + hasMap (97 Songdohaebyeon-ro 49269; 35.0772420/129.0178550). Score snapshots across locale pages: 8.8/692, 8.4/753, 8.3/759, 8.1/828 — drift recorded. Rooms: 'Asian rooms' praised as roomy in guest text; no bed labels captured.",
    secondary=secondary("not-found", "Agoda index query (2026-08-30) surfaced reseller mirrors (hotelincn, southkrhotel, travelweekly) but no agoda.com page. Existence on Agoda NOT confirmed — manual check recommended given the rebrand confusion.")))

R.append(rec(
    id="daejeon-hotel-onoma", city="Daejeon", name="Hotel Onoma, Daejeon, Autograph Collection", tier="luxury", stars=5,
    area="Yuseong (Expo side)", neighborhood="On the Expo-district edge near Daejeon Expo Park",
    address="1 Expo-ro, Yuseong-gu, Daejeon 34121 (Trivago copy shows 34126)", lat=36.378554, lng=127.387597,
    idxPrice="from US$168/night for upcoming dates",
    compareUrl="https://www.booking.com/hotel/kr/onoma-daejeon-autograph-collection.html", compareLabel="Open property page (Booking.com)",
    sourceUrl="https://www.booking.com/hotel/kr/onoma-daejeon-autograph-collection.html",
    canonicalName="Hotel Onoma, Daejeon, Autograph Collection",
    amenities=["Indoor pool", "Fitness centre", "Free bikes (Booking index copy)"],
    why="Daejeon's Marriott-signature five-star — the quality anchor the Expo/Yuseong cluster lacked.",
    highlights=["8.4–8.6 across 254–272 reviews", "FLAGGED: two coordinate sets in Booking index copies", "FLAGGED: postal-code mismatch 34121 vs 34126"],
    vnote="Booking index: 1 Expo-ro, Yuseong-gu, 5★ Marriott Autograph, from $168, 8.4–8.6/254–272 snapshots. FLAGGED (two divergences, neither overwritten): one index entry's map centre is 36.378554/127.387597, another's is 36.374805/127.3833484 (~450 m apart); Booking's address block says 34121 while the Trivago copy of the same listing shows 34126. A human should settle map pin + postal code on the fetched property page. Breakfast praised in a guest quote on the city page — not a captured rate row.",
    secondary=secondary("not-found", "Agoda index query (2026-08-30) returned only Agoda-priced neighbors inside a Tripadvisor widget — no Onoma agoda.com page. Existence on Agoda NOT confirmed (expected for a new Marriott, but unverified — blank).")))

R.append(rec(
    id="daejeon-skypark-1", city="Daejeon", name="Skypark Daejeon 1", tier="budget", stars=3,
    area="Yuseong (Daedeok Techno Valley)", neighborhood="Inside Daejeon Hyundai Premium Outlet complex",
    address="161 Techno jungang-ro, Yuseong-gu, Daejeon 34030", lat=36.42402, lng=127.395813,
    idxPrice="from US$67–74/night for upcoming dates",
    compareUrl="https://www.booking.com/hotel/kr/skypark-daejeoni.html", compareLabel="Open property page (Booking.com)",
    sourceUrl="https://www.booking.com/hotel/kr/skypark-daejeoni.html",
    canonicalName="Skypark Daejeon 1",
    amenities=["Family rooms with balcony", "Free parking (Booking index copy)"],
    why="Techno-valley chain hotel inside the outlet complex — practical for KAIST/Expo meetings; fills Daejeon's budget tier the repo only had as 6/10 rated options.",
    highlights=["8.4–8.5 across 114–258 reviews", "Sold as 'Hotel Skypark Daejeon Branch 1' on Korean channels", "One source cites 1,318 reviews / 4.9 — different review scale, flagged"],
    vnote="Booking index: 161 Techno jungang-ro 34030, hasMap 36.42402/127.395813, 3★, 8.4–8.5 (114–258 reviews). FLAGGED: world.nol.com (Korea Grand Travel, the chain's Korean distribution) quotes '4.9 stars with 1,318 verified reviews' — a different rating scale/site; recorded, not merged. Booking slug is 'skypark-daejeoni' (trailing Roman Ⅰ) — a slug oddity worth knowing before manual checks.",
    secondary=secondary("not-found", "Agoda index query (2026-08-30) returned the nol/world channel page but no agoda.com page for this branch. Existence on Agoda NOT confirmed.")))

R.append(rec(
    id="daejeon-hotel-icc", city="Daejeon", name="Hotel ICC", tier="budget", stars=None,
    area="Yuseong", neighborhood="1.1 mi from Hanbat Arboretum",
    address="55 Expo-ro 123beon-gil, Yuseong-gu, Daejeon 34125", lat=36.3769037, lng=127.3929656,
    idxPrice="from US$73–112/night for upcoming dates (locale-dependent)",
    compareUrl="https://www.booking.com/hotel/kr/icc.html", compareLabel="Open property page (Booking.com)",
    sourceUrl="https://www.booking.com/hotel/kr/icc.html",
    canonicalName="Hotel ICC",
    policies=[
        "Booking copy: cribs and extra beds are NOT available at this property.",
        "Pets not allowed (Booking index copy).",
        "Room inventory, cancellation terms, and inclusions vary by rate; confirm them on the official booking page.",
    ],
    amenities=["Garden", "Free private parking", "Restaurant", "24-hour front desk", "Currency exchange (Booking index copy)"],
    why="Kept deliberately: a real Booking-indexed Yuseong option near Expo-district venues — but its low, wildly inconsistent review scores are recorded in the card so no one mistakes it for a safe pick.",
    highlights=["Booking shows 'Low score for Daejeon' label in an index copy", "Snapshots range 6.4–7.9/45–52 reviews", "Extra beds unavailable — hard constraint"],
    vnote="Booking index pages captured the same day disagree heavily and ALL are recorded without merging: 7.9/50 (en), 6.6/48 (ru), 6.4/52 (en-gb), 7.3/49 (it) — one page even renders 'Scored 7.7 · 30 reviews' in its header block. FLAGGED: this level of divergence means any booking decision here needs a fresh fetched page, not this index round. Address + hasMap 36.3769037/127.3929656 consistent across locales. An Expedia-adjacent widget shows Agoda $92-101 lines.",
    secondary=secondary("unresolved", "A 'Hotel ICC' Agoda deal line ($92) appears inside an Expedia/Tripadvisor adjacent-properties widget, so an Agoda listing likely exists; no agoda.com URL surfaced. Resolve manually — low-score property, treat with caution.")))

R.append(rec(
    id="cheonan-jtop", city="Cheonan", name="Hotel J-TOP Cheonan", tier="budget", stars=None,
    area="Cheonan downtown (Seobuk-gu)", neighborhood="Geomeundeul alley off the downtown grid",
    address="19 Geomeundeul 3-gil, Seobuk-gu, Cheonan-si 31163", lat=36.811451, lng=127.110756,
    idxPrice="Agoda page shows no dollar floor in the captured snippet; 8.2/10 from 451 reviews",
    distributionStatus={"status": "Not found on Booking.com in the 2026-08-30 index round", "asOf": DATE,
                        "evidence": "Booking.com Cheonan searches returned no J-TOP listing (only generic hotels near the station). Identity verified entirely from the property's Agoda.com page — so the Booking column stays honestly empty for this record."},
    sourceType="Agoda.com property page (search-index capture) — Booking.com listing not found",
    compareUrl="https://www.agoda.com/hotel-j-top-cheonan_2/hotel/cheonan-si-kr.html", compareLabel="Open property page (Agoda)",
    sourceUrl="https://www.agoda.com/hotel-j-top-cheonan_2/hotel/cheonan-si-kr.html",
    canonicalName="Hotel J-TOP Cheonan",
    amenities=["Free on-site parking (Agoda property copy)", "Location rated 8.8 'Excellent' (Agoda copy)"],
    why="Adds a downtown-Cheonan option (the repo's Cheonan set clusters around the station/A San edge); the one new entry whose PRIMARY identity source is Agoda because Booking has no listing.",
    highlights=["8.2/451 Agoda snapshot", "Agoda property page is the verified source — flagged as the primary", "Map centre from Agoda's own hasMap data"],
    vnote="Agoda property page (en-gb variant indexed): title 'Hotel J-TOP Cheonan', 19 Geomeundeul 3-gil, Seobuk-gu, 31163, geo 36.8114510/127.1107559, 8.2/10 · 451 reviews, free car park. No Booking.com listing found in this round (searched several variants incl. the city page) — recorded as absence-in-index, not as verified absence. URL pattern carries '_2' — a sibling listing may exist; a human should check whether 'Hotel J-TOP Cheonan' without _2 is a different building.",
    secondary=secondary("verified", "For this record the Agoda page IS the primary identity source (see verification); stored here to keep the dual-source column complete. Page seen as the en-gb locale variant; canonical locale-less URL stored — fetch-confirm pending (fetch tool down).", url="https://www.agoda.com/hotel-j-top-cheonan_2/hotel/cheonan-si-kr.html")))

R.append(rec(
    id="suwon-hotel-biz", city="Suwon", name="Hotel Biz Suwon", tier="budget", stars=2,
    area="Gwonseon-gu (Suwon City Hall side)", neighborhood="2.7 mi from Hwaseong Fortress",
    address="10 Gyeongsu-daero 335beon-gil, Gwonseon-gu, Suwon 16565", lat=37.25694, lng=127.0215,
    idxPrice="Booking landmark page shows 'from $54.76, 1 night, 2 adults'; Agoda shows 8.5/11 reviews",
    compareUrl="https://www.booking.com/reviews/kr/hotel/biz-suwon.html", compareLabel="Open reviews page (Booking.com)",
    sourceUrl="https://www.booking.com/reviews/kr/hotel/biz-suwon.html",
    canonicalName="Hotel Biz Suwon",
    amenities=["Free parking", "Air-conditioned rooms with private bathroom", "Free Wi-Fi (Booking landmark copy)"],
    why="Adds a Gwonseon-district Suwon base near the City Hall business cluster — flagged clearly as micro-review territory (5–8 reviews) so it is never over-trusted.",
    highlights=["Booking shows '10/10 Exceptional' but on only 5–8 reviews — sample size recorded", "Newly-opened badge on Trip.com copy", "Agoda self-declared 2-star"],
    vnote="Booking index evidence: the property's page on Booking's own Suwon-station/University landmark listings (title, 'from $54.76', '10 Exceptional · 6–8 reviews', address 2.7 mi from Hwaseong Fortress) plus its Booking reviews page (10 Gyeongsu-daero 335beon-gil 16565). FLAGGED: review base is tiny and the score snapshots swing (Booking '10/10' on 6 reviews vs 4.x-style elsewhere) — treat everything except the address as provisional. Coordinates 37.25694/127.0215 from the Agoda property map; travelmyth adds lot address 권선구 권선동 991-9. A separate 'Suwon Station BIZ Hotel' exists (Paldal-gu) — different property, do not merge.",
    secondary=secondary("verified", "Agoda property page surfaced in index: title + identical address + 8.5/11 reviews + self-declared '2 stars (property-provided)'. Fetch-confirm of the stored URL still pending (fetch tool down 2026-08-30).", url="https://www.agoda.com/hotel-biz-suwon/hotel/suwon-si-kr.html")))

assert len(R) == 20, len(R)

def main():
    data = json.load(open(DATA, encoding="utf-8"))
    hotels = data["hotels"]
    have = {h["id"] for h in hotels}

    # Step 1: apply Busan secondarySource table
    src = json.load(open(SRC, encoding="utf-8"))
    applied = 0
    for h in hotels:
        if h["id"] in src and "secondarySource" not in h:
            h["secondarySource"] = src[h["id"]]
            applied += 1

    # Step 2: append new records (skip existing ids → idempotent)
    added = 0
    for r in R:
        if r["id"] in have:
            print("skip (exists):", r["id"]); continue
        hotels.append(r); added += 1

    data["meta"]["verifiedHotelRecords"] = len(hotels)
    data["meta"]["hotelResearchLastChecked"] = DATE
    data["meta"]["secondarySourceLastChecked"] = DATE
    data["meta"]["round15"] = ("2026-08-30: +20 identity-verified new entries (Seoul 8, Busan 7, Daejeon 3, "
                                "Cheonan 1, Suwon 1); 26 Busan + 20 new records carry Agoda secondarySource "
                                "statuses; remaining 115 records stay in the validate.py queue until checked. "
                                "No dated pricing captured (fetch tool down).")
    tmp = DATA + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    os.replace(tmp, DATA)
    print(f"secondarySource applied: {applied}; new records added: {added}; total hotels: {len(hotels)}")

if __name__ == "__main__":
    main()
