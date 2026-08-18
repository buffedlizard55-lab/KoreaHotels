# Line-by-line hotel checklist — live pass 2026-08-18T18:46Z

**Purpose:** a complete, source-tied checklist of every hotel in `data/hotels.json` against the trip requirements (one queen/king bed ≥ ~150 cm, private bath, refundable dated rate, real current price). Nothing below is guessed.

**This pass (18:41–18:46 UTC, 2026-08-18):** dated Booking.com tables and official Accor / Nine Tree / Marriott / Toyoko pages were opened again for Seoul/Myeongdong, all 5 Suwon hotels, and the previously unsourced Cheonan / Daejeon / Busan / Gyeongju GG rows. Hotels not re-opened this hour keep their **PRIOR same-day** timestamped capture and are labeled as such.

**Stay windows:** Seoul / Suwon **Nov 1–9, 2026** (8 nights) · Gyeongju **Nov 9–15** (6 nights) · Busan **Nov 15–22** (7 nights) · Cheonan / Daejeon **Nov 8–14** (6 nights). Occupancy: 2 adults, 1 room, USD display.

**What “verified” means**

| Class | Meaning |
|---|---|
| **LIVE** | Dated Booking.com rate table and/or official brand page opened this session (2026-08-18 ~18:41–18:46 UTC). Price + cancellation copied from the page. |
| **PRIOR** | Timestamped Booking.com capture already in `data/pricing-history.json` from earlier today. Re-open the linked URL before paying. |
| **NOT LIVE** | Identity is sourced, but the stored price has **no dated URL and no UTC timestamp**. These are **flagged, not treated as quotes**. |

**Honesty limits:** Booking.com USD is a snapshot (usually before 10% tax). Official Accor/Marriott/Hyatt live prices are JS/login-gated. Booking’s “full/queen/king” is a **label**, not a millimetre measurement — bed *size* is taken from official pages when published; otherwise it is marked **width unpublished**.

Dated Booking URL pattern:

```
https://www.booking.com/hotel/kr/{slug}.html?checkin={in}&checkout={out}&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD
```

---

## 1. Seoul / Myeongdong — 30 hotels (Nov 1–9)

### A. Core Myeongdong / palace list — LIVE this session unless noted

| # | Hotel (ID) | Bed count / size | Refundable one-bed Nov 1–9 | Core match? | Manual links |
|---|---|---|---|:---:|---|
| 1 | L7 MYEONGDONG (`seoul-l7-myeongdong`) | LIVE: Standard Double = **1 full**. Twin = 2 twin. Hollywood = joined. No queen. | **LIVE ✅** Standard Double **$295/nt ($2,358)** · free cancel **Oct 29** · no prepay · 10% tax excl. · 5 left | ❌ no queen/king | [Booking](https://www.booking.com/hotel/kr/l7-myeongdong-by-lotte.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Lotte](https://www.lottehotel.com/myeongdong-l7/en/main.html) |
| 2 | Nine Tree MD1 (`seoul-nine-tree`) | **Official LIVE:** Standard Double **더블 1,600×1,900 mm** (queen width). Hollywood = 2 singles joined. | **LIVE ✅** Double **$208/nt ($1,661)** · free cancel **Oct 29** · pay nothing until Oct 27. Cheaper $199/$1,594 closes **Oct 18** and charges **total stay** inside 14 days. **Price moved** from prior $205/$1,643. | ✅ book Standard Double only | [Booking](https://www.booking.com/hotel/kr/nine-tree.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [official spec](https://www.ninetreehotels.com/nth1/room_standard_double.php) |
| 3 | ibis Styles Myeongdong (`seoul-ibis-styles`) | Accor /9771 LIVE: Standard = **1 x Double bed(s), 16 m²**. Width unpublished. | **LIVE ✅** Standard Double **$187/nt ($1,499)** · free cancel **Oct 31** · no prepay | ❌ double, not queen | [Booking](https://www.booking.com/hotel/kr/ibis-styles-seoul-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Accor /9771](https://all.accor.com/hotel/9771/index.en.shtml) |
| 4 | ibis Ambassador Insadong (`seoul-ibis-insadong`) | Accor /8002 LIVE: Superior “1 Double Bed” = **1 x Queen size bed**, 19 m². Premium = 1 queen + 1 single. | **LIVE 🚫** Booking dated page rendered **almost empty** this fetch. Book Accor direct. | ✅ queen (book Accor) | [Accor /8002](https://all.accor.com/hotel/8002/index.en.shtml) · [Booking](https://www.booking.com/hotel/kr/ibis-ambassador-insadong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 5 | Four Seasons Seoul (`seoul-four-seasons`) | Official Deluxe/Premier = king (not re-read this hour). | **PRIOR 🚫** Booking no availability Nov 1–9 (captured 05:52Z). | ✅ (book official) | [Official](https://www.fourseasons.com/seoul/) · [Booking](https://www.booking.com/hotel/kr/four-seasons-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 6 | Fairmont Ambassador (`seoul-fairmont`) | Official Deluxe = king. | **PRIOR ⚠️** captured refundable is **Fairmont Twin (2 twins) $583/nt**. King exists; captured rate is 2-bed. | ⚠️ | [Booking](https://www.booking.com/hotel/kr/fairmont-ambassador-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Fairmont](https://www.fairmont.com/en/hotels/seoul/fairmont-ambassador-seoul.html) |
| 7 | Skypark Myeongdong 3 (`seoul-skypark-myeongdong3`) | LIVE: Double = **1 full**. Prior hotel-confirmed **1400×2000 mm**. | **LIVE ✅** Double **$180/nt ($1,612)** · free cancel **Oct 29** · 10% service incl. | ❌ 140 cm | [Booking](https://www.booking.com/hotel/kr/skypark-myeongdong-3.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 8 | L'Escape (`seoul-lescape`) | LIVE: Classic King = **1 king**. | **LIVE ✅** Classic King **$305/nt ($2,443)** · free cancel **day of arrival** | ✅ | [Booking](https://www.booking.com/hotel/kr/l-39-escape.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Marriott](https://www.marriott.com/en-us/hotels/sellm-lescape-a-luxury-collection-hotel-seoul-myeongdong/overview/) |
| 9 | Somerset Palace (`seoul-somerset-palace`) | LIVE: Executive One-Bedroom = **1 queen**. Booking Studio = 1 full. | **LIVE ✅** Executive One-Bedroom **$228/nt ($1,824)** breakfast incl. · free cancel **Oct 30** · 2 left | ✅ | [Booking](https://www.booking.com/hotel/kr/somerset-palace-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Ascott](https://www.discoverasr.com/en/somerset-serviced-residence/korea-south/somerset-palace-seoul/studio-executive) |
| 10 | ibis Ambassador Myeongdong (`seoul-ibis-ambassador-myeongdong`) | Accor /6317 LIVE: Standard = **1 x Double bed(s), 21 m²**. Width unpublished. | **LIVE ✅** Standard Double **$313/nt ($2,503)** · free cancel **Oct 31 18:00**. Non-ref $266/$2,127. | ❌ double width unpublished | [Booking](https://www.booking.com/hotel/kr/ibis-myeong-dong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Accor /6317](https://all.accor.com/hotel/6317/index.en.shtml) |
| 11 | Moxy Myeongdong (`seoul-moxy-myeongdong`) | Official Marriott `/rooms/` LIVE: Guest room **1 Queen**; also 2 Double / 2 Queen / bunks / suite 1 Queen. | **LIVE ✅** Queen Room with City View **$308/nt ($2,460)** · free cancel **day of arrival**. Do **not** book “Queen Room with Two Queen Beds” ($296) — that is **2 queens**. | ✅ | [Booking](https://www.booking.com/hotel/kr/moxy-seoul-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Marriott rooms](https://www.marriott.com/en-us/hotels/selmx-moxy-seoul-myeongdong/rooms/) |
| 12 | Le Méridien Myeongdong (`seoul-le-meridien-myeongdong`) | LIVE: Deluxe King = **1 king**. | **LIVE ✅** Deluxe King **$624/nt ($4,992)** breakfast incl. · free cancel **day of arrival** · 5 left | ✅ | [Booking](https://www.booking.com/hotel/kr/le-meridien-seoul-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Marriott](https://www.marriott.com/en-us/hotels/selmm-le-meridien-seoul-myeongdong/overview/) |
| 13 | Aloft Myeongdong (`seoul-aloft-myeongdong`) | LIVE: Aloft Room = **1 king**. Coin laundry confirmed. | **LIVE ✅** Aloft Room 1 King **$323/nt ($2,581)** · free cancel **Oct 31** | ✅ | [Booking](https://www.booking.com/hotel/kr/aloft-seoul-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Marriott](https://www.marriott.com/en-us/hotels/selmo-aloft-seoul-myeongdong/overview/) |
| 14 | Courtyard Myeongdong (`seoul-courtyard-myeongdong`) | LIVE: Guest Room = **1 king**. | **LIVE ✅** Guest Room, 1 King **$324/nt** · free cancel **day of arrival** | ✅ | [Booking](https://www.booking.com/hotel/kr/courtyard-by-marriott-seoul-namdaemun.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Marriott](https://www.marriott.com/en-us/hotels/selsn-courtyard-seoul-myeongdong/overview/) |
| 15 | Four Points Josun MD (`seoul-four-points-myeongdong`) | LIVE: Superior = **1 full**. Official Deluxe King exists separately. | **LIVE ✅** Superior double **$234/nt ($2,081)** · 1 full · 10% service incl. | ⚠️ king exists; cheapest refundable is full | [Booking](https://www.booking.com/hotel/kr/four-points-by-sheraton-seoul-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Marriott](https://www.marriott.com/en-us/hotels/selfd-four-points-josun-seoul-myeongdong/overview/) |
| 16 | Nine Tree MD2 (`seoul-nine-tree-myeongdong2`) | Hollywood Double = Booking “1 king”; physical bed is typically **joined mattresses**. | **PRIOR ✅** Hollywood Double **$303/nt ($2,422)** · free cancel **Oct 29**. This hour’s table started at Hollywood Double (chunk cut). | ⚠️ Hollywood = joined | [Booking](https://www.booking.com/hotel/kr/nine-tree-premier-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Official](https://www.ninetreehotels.com/nth2/?lang=en) |
| 17 | Nine Tree Insadong (`seoul-nine-tree-insadong`) | Official brand is Nine Tree Premier Hotel Insadong. Width unpublished. | **PRIOR ✅** Deluxe Double Jogyesa **$235/nt ($1,881)** · 1 queen label · free cancel **Oct 29** | ⚠️ width unpublished | [Booking](https://www.booking.com/hotel/kr/nine-tree-premier-insadong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Official](https://www.ninetreehotels.com/nth3/) |
| 18 | Shilla Stay Gwanghwamun (`seoul-shilla-stay-gwanghwamun`) | Identity LIVE: 71 Sambong-ro; 24-hour desk. Rate table not isolated this hour. | **PRIOR ✅** Standard Double **$200/nt ($1,600)** · 1 full · free cancel **Oct 29** | ⚠️ captured room is full | [Booking](https://www.booking.com/hotel/kr/shilla-stay-gwanghwamun.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 19 | LOTTE HOTEL SEOUL / THE GRAND LOTTE (`seoul-lotte-hotel`) | Booking: Main Tower Grand Superior Double = 1 full. | **PRIOR ✅** Grand Superior Double **$364/nt ($3,235)** · free cancel **Oct 29** | ❌ full, not king | [Booking](https://www.booking.com/hotel/kr/lotte-seoul-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Lotte](https://www.lottehotel.com/seoul-hotel/en/rooms) |
| 20 | Westin Josun Seoul (`seoul-westin-josun`) | LIVE: Deluxe King = **1 king**. | **LIVE ✅** Deluxe King **$398/nt ($3,532)** · free cancel **day of arrival** · 10% service incl. | ✅ | [Booking](https://www.booking.com/hotel/kr/westin-chosun-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Marriott](https://www.marriott.com/en-us/hotels/selwi-the-westin-josun-seoul/overview/) |

### B. Extra 10 Seoul hotels

| # | Hotel (ID) | Bed | Refundable Nov 1–9 | vs stored | Core? | Manual links |
|---|---|---|---|---|:---:|---|
| 21 | Four Points Josun Seoul Station (`seoul-four-points-seoul-station`) | LIVE: Superior Double = **1 full**. Official Deluxe = 1 King. | **LIVE ✅** Superior Double **$181/nt ($1,609)** · 10% service incl. · free cancel **Nov 1** | Confirmed. King not priced this fetch. | ⚠️ | [Booking](https://www.booking.com/hotel/kr/four-points-by-sheraton-seoul-namsan.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Marriott rooms](https://www.marriott.com/en-us/hotels/selfp-four-points-josun-seoul-station/rooms/) |
| 22 | THE PLAZA Autograph (`seoul-the-plaza-autograph-collection`) | Listed Deluxe King = 1 king. | **PRIOR 🚫** Booking sold out Nov 1–9 (18:21Z). | Stored $199 is not a live dated rate. | ✅ book Marriott | [Booking](https://www.booking.com/hotel/kr/theplaza.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Marriott](https://www.marriott.com/en-us/hotels/selak-the-plaza-seoul-autograph-collection/overview/) |
| 23 | Travelodge Myeongdong Euljiro (`seoul-travelodge-myeongdong-euljiro`) | LIVE: Superior Queen = **1 queen** (231 ft²). Twin = 2 twin. Self-service laundromat confirmed. | **LIVE ✅** Superior Queen refundable **$172/nt ($1,377)** · free cancel **Oct 30**. Non-ref queen **$153/$1,226**. Twin non-ref $151. | Stored $90 unsourced. Prior pass had only the non-ref twin. | ✅ queen isolated | [Booking](https://www.booking.com/hotel/kr/holiday-inn-express-seoul-euljiro.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 24 | Sotetsu Fresa Inn Myeongdong (`seoul-sotetsu-fresa-inn-myeongdong`) | LIVE: Standard Double = **1 full**. | **LIVE ✅ $180/nt ($1,442)** · free cancel **Oct 30**. **Price drop** from prior $196. | Stored typical $95 was never live. | ❌ 1 full; width unpublished | [Booking](https://www.booking.com/hotel/kr/sotetsu-fresa-inn-seoul-myeong-dong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Official](https://sotetsu-hotels.com/en/fresa-inn/myeong-dong/) |
| 25 | Stanford Hotel Myeongdong (`seoul-stanford-hotel-myeongdong`) | Prior: one-bed not isolated. | **PRIOR ⚠️** one-bed refundable not captured (18:21Z). | Stored $116 unsourced. | ❌ | [Booking](https://www.booking.com/hotel/kr/seutaenpodeuhotel-myeongdong-stanford-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Official](https://www.stanford-hotel.com/myeongdong/en/) |
| 26 | Sotetsu Splaisir Myeongdong (`seoul-sotetsu-splaisir-myeongdong`) | LIVE: Deluxe High-Floor Double = **1 full** (1 left). | **LIVE ✅ $204/nt ($1,628)** · free cancel **Oct 30** | Confirmed. Stored $119 was not live. | ❌ 1 full | [Booking](https://www.booking.com/hotel/kr/the-m-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Official](https://sotetsu-hotels.com/en/splaisir/myeong-dong/) |
| 27 | Hotel Vert (`seoul-hotel-vert`) | Listed Deluxe King = 1 king. Working slug is `vert`. | **PRIOR 🚫** Booking sold out Nov 1–9 (18:21Z). | Stored $133 not a live dated rate. | ✅ king listed | [Booking](https://www.booking.com/hotel/kr/vert.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 28 | Royal Hotel Seoul (`seoul-royal-hotel`) | LIVE: Premier Double = **1 queen bed** (237 ft²). **Not a king.** Booking H1: “Royal Hotel Seoul Myeongdong”, 61 Myeongdong-gil. | **LIVE ✅ $320/nt ($2,556)** · free cancel **Oct 30** · pay nothing until Oct 28. Non-ref $303/$2,427. Breakfast-incl refundable $361/$2,887. | Stored **$173 “king” is wrong bed + unsourced price**. | ✅ queen + Myeongdong | [Booking](https://www.booking.com/hotel/kr/seoul-royal.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Official](https://www.royal.co.kr/en/index.php) |
| 29 | Sejong Hotel Myeongdong (`seoul-sejong-hotel-myeongdong`) | LIVE: Deluxe Double with Bath = **1 queen** (338 ft²). Score **7.4/10**. | **LIVE ✅ $207/nt ($1,656)** · free cancel **Oct 29** · ⚠️ inside 3 days = **total stay** | Confirmed. Stored $117 “king” was wrong. | ✅ queen | [Booking](https://www.booking.com/hotel/kr/sejong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Official](http://www.sejong.co.kr/eng/) |
| 30 | Orakai Insadong Suites (`seoul-orakai-insadong-suites`) | Prior: cheapest refundable isolated was two-bed. | **PRIOR ⚠️** Two-Bedroom Premier **$288/nt** (1 king + 1 twin). One-bed not isolated. | Stored $146 one-bed unsourced. | ⚠️ | [Booking](https://www.booking.com/hotel/kr/orakai-insadong-suites.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |

---

## 2. Suwon — 5 hotels (Nov 1–9) — all LIVE this session

| # | Hotel (ID) | Bed | Refundable Nov 1–9 | Core match? | Manual links |
|---|---|---|---|:---:|---|
| 1 | Novotel Ambassador Suwon (`suwon-novotel-ambassador`) | Accor /8748 LIVE: Superior / Deluxe / Executive = **1 x King size bed**. Direct covered access to Suwon KTX + subway. | **LIVE 🚫** Booking: “no availability between Sun, Nov 1 and Mon, Nov 9.” Book Accor. | ✅ only Suwon green match | [Accor /8748](https://all.accor.com/hotel/8748/index.en.shtml) · [Booking](https://www.booking.com/hotel/kr/novotel-ambassador-suwon.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 2 | Four Points Suwon (`suwon-four-points`) | LIVE: Premier King = **1 king**. Premier Double City View at the **same $157** is **2 twin beds**. | **LIVE ✅** Premier King **$157/nt ($1,259)** · free cancel **day of arrival** | ❌ walkable metro not established (Hyowon-ro / Paldal) | [Booking](https://www.booking.com/hotel/kr/four-points-by-sheraton-suwon.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Marriott](https://www.marriott.com/en-us/hotels/selfo-four-points-suwon/overview/) |
| 3 | Ramada Plaza Suwon (`suwon-ramada-plaza`) | LIVE: Superior Double = **1 full**. Prior Deluxe King = **1 queen** despite “King” name. ~12 min **drive** from Suwon Station. | **LIVE ✅** Superior Double **$127/nt ($1,018)** · free cancel **Oct 31**. Cheaper than the prior Deluxe King $139 row. | ❌ not walkable; cheapest is full | [Booking](https://www.booking.com/hotel/kr/ramada-plaza-suwon.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 4 | Courtyard Suwon (`suwon-courtyard`) | LIVE: Comfortable = **1 king**. Gwanggyo / Yeongtong. | **LIVE ✅** Comfortable King **$177/nt ($1,419)** · free cancel **day of arrival** | ❌ wrong district for Hwaseong / Suwon Station | [Booking](https://www.booking.com/hotel/kr/courtyard-by-marriott-suwon.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Marriott](https://www.marriott.com/en-us/hotels/selcw-courtyard-suwon/overview/) |
| 5 | ibis Ambassador Suwon (`suwon-ibis`) | LIVE: Standard/Superior Double = **1 full**. Junior King Suite = **1 king**. ~2 min walk to Suwon City Hall (Bundang Line), **not** Suwon KTX. | **LIVE ✅** Standard lead-in **$104/nt ($834)** · Superior Double **$111/nt ($891)** · free cancel **Oct 31 18:00** | ❌ double; KTX walk unverified | [Booking](https://www.booking.com/hotel/kr/ibis-suwon-ambassador.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |

---

## 3. Gyeongju — 15 hotels (Nov 9–15)

Gyeongju has **no subway**. Singyeongju KTX is outside Old Town and Bomun. **No property gets a full green core-needs badge.**

| # | Hotel (ID) | Bed | Refundable Nov 9–15 | Status | Manual links |
|---|---|---|---|---|---|
| 1 | Hwangnamkwan (`gyeongju-hwangnamkwan`) | Ondol / hanok. Check-in **ends 22:00**. | PRIOR 🚫 no full-window availability | ⚠️ 22:00 lockout | [Booking](https://www.booking.com/hotel/kr/hwangnamguan-hanok-village-gyeongjusi.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 2 | Commodore (`gyeongju-commodore`) | Captured Imperial Suite = **2 beds**. | PRIOR ✅ Imperial Suite **$205/nt ($1,365)** · free cancel **Nov 8** | ⚠️ 2-bed | [Booking](https://www.booking.com/hotel/kr/commodore-gyeongju.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 3 | Lahan Select (`gyeongju-lahan`) | Deluxe King Suite = **1 queen** (page spec despite “King”). | PRIOR ✅ **$265/nt ($1,764)** · free cancel **Nov 7** | ⚠️ name/size mismatch | [Booking](https://www.booking.com/hotel/kr/hyundai-gyeongju.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Lahan](https://www.lahan.com/gyeongju/en/main.do) |
| 4 | Hilton Gyeongju (`gyeongju-hilton`) | Premium King = **1 king**, lake view. | PRIOR LIVE (18:21Z) ✅ **$257/nt ($1,712)** · free cancel **Nov 7** | strongest bed-only pick | [Booking](https://www.booking.com/hotel/kr/gyeongju-hilton.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Hilton](https://www.hilton.com/en/hotels/kyjgyhi-hilton-gyeongju/) |
| 5 | GG Hotel (`gyeongju-gg-hotel`) | LIVE: Standard Double = **1 full**; Deluxe Double = **1 queen**; Korean-style = **4 futons**. Male-only sauna. | **LIVE 🚫** no availability Nov 9–15. Stored $88 is **not a quote**. | listed queen exists but unsellable this window | [Booking](https://www.booking.com/hotel/kr/gyeongju-dy-tourist.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 6 | Kolon (`gyeongju-kolon`) | Premier Double = **1 full**. Score **6.6/10**. | PRIOR LIVE ✅ **$82/nt ($491)** · free cancel **Nov 6** · ⚠️ inside 3 days = **total stay** · **full prepay** | harsh terms | [Booking](https://www.booking.com/hotel/kr/kolon.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 7 | The-K (`gyeongju-the-k`) | Captured Hwangnyoung View = **4 futons**. Score 7.1/10. | PRIOR ✅ **$125/nt ($752)** · free cancel **Nov 6** · ⚠️ inside = **total stay** | not a western one-bed | [Booking](https://www.booking.com/hotel/kr/the-k-gyeong-ju.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 8 | KINOCK (`gyeongju-kinock`) | PKG = **1 queen**. **Pet hotel**. | PRIOR ✅ **$171/nt ($1,028)** · free cancel **Nov 2** | ⚠️ pet-focused | [Booking](https://www.booking.com/hotel/kr/the-suite-gyeongju.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 9 | Swiss Rosen (`gyeongju-swiss-rosen`) | Captured Standard Twin = twin + full. | PRIOR ✅ **$83/nt ($556)** · free cancel **Nov 6** | ⚠️ 2-bed | [Booking](https://www.booking.com/hotel/kr/swiss-rosen.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 10 | Rivertain (`gyeongju-rivertain`) | Standard Double = **1 full** + spa tub. Adults-only rooms. | PRIOR ✅ **$82/nt ($490)** breakfast incl. · free cancel **Nov 6** · ⚠️ inside = **total stay** | one-bed; width unpublished | [Booking](https://www.booking.com/hotel/kr/rivertain-hotel-gyeongju.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 11 | HanokInn (`gyeongju-hanokinn`) | Ondol/futon. | PRIOR 🚫 no full-window availability | book direct | [Booking](https://www.booking.com/hotel/kr/hanogin.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 12 | Wiyeonjae (`gyeongju-wiyeonjae`) | Ondol. | 🚫 **not listed on Booking** — wiyeonjae.kr | not capturable here | [VisitKorea](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=45556) |
| 13 | Nadul Hanok (`gyeongju-nadul-hanok`) | Bed + en-suite (width unpublished). | 🚫 **not listed on Booking** | not capturable here | [VisitKorea](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=63076) |
| 14 | SONO Calm (`gyeongju-sono-calm`) | Family units. Slug `daemyung-resort-gyeongju`. | PRIOR 🚫 no full-window availability | book SONO | [Booking](https://www.booking.com/hotel/kr/daemyung-resort-gyeongju.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 15 | Kensington (`gyeongju-kensington`) | Captured Deluxe = **2 full beds**. | PRIOR ✅ **$160/nt ($957)** breakfast incl. · free cancel **Nov 2** | ⚠️ 2-bed | [Booking](https://www.booking.com/hotel/kr/kensington-resort-gyeongju.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |

**Gyeongju one-bed refundable options that actually exist on Booking for the full window:** Rivertain $490 (1 full + breakfast), Kolon $491 (1 full, harsh prepay), Hilton $1,712 (1 king), Lahan $1,764 (1 queen), Kinock $1,028 (1 queen, pet hotel). Hanok inventory and GG do **not** stretch across 6 nights.

---

## 4. Busan — 20 hotels (Nov 15–22)

| # | Hotel (ID) | Bed | Refundable Nov 15–22 | Core match? | Manual links |
|---|---|---|---|:---:|---|
| 1 | Shilla Stay Haeundae | PRIOR: Standard Double = **1 full** $184/$1,288 | PRIOR ✅ free cancel Nov 12 | ⚠️ captured is full | [Booking](https://www.booking.com/hotel/kr/shilla-stay-haeundae.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 2 | L7 HAEUNDAE | PRIOR: Standard King Town View = **1 king** $185/$1,294 | PRIOR ✅ free cancel Nov 12 | ✅ | [Booking](https://www.booking.com/hotel/kr/l7-haeundae-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 3 | ASTI Busan Station | PRIOR: Standard Double = **1 full** $78/$543 | PRIOR ⚠️ partner / pay-in-advance | ✅ Executive King exists separately | [Booking](https://www.booking.com/hotel/kr/asti-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 4 | Grand Josun Busan | PRIOR: Premier King = **1 queen** (page spec) $347/$2,431 | PRIOR ✅ free cancel Nov 13 · ⚠️ inside = total stay | ⚠️ name/size mismatch | [Booking](https://www.booking.com/hotel/kr/grand-josun-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 5 | Park Hyatt Busan | PRIOR: King Ocean View = **1 king** $532/$3,721 | PRIOR ✅ free cancel Nov 14 | ✅ | [Booking](https://www.booking.com/hotel/kr/park-hyatt-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 6 | Toyoko Inn Haeundae 2 | Double = 1 full (Toyoko 140 cm class). | PRIOR 🚫 no availability Nov 15–22 | ❌ 140 cm | [Booking](https://www.booking.com/hotel/kr/toyoko-inn-busan-haeundae-2.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 7 | Ramada Encore Haeundae | LIVE: **Adults only**. King / queen rooms listed. | **LIVE 🚫** no availability Nov 15–22. Stored $74 is **not a quote**. | ⚠️ adults-only | [Booking](https://www.booking.com/hotel/kr/haeundae-ramada-encore.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 8 | SIGNIEL BUSAN | PRIOR: Premier Double = **1 king** $297/$2,306 | PRIOR ✅ free cancel Nov 10 | ✅ | [Booking](https://www.booking.com/hotel/kr/signiel-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 9 | Paradise Busan | PRIOR: Deluxe Double = **1 king** $246/$1,915 | PRIOR ✅ free cancel Nov 13 | ✅ | [Booking](https://www.booking.com/hotel/kr/paradise-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 10 | Westin Josun Busan | PRIOR: Deluxe Park King = **1 full** (page spec despite “King”) $224/$1,742 | PRIOR ✅ | ⚠️ name/size mismatch | [Booking](https://www.booking.com/hotel/kr/the-westin-chosun-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 11 | Fairfield Haeundae | PRIOR LIVE: Standard **1 King** $113/$793 | PRIOR LIVE ✅ free cancel **Nov 15 00:00** | ✅ | [Booking](https://www.booking.com/hotel/kr/fairfield-by-marriott-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 12 | ibis budget Haeundae | Accor /9106 returned **HTTP 410 Gone** this fetch. | **NOT LIVE.** Stored $45 unsourced. | ❌ 140 cm class | [Accor /9106](https://all.accor.com/hotel/9106/index.en.shtml) — 410 this session |
| 13 | ibis Ambassador Haeundae | Accor /9643 returned **HTTP 410 Gone** this fetch. | **NOT LIVE.** Stored $49 unsourced. | ⚠️ | [Accor /9643](https://all.accor.com/hotel/9643/index.en.shtml) — 410 this session |
| 14 | LOTTE HOTEL BUSAN | PRIOR: Deluxe Double = **1 king** $162/$1,256 | PRIOR ✅ | ✅ Seomyeon | [Booking](https://www.booking.com/hotel/kr/lotte-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 15 | Avani Central | PRIOR: Deluxe King = **1 queen** (page spec) $86/$599 | PRIOR ✅ free cancel Nov 12 | ⚠️ name/size mismatch | [Booking](https://www.booking.com/hotel/kr/avani-central-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 16 | Ramada Encore Station | PRIOR: Superior Double = **1 full** $94/$655 | PRIOR ✅ free cancel Nov 13 | ⚠️ | [Booking](https://www.booking.com/hotel/kr/ramada-encore-by-wyndham-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 17 | Toyoko Inn Station No.1 | PRIOR: Economy Double = **1 full** $58/$406 breakfast | PRIOR ✅ free cancel Nov 14 · ⚠️ inside 1 day = total stay | ❌ 140 cm | [Booking](https://www.booking.com/hotel/kr/toyoko-inn-busan-no-1.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 18 | Crown Harbor | LIVE: Executive Double City = **1 full**. Jungang Station a couple of minutes. 24-hour desk. | **LIVE ✅ $98/nt ($688)** · free cancel **Nov 13** · ⚠️ inside 2 days = **total stay** | ⚠️ width unpublished | [Booking](https://www.booking.com/hotel/kr/crown-harbour-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 19 | Fairfield Songdo | PRIOR LIVE: Standard **1 King, Sea view** $130/$912 | PRIOR LIVE ✅ free cancel Nov 15 00:00 | ❌ no walkable metro in Songdo | [Booking](https://www.booking.com/hotel/kr/fairfield-by-marriott-busan-songdo-beach.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 20 | Wyndham Grand Busan | LIVE: Premium King = **1 king**, sea view, hot tub. Accessible “Premium King” = **1 queen**. | **LIVE ✅ $147/nt ($1,027)** · free cancel **Nov 14** · ⚠️ inside 1 day = **total stay** · **full prepay charged any time** | ❌ Songdo, no metro; harsh terms | [Booking](https://www.booking.com/hotel/kr/wyndham-grand-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Wyndham](https://www.wyndhamhotels.com/wyndham-grand/busan-south-korea/wyndham-grand-busan-ijin/overview) |

---

## 5. Cheonan — 7 hotels (Nov 8–14 alternative)

| # | Hotel (ID) | Bed | Refundable Nov 8–14 | Core match? | Manual links |
|---|---|---|---|:---:|---|
| 1 | Shilla Stay Cheonan | PRIOR LIVE: Standard Double = **1 full**. KTX **9.3 mi**. | PRIOR LIVE ✅ **$99/nt ($594)** · free cancel **Nov 7** | ❌ full; not walkable to KTX | [Booking](https://www.booking.com/hotel/kr/shilla-cheonan.html?checkin=2026-11-08&checkout=2026-11-14&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 2 | Ramada Encore Cheonan | PRIOR LIVE: Double = **1 full**. ~2.6 mi from Cheonan-Asan. | PRIOR LIVE ✅ **$68/nt ($408)** · free cancel **Nov 7** | ❌ full; not walkable | [Booking](https://www.booking.com/hotel/kr/ramada-encore-cheonan.html?checkin=2026-11-08&checkout=2026-11-14&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 3 | ON City Hotel | LIVE: Standard Double listed = **1 full**. 2.2 mi north of Cheonan-Asan. Score 7.9. | **LIVE 🚫** no availability Nov 8–14. Stored $58 is **not a quote**. | ❌ | [Booking](https://www.booking.com/hotel/kr/on-city.html?checkin=2026-11-08&checkout=2026-11-14&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 4 | SONO Belle Cheonan | Official family rooms = **2 double beds**. | **NOT LIVE.** Stored $95 typical. | ❌ family resort | [SONO](https://www.sonohotelsresorts.com/belle_ca/roomsviewall) |
| 5 | SureStay / Best Western Asan | LIVE: Booking H1 is now **“Best Western Asan Hotel”**, 32 Onsaem-ro, Tangjeong-myeon, **Asan**. Standard Double = **1 full**. ~4 mi from Cheonan-Asan. | **LIVE ✅ $65/nt ($390)** · free cancel **Nov 5** · ⚠️ inside 3 days = **total stay** | ❌ Asan, not walkable | [Booking](https://www.booking.com/hotel/kr/surestay-plus-by-best-western.html?checkin=2026-11-08&checkout=2026-11-14&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 6 | Brown Dot Dongnam | ~900 m from Cheonan Station (Line 1, not KTX). | **NOT LIVE.** Stored $48 typical. | ❌ width unpublished | [Trip.com listing](https://www.trip.com/hotels/cheonan-si-hotel-detail-62705121/brown-dot-hotel-cheonan-dongnam/) |
| 7 | The Mains Hotel | LIVE: Standard Double = **1 full** (226 ft²). 34 Cheongsu 11-ro. | **LIVE ✅ $45/nt ($272)** · free cancel **Nov 6** · 2 left | ❌ width unpublished; not KTX-walkable | [Booking](https://www.booking.com/hotel/kr/the-mains.html?checkin=2026-11-08&checkout=2026-11-14&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |

---

## 6. Daejeon — 7 hotels (Nov 8–14 alternative)

| # | Hotel (ID) | Bed | Refundable Nov 8–14 | Core match? | Manual links |
|---|---|---|---|:---:|---|
| 1 | Toyoko Inn Gov. Complex | LIVE Booking: Standard Double = **1 queen** label, 163 ft². Official Toyoko page did **not** publish mm. Brand double is typically **140 cm**. ~10 min Government Complex metro. | **LIVE ✅ $60/nt ($359)** breakfast incl. · free cancel **Nov 7** · ⚠️ inside 1 day = **total stay** | ❌ width not officially published as ≥150 cm; not KTX-walkable | [Booking](https://www.booking.com/hotel/kr/toyoko-inn-daejeon-government-complex.html?checkin=2026-11-08&checkout=2026-11-14&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Toyoko](https://www.toyoko-inn.com/eng/search/detail/00234/) |
| 2 | Ramada Daejeon | LIVE: Double = 1 full; King / Executive King / King Suite listed. Yuseong. Only **8 reviews**. | **LIVE 🚫** no availability Nov 8–14. Stored $72 is **not a quote**. | ❌ Yuseong | [Booking](https://www.booking.com/hotel/kr/ramada-daejeon.html?checkin=2026-11-08&checkout=2026-11-14&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 3 | LOTTE City Daejeon | PRIOR LIVE: Standard Double = **1 full**. 4.8 mi from Daejeon Station. | PRIOR LIVE ✅ **$156/nt ($933)** · free cancel **Nov 5** | ❌ full; Expo district | [Booking](https://www.booking.com/hotel/kr/lotte-city-daejeon.html?checkin=2026-11-08&checkout=2026-11-14&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 4 | BENIKEA Daelim | Jungangno area. | **NOT LIVE.** Stored $48 typical. | ❌ | [VisitKorea](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=85393) |
| 5 | Le Stendal | Yuseong. | **NOT LIVE.** Stored $75 typical. | ❌ Yuseong | [Official](http://stendhalhotel.co.kr/) |
| 6 | Hotel Interciti | Yuseong. | **NOT LIVE.** Stored $72 typical. | ❌ Yuseong | [VisitKorea](https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=86274) |
| 7 | Anook Air / Aank Daejeon Station | LIVE: Standard Double = **1 full**. ~9 min walk to Daejeon Station. Booking H1: 은행 아늑에어 대전역점. | **LIVE ✅ $41/nt ($246)** · free cancel **Nov 1** · ⚠️ inside 7 days = **total stay**. Non-ref $37/$221. | ❌ width unpublished; closest to KTX of this set | [Booking](https://www.booking.com/hotel/kr/aank-daejeon-station.html?checkin=2026-11-08&checkout=2026-11-14&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |

---

## 7. Options that actually meet the core rule

One **source-backed queen/king** + private bath + **walkable rail**. Prices are snapshots.

### Seoul (Nov 1–9)

| Hotel | Room to book | Bed evidence | Refundable snapshot | Link |
|---|---|---|---|---|
| Somerset Palace | Executive One-Bedroom / Studio Executive | Official 1 queen | $228/nt ($1,824) · cancel Oct 30 | [Booking](https://www.booking.com/hotel/kr/somerset-palace-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Nine Tree MD1 | **Standard Double only** | Official 160×190 cm | **$208/nt ($1,661)** · cancel Oct 29 | [spec](https://www.ninetreehotels.com/nth1/room_standard_double.php) |
| Moxy Myeongdong | Queen Room with City View (**not** Two Queens) | Official 1 queen | $308/nt ($2,460) · cancel day-of | [Marriott rooms](https://www.marriott.com/en-us/hotels/selmx-moxy-seoul-myeongdong/rooms/) |
| L'Escape | Classic King | 1 king | $305/nt ($2,443) · cancel day-of | [Booking](https://www.booking.com/hotel/kr/l-39-escape.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Courtyard Myeongdong | Guest Room, 1 King | Official 1 king | $324/nt · cancel day-of | [Marriott](https://www.marriott.com/en-us/hotels/selsn-courtyard-seoul-myeongdong/overview/) |
| Aloft Myeongdong | Aloft Room, 1 King | Official 1 king | $323/nt ($2,581) | [Marriott](https://www.marriott.com/en-us/hotels/selmo-aloft-seoul-myeongdong/overview/) |
| Le Méridien Myeongdong | Deluxe King | Official 1 king | $624/nt ($4,992) breakfast | [Marriott](https://www.marriott.com/en-us/hotels/selmm-le-meridien-seoul-myeongdong/overview/) |
| Westin Josun Seoul | Deluxe King | Official 1 king | $398/nt ($3,532) · cancel day-of | [Marriott](https://www.marriott.com/en-us/hotels/selwi-the-westin-josun-seoul/overview/) |
| ibis Ambassador Insadong | Superior (Renovated) | Accor = 1 queen | no Booking inventory — Accor direct | [Accor /8002](https://all.accor.com/hotel/8002/index.en.shtml) |
| Sejong Myeongdong | Deluxe Double with Bath | LIVE Booking = 1 queen | $207/nt ($1,656) · ⚠️ total-stay inside 3 days | [Booking](https://www.booking.com/hotel/kr/sejong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Travelodge Euljiro | **Superior Queen** | LIVE Booking = 1 queen | **$172/nt ($1,377)** · cancel Oct 30 | [Booking](https://www.booking.com/hotel/kr/holiday-inn-express-seoul-euljiro.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Royal Hotel Seoul | Premier Double | LIVE Booking = **1 queen** (not king) | **$320/nt ($2,556)** · cancel Oct 30 | [Booking](https://www.booking.com/hotel/kr/seoul-royal.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Four Points Seoul Station | **Deluxe Guest room, 1 King** (not Superior Double) | Official Marriott Deluxe = 1 King | Deluxe King not priced this fetch; Superior Double $181 is 1 full | [Marriott rooms](https://www.marriott.com/en-us/hotels/selfp-four-points-josun-seoul-station/rooms/) |

### Suwon

| Hotel | Room | Note |
|---|---|---|
| Novotel Ambassador Suwon | Superior 1 King | Only Suwon green match. Book Accor — Booking sold out. |

### Busan (Nov 15–22) — king/queen + walkable metro

L7 Haeundae Standard King $185 · SIGNIEL Premier $297 · Park Hyatt King Ocean $532 · Paradise Deluxe $246 · LOTTE Hotel Busan Deluxe $162 · Fairfield Haeundae **$113** · Avani “King” (actually 1 queen) $86.

### Gyeongju / Cheonan / Daejeon

No complete green match (no walkable KTX/subway + confirmed queen/king together). Strongest *bed-only* Gyeongju pick if the station rule is relaxed: **Hilton Premium King $257/nt**. Closest *station* Daejeon pick is Anook Air ($41 refundable, 1 full, harsh 7-day total-stay penalty).

---

## 8. Irregularities flagged for review

1. **Royal Hotel Premier Double is a queen, not a king.** Live Booking: “1 queen bed”, 237 ft². Stored $173 “king” was unsourced. Live refundable is **$320/nt ($2,556)**.
2. **Nine Tree MD1 price moved** $205 → **$208** ($1,643 → $1,661) on the 3-day cancel row.
3. **Sotetsu Fresa price dropped** $196 → **$180** ($1,567 → $1,442).
4. **Travelodge Superior Queen is now isolated** at $172/$1,377 refundable. Do not use the $151 Twin (2 beds, non-refundable).
5. **Four Points Suwon Premier Double at $157 is 2 twins.** Book **Premier King** at the same price.
6. **SureStay Plus Asan listing title is now “Best Western Asan Hotel”.** Same slug. Property is in **Asan**, ~4 mi from Cheonan-Asan Station.
7. **Toyoko Daejeon Booking label = “1 queen”** but official Toyoko page did not publish millimetres. Do not treat this as a confirmed ≥150 cm queen.
8. **Accor /9106 (ibis budget Haeundae) and /9643 (ibis Ambassador Haeundae) returned HTTP 410** this session. Stored $45 / $49 remain unsourced.
9. **Wyndham Grand Busan terms are harsh:** free cancel until Nov 14, then **total stay**; **full prepay charged any time**. Accessible “Premium King” is **1 queen**.
10. **Crown Harbor / Kolon / Sejong / Anook Air / Best Western Asan** use **total-stay** penalties inside the free-cancel window (not first-night). Read the row.
11. **Ramada Encore Haeundae is adults-only** and sold out for Nov 15–22.
12. **ON City, Ramada Daejeon, GG Gyeongju** have **no Booking inventory** for the full city window. Stored typical prices are not quotes.
13. **Hollywood / joined-mattress rooms** (L7, Nine Tree MD1/MD2, Shilla) conflict with “not two beds pushed together.”
14. **King/queen naming mismatches:** Ramada Plaza Suwon Deluxe King = 1 queen; Lahan “King Suite” = 1 queen; Grand Josun “Premier King” = 1 queen; Westin Josun Busan “Park King” = 1 full; Avani “Deluxe King” = 1 queen; Royal “Premier Double king” = 1 queen.
15. **KINOCK is a pet hotel.** Rivertain rooms are adults-only. GG has a **male-only sauna**.
16. **Five records remain NOT LIVE** (typical autumn rates, no `sourceUrl` / no UTC): SONO Belle Cheonan, Brown Dot Cheonan, BENIKEA Daelim, Le Stendal, Hotel Interciti.
17. **Korean “double” ≠ automatically 140 cm.** Nine Tree MD1 official double is **160 cm**. Width must come from the official spec.

---

## 9. What changed in data this pass

- Live `refundableRate` + UTC `2026-08-18T18:46:25Z` written or re-confirmed for 35 hotels (full Seoul/Myeongdong core + extra Royal/Travelodge/Fresa + all 5 Suwon + Cheonan Mains/Asan/ON City + Daejeon Toyoko/Aank/Ramada + Busan Wyndham/Crown/Ramada Encore Haeundae + Gyeongju GG).
- Royal Premier Double **king → queen**; live $320 written.
- Travelodge refundable one-bed isolated as **Superior Queen $172**.
- Nine Tree MD1 $205 → $208; Sotetsu Fresa $196 → $180.
- Planner cards now use each hotel’s own stay window (no more hardcoded “Nov 1–9 / 8 nights” on Gyeongju/Busan/Cheonan/Daejeon).
- Coverage copy updated to **84 hotels** (30 Seoul / 15 Gyeongju / 20 Busan / 7 Cheonan / 7 Daejeon / 5 Suwon).

`python3 validate.py` and `python3 build.py` should be run after this file.

*Live fetches completed 2026-08-18 ~18:41–18:46 UTC. Prior same-day captures remain in `data/pricing-history.json`. Re-open every link before paying.*
