# Seoul · Myeongdong · Suwon — Independent Line-by-line Verification (Pass 3, 2026-08-18)

**Verifier:** independent agent, fresh live fetches 2026-08-18
**Scope:** 20 Seoul/Myeongdong + 5 Suwon hotels in `data/hotels.json` (25 records)
**Dates used for pricing:** Seoul/Myeongdong **Nov 1–9, 2026** (8 nights, 2 adults, 1 room); Suwon uses the same window as an anchor.

## What "verified" means in this pass

Three different classes of fact are checked per hotel, and they are **not** equally re-verifiable from a static fetch:

| Fact | How verified this pass | Confidence |
|---|---|---|
| **Identity / address / star rating / room names** | Official Accor, Marriott, Lotte, Nine Tree, Shilla, Ascott pages + Booking/OTA listings, fetched live | High |
| **Bed size & bed count** | Official room-spec pages (Accor bedding fields, Nine Tree mm specs, Marriott room-pool codes, Ascott JSON-LD) + Booking room tables | High (where a spec/measurement is published) |
| **Refundable status & current price** | These are **dynamic**. The repo carries timestamped Booking.com captures from 2026-08-18 (`refundableRate` blocks). I could **not** independently re-read Booking's live dated rate table this session (Booking serves it via JS/login and it changes continuously). | Snapshot only — **re-open the linked page before paying** |

> ⚠️ **Honesty note:** "Real current pricing" cannot be pinned to a static number. Every price below is either (a) the repo's own UTC-timestamped capture from 2026-08-18, or (b) an OTA "from $" anchor. Treat all of them as a **snapshot**, and always re-open the linked official booking page for the live total and cancellation terms. I have **not** fabricated or rounded any number that I could not read from a source.

---

## 1. Seoul / Myeongdong — 20 hotels

Legend: ✅ verified · ⚠️ irregularity · 🔗 manual-verification link

| # | Hotel (data ID) | Bed size & count (verified) | Refundable / price snapshot | Status |
|---|---|---|---|---|
| 1 | **L7 MYEONGDONG by LOTTE** (`seoul-l7-myeongdong`) | Standard/Superior Double = **1 full/double bed**; Standard/Superior Twin = 2 singles; **Hollywood Double = 2 single beds joined**; Family Twin; suites. **No queen room exists.** (Booking room table, fetched live) | Capture: Standard Double $295/nt, free-cancel before Oct 29. | ✅ data corrected; ⚠️ Hollywood = 2 joined singles |
| 2 | **Nine Tree by Parnas MD 1** (`seoul-nine-tree`) | **Standard Double = 더블 160×190 cm (queen-width)**; **Hollywood Double = 싱글 110×190 cm ×2 (two joined singles)**; Standard Twin = 2 singles. Check-out **12:00** (not 11:00). (Official Korean room spec, fetched live) | Capture: "Double Room" $205/nt, free-cancel before Oct 29. | ✅ corrected this pass; ⚠️ Hollywood mislabeled as "queen" before |
| 3 | **ibis Styles Ambassador Seoul Myeongdong** (`seoul-ibis-styles`) | **4★**, 302 Samil-daero, 180 rooms. Standard 1 Double (16 m², "1 x Double bed(s)"), Standard 2 Single, Superior 1 Double (24 m²). (Accor /9771, fetched live) | Capture: Standard Double $187/nt, free-cancel before Oct 31. | ✅ |
| 4 | **ibis Ambassador Insadong** (`seoul-ibis-insadong`) | **3★**, 31 Samil-daero 30-gil, 363 rooms. **Superior "1 Double Bed" = "1 x Queen size bed(s)"** (19 m²); Premium = 1 Queen + 1 Single. (Accor /8002, fetched live) | No Booking availability Nov 1–9 (capture). Book Accor direct. | ✅ queen correction confirmed |
| 5 | **Four Seasons Hotel Seoul** (`seoul-four-seasons`) | Deluxe/Premier = **king** (official category; not re-fetched this pass — Marriott-style JS/rate-limit). | Capture: no Booking availability Nov 1–9. | ✅ (carried) |
| 6 | **Fairmont Ambassador Seoul** (`seoul-fairmont`) | Deluxe King / Corner Deluxe = **king** (official; not re-fetched this pass). | ⚠️ Capture row is **"Fairmont Twin" = 2 twin beds** $583/nt — a genuine refundable, but **2 beds**, not the king room. | ⚠️ captured room ≠ one-bed preference |
| 7 | **Hotel Skypark Myeongdong 3** (`seoul-skypark-myeongdong3`) | Standard Double = **1 double (1400×2000 mm)** (hotel-confirmed, prior capture). | Capture: Double Room $180/nt, free-cancel before Oct 29. | ✅ |
| 8 | **L'Escape, Luxury Collection, Myeongdong** (`seoul-lescape`) | **Lead-in king category on Marriott is "Classic" (roomPoolCode=KING)**; "Deluxe King" = **Amour** (DKNG); also Secret (EKNG/EDDB), Atelier Jr. Suite. (Marriott overview, fetched live) | Capture: "Classic King, 1 king" $305/nt, free-cancel day-of-arrival. | ⚠️ data room name "Deluxe King" ≠ lead-in "Classic King" |
| 9 | **Somerset Palace Seoul** (`seoul-somerset-palace`) | **Studio Executive = "1 queen-size bed" + washer/dryer** (Ascott JSON-LD, fetched live). | ⚠️ Capture row is **"Deluxe Queen — 2 Queen Beds"** $249/nt; the 1-queen Studio total was only partially captured. | ⚠️ captured room = 2 beds |
| 10 | **ibis Ambassador Seoul Myeongdong** (`seoul-ibis-ambassador-myeongdong`) | **3★**, 78 Namdaemun-ro. Standard 1 double = "1 x Double bed(s)" (21 m²); 2-single; Junior Suite 1 double. (Accor /6317, fetched live) | Capture: Standard Double $313/nt (refundable) vs $266/nt non-refundable. | ✅ |
| 11 | **Moxy Seoul, Myeongdong** (`seoul-moxy-myeongdong`) | Lead-in **"Queen Guest Room" = 1 queen**; "2 Double" also exists. Booking: "Queen Room w/ City View" = 1 large double; "Queen Room w/ Two Queen Beds" = 2 large doubles. (Booking + Marriott, fetched live) | ⚠️ Capture row is **2-queen** $296/nt; the 1-queen rate not captured. | ⚠️ captured room = 2 beds |
| 12 | **Le Méridien Seoul, Myeongdong** (`seoul-le-meridien-myeongdong`) | Deluxe **King** (official; not re-fetched this pass). | Capture: Deluxe King $624/nt (incl. breakfast). | ✅ (carried) |
| 13 | **Aloft Seoul Myeongdong** (`seoul-aloft-myeongdong`) | **"Aloft Room, 1 King"** (official Marriott category; not re-fetched this pass). | ⚠️ **No `refundableRate` block** in data. | ⚠️ missing capture |
| 14 | **Courtyard by Marriott Seoul Myeongdong** (`seoul-courtyard-myeongdong`) | **Guest Room, 1 King** (official; not re-fetched this pass). | Capture: Guest Room 1 King $324/nt, free-cancel day-of-arrival. | ⚠️ Booking slug was 404 in prior pass — re-verify source of capture |
| 15 | **Four Points Josun, Seoul Myeongdong** (`seoul-four-points-myeongdong`) | Deluxe **King** (official; Booking shows cheaper "Superior double = 1 full" lead-in). | ⚠️ **No `refundableRate` block** in data. | ⚠️ missing capture |
| 16 | **Nine Tree by Parnas MD 2** (`seoul-nine-tree-myeongdong2`) | 408 rooms. Rooms incl. **Hollywood Double, Standard Double, Sky Double, Premier Double**, Standard Twin, Family Twin, Triple, suites. (nth2, fetched live) | Capture: "Hollywood Double" $303/nt ("1 king" per Booking). | ⚠️ "Hollywood" = joined mattresses — data lists only Hollywood Double and calls it "king"; physical bed unverified |
| 17 | **Nine Tree by Parnas Insadong** (`seoul-nine-tree-insadong`) | **Official brand is "Nine Tree Premier Hotel Insadong"** (나인트리 프리미어 호텔 인사동). Rooms: Standard Double/Twin/Triple, Family Twin, Family Kids, suites. Bed mm **not published** on the page. (nth3, fetched live) | Capture: "Deluxe Double w/ Jogyesa View" $235/nt ("1 queen"). | ⚠️ name omits "Premier"; Standard Double "queen" not sourced to a measurement |
| 18 | **Shilla Stay Gwanghwamun Myeongdong** (`seoul-shilla-stay-gwanghwamun`) | **Standard Double = 1 full; Hollywood Double = 1 king (per OTA)**; Deluxe Double = 1 double. (OTA listings, fetched live) | ⚠️ Capture row is **"Standard Double (1 full)"** $200/nt — the cheapest one-bed total, but **not** the king Hollywood. | ⚠️ "Hollywood" naming implies joined mattresses; captured room = full bed |
| 19 | **LOTTE HOTEL SEOUL** (`seoul-lotte-hotel`) | **Main Tower Deluxe/Grand Superior Double = "1 full bed"** (Booking). Not a king. (carried; Lotte page JS-heavy) | Capture: Grand Superior Double $364/nt, free-cancel before Oct 29. | ✅ corrected (king→double) |
| 20 | **The Westin Josun Seoul** (`seoul-westin-josun`) | Deluxe **King** (official; not re-fetched this pass). | Capture: Deluxe King $398/nt, free-cancel day-of-arrival. | ✅ (carried) |

---

## 2. Suwon — 5 hotels

| # | Hotel (data ID) | Bed size & count (verified) | Refundable / price snapshot | Status |
|---|---|---|---|---|
| 1 | **Novotel Ambassador Suwon** (`suwon-novotel-ambassador`) | **4★**, 902 Dukyoungdaero, 287 rooms. **Superior 1 King (28 m², "1 x King size bed(s)")**, Superior 2 Single ("2 x Twin"), Deluxe 1 King, Executive King, Junior/Executive Suite King. "Direct access to Suwon KTX & subway". (Accor /8748, fetched live) | ⚠️ **No `refundableRate` block**. Book Accor direct (flexible rates exist). | ✅ identity/king; ⚠️ missing price capture |
| 2 | **Four Points by Sheraton Suwon** (`suwon-four-points`) | 4★ (2022, 221 rooms). **Premier King = king bed; Premier Twin = 2 singles**. (NamuWiki + Marriott, fetched) | ⚠️ **No `refundableRate` block**. Marriott flexible rates exist. | ✅ beds; ⚠️ missing capture |
| 3 | **Ramada Plaza by Wyndham Suwon** (`suwon-ramada-plaza`) | 4★, 150 Jungbu-daero. **"Deluxe King" = "1 Queen Size Bed" on multiple sources**; Superior Double = 1 double; Deluxe Twin = 2 twins. ~12 min **by car** from Suwon Station. (OTA, fetched) | ⚠️ **No `refundableRate` block**; **`officialUrl` = null** (no Wyndham page in data). | ⚠️ King/queen naming mismatch; no official URL |
| 4 | **Courtyard by Marriott Suwon** (`suwon-courtyard`) | 4★ (286 rooms per Booking; data says 288). **Comfortable King = 1 king; Comfortable 2 Double = 2 full**. Gwanggyo New Town (~30 min from Suwon Station/Hwaseong). (Booking, fetched) | ⚠️ **No `refundableRate` block**. Marriott flexible rates exist. | ✅ beds; ⚠️ room count 288 vs 286; missing capture |
| 5 | **ibis Ambassador Suwon** (`suwon-ibis`) | 3★, 132 Kwonkwang-ro (renovated 2021). Standard 1 Double; Standard 2 Twin; Junior Suite 1 King. (Accor ibis Suwon page) | ⚠️ **No `refundableRate` block**. | ⚠️ official URL is a city-search page, not property-specific; missing capture |

---

## 3. Irregularities flagged for review (consolidated + NEW)

**New findings this pass (Pass 3):**

1. **Nine Tree MD1 "Hollywood Double" is not a queen — it is 2 joined single beds.** Official Korean spec: `싱글(1,100×1,900mm) 2EA` = two 110 cm singles pushed together. The data had it as `bedType: queen`, `oneBed: true`, "Single queen bed (not two beds pushed together)". **Corrected this pass.**
2. **Nine Tree MD1 check-out is 12:00, not 11:00.** Official room page says `체크아웃 12:00`. **Corrected this pass.**
3. **Nine Tree MD1 had a non-existent "Deluxe Twin" room.** Actual inventory is "Standard Twin" (2 singles) and "Deluxe Family Twin" (2 doubles). **Corrected to "Standard Twin" this pass.**
4. **Nine Tree Insadong's real brand is "Nine Tree Premier Hotel Insadong"** (official site text), not "Nine Tree by Parnas Seoul Insadong". The "Premier" is missing from the record name.
5. **L'Escape's lead-in king is "Classic King", not "Deluxe King".** On Marriott, "Classic" = roomPoolCode KING; "Deluxe King" is the "Amour" category (DKNG). The data lists "Deluxe King" (which is a real, pricier category) but the captured refundable is the cheaper "Classic King".
6. **Prior "independent" report (`-indy.md`) contains mangled URLs** (`bookig.com`, `grup_adults`, `n_rooms`, `grorup_children`, `checkut`) — treat that report's link list as unreliable; use this pass's links.

**Carried-forward irregularities (still open):**

7. **Refundable captures record the wrong room for the one-bed preference** at Fairmont (2-twin $583), Somerset (2-queen $249) and Moxy (2-queen $296). These are genuine refundables but not single queen/king rooms.
8. **"Hollywood Double" naming** (L7, Nine Tree MD1/MD2, Shilla Gwanghwamun) = **joined mattresses**, conflicting with the repo's "not two beds pushed together" rule. Physical single-mattress status is unverified for the L7/MD2/Shilla variants.
9. **7 hotels have no `refundableRate` block**: Aloft MD, Four Points Josun MD (Seoul) + all **5 Suwon** hotels. These need live pricing/refundability capture before they can be fairly compared.
10. **Ramada Plaza Suwon has `officialUrl: null`** and its "King" rooms are listed as **1 queen** on OTAs — the strongest unresolved identity/bed mismatch in scope.
11. **Korean "double" ≠ 140 cm.** Nine Tree's official "double" is 160 cm (queen-width). The repo's blanket "double ≈ 140 cm → not a fit" rule misclassifies some Korean doubles. (This was already flagged in Pass 1; still true.)
12. **Courtyard Suwon room count** is 286 (Booking) vs 288 (data note) — minor.

---

## 4. Corrections applied to `data/hotels.json` this pass

- `seoul-nine-tree`: `checkOut` 11:00 → **12:00** (and policy line); **Hollywood Double** re-typed to `twin` (2 joined singles), `oneBed/oneBedOnly` false; **"Deluxe Twin" → "Standard Twin"**; `fitReason` updated to reference only the Standard Double; verification note updated with the exact mm specs.
- Arrival-night candidate `seoul-nine-tree-myeongdong-1`: room/tradeoff/bookingNote corrected to point at Standard Double only (Hollywood Double no longer presented as a queen-width bed).
- `validate.py` passes (74/74 records, 0 duplicates).

Not changed (flagged for review, not silently edited): Nine Tree Insadong "Premier" name, L'Escape "Classic vs Deluxe King", the 7 missing `refundableRate` blocks, Ramada Plaza Suwon official URL, and the carried "captured-refundable-is-2-bed" issues.

---

## 5. Manual-verification links (official sources, this pass)

**Accor (official property pages, live-verified):**
- ibis Styles Ambassador Seoul Myeongdong (4★) — https://all.accor.com/hotel/9771/index.en.shtml
- ibis Ambassador Seoul Insadong (3★, Superior = 1 Queen) — https://all.accor.com/hotel/8002/index.en.shtml
- ibis Ambassador Seoul Myeongdong (3★, Standard = 1 Double) — https://all.accor.com/hotel/6317/index.en.shtml
- Novotel Ambassador Suwon (4★, Superior/Deluxe 1 King, direct KTX) — https://all.accor.com/hotel/8748/index.en.shtml

**Nine Tree (official, live-verified):**
- MD1 Standard Double (160×190 cm) — https://www.ninetreehotels.com/nth1/room_standard_double.php
- MD1 Hollywood Double (2×110×190 cm joined) — https://www.ninetreehotels.com/nth1/room_hollywood_double.php
- MD2 room list — https://www.ninetreehotels.com/nth2/?lang=en
- Insadong ("Nine Tree Premier Hotel Insadong") — https://www.ninetreehotels.com/nth3/

**Marriott (official overviews):**
- L'Escape Myeongdong (Classic = King) — https://www.marriott.com/en-us/hotels/sellm-lescape-a-luxury-collection-hotel-seoul-myeongdong/overview/
- Moxy Seoul Myeongdong — https://www.marriott.com/en-us/hotels/selmx-moxy-seoul-myeongdong/overview/
- Aloft Seoul Myeongdong — https://www.marriott.com/en-us/hotels/selmo-aloft-seoul-myeongdong/overview/
- Courtyard Seoul Myeongdong — https://www.marriott.com/en-us/hotels/selsn-courtyard-seoul-myeongdong/overview/
- Four Points Josun Seoul Myeongdong — https://www.marriott.com/en-us/hotels/selfd-four-points-josun-seoul-myeongdong/overview/
- The Westin Josun Seoul — https://www.marriott.com/en-us/hotels/selwi-the-westin-josun-seoul/overview/
- Le Méridien Seoul Myeongdong — https://www.marriott.com/en-us/hotels/selmm-le-meridien-seoul-myeongdong/overview/
- Four Points by Sheraton Suwon — https://www.marriott.com/en-us/hotels/selfo-four-points-suwon/overview/
- Courtyard by Marriott Suwon — https://www.marriott.com/en-us/hotels/selcw-courtyard-suwon/overview/

**Lotte:**
- L7 Myeongdong — https://www.lottehotel.com/myeongdong-l7/en/main.html (JS-heavy; room table via Booking: https://www.booking.com/hotel/kr/l7-myeongdong-by-lotte.html)
- LOTTE HOTEL SEOUL — https://www.lottehotel.com/seoul-hotel/en/rooms

**Other:**
- Somerset Palace Seoul — Studio Executive (1 queen + washer/dryer) — https://www.discoverasr.com/en/somerset-serviced-residence/korea-south/somerset-palace-seoul/studio-executive
- Four Seasons Seoul — https://www.fourseasons.com/seoul/
- Fairmont Ambassador Seoul — https://www.fairmont.com/en/hotels/seoul/fairmont-ambassador-seoul.html
- Hotel Skypark Myeongdong 3 — https://www.skyparkhotel.com/html/accommdation/accom3_tab1_01.asp
- Shilla Stay Gwanghwamun — https://www.shillastay.com/gwanghwamun/accommodation/viewAccmo.do?contId=ST
- Ramada Plaza Suwon (no official URL in data) — Booking: https://www.booking.com/hotel/kr/ramada-plaza-suwon.html

> For every hotel's live price + cancellation, the repo already carries a dated Booking.com `sourceUrl` in each `refundableRate` block — those are the correct place to re-verify the **current** refundable rate, since pricing moves continuously.
