# Verified hotel checklist — live pass 2026-08-18

**Purpose:** a complete, source-tied checklist of every hotel in `data/hotels.json` against the trip requirements (one queen/king bed ≥ ~150 cm, private bath, refundable dated rate, real current price). Nothing below is guessed.

**Stay windows:** Seoul / Suwon **Nov 1–9, 2026** (8 nights) · Gyeongju **Nov 9–15** (6 nights) · Busan **Nov 15–22** (7 nights) · Cheonan / Daejeon **Nov 8–14** (6 nights). Occupancy: 2 adults, 1 room, USD display.

**What “verified” means on this pass**

| Class | Meaning |
|---|---|
| **LIVE** | Dated Booking.com rate table and/or official brand page opened this session (~18:15–18:22 UTC, 2026-08-18). Price + cancellation copied from the page. |
| **PRIOR** | Timestamped Booking.com capture already in `data/pricing-history.json` from earlier today. Re-open the linked URL before paying. |
| **NOT LIVE** | Identity is sourced, but the stored price is a “typical autumn rate” with **no dated URL and no UTC timestamp**. These are **flagged, not treated as quotes**. |

**Honesty limits:** Booking.com USD is a snapshot (usually before 10% tax). Official Accor/Marriott/Hyatt live prices are JS/login-gated. Booking’s “full/queen/king” is a **label**, not a millimetre measurement — bed *size* is taken from official pages when published; otherwise it is marked **width unpublished**.

---

## How to re-check any row

Dated Booking URL pattern:

```
https://www.booking.com/hotel/kr/{slug}.html?checkin={in}&checkout={out}&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD
```

Always re-open the link. Inventory and cancellation windows move.

---

## 1. Seoul / Myeongdong — 30 hotels

### A. Original 20 (PRIOR same-day timestamped captures)

These 20 already have UTC-timestamped Booking.com captures in `data/pricing-history.json`. This pass does **not** re-invent those numbers. Re-open the source URL.

| # | Hotel (ID) | Bed count / size (official or prior live) | Refundable one-bed snapshot | Core match? | Manual links |
|---|---|---|---|:---:|---|
| 1 | L7 MYEONGDONG (`seoul-l7-myeongdong`) | Standard/Superior Double = **1 full**. No queen exists. Hollywood = joined mattresses. | PRIOR ✅ Standard Double **$295/nt ($2,358)** · free cancel **Oct 29** | ❌ no queen/king | [Booking](https://www.booking.com/hotel/kr/l7-myeongdong-by-lotte.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Lotte](https://www.lottehotel.com/myeongdong-l7/en/main.html) |
| 2 | Nine Tree MD1 (`seoul-nine-tree`) | Official: Standard Double **160×190 cm** (queen-width). Hollywood = 2×110 cm joined. | PRIOR ✅ Double **$205/nt ($1,643)** · free cancel **Oct 29** | ✅ | [Booking](https://www.booking.com/hotel/kr/nine-tree.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [spec](https://www.ninetreehotels.com/nth1/room_standard_double.php) |
| 3 | ibis Styles Myeongdong (`seoul-ibis-styles`) | Accor /9771: Standard = **1 Double** (16 m²). Width unpublished. | PRIOR ✅ Standard Double **$187/nt ($1,499)** · free cancel **Oct 31** | ❌ double, not queen | [Booking](https://www.booking.com/hotel/kr/ibis-styles-seoul-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Accor](https://all.accor.com/hotel/9771/index.en.shtml) |
| 4 | ibis Ambassador Insadong (`seoul-ibis-insadong`) | Accor /8002: Superior “1 Double Bed” = **1 Queen**. | PRIOR 🚫 **no Booking availability** Nov 1–9 — book Accor direct | ✅ queen (book direct) | [Accor](https://all.accor.com/hotel/8002/index.en.shtml) · [Booking](https://www.booking.com/hotel/kr/ibis-ambassador-insadong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 5 | Four Seasons Seoul (`seoul-four-seasons`) | Official Deluxe/Premier = **king**. | PRIOR 🚫 **no Booking availability** Nov 1–9 | ✅ (book direct) | [Official](https://www.fourseasons.com/seoul/) · [Booking](https://www.booking.com/hotel/kr/four-seasons-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 6 | Fairmont Ambassador (`seoul-fairmont`) | Official Deluxe = **king**. | PRIOR ⚠️ captured refundable row is **Fairmont Twin (2 twins) $583/nt** — not the king | ⚠️ king exists; captured rate is 2-bed | [Booking](https://www.booking.com/hotel/kr/fairmont-ambassador-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Fairmont](https://www.fairmont.com/en/hotels/seoul/fairmont-ambassador-seoul.html) |
| 7 | Skypark Myeongdong 3 (`seoul-skypark-myeongdong3`) | Hotel-confirmed Double = **1400×2000 mm**. | PRIOR ✅ Double **$180/nt ($1,612)** · free cancel **Oct 29** | ❌ 140 cm | [Booking](https://www.booking.com/hotel/kr/skypark-myeongdong-3.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 8 | L'Escape (`seoul-lescape`) | Marriott lead-in = **Classic King** (1 king). | PRIOR ✅ Classic King **$305/nt ($2,443)** · free cancel **day of arrival** | ✅ | [Booking](https://www.booking.com/hotel/kr/l-39-escape.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Marriott](https://www.marriott.com/en-us/hotels/sellm-lescape-a-luxury-collection-hotel-seoul-myeongdong/overview/) |
| 9 | Somerset Palace (`seoul-somerset-palace`) | Official Studio Executive = **1 queen**. | PRIOR ✅ Executive One-Bedroom **$228/nt ($1,824)** · free cancel **Oct 30** | ✅ | [Booking](https://www.booking.com/hotel/kr/somerset-palace-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Ascott](https://www.discoverasr.com/en/somerset-serviced-residence/korea-south/somerset-palace-seoul/studio-executive) |
| 10 | ibis Ambassador Myeongdong (`seoul-ibis-ambassador-myeongdong`) | Accor /6317: Standard = **1 Double** (21 m²). | PRIOR ✅ Standard Double **$313/nt ($2,503)** · free cancel **Oct 31 18:00** | ❌ double width unpublished | [Booking](https://www.booking.com/hotel/kr/ibis-myeong-dong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Accor](https://all.accor.com/hotel/6317/index.en.shtml) |
| 11 | Moxy Myeongdong (`seoul-moxy-myeongdong`) | Official lead-in = **1 Queen**. | PRIOR ✅ Queen City View **$308/nt ($2,460)** · free cancel **day of arrival** | ✅ | [Booking](https://www.booking.com/hotel/kr/moxy-seoul-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Marriott](https://www.marriott.com/en-us/hotels/selmx-moxy-seoul-myeongdong/overview/) |
| 12 | Le Méridien Myeongdong (`seoul-le-meridien-myeongdong`) | Official Deluxe = **1 king**. | PRIOR ✅ Deluxe King **$624/nt ($4,992)** breakfast incl. · free cancel **day of arrival** | ✅ | [Booking](https://www.booking.com/hotel/kr/le-meridien-seoul-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Marriott](https://www.marriott.com/en-us/hotels/selmm-le-meridien-seoul-myeongdong/overview/) |
| 13 | Aloft Myeongdong (`seoul-aloft-myeongdong`) | Official = **Aloft Room, 1 King**. | PRIOR ✅ 1 King **$323/nt ($2,581)** · free cancel **Oct 31** | ✅ | [Booking](https://www.booking.com/hotel/kr/aloft-seoul-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Marriott](https://www.marriott.com/en-us/hotels/selmo-aloft-seoul-myeongdong/overview/) |
| 14 | Courtyard Myeongdong (`seoul-courtyard-myeongdong`) | Official = **Guest Room, 1 King**. | PRIOR ✅ 1 King **$324/nt ($2,595)** · free cancel **day of arrival** | ✅ | [Booking](https://www.booking.com/hotel/kr/courtyard-by-marriott-seoul-namdaemun.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Marriott](https://www.marriott.com/en-us/hotels/selsn-courtyard-seoul-myeongdong/overview/) |
| 15 | Four Points Josun MD (`seoul-four-points-myeongdong`) | Official Deluxe King exists; Booking lead-in = **1 full**. | PRIOR ✅ Superior double **$234/nt ($2,081)** · 1 **full** · free cancel **Oct 29** | ⚠️ king exists; cheapest refundable is full | [Booking](https://www.booking.com/hotel/kr/four-points-by-sheraton-seoul-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Marriott](https://www.marriott.com/en-us/hotels/selfd-four-points-josun-seoul-myeongdong/overview/) |
| 16 | Nine Tree MD2 (`seoul-nine-tree-myeongdong2`) | Hollywood Double = Booking “1 king”; physical bed is typically **joined mattresses**. | PRIOR ✅ Hollywood Double **$303/nt ($2,422)** · free cancel **Oct 29** | ⚠️ Hollywood = joined | [Booking](https://www.booking.com/hotel/kr/nine-tree-premier-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Official](https://www.ninetreehotels.com/nth2/?lang=en) |
| 17 | Nine Tree Insadong (`seoul-nine-tree-insadong`) | Official brand is **Nine Tree Premier Hotel Insadong**. Width unpublished. | PRIOR ✅ Deluxe Double Jogyesa **$235/nt ($1,881)** · 1 queen label · free cancel **Oct 29** | ⚠️ width unpublished | [Booking](https://www.booking.com/hotel/kr/nine-tree-premier-insadong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Official](https://www.ninetreehotels.com/nth3/) |
| 18 | Shilla Stay Gwanghwamun (`seoul-shilla-stay-gwanghwamun`) | Standard Double = **1 full**. Hollywood = joined / OTA “king”. | PRIOR ✅ Standard Double **$200/nt ($1,600)** · 1 full · free cancel **Oct 29** | ⚠️ captured room is full, not king | [Booking](https://www.booking.com/hotel/kr/shilla-stay-gwanghwamun.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 19 | LOTTE HOTEL SEOUL (`seoul-lotte-hotel`) | Booking: Main Tower Grand Superior Double = **1 full**. Rebranded **THE GRAND LOTTE SEOUL**. | PRIOR ✅ Grand Superior Double **$364/nt ($3,235)** · free cancel **Oct 29** | ❌ full, not king | [Booking](https://www.booking.com/hotel/kr/lotte-seoul-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Lotte](https://www.lottehotel.com/seoul-hotel/en/rooms) |
| 20 | Westin Josun Seoul (`seoul-westin-josun`) | Official Deluxe = **1 king**. | PRIOR ✅ Deluxe King **$398/nt ($3,532)** · free cancel **day of arrival** | ✅ | [Booking](https://www.booking.com/hotel/kr/westin-chosun-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Marriott](https://www.marriott.com/en-us/hotels/selwi-the-westin-josun-seoul/overview/) |

### B. Extra 10 Seoul hotels — LIVE this session (2026-08-18 ~18:20 UTC)

These ten previously had **unsourced** “typical” prices with no `sourceUrl` / `capturedAtUtc`. Live dated pages were opened this session.

| # | Hotel (ID) | LIVE bed count | LIVE refundable price Nov 1–9 | vs stored price | Core match? | Manual links |
|---|---|---|---|---|:---:|---|
| 21 | Four Points Josun Seoul Station (`seoul-four-points-seoul-station`) | LIVE Booking: **Superior Double = 1 full bed**. Official Marriott `/rooms/`: Guest room **1 Double**; **Deluxe Guest room 1 King** exists. | LIVE ✅ Superior Double **$181/nt ($1,609)** · 10% service incl. · free cancel **Nov 1** · 10% VAT excl. | Stored $154 “Superior King” is **wrong room + unsourced**. King exists as Deluxe, not priced on this fetch. | ⚠️ king exists (Deluxe); cheapest refundable is 1 full | [Booking](https://www.booking.com/hotel/kr/four-points-by-sheraton-seoul-namsan.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Marriott rooms](https://www.marriott.com/en-us/hotels/selfp-four-points-josun-seoul-station/rooms/) |
| 22 | THE PLAZA Autograph (`seoul-the-plaza-autograph-collection`) | Listed: Deluxe King / Club Deluxe / suites = **1 king** each. | LIVE 🚫 **“We have no availability here between Sun, Nov 1, 2026 and Mon, Nov 9, 2026.”** | Stored $199 is **not a live dated rate**. | ✅ king listed; book Marriott direct | [Booking](https://www.booking.com/hotel/kr/theplaza.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Marriott](https://www.marriott.com/en-us/hotels/selak-the-plaza-seoul-autograph-collection/overview/) |
| 23 | Travelodge Myeongdong Euljiro (`seoul-travelodge-myeongdong-euljiro`) | Visible row: Superior Twin = **2 twin beds**. One-bed refundable row **not isolated** this fetch. Self-service laundromat confirmed. | LIVE ⚠️ Superior Twin **$151/nt ($1,211)** is **non-refundable**. Refundable one-bed not captured. | Stored $90 “Superior Queen” is **unsourced**. | ⚠️ queen claim not re-read on the dated table | [Booking](https://www.booking.com/hotel/kr/holiday-inn-express-seoul-euljiro.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 24 | Sotetsu Fresa Inn Myeongdong (`seoul-sotetsu-fresa-inn-myeongdong`) | LIVE: Standard Double = **1 full bed** (3 left). | LIVE ✅ **$196/nt ($1,567)** · free cancel **Oct 30** (2 days; then 1st night) · pay nothing until **Oct 28** · 10% tax excl. | Stored $95 is **not the live rate**. | ❌ 1 full; width unpublished | [Booking](https://www.booking.com/hotel/kr/sotetsu-fresa-inn-seoul-myeong-dong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Official](https://sotetsu-hotels.com/en/fresa-inn/seoul-myeongdong/) |
| 25 | Stanford Hotel Myeongdong (`seoul-stanford-hotel-myeongdong`) | Page: “mostly unavailable”. Visible Family Twin = **2 full beds** $269. Standard Double **not isolated**. | LIVE ⚠️ one-bed refundable **not captured**. Family Twin 2-full **$269/nt ($2,154)** · free cancel **Oct 29**. | Stored $116 is **unsourced**. | ❌ one-bed rate not isolated | [Booking](https://www.booking.com/hotel/kr/seutaenpodeuhotel-myeongdong-stanford-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Official](https://www.stanford-hotel.com/myeongdong/en/) |
| 26 | Sotetsu Splaisir Myeongdong (`seoul-sotetsu-splaisir-myeongdong`) | LIVE: Deluxe High-Floor Double = **1 full bed** (1 left). | LIVE ✅ **$204/nt ($1,628)** · free cancel **Oct 30** · pay nothing until **Oct 28** · 10% tax excl. | Stored $119 is **not the live rate**. | ❌ 1 full; width unpublished | [Booking](https://www.booking.com/hotel/kr/the-m-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Official](https://sotetsu-hotels.com/en/splaisir/myeong-dong/) |
| 27 | Hotel Vert (`seoul-hotel-vert`) | Listed Deluxe King = **1 king**; Deluxe Twin = 2 twin. Kitchen in rooms. 24-hour desk. | LIVE 🚫 **no availability Nov 1–9** on Booking. | Stored $133 is **not a live dated rate**. Slug `vert-seoul` **404s**; working slug is **`vert`**. | ✅ king listed; book other channel | [Booking](https://www.booking.com/hotel/kr/vert.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 28 | Royal Hotel Seoul (`seoul-royal-hotel`) | Identity confirmed: 61 Myeongdong-gil; 310 rooms; 24-hour desk. Dated rate table **failed to render** this fetch. | LIVE ⏳ price **not captured** (blank page / render fail). | Stored $173 is **unsourced**. | ⚠️ official claims Premier Double king — not re-read on dated table | [Booking](https://www.booking.com/hotel/kr/seoul-royal.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Official](https://www.royal.co.kr/en/index.php) |
| 29 | Sejong Hotel Myeongdong (`seoul-sejong-hotel-myeongdong`) | LIVE: Deluxe Double with Bath = **1 queen bed** (338 ft², extra-long beds). **Not a king.** | LIVE ✅ **$207/nt ($1,656)** · 54% off · free cancel **Oct 29** · ⚠️ inside 3 days = **total stay** · pay nothing until Oct 27 · 10% tax excl. | Stored $117 “King” is **wrong bed + unsourced price**. | ✅ queen + private bath + Myeongdong Exit 10 | [Booking](https://www.booking.com/hotel/kr/sejong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Official](http://www.sejong.co.kr/eng/) |
| 30 | Orakai Insadong Suites (`seoul-orakai-insadong-suites`) | LIVE cheapest refundable isolated row is **Two-Bedroom Premier = 1 king + 1 twin** (not one-bed). 24-hour reception + in-room washer confirmed. | LIVE ⚠️ refundable two-bed **$288/nt ($2,302)** · free cancel **Oct 27** (5 days; then 1st night). One-bed apartment **not isolated**. | Stored $146 one-bed king is **unsourced**. | ⚠️ one-bed rate not isolated | [Booking](https://www.booking.com/hotel/kr/orakai-insadong-suites.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |

---

## 2. Suwon — 5 hotels (PRIOR same-day dated captures)

| # | Hotel (ID) | Bed | Refundable Nov 1–9 | Core match? | Manual links |
|---|---|---|---|:---:|---|
| 1 | Novotel Ambassador Suwon (`suwon-novotel-ambassador`) | Accor: Superior/Deluxe/Executive = **1 King**. Direct covered access to Suwon KTX/subway. | PRIOR 🚫 **no Booking availability** — book Accor direct | ✅ | [Accor /8748](https://all.accor.com/hotel/8748/index.en.shtml) · [Booking](https://www.booking.com/hotel/kr/novotel-ambassador-suwon.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 2 | Four Points Suwon (`suwon-four-points`) | Official Premier = **1 king**. | PRIOR ✅ Premier King **$157/nt ($1,259)** · free cancel **day of arrival** | ❌ walkable metro not established | [Booking](https://www.booking.com/hotel/kr/four-points-by-sheraton-suwon.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Marriott](https://www.marriott.com/en-us/hotels/selfo-four-points-suwon/overview/) |
| 3 | Ramada Plaza Suwon (`suwon-ramada-plaza`) | Booking: “Deluxe King” = **1 queen**. ~12 min **drive** from Suwon Station. | PRIOR ✅ Deluxe King **$139/nt ($1,114)** · 1 queen · free cancel **Oct 31** | ❌ not walkable; king name = queen | [Booking](https://www.booking.com/hotel/kr/ramada-plaza-suwon.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 4 | Courtyard Suwon (`suwon-courtyard`) | Official Comfortable = **1 king**. Gwanggyo (~30 min from Suwon Station / Hwaseong). | PRIOR ✅ Comfortable King **$177/nt ($1,419)** · free cancel **day of arrival** | ❌ wrong district for Hwaseong | [Booking](https://www.booking.com/hotel/kr/courtyard-by-marriott-suwon.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Marriott](https://www.marriott.com/en-us/hotels/selcw-courtyard-suwon/overview/) |
| 5 | ibis Ambassador Suwon (`suwon-ibis`) | Standard/Superior = **1 full**. King = Junior Suite only. | PRIOR ✅ Standard/Superior Double **$104/nt ($834)** · free cancel **Oct 31 18:00** | ❌ double; station walk unverified | [Booking](https://www.booking.com/hotel/kr/ibis-suwon-ambassador.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Accor city page](https://ibis.accor.com/en/destination/city/hotels-suwon-v5590.html) |

---

## 3. Gyeongju — 15 hotels (Nov 9–15)

Gyeongju has **no subway**. Singyeongju KTX is outside Old Town and Bomun. **No property gets a full green core-needs badge.**

| # | Hotel (ID) | Bed | Refundable Nov 9–15 | Status | Manual links |
|---|---|---|---|---|---|
| 1 | Hwangnamkwan (`gyeongju-hwangnamkwan`) | Ondol / hanok bedding. Check-in **ends 22:00**. | PRIOR 🚫 no full-window availability | ⚠️ 22:00 lockout | [Booking](https://www.booking.com/hotel/kr/hwangnamguan-hanok-village-gyeongjusi.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [VisitKorea](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=63039) |
| 2 | Commodore (`gyeongju-commodore`) | Captured Imperial Suite = **2 beds** (twin + full). | PRIOR ✅ Imperial Suite **$205/nt ($1,365)** · free cancel **Nov 8** | ⚠️ captured room is 2-bed | [Booking](https://www.booking.com/hotel/kr/commodore-gyeongju.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 3 | Lahan Select (`gyeongju-lahan`) | Deluxe King Suite = **1 queen** (page’s own spec despite “King”). | PRIOR ✅ **$265/nt ($1,764)** · free cancel **Nov 7** | ⚠️ name/size mismatch | [Booking](https://www.booking.com/hotel/kr/hyundai-gyeongju.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Lahan](https://www.lahan.com/gyeongju/en/main.do) |
| 4 | Hilton Gyeongju (`gyeongju-hilton`) | LIVE: Premium King = **1 king**, lake view. | **LIVE** ✅ refundable **$257/nt ($1,712)** · free cancel **Nov 7** (2 days; then 1st night) · no prepay · 10% service incl. · 10% tax excl. Non-ref breakfast-incl. $237/$1,575. | Stored $165 is **unsourced and too low**. | [Booking](https://www.booking.com/hotel/kr/gyeongju-hilton.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Hilton](https://www.hilton.com/en/hotels/kyjgyhi-hilton-gyeongju/) |
| 5 | GG Hotel (`gyeongju-gg-hotel`) | Identity: Taejong-ro 699beon-gil 3, near bus terminal. Slug `gyeongju-dy-tourist`. Dated table **did not render**. | LIVE ⏳ **not captured**. Stored $88 is **unsourced**. | Do not treat $88 as a quote. | [Booking](https://www.booking.com/hotel/kr/gyeongju-dy-tourist.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 6 | Kolon (`gyeongju-kolon`) | LIVE: Premier Double or Twin = **1 full *or* twin+full**. Premier Super Twin = **2 queen**. Guest score **6.6/10**. | **LIVE** ✅ Premier Double **$82/nt ($491)** · free cancel **Nov 6** · ⚠️ inside 3 days = **total stay** · **full prepay charged any time**. Partner $65/$389 pay-in-advance. | Stored $75 is close but unsourced. Score is low. | [Booking](https://www.booking.com/hotel/kr/kolon.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 7 | The-K (`gyeongju-the-k`) | Captured Hwangnyoung View = **4 futons (ondol)**. | PRIOR ✅ **$125/nt ($752)** · free cancel **Nov 6** · ⚠️ inside = **total stay** | ⚠️ not a western one-bed | [Booking](https://www.booking.com/hotel/kr/the-k-gyeong-ju.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 8 | KINOCK (`gyeongju-kinock`) | PKG = **1 queen**. **Pet hotel**. | PRIOR ✅ PKG **$171/nt ($1,028)** · free cancel **Nov 2** (7 days; then 1st night) | ⚠️ pet-focused property | [Booking](https://www.booking.com/hotel/kr/the-suite-gyeongju.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Official](https://www.kinock.co.kr/gj/ko/Home/Main) |
| 9 | Swiss Rosen (`gyeongju-swiss-rosen`) | Captured Standard Twin = **twin + full**. | PRIOR ✅ **$83/nt ($556)** · free cancel **Nov 6** | ⚠️ 2-bed room | [Booking](https://www.booking.com/hotel/kr/swiss-rosen.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 10 | Rivertain (`gyeongju-rivertain`) | Standard Double = **1 full** + spa tub. Adults-only rooms. | PRIOR ✅ **$82/nt ($490)** breakfast incl. · free cancel **Nov 6** · ⚠️ inside = **total stay** | one-bed; width unpublished | [Booking](https://www.booking.com/hotel/kr/rivertain-hotel-gyeongju.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 11 | HanokInn (`gyeongju-hanokinn`) | Ondol/futon. | PRIOR 🚫 no full-window availability | book direct | [Booking](https://www.booking.com/hotel/kr/hanogin.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 12 | Wiyeonjae (`gyeongju-wiyeonjae`) | Ondol. | 🚫 **not listed on Booking** — books at wiyeonjae.kr | not capturable here | [VisitKorea](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=45556) |
| 13 | Nadul Hanok (`gyeongju-nadul-hanok`) | Bed + en-suite (width unpublished). | 🚫 **not listed on Booking** — gjhanok.com / hanok platforms | not capturable here | [VisitKorea](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=63076) |
| 14 | SONO Calm (`gyeongju-sono-calm`) | Family units (multi-bed). Legacy slug `daemyung-resort-gyeongju`. | PRIOR 🚫 no full-window availability | book SONO direct | [Booking](https://www.booking.com/hotel/kr/daemyung-resort-gyeongju.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [SONO](https://www.sonohotelsresorts.com/calm_gju/resort) |
| 15 | Kensington (`gyeongju-kensington`) | Captured Deluxe = **2 full beds**. | PRIOR ✅ **$160/nt ($957)** breakfast incl. · free cancel **Nov 2** (7-day cutoff) | ⚠️ 2-bed apartment | [Booking](https://www.booking.com/hotel/kr/kensington-resort-gyeongju.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Official](https://www.kensington.co.kr/rgj) |

**Gyeongju one-bed refundable options that actually exist on Booking for the full window:** Rivertain $490 (1 full + breakfast), Kolon $491 (1 full, harsh prepay), Hilton $1,712 (1 king), Lahan $1,764 (1 queen), Kinock $1,028 (1 queen, pet hotel). Hanok inventory does **not** stretch across 6 nights.

---

## 4. Busan — 20 hotels (Nov 15–22)

| # | Hotel (ID) | Bed | Refundable Nov 15–22 | Core match? | Manual links |
|---|---|---|---|:---:|---|
| 1 | Shilla Stay Haeundae | PRIOR: Standard Double = **1 full** $184/$1,288 | PRIOR ✅ free cancel Nov 12 | ⚠️ captured is full; Deluxe/Premier queen is a different selection | [Booking](https://www.booking.com/hotel/kr/shilla-stay-haeundae.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 2 | L7 HAEUNDAE | PRIOR: Standard King Town View = **1 king** $185/$1,294 | PRIOR ✅ free cancel Nov 12 | ✅ | [Booking](https://www.booking.com/hotel/kr/l7-haeundae-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Lotte](https://www.lottehotel.com/haeundae-l7/en/main.html) |
| 3 | ASTI Busan Station | PRIOR: Standard Double = **1 full** $78/$543 | PRIOR ⚠️ partner-offer / pay-in-advance row | ✅ Executive King exists separately | [Booking](https://www.booking.com/hotel/kr/asti-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 4 | Grand Josun Busan | PRIOR: Premier King = **1 queen** (page spec despite “King”) $347/$2,431 | PRIOR ✅ free cancel Nov 13 · ⚠️ inside = **total stay** | ⚠️ name/size mismatch | [Booking](https://www.booking.com/hotel/kr/grand-josun-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 5 | Park Hyatt Busan | PRIOR: King Ocean View = **1 king** $532/$3,721 | PRIOR ✅ free cancel Nov 14 | ✅ | [Booking](https://www.booking.com/hotel/kr/park-hyatt-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Hyatt](https://www.hyatt.com/park-hyatt/en-US/busph-park-hyatt-busan) |
| 6 | Toyoko Inn Haeundae 2 | Double = 1 full (Toyoko standard). | PRIOR 🚫 no availability Nov 15–22 | ❌ 140 cm class | [Booking](https://www.booking.com/hotel/kr/toyoko-inn-busan-haeundae-2.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Toyoko](https://www.toyoko-inn.com/eng/search/detail/00256/) |
| 7 | Ramada Encore Haeundae | Queen room exists; **adults-only** flag on listings. | Stored $74 has **no sourceUrl**. Prior capture was partial. **NOT treated as a quote.** | ⚠️ adults-only | [Booking](https://www.booking.com/hotel/kr/haeundae-ramada-encore.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 8 | SIGNIEL BUSAN | PRIOR: Premier Double = **1 king** $297/$2,306 | PRIOR ✅ free cancel Nov 10 (5 days) | ✅ | [Booking](https://www.booking.com/hotel/kr/signiel-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 9 | Paradise Busan | PRIOR: Deluxe Double = **1 king** $246/$1,915 | PRIOR ✅ free cancel Nov 13 | ✅ | [Booking](https://www.booking.com/hotel/kr/paradise-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 10 | Westin Josun Busan | PRIOR: Deluxe Park King = **1 full** (page spec despite “King”) $224/$1,742 | PRIOR ✅ | ⚠️ name/size mismatch | [Booking](https://www.booking.com/hotel/kr/the-westin-chosun-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 11 | Fairfield Haeundae | LIVE: Standard Room **1 King**, city view. | **LIVE** ✅ **$113/nt ($793)** · free cancel **Nov 15 00:00 (day of arrival)** · no prepay · 10% VAT excl. | ✅ | [Booking](https://www.booking.com/hotel/kr/fairfield-by-marriott-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Marriott](https://www.marriott.com/en-us/hotels/pusfi-fairfield-busan/overview/) |
| 12 | ibis budget Haeundae | Accor /9106: Standard = 1 double. | LIVE ⏳ slug `ibis-budget-haeundae` **bounced to Busan search** — property page not confirmed this fetch. Stored $45 **unsourced**. | ❌ 140 cm class | [Accor](https://all.accor.com/hotel/9106/index.en.shtml) |
| 13 | ibis Ambassador Haeundae | Accor /9643. | LIVE ⏳ slug `ibis-ambassador-busan-haeundae` **bounced to Busan search**. Stored $49 **unsourced**. | ⚠️ queen claim not re-read | [Accor](https://all.accor.com/hotel/9643/index.en.shtml) |
| 14 | LOTTE HOTEL BUSAN | PRIOR: Deluxe Double = **1 king** $162/$1,256 | PRIOR ✅ | ✅ Seomyeon connected | [Booking](https://www.booking.com/hotel/kr/lotte-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 15 | Avani Central | PRIOR: Deluxe King = **1 queen** (page spec despite “King”) $86/$599 | PRIOR ✅ free cancel Nov 12 | ⚠️ name/size mismatch; still one-bed | [Booking](https://www.booking.com/hotel/kr/avani-central-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 16 | Ramada Encore Station | PRIOR: Superior Double = **1 full** $94/$655 | PRIOR ✅ free cancel Nov 13 | ⚠️ Queen Room is a different (pricier) selection | [Booking](https://www.booking.com/hotel/kr/ramada-encore-by-wyndham-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 17 | Toyoko Inn Station No.1 | PRIOR: Economy Double = **1 full** $58/$406 breakfast incl. | PRIOR ✅ free cancel Nov 14 · ⚠️ inside 1 day = **total stay** | ❌ 140 cm class | [Booking](https://www.booking.com/hotel/kr/toyoko-inn-busan-no-1.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Toyoko](https://www.toyoko-inn.com/eng/search/detail/00194/) |
| 18 | Crown Harbor | 24-hour desk; Jungang Station a couple of minutes. | LIVE ⏳ dated rate table **did not render** on retry. Stored $86 **unsourced**. | ⚠️ width unpublished | [Booking](https://www.booking.com/hotel/kr/crown-harbour-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 19 | Fairfield Songdo | LIVE: Standard **1 King, Sea view**. | **LIVE** ✅ **$130/nt ($912)** · free cancel **Nov 15 00:00** · no prepay · 10% VAT excl. | ❌ no walkable metro in Songdo | [Booking](https://www.booking.com/hotel/kr/fairfield-by-marriott-busan-songdo-beach.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Marriott](https://www.marriott.com/en-us/hotels/pusfb-fairfield-busan-songdo-beach/overview/) |
| 20 | Wyndham Grand Busan Ijin | Official Deluxe King exists. Slug `wyndham-grand-busan`. | Stored $139 has **no sourceUrl**. **NOT treated as a quote.** | ❌ no walkable metro in Songdo | [Booking](https://www.booking.com/hotel/kr/wyndham-grand-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Wyndham](https://www.wyndhamhotels.com/wyndham-grand/busan-south-korea/wyndham-grand-busan-ijin/overview) |

---

## 5. Cheonan — 7 hotels (Nov 8–14 alternative)

| # | Hotel (ID) | Bed | Refundable Nov 8–14 | Core match? | Manual links |
|---|---|---|---|:---:|---|
| 1 | Shilla Stay Cheonan (`cheonan-shilla-stay`) | LIVE: Standard Double City View = **1 full**. Page: **Cheonan KTX is 9.3 mi**. 24-hour desk. | **LIVE** ✅ **$99/nt ($594)** · 24% off · free cancel **Nov 7** (1 day; then 1st night) · no prepay · 10% tax excl. | ❌ 1 full; not walkable to KTX | [Booking](https://www.booking.com/hotel/kr/shilla-cheonan.html?checkin=2026-11-08&checkout=2026-11-14&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 2 | Ramada Encore Cheonan (`cheonan-ramada-encore`) | LIVE: Double Room = **1 full** (269 ft²). ~2.6 mi from Cheonan-Asan Station. | **LIVE** ✅ **$68/nt ($408)** · free cancel **Nov 7** · no prepay · city tax + 10% tax excl. | ❌ 1 full; not walkable to KTX | [Booking](https://www.booking.com/hotel/kr/ramada-encore-cheonan.html?checkin=2026-11-08&checkout=2026-11-14&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Wyndham](https://www.wyndhamhotels.com/ramada/cheonan-si-south-korea/ramada-encore-cheonan/overview) |
| 3 | ON City Hotel (`cheonan-on-city`) | Identity: 105 Buldang 4-ro; 2.2 mi north of Cheonan-Asan. | **NOT LIVE.** Stored $58 is a typical autumn rate. Slug `on-city`. | ❌ | [Booking](https://www.booking.com/hotel/kr/on-city.html?checkin=2026-11-08&checkout=2026-11-14&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Official](http://www.oncityhotel.com/web/eng/asp/index/index.asp) |
| 4 | SONO Belle Cheonan (`cheonan-sono-belle`) | Official family rooms = **2 double beds**. | **NOT LIVE.** Stored $95 typical. | ❌ family resort; no walkable rail | [SONO](https://www.sonohotelsresorts.com/belle_ca/roomsviewall) |
| 5 | SureStay Plus Asan (`cheonan-best-western-asan`) | Identity via Booking listing. | **NOT LIVE.** Stored $75 typical. | ❌ | [Booking](https://www.booking.com/hotel/kr/surestay-plus-by-best-western.html) |
| 6 | Brown Dot Dongnam (`cheonan-brown-dot`) | ~900 m from Cheonan Station (Line 1, not KTX). | **NOT LIVE.** Stored $48 typical. | ❌ width unpublished | [Trip.com listing](https://www.trip.com/hotels/cheonan-si-hotel-detail-62705121/brown-dot-hotel-cheonan-dongnam/) |
| 7 | The Mains Hotel (`cheonan-mains`) | Identity via Booking. | **NOT LIVE.** Stored $58 typical. | ❌ | [Booking](https://www.booking.com/hotel/kr/the-mains.html) |

---

## 6. Daejeon — 7 hotels (Nov 8–14 alternative)

| # | Hotel (ID) | Bed | Refundable Nov 8–14 | Core match? | Manual links |
|---|---|---|---|:---:|---|
| 1 | Toyoko Inn Gov. Complex (`daejeon-toyoko-inn`) | Official Toyoko double = **140 cm class**. ~10 min from Government Complex metro. | **NOT LIVE.** Stored $55 typical (breakfast incl. is brand-standard, not a dated quote). Slug `toyoko-inn-daejeon-government-complex`. | ❌ 140 cm | [Booking](https://www.booking.com/hotel/kr/toyoko-inn-daejeon-government-complex.html?checkin=2026-11-08&checkout=2026-11-14&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Toyoko](https://www.toyoko-inn.com/eng/search/detail/00234/) |
| 2 | Ramada Daejeon (`daejeon-ramada`) | Yuseong. 24-hour desk. | **NOT LIVE.** Stored $72 typical. Slug `ramada-daejeon`. | ❌ Yuseong, not KTX-walkable | [Booking](https://www.booking.com/hotel/kr/ramada-daejeon.html?checkin=2026-11-08&checkout=2026-11-14&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Wyndham](https://www.wyndhamhotels.com/ramada/daejeon-south-korea/ramada-daejeon/overview) |
| 3 | LOTTE City Daejeon (`daejeon-lotte-city`) | LIVE: Standard Double / Hollywood Double = **1 full**. Page: **4.8 mi from Daejeon Station**. 24-hour desk. | **LIVE** ✅ Standard Double **$156/nt ($933)** · free cancel **Nov 5** (3 days; then 1st night) · no prepay · 10% tax excl. | ❌ 1 full; Expo/CCC district, not KTX-walkable | [Booking](https://www.booking.com/hotel/kr/lotte-city-daejeon.html?checkin=2026-11-08&checkout=2026-11-14&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Lotte](https://www.lottehotel.com/prerendered/daejeon-city/en/index.html) |
| 4 | BENIKEA Daelim (`daejeon-benikea-daelim`) | Jungangno area. | **NOT LIVE.** Stored $48 typical. | ❌ | [VisitKorea](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=85393) |
| 5 | Le Stendal (`daejeon-hotel-stendhal`) | Yuseong. | **NOT LIVE.** Stored $75 typical. | ❌ Yuseong | [Official](http://stendhalhotel.co.kr/) |
| 6 | Hotel Interciti (`daejeon-hotel-interciti`) | Yuseong. | **NOT LIVE.** Stored $72 typical. | ❌ Yuseong | [VisitKorea](https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=86274) |
| 7 | Aank Air Daejeon Station (`daejeon-aank-air`) | ~9 min walk to Daejeon Station. | **NOT LIVE.** Stored $45 typical. | ❌ width unpublished; closest to KTX of this set | [Booking](https://www.booking.com/hotel/kr/aank-daejeon-station.html) |

---

## 7. Options that actually meet the core rule (one queen/king + private bath + walkable rail)

These are the only rows where **bed type is source-backed as queen/king** and **rail is walkable**. Prices are snapshots.

### Seoul (Nov 1–9)

| Hotel | Room to book | Bed evidence | Refundable snapshot | Link |
|---|---|---|---|---|
| Somerset Palace | Studio Executive / Executive One-Bedroom | Official 1 queen | $228/nt ($1,824) · cancel Oct 30 | [Booking](https://www.booking.com/hotel/kr/somerset-palace-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Nine Tree MD1 | **Standard Double only** (not Hollywood) | Official 160×190 cm | $205/nt ($1,643) · cancel Oct 29 | [spec](https://www.ninetreehotels.com/nth1/room_standard_double.php) |
| Moxy Myeongdong | Queen Room with City View | Official 1 queen | $308/nt ($2,460) · cancel day-of | [Marriott](https://www.marriott.com/en-us/hotels/selmx-moxy-seoul-myeongdong/overview/) |
| L'Escape | Classic King | Marriott Classic = 1 king | $305/nt ($2,443) · cancel day-of | [Booking](https://www.booking.com/hotel/kr/l-39-escape.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Courtyard Myeongdong | Guest Room, 1 King | Official 1 king | $324/nt ($2,595) · cancel day-of | [Marriott](https://www.marriott.com/en-us/hotels/selsn-courtyard-seoul-myeongdong/overview/) |
| Aloft Myeongdong | Aloft Room, 1 King | Official 1 king | $323/nt ($2,581) | [Marriott](https://www.marriott.com/en-us/hotels/selmo-aloft-seoul-myeongdong/overview/) |
| Le Méridien Myeongdong | Deluxe King | Official 1 king | $624/nt ($4,992) breakfast | [Marriott](https://www.marriott.com/en-us/hotels/selmm-le-meridien-seoul-myeongdong/overview/) |
| Westin Josun Seoul | Deluxe King | Official 1 king | $398/nt ($3,532) · cancel day-of | [Marriott](https://www.marriott.com/en-us/hotels/selwi-the-westin-josun-seoul/overview/) |
| ibis Ambassador Insadong | Superior (Renovated) | Accor = 1 queen | no Booking inventory — Accor direct | [Accor /8002](https://all.accor.com/hotel/8002/index.en.shtml) |
| Sejong Myeongdong | Deluxe Double with Bath | LIVE Booking = **1 queen** | **$207/nt ($1,656)** · cancel Oct 29 · ⚠️ total-stay penalty inside 3 days | [Booking](https://www.booking.com/hotel/kr/sejong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Four Points Seoul Station | **Deluxe Guest room, 1 King** (not Superior Double) | Official Marriott Deluxe = 1 King | Deluxe King not priced this fetch; Superior Double $181 is 1 full | [Marriott rooms](https://www.marriott.com/en-us/hotels/selfp-four-points-josun-seoul-station/rooms/) |

### Suwon

| Hotel | Room | Note |
|---|---|---|
| Novotel Ambassador Suwon | Superior 1 King | Only Suwon green match. Book Accor — Booking sold out. |

### Busan (Nov 15–22) — king/queen + walkable metro

L7 Haeundae Standard King $185 · SIGNIEL Premier $297 · Park Hyatt King Ocean $532 · Paradise Deluxe $246 · LOTTE Hotel Busan Deluxe $162 · Fairfield Haeundae **LIVE $113** · Avani “King” (actually 1 queen) $86.

### Gyeongju / Cheonan / Daejeon

No complete green match (no walkable KTX/subway + confirmed queen/king together). Strongest *bed-only* Gyeongju pick if the station rule is relaxed: **Hilton Premium King LIVE $257/nt**.

---

## 8. Irregularities flagged for review

1. **Fourteen “typical autumn rate” blocks are not quotes.** All 7 Cheonan + 7 Daejeon originally stored prices with no `sourceUrl` / no `capturedAtUtc`. This pass replaced **Shilla Stay Cheonan, Ramada Encore Cheonan, and LOTTE City Daejeon** with live dated rows. The other 11 remain **unsourced**.
2. **Ten extra Seoul hotels had invented-looking prices.** Live fetch contradicted several: Sotetsu Fresa $95→**$196**; Splaisir $119→**$204**; Sejong $117 king→**$207 queen**; Four Points Station $154 king→**$181 full**; Plaza / Vert **sold out** on Booking (stored prices were not real for these dates).
3. **Hotel Vert verification URL 404s.** `booking.com/hotel/kr/vert-seoul.html` is dead. Working slug is **`vert`**.
4. **Sejong Deluxe is a queen, not a king** (Booking: “1 queen bed”, 338 ft²). Cancellation inside 3 days is the **total stay**, not first night.
5. **Four Points Seoul Station official inventory is Double / Twin / Deluxe King.** The record’s “Superior King” as the lead-in room is not what Booking or Marriott `/rooms/` lead with.
6. **King/queen naming mismatches (live or prior page spec):** Ramada Plaza Suwon Deluxe King = 1 queen; Lahan “King Suite” = 1 queen; Grand Josun “Premier King” = 1 queen; Westin Josun Busan “Park King” = 1 full; Avani “Deluxe King” = 1 queen.
7. **Hollywood / joined-mattress rooms** (L7, Nine Tree MD1/MD2, Shilla, LOTTE City Daejeon Hollywood Double) conflict with “not two beds pushed together.”
8. **Fairmont / several Gyeongju captures are 2-bed rooms** presented as the hotel’s refundable rate. They are genuine refundables but not the one-bed preference.
9. **ibis Ambassador / ibis budget Busan Haeundae** slugs bounced to city search this session — do not treat stored $45 / $49 as dated quotes until a property page is re-resolved.
10. **KINOCK is a pet hotel.** Rivertain rooms are adults-only. Ramada Encore Haeundae is listed adults-only.
11. **Hwangnamkwan check-in ends 22:00.** Kolon guest score **6.6/10**. The-K score **7.1/10**.
12. **Korean “double” ≠ automatically 140 cm.** Nine Tree MD1 official double is **160 cm**. Width must come from the official spec, not Booking’s “full” label.
13. **Gyeongju 6-night hanok window is largely unsellable** on Booking (Hwangnamkwan, HanokInn, SONO Calm sold out; Wiyeonjae / Nadul not listed).

---

## 9. What was changed in data this pass

See the matching updates in `data/hotels.json` / `data/pricing-history.json`:

- Live `refundableRate` + source URL + UTC timestamp written for: Four Points Seoul Station, THE PLAZA, Sotetsu Fresa, Sotetsu Splaisir, Hotel Vert (no-avail), Sejong, Orakai (two-bed isolation note), Hilton Gyeongju, Kolon, Fairfield Haeundae, Fairfield Songdo, Shilla Stay Cheonan, Ramada Encore Cheonan, LOTTE City Daejeon.
- Sejong Deluxe bed **king → queen**.
- Four Points Seoul Station rooms aligned to official Marriott (Guest room 1 Double + Deluxe 1 King).
- Hotel Vert verification URL slug `vert-seoul` → `vert`.
- Unsourced leftover Cheonan/Daejeon/Busan/Seoul extra rates left in place **only where no live row was isolated**, and flagged above — they are **not** presented as quotes.

`python3 validate.py` and `python3 build.py` should be run after review.

*Live fetches completed 2026-08-18 ~18:15–18:22 UTC. Prior same-day captures remain in `data/pricing-history.json`. Re-open every link before paying.*
