# Seoul · Myeongdong · Suwon — Line-by-line verification (2026-08-18)

**Scope:** every Seoul/Myeongdong hotel currently in `data/hotels.json` (20), plus a new Suwon shortlist (5).
**What was checked per hotel:** bed size, bed count, refundable (free-cancellation) status, and current pricing.
**Dates used for pricing:** Seoul/Myeongdong **Nov 1–9, 2026** (8 nights, 2 adults); Suwon uses the same window as a like-for-like anchor.
**Method:** each fact below is tied to a link that was opened this session (official hotel/brand pages, Booking.com live availability, or a major trusted listing/OTA). Where a fact could not be re-confirmed to a source, it is explicitly labelled **NOT re-verified** — nothing is guessed.

> ⚠️ **Honesty note on "current pricing":** hotel rates are per-rate-plan and move constantly. The figures below are (a) live reads from Booking.com fetched today, (b) the repo's own timestamped Booking captures from today (2026-08-18), and/or (c) OTA "from $" anchors. They are a snapshot, not a quote. Always re-open the linked page and read the rate shown at checkout before paying.

---

## 1. Seoul / Myeongdong — 20 hotels

Legend: ✅ verified as listed · ⚠️ irregularity found · 🔗 manual-verification link.

| # | Hotel (data ID) | Bed size & count (data → verified) | Refundable | Current price anchor | Status |
|---|---|---|---|---|---|
| 1 | L7 MYEONGDONG by LOTTE (`seoul-l7-myeongdong`) | "Deluxe Double = queen 150×200" → **no such room**. Official inventory is Superior/Standard **Double = 1 double ("1 full bed")**, Twin = 2 single, Hollywood = joined mattresses. | Yes — free-cancel inventory (capture: Standard Double $295/nt, cancel before Oct 29). | Live: Standard **Twin $287/nt ($2,297/8nt)**; double ≈ $295/nt. | ⚠️ room names + "queen" claim unsupported |
| 2 | Nine Tree by Parnas MD 1 (`seoul-nine-tree`) | "Deluxe = queen" → **no "Deluxe" room**. Official **Standard Double = 160×190 cm** bed; **Hollywood Double = 1 queen**. | Yes (capture: Double $205/nt, cancel before Oct 29). | $34–152/nt OTA spread; capture $205/nt. | ⚠️ queen room is "Hollywood Double", not "Deluxe" |
| 3 | ibis Styles Ambassador Seoul Myeongdong (`seoul-ibis-styles`) | Standard/Superior = **1 double** (16–24 m²). | Yes (capture: Standard Double $187/nt). | $187/nt (capture). | ⚠️ official URL + star rating wrong (see flags) |
| 4 | ibis Ambassador Insadong (`seoul-ibis-insadong`) | "double ~140 cm" → **Superior = 1 QUEEN** (Accor "1 Double Bed" = "1 Queen size bed(s)"). | No Booking availability Nov 1–9 (book direct Accor). | n/a (no Booking inventory). | ⚠️ bed is queen, not double; URL + stars wrong |
| 5 | Four Seasons Hotel Seoul (`seoul-four-seasons`) | Deluxe = **king** (official category). | No Booking availability Nov 1–9. | n/a. | ✅ (bed = official category) |
| 6 | Fairmont Ambassador Seoul (`seoul-fairmont`) | Deluxe **King** (official). | Yes — but captured refundable row is a **2-twin** room ($583/nt). | $467–583/nt. | ⚠️ captured "refundable" room is 2 beds |
| 7 | Hotel Skypark Myeongdong 3 (`seoul-skypark-myeongdong3`) | Standard Double = **1 double 1400×2000 mm** (hotel-confirmed). | Yes (capture: $180/nt). | $180/nt. | ✅ |
| 8 | L'Escape, Luxury Collection (`seoul-lescape`) | Deluxe **King** (capture: "Classic King, 1 king bed"). | Yes ($305/nt, day-of-arrival cutoff). | $305/nt. | ✅ (room naming "Classic" vs "Deluxe") |
| 9 | Somerset Palace Seoul (`seoul-somerset-palace`) | Studio Executive = **1 queen** (official Ascott page). | Yes — but captured row is a **2-queen** room ($249/nt); the 1-queen Studio total was only partially captured. | $249/nt (2-queen). | ⚠️ captured refundable room = 2 beds |
| 10 | ibis Ambassador Seoul Myeongdong (`seoul-ibis-ambassador-myeongdong`) | Standard = **1 double** ("1 Double bed", 21 m²). | Yes — refundable ≈ **$313/nt**; non-refundable **$266/nt** (live). | $266 non-ref / $313 refundable (live). | ✅ |
| 11 | Moxy Seoul, Myeongdong (`seoul-moxy-myeongdong`) | "King Guest Room" → base room is **1 Queen / 2 Double** (no king). | Yes (capture: 2-queen $296/nt, day-of-arrival cutoff). | $296/nt (2-queen). | ⚠️ "King" should be "Queen" |
| 12 | Le Méridien Seoul, Myeongdong (`seoul-le-meridien-myeongdong`) | Deluxe **King** ✓ (also Deluxe Double/Queen exist). | Yes ($624/nt incl. breakfast). | $567–624/nt. | ✅ |
| 13 | Aloft Seoul Myeongdong (`seoul-aloft-myeongdong`) | "Deluxe King" = **Room, 1 King** ✓. | Yes (OTA "Free Cancellation" rows). | $258/nt (MakeMyTrip). | ⚠️ no refundable capture recorded |
| 14 | Courtyard Seoul Myeongdong (`seoul-courtyard-myeongdong`) | **Guest Room, 1 King** ✓. | Yes ($324/nt, day-of-arrival cutoff). | $324/nt. | ✅ |
| 15 | Four Points Josun Seoul Myeongdong (`seoul-four-points-myeongdong`) | Deluxe **King** (official category). | Not captured (official Marriott flexible rates exist). | $120–190 range (planning). | ⚠️ no refundable capture recorded |
| 16 | Nine Tree MD 2 (`seoul-nine-tree-myeongdong2`) | Hollywood Double = **1 king** (capture). | Yes ($303/nt). | $303/nt. | ⚠️ "Hollywood" = joined mattresses — confirm rule |
| 17 | Nine Tree Insadong (`seoul-nine-tree-insadong`) | Standard Double = **queen-width (160 cm class)**. | Yes ($235/nt). | $235/nt. | ⚠️ width depends on Korean "double" = 160 cm |
| 18 | Shilla Stay Gwanghwamun (`seoul-shilla-stay-gwanghwamun`) | **Hollywood Double = 1 KING** ✓ (Standard/Deluxe Double = 1 full). | Yes ($200/nt). | $200/nt (standard double). | ✅ |
| 19 | LOTTE HOTEL SEOUL (`seoul-lotte-hotel`) | "Main Tower Deluxe Double = king" → **1 full/double bed** (Booking). | Yes ($364/nt). | $364/nt. | ⚠️ "king" → double/full; fits unsupported |
| 20 | The Westin Josun Seoul (`seoul-westin-josun`) | Deluxe **King** ✓. | Yes ($398/nt, day-of-arrival cutoff). | $398/nt. | ✅ |

### Manual-verification links (Seoul)

- L7 Myeongdong live: [Booking.com (Nov 1–9)](https://www.booking.com/hotel/kr/l7-myeongdong-by-lotte.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Lotte official](https://www.lottehotel.com/myeongdong-l7/en/main.html)
- Nine Tree MD1: [Official room specs (Korean, 160×190 mm)](https://www.ninetreehotels.com/nth1/room_standard_double.php) · [Booking.com](https://www.booking.com/hotel/kr/nine-tree.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD)
- ibis Styles Myeongdong: [Accor /9771 (4★, 180 rooms)](https://all.accor.com/hotel/9771/index.en.shtml)
- ibis Ambassador Insadong: [Accor /8002 (3★, "1 Queen" Superior)](https://all.accor.com/hotel/8002/index.en.shtml)
- ibis Ambassador Myeongdong: [Accor /6317](https://all.accor.com/hotel/6317/index.en.shtml) · [Booking live](https://www.booking.com/hotel/kr/ibis-myeong-dong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD)
- Skypark Myeongdong 3: [Hotel-confirmed bed sizes (Double = 1400 mm)](https://www.tripadvisor.com/FAQ_Answers-g294197-d2202400-t9891111-How_big_is_the_double_bed_Is_this_as_same_as.html)
- Somerset Palace: [Official Studio Executive = 1 queen + washer/dryer](https://www.discoverasr.com/en/somerset-serviced-residence/korea-south/somerset-palace-seoul/studio-executive)
- Moxy Myeongdong: [Marriott official](https://www.marriott.com/en-us/hotels/selmx-moxy-seoul-myeongdong/overview/) (lead-in = 1 Queen / 2 Double)
- Aloft Myeongdong: [Marriott official](https://www.marriott.com/en-us/hotels/selmo-aloft-seoul-myeongdong/overview/) · [Room 1 King, $258](https://www.makemytrip.global/hotels-international/en-us/south_korea/seoul-hotels/aloft_seoul_myeongdong_by_marriott-details.html)
- Shilla Stay Gwanghwamun: [Room inventory (Hollywood = 1 king)](https://www.myboutiquehotel.com/en/boutique-hotels-seoul/shilla-stay-gwanghwamun.html)
- LOTTE HOTEL SEOUL: [Booking room list (Deluxe Double Main Tower = 1 full bed)](https://www.booking.com/hotel/kr/lotte-seoul-seoul.html)
- Le Méridien Myeongdong: [Marriott official](https://www.marriott.com/en-us/hotels/selmm-le-meridien-seoul-myeongdong/overview/)
- Westin Josun Seoul: [Marriott official](https://www.marriott.com/en-us/hotels/selwi-the-westin-josun-seoul/overview/)
- Four Seasons: [Official](https://www.fourseasons.com/seoul/) · Fairmont: [Official](https://www.fairmont.com/en/hotels/seoul/fairmont-ambassador-seoul.html) · Courtyard MD: [Marriott](https://www.marriott.com/en-us/hotels/selsn-courtyard-seoul-myeongdong/overview/) · Four Points MD: [Marriott](https://www.marriott.com/en-us/hotels/selfd-four-points-josun-seoul-myeongdong/overview/) · L'Escape: [Marriott](https://www.marriott.com/en-us/hotels/sellm-lescape-a-luxury-collection-hotel-seoul-myeongdong/overview/) · Nine Tree MD2: [Official](https://www.ninetreehotels.com/nth2/?lang=en) · Nine Tree Insadong: [Official](https://www.ninetreehotels.com/nth3/)

---

## 2. Suwon — new shortlist (5 hotels)

Suwon is **not currently in the repo**. It is a practical Seoul-area base: **Suwon Station** is on the Gyeongbu KTX line and Seoul Metro Line 1 (~30–40 min from central Seoul), and **Hwaseong Fortress (UNESCO)** is the main sight. Reference window used for pricing: **Nov 1–9, 2026**.

| # | Hotel | Area | Bed (verified) | Bed count | Refundable | Price anchor | Link |
|---|---|---|---|---|---|---|---|
| 1 | **Novotel Ambassador Suwon** (4★, Accor) | Suwon Station (direct connection) | King | 1 | Flexible rates on official (free-cancel plans exist) | from ~$121/nt | [Accor /8748](https://all.accor.com/hotel/8748/index.en.shtml) |
| 2 | **Four Points by Sheraton Suwon** (4★, Marriott, 2022) | Ingye-dong (central) | Premier **King** | 1 (Premier Twin = 2 single) | Marriott flexible rates | from ~$116/nt | [Marriott](https://www.marriott.com/en-us/hotels/selfo-four-points-suwon/overview/) |
| 3 | **Ramada Plaza by Wyndham Suwon** (4★) | Paldal-gu | "King" rooms = **1 queen** per Booking; Superior = 1 double | 1–2 | Flexible (24-hr desk) | $93–122/nt | [Booking](https://www.booking.com/hotel/kr/ramada-plaza-suwon.html) |
| 4 | **Courtyard by Marriott Suwon** (4★) | Gwanggyo New Town | Comfortable **King** / 2-Double | 1–2 | Marriott flexible rates | from ~$141/nt | [Marriott](https://www.marriott.com/en-us/hotels/selcw-courtyard-suwon/overview/) |
| 5 | **ibis Ambassador Suwon** (3★, Accor, renovated 2021) | Suwon City Hall | Standard/Superior = **1 double**; Junior Suite = 1 king | 1–2 | Accor flexible rates | budget-mid | [ibis/Accor Suwon](https://ibis.accor.com/en/destination/city/hotels-suwon-v5590.html) |

### Suwon notes

- **Novotel Ambassador Suwon** is the strongest Suwon pick: official Accor text says *"Best location with direct access to Suwon KTX train & subway stations"* and the room list confirms **Superior 1 King (28 m²)**, Deluxe King, Executive King and Junior Suite King. It is the only Suwon entry marked **core-needs fit** (king + private bath + station access).
- **Ramada Plaza Suwon** has a naming mismatch worth checking: Booking/hotel-rez list "Deluxe King / Premier King / Executive King" as **"1 queen bed"**, while "Superior Double" is 1 double. It is ~12 min **by car** from Suwon Subway Station, so it does **not** meet the walkable-rail rule.
- **Courtyard Suwon** sits in Gwanggyo New Town (6 min from Gwanggyo Jungang Station, ~30 min from Suwon Station/Hwaseong) — convenient for Gwanggyo Lake Park, not for Hwaseong/shopping.
- **ibis Ambassador Suwon** and **Four Points Suwon** are the central (city-hall / Ingye-dong) options; king rooms exist but the lead-in standard rooms are doubles/twins.

---

## 3. Irregularities flagged for review

1. **Wrong Accor property codes (data pointed at hotels in France):**
   - `seoul-ibis-styles` → `all.accor.com/hotel/1976` is **Mercure Forbach, France**. Correct property = `/9771` (ibis Styles Ambassador Seoul Myeongdong, 4★, 180 rooms).
   - `seoul-ibis-insadong` → `all.accor.com/hotel/1888` is **Hôtel de Bourbon Mercure Bourges, France**. Correct property = `/8002`.
2. **Star-rating errors:** ibis Styles Myeongdong is **4★** (data said 3); ibis Ambassador Insadong is **3★** (data said 4).
3. **ibis Ambassador Insadong bed misclassified:** Accor lists the renovated **Superior "1 Double Bed" = "1 Queen size bed(s)"** — the repo said "double ~140 cm" and `fits:false`. It is actually a queen room → eligible for a core-needs match.
4. **L7 MYEONGDONG room inventory is not the real inventory:** "Deluxe Double (queen)", "Corner Deluxe (king)", "Deluxe Twin" do not exist. Real rooms: Standard/Superior Double (1 double), Standard/Superior Twin (2 single), Family Twin, Hollywood Double (joined mattresses), suites. The **"queen 150×200" claim and the arrival-night "Deluxe Double — queen" line are unsupported.**
5. **Nine Tree MD 1:** the queen room is **"Hollywood Double"**, not "Deluxe". Official Standard Double is **160×190 cm** (queen-width), not the implied 140 cm.
6. **Moxy Seoul Myeongdong:** lead-in room is **1 Queen or 2 Double**, not "King Guest Room".
7. **LOTTE HOTEL SEOUL:** "Main Tower Deluxe Double" is **1 full/double bed** per Booking — the repo's "king" label and `fits:true` are unsupported under the repo's own "double ≠ queen" rule.
8. **Refundable captures record the wrong room for the one-bed preference** at Fairmont (captured **2-twin**, $583/nt), Somerset (captured **2-queen**, $249/nt) and Moxy (captured **2-queen**, $296/nt). These rows are genuine refundable rates but do **not** describe a single queen/king room — the one-bed rate must be read separately.
9. **Missing refundable captures:** Aloft Seoul Myeongdong and Four Points Josun Seoul Myeongdong have no `refundableRate` block.
10. **"Hollywood Double" caveat (Nine Tree MD2, Shilla Gwanghwamun, L7):** a "Hollywood" bed is typically **two mattresses joined**, which conflicts with the repo's "not two beds pushed together" rule — confirm the physical bed before relying on these as a single king.
11. **Korean "double" ≠ 140 cm.** Official Korean specs (e.g., Nine Tree "더블 1,600×1,900 mm") are **160 cm wide (queen-width)**. The repo's blanket "double ≈ 140 cm → not a fit" rule misclassifies several genuinely queen-width Korean doubles.
12. **Date mismatch:** `data/hotels.json` trip note says "Oct 31 – Nov 22" while the Seoul refundable captures and `itinerary.json` use **Nov 1–9**; `guide/seoul.md` still says "Oct 31 – Nov 8". These should be reconciled.

---

## 4. Corrections applied to `data/hotels.json` (this session)

- Fixed `seoul-ibis-styles` officialUrl + verification source → Accor **/9771**; stars 3 → **4**.
- Fixed `seoul-ibis-insadong` officialUrl + verification source → Accor **/8002**; stars 4 → **3**; room beds **double → queen** (Superior); `fits` false → **true**.
- Replaced L7 MYEONGDONG rooms with the real inventory and set `fits` → **false** (no confirmed single queen/king); updated its arrival-night card wording.
- Replaced Nine Tree MD 1 rooms (Standard Double 160 cm / Hollywood Double queen / Deluxe Twin).
- Moxy Myeongdong room "King Guest Room" → **"Queen Guest Room"**.
- LOTTE HOTEL SEOUL room "king" → **double/full**, `fits` → **false**.
- Added **5 Suwon hotels** (Novotel, Four Points, Ramada Plaza, Courtyard, ibis) with source-verified identity/room blocks; only Novotel marked `fits:true`.
- Updated `meta.verifiedHotelRecords` 69 → **74**.

Run `python3 validate.py` then `python3 build.py` after reviewing.
