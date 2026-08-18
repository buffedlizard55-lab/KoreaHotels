# Gyeongju, Busan, Cheonan, Daejeon, Suwon — Line-by-line Verification

**Scope:** Gyeongju (15 hotels) · Busan (20 hotels) · Cheonan (7 hotels) · Daejeon (7 hotels) · Suwon (5 hotels).
**Priced stay windows:** Gyeongju **Nov 9–15, 2026** (6 nights, 2 adults); Busan **Nov 15–22, 2026** (7 nights, 2 adults); Cheonan, Daejeon, and Suwon use typical rate baselines or date-anchored captures.
**Method:** Verified line-by-line against official brand pages (Marriott, Accor, Lotte, Shilla, Josun, Wyndham) and live Booking.com dated rate tables.

---

## 1. Suwon — 5 Hotels Checklist
*Stay window: Nov 1–9, 2026 (8 nights, 2 adults, before taxes).*

| # | Hotel Name (ID) | Checked Bed Size & Count (Official Spec) | Refundable Pricing Snapshot (Nov 1–9, 2026) | Core Needs Match? | Manual Verification Link |
|---|---|---|---|:---:|---|
| 1 | **Novotel Ambassador Suwon** (`suwon-novotel-ambassador`) | Superior 1 King: **1 King bed** (Accor: 1 x King size bed) | *Sold out on Booking* (Check direct Accor) | ✅ **Yes** (Covered bridge directly connects to Suwon Station KTX/metro and shopping) | [Accor Official](https://all.accor.com/hotel/8748/index.en.shtml) |
| 2 | **Four Points by Sheraton Suwon** (`suwon-four-points`) | Premier King: **1 King bed** (official Marriott category) | $157/night ($1,259 total) | ❌ **No** (King bed + private bath confirmed, but walkable metro distance is unverified) | [Marriott Official](https://www.marriott.com/en-us/hotels/selfo-four-points-suwon/overview/) / [Booking](https://www.booking.com/hotel/kr/four-points-by-sheraton-suwon.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 3 | **Ramada Plaza by Wyndham Suwon** (`suwon-ramada-plaza`) | Deluxe King: **1 Queen bed** (Booking lists 1 queen bed despite the 'King' room name) | $139/night ($1,114 total) | ❌ **No** (Not walkable to station, ~12 min drive; 'King' room is actually a queen) | [Booking](https://www.booking.com/hotel/kr/ramada-plaza-suwon.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 4 | **Courtyard by Marriott Suwon** (`suwon-courtyard`) | Comfortable King: **1 King bed** (official Marriott category) | $177/night ($1,419 total) | ❌ **No** (Location in Gwanggyo is ~30 min from Suwon Stn/Hwaseong Fortress) | [Marriott Official](https://www.marriott.com/en-us/hotels/selcw-courtyard-suwon/overview/) / [Booking](https://www.booking.com/hotel/kr/courtyard-by-marriott-suwon.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 5 | **ibis Ambassador Suwon** (`suwon-ibis`) | Standard 1 Double: **1 double bed** (width unstated) | $104/night ($834 total) | ❌ **No** (Standard is double; King is Junior Suite only; station walk unverified) | [Accor Official](https://ibis.accor.com/en/destination/city/hotels-suwon-v5590.html) / [Booking](https://www.booking.com/hotel/kr/ibis-suwon-ambassador.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |

---

## 2. Gyeongju — 15 Hotels Checklist
*Stay window: Nov 9–15, 2026 (6 nights, 2 adults, before taxes).*

Gyeongju has no subway system, and Singyeongju KTX is located outside both the Old Town and Bomun Lake Resort zones. Thus, none of the Gyeongju properties are awarded the complete walkable rail match (`fits: false`).

| # | Hotel Name (ID) | Checked Bed Size & Count (Official Spec) | Refundable Pricing Snapshot (Nov 9–15, 2026) | Transit Note & Area | Verification Link |
|---|---|---|---|---|---|
| 1 | **Hwangnamkwan Hanok Hotel** (`gyeongju-hwangnamkwan`) | Standard/Deluxe: Ondol floor bedding (Double-wide, ~140–180 cm) | *Sold out on Booking* (Check direct hanokvillage.co.kr) | Old Town; no subway | [VisitKorea Official](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=63039) |
| 2 | **Commodore Hotel Gyeongju** (`gyeongju-commodore`) | Superior/Deluxe Double: 1 double bed (approx 140–180 cm wide) | $205/night ($1,365 total) for Imperial Suite | Bomun Lake Resort | [VisitKorea Official](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=99034) |
| 3 | **Lahan Select Gyeongju** (`gyeongju-lahan`) | Deluxe King Suite: 1 Queen bed (approx 150 cm wide) | $265/night ($1,764 total) | Bomun Lake Resort | [Lahan Official](https://www.lahan.com/gyeongju/en/main.do) |
| 4 | **Hilton Gyeongju** (`gyeongju-hilton`) | Deluxe King Room: 1 King-size bed (36 m²) | $165/night ($990 total) | Bomun Lake Resort | [Hilton Official](https://www.hilton.com/en/hotels/kyjgyhi-hilton-gyeongju/) |
| 5 | **GG Hotel Gyeongju** (`gyeongju-gg-hotel`) | Deluxe Double: 1 King bed (36 m²); Standard Double: 1 double bed | $88/night ($528 total) | City Center; near Bus Terminal | [KoreaETour Cross-Check](https://www.koreaetour.com/gyeongju-gg-hotel/) |
| 6 | **Kolon Hotel Gyeongju** (`gyeongju-kolon`) | Executive Double: 1 Queen bed; Premier: 1 double bed | $75/night ($450 total) | Bulguksa / Tohamsan area | [VisitKorea Official](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=99009) |
| 7 | **The-K Hotel Gyeongju** (`gyeongju-the-k`) | Standard Double: 1 double bed; Ondol: Traditional futons | $125/night ($752 total) for Ondol Room (4 futons) | Bomun Lake Resort / HICO | [VisitKorea Official](https://english.visitkorea.or.kr/enu/ATR/SI_EN_3_1_1_1.jsp?cid=1061398) |
| 8 | **KINOCK Gyeongju** (`gyeongju-kinock`) | KINOCK Premier: 1 Queen bed (Dog-friendly property) | $171/night ($1,028 total) for PKG private pool room | North Bomun (ex-Suites Hotel) | [Kinock Official](https://www.kinock.co.kr/gj/ko/Home/Main) |
| 9 | **Benikea Swiss Rosen Hotel Gyeongju** (`gyeongju-swiss-rosen`) | Deluxe Double: 1 double bed (exact width unstated) | $83/night ($556 total) for Standard Twin | Bomun Lake Resort / HICO | [VisitKorea Official](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=85181) |
| 10 | **Rivertain Hotel Gyeongju** (`gyeongju-rivertain`) | Standard Double: 1 double bed (en-suite enclosed spa tub) | $82/night ($490 total) with breakfast | City Center; near Bus Terminal | [VisitKorea Official](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=60519) |
| 11 | **HanokInn** (`gyeongju-hanokinn`) | Hanok Double Room: Traditional ondol/futon bedding | *Sold out on Booking* (Check direct hanokinn.com) | Hwangnidan-gil / Old Town | [VisitKorea Official](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=45559) |
| 12 | **Wiyeonjae Hanok Stay** (`gyeongju-wiyeonjae`) | Ondol Room: Traditional ondol/futon floor bedding | *Books direct only* at wiyeonjae.kr or hanok platforms | Historic Area / Cheomseongdae | [VisitKorea Official](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=45556) |
| 13 | **Nadul Hanok** (`gyeongju-nadul-hanok`) | Hanok Room with Bed: 1 double bed (en-suite bath) | *Books direct only* at gjhanok.com or traditional channels | Historic Area / Cheomseongdae | [VisitKorea Official](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=63076) |
| 14 | **SONO Calm Gyeongju** (`gyeongju-sono-calm`) | Family Lake: 1 double + 2 single beds; kitchen | *Sold out on Booking* (Check direct sonohotelsresorts.com) | Bomun Lake Resort | [SONO Official](https://www.sonohotelsresorts.com/calm_gju/resort) |
| 15 | **Kensington Resort Gyeongju** (`gyeongju-kensington`) | Kensington Studio: 1 double bed (width unstated) | $160/night ($957 total) for Deluxe 2-full beds | North Bomun Lake | [Kensington Official](https://www.kensington.co.kr/rgj) |

---

## 3. Busan — 20 Hotels Checklist
*Stay window: Nov 15–22, 2026 (7 nights, 2 adults, before taxes).*

| # | Hotel Name (ID) | Checked Bed Size & Count (Official Spec) | Refundable Pricing Snapshot (Nov 15–22, 2026) | Core Needs Match? | Manual Verification Link |
|---|---|---|---|:---:|---|
| 1 | **Shilla Stay Busan Haeundae** | Deluxe/Premier: 1 Queen bed (150×200 cm) | $184/night ($1,288 total) | ✅ **Yes** (~5-9 min to Haeundae Stn) | [Shilla Official](https://www.shillastay.com/haeundae/main.do?lang=en) / [Booking](https://www.booking.com/hotel/kr/shilla-stay-haeundae.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 2 | **L7 HAEUNDAE by LOTTE HOTELS** | Deluxe: 1 Queen bed (150×200 cm) | $185/night ($1,294 total) for Standard King | ✅ **Yes** (~10 min to Haeundae Stn) | [Lotte Official](https://www.lottehotel.com/haeundae-l7/en/main.html) / [Booking](https://www.booking.com/hotel/kr/l7-haeundae-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 3 | **ASTI Hotel Busan Station** | Executive: 1 King bed (180×200 cm); Standard: 1 double | $78/night ($543 total) for Standard Double | ✅ **Yes** (~1 min to KTX Station) | [ASTI Official](https://www.astihotel.com) / [Booking](https://www.booking.com/hotel/kr/asti-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 4 | **Grand Josun Busan** | Deluxe Queen or King (150/180×200 cm) | $347/night ($2,431 total) for Premier King | ✅ **Yes** (~7-10 min to Haeundae Stn) | [Josun Official](https://gjb.josunhotel.com/main.do?locale=en) / [Booking](https://www.booking.com/hotel/kr/grand-josun-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 5 | **Park Hyatt Busan** | Deluxe King: 1 King bed (180×200 cm) | $532/night ($3,721 total) for King Ocean View | ✅ **Yes** (~8 min to Dongbaek Stn) | [Hyatt Official](https://www.hyatt.com/park-hyatt/en-US/busph-park-hyatt-busan) / [Booking](https://www.booking.com/hotel/kr/park-hyatt-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 6 | **Toyoko Inn Busan Haeundae No.2** | Standard Double: 1 double bed (140×200 cm) | *Sold out on Booking* (Check Toyoko site) | ❌ **No** (Double bed below 150 cm queen minimum) | [Toyoko Official](https://www.toyoko-inn.com/eng/search/detail/00256/) / [Booking](https://www.booking.com/hotel/kr/toyoko-inn-busan-haeundae-2.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 7 | **Ramada Encore by Wyndham Haeundae** | Standard Double: 1 double bed (140×200 cm) | $74/night ($518 total) for Queen Room | ❌ **No** (Standard is double; Queen is a separate selection) | [Wyndham Official](https://www.wyndhamhotels.com/ramada/busan-south-korea/ramada-encore-haeundae/overview) / [Booking](https://www.booking.com/hotel/kr/haeundae-ramada-encore.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 8 | **SIGNIEL BUSAN** | Premier Double: 1 Queen bed (150×200 cm) | $297/night ($2,306 total) | ✅ **Yes** (~12 min to Jung-dong Stn) | [Lotte Official](https://www.lottehotel.com/busan-signiel/en/rooms/signiel-premier-familytwin-ocean-view.html) / [Booking](https://www.booking.com/hotel/kr/signiel-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 9 | **Paradise Hotel Busan** | Premium Deluxe Ocean King: 1 King bed (180×200 cm) | $246/night ($1,915 total) for Deluxe Double | ✅ **Yes** (~10 min to Haeundae Stn) | [Paradise Official](https://www.busanparadisehotel.co.kr/front/hotel/room/view?RR_ROOM_CATEGORY=PREMIUM_DELUXE&RR_ROOM_TYPE=PREMIUM_DELUXE_OCEAN_DOUBLE) / [Booking](https://www.booking.com/hotel/kr/paradise-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 10 | **The Westin Josun Busan** | Deluxe King: 1 King bed (180×200 cm) | $224/night ($1,742 total) for Deluxe Park King | ✅ **Yes** (~10 min to Dongbaek Stn) | [Marriott Official](https://www.marriott.com/en-us/hotels/puswi-the-westin-josun-busan/overview/) / [Booking](https://www.booking.com/hotel/kr/the-westin-chosun-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 11 | **Fairfield by Marriott Busan** | Standard King: 1 King bed (180×200 cm) | $93/night ($651 total) | ✅ **Yes** (~10 min to Haeundae Stn) | [Marriott Official](https://www.marriott.com/en-us/hotels/pusfi-fairfield-busan/overview/) / [Booking](https://www.booking.com/hotel/kr/fairfield-by-marriott-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 12 | **ibis budget Ambassador Busan Haeundae** | Standard Double: 1 double bed (140×200 cm) | $45/night ($315 total) | ❌ **No** (Double bed below 150 cm queen minimum) | [Accor Official](https://all.accor.com/hotel/9106/index.en.shtml) / [Booking](https://www.booking.com/hotel/kr/ibis-budget-ambassador-busan-haeundae.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 13 | **ibis Ambassador Busan Haeundae** | Standard Room: 1 Queen bed (150×200 cm) | $49/night ($343 total) | ✅ **Yes** (~8 min to Haeundae Stn) | [Accor Official](https://all.accor.com/hotel/9643/index.en.shtml) / [Booking](https://www.booking.com/hotel/kr/ibis-ambassador-busan-haeundae.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 14 | **LOTTE HOTEL BUSAN** | Premier Double: 1 King bed (180×200 cm); Deluxe: 1 King | $162/night ($1,256 total) for Deluxe Double | ✅ **Yes** (Connected to Seomyeon Station) | [Lotte Official](https://www.lottehotel.com/busan-hotel/en/rooms/premier-room.html) / [Booking](https://www.booking.com/hotel/kr/lotte-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 15 | **Avani Central Busan** | Deluxe King: 1 King bed (180×200 cm) | $86/night ($599 total) | ✅ **Yes** (~2 min to BIFC Station) | [Avani Official](https://www.avanihotels.com/en/central-busan) / [Booking](https://www.booking.com/hotel/kr/avani-central-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 16 | **Ramada Encore by Wyndham Busan Station** | Queen Room: 1 Queen bed (150×200 cm) | $94/night ($655 total) for Superior Double | ✅ **Yes** (~1 min to KTX Station) | [Wyndham Official](https://www.wyndhamhotels.com/ramada/busan-south-korea/ramada-encore-busan-station/overview) / [Booking](https://www.booking.com/hotel/kr/ramada-encore-by-wyndham-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 17 | **Toyoko Inn Busan Station No.1** | Double Room: 1 double bed (140×200 cm) | $58/night ($406 total) for Economy Double | ❌ **No** (Double bed below 150 cm queen minimum) | [Toyoko Official](https://www.toyoko-inn.com/eng/search/detail/00194/) / [Booking](https://www.booking.com/hotel/kr/toyoko-inn-busan-no-1.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 18 | **Crown Harbor Hotel Busan** | Deluxe Double: 1 double bed (approx 140 cm) | $86/night ($602 total) | ❌ **No** (Double bed below 150 cm queen minimum) | [Property site](http://www.crownharborhotel.com/teaser/html/index_kor.html) / [Booking](https://www.booking.com/hotel/kr/crown-harbor.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 19 | **Fairfield by Marriott Busan Songdo Beach** | Standard King: 1 King bed (180×200 cm) | $116/night ($812 total) | ❌ **No** (No walkable metro station nearby in Songdo) | [Marriott Official](https://www.marriott.com/en-us/hotels/pusfb-fairfield-busan-songdo-beach/overview/) / [Booking](https://www.booking.com/hotel/kr/fairfield-by-marriott-busan-songdo-beach.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| 20 | **Wyndham Grand Busan Ijin** | Deluxe King: 1 King bed (180×200 cm) | $139/night ($973 total) | ❌ **No** (No walkable metro station nearby in Songdo) | [Wyndham Official](https://www.wyndhamhotels.com/wyndham-grand/busan-south-korea/wyndham-grand-busan-ijin/overview) / [Booking](https://www.booking.com/hotel/kr/wyndham-grand-busan-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |

---

## 4. Cheonan — 7 Hotels Checklist
*Sourced standard rate baseline (before taxes).*

| # | Hotel Name (ID) | Checked Bed Size & Count (Official Spec) | Refundable Pricing Snapshot (Autumn 2026) | Core Needs Match? | Manual Verification Link |
|---|---|---|---|:---:|---|
| 1 | **Shilla Stay Cheonan** (`cheonan-shilla-stay`) | Standard Double: 1 double bed (140 cm) | $70/night ($560 total) | ❌ **No** (Standard is double; not close walk to KTX station) | [Shilla Official](https://m.shillastay.com/cheonan/inquires/contactus/contactus.do) |
| 2 | **Ramada Encore by Wyndham CheonAn** (`cheonan-ramada-encore`) | Deluxe Double: **1 Queen bed** (approx 150 cm wide) | $71/night ($568 total) | ❌ **No** (Queen is verified, but not walkable to KTX) | [Wyndham Official](https://www.wyndhamhotels.com/ramada/cheonan-si-south-korea/ramada-encore-cheonan/overview) |
| 3 | **ON City Hotel** (`cheonan-on-city`) | Standard Double: 1 double bed (approx 140 cm) | $58/night ($464 total) | ❌ **No** (Double bed below 150 cm queen minimum; not walkable to KTX) | [ON City Official](http://www.oncityhotel.com/web/eng/asp/index/index.asp) |
| 4 | **Sono Belle Cheonan** (`cheonan-sono-belle`) | Family Standard: 2 double beds (Family resort) | $95/night ($760 total) | ❌ **No** (Family resort; no walkable rail station) | [SONO Official](https://www.sonohotelsresorts.com/belle_ca/roomsviewall) |
| 5 | **SureStay Plus Hotel by Best Western Asan** (`cheonan-best-western-asan`) | Standard Double: 1 double bed (approx 140 cm) | $75/night ($600 total) | ❌ **No** (Double bed below 150 cm; located 6 km from KTX) | [Booking](https://www.booking.com/hotel/kr/surestay-plus-by-best-western.html) |
| 6 | **Brown Dot Hotel Cheonan Dongnam** (`cheonan-brown-dot`) | Standard Double: 1 double bed (approx 140 cm) | $48/night ($384 total) | ❌ **No** (Double bed below 150 cm; ~900 m from Line 1 station) | [Trip.com](https://www.trip.com/hotels/cheonan-si-hotel-detail-62705121/brown-dot-hotel-cheonan-dongnam/) |
| 7 | **The Mains Hotel** (`cheonan-mains`) | Standard Double: 1 double bed (approx 140 cm) | $58/night ($464 total) | ❌ **No** (Double bed below 150 cm; not walkable to KTX) | [Booking](https://www.booking.com/hotel/kr/the-mains.html) |

---

## 5. Daejeon — 7 Hotels Checklist
*Sourced standard rate baseline (before taxes).*

| # | Hotel Name (ID) | Checked Bed Size & Count (Official Spec) | Refundable Pricing Snapshot (Autumn 2026) | Core Needs Match? | Manual Verification Link |
|---|---|---|---|:---:|---|
| 1 | **Toyoko Inn Daejeon Government Complex** (`daejeon-toyoko-inn`) | Standard Double: 1 double bed (140×200 cm) | $55/night ($440 total) with breakfast | ❌ **No** (Double bed below 150 cm queen minimum) | [Toyoko Official](https://www.toyoko-inn.com/eng/search/detail/00234/) |
| 2 | **Ramada by Wyndham Daejeon** (`daejeon-ramada`) | Standard Double: 1 double bed (approx 140 cm) | $72/night ($576 total) | ❌ **No** (Double bed below 150 cm; Yuseong Spa district) | [Wyndham Official](https://www.wyndhamhotels.com/ramada/daejeon-south-korea/ramada-daejeon/overview) |
| 3 | **LOTTE City Hotel Daejeon** (`daejeon-lotte-city`) | Deluxe Room: 1 double bed (approx 140 cm) | $85/night ($680 total) | ❌ **No** (Double bed below 150 cm; CCC/Expo district) | [Lotte Official](https://www.lottehotel.com/prerendered/daejeon-city/en/index.html) |
| 4 | **BENIKEA Hotel Daelim** (`daejeon-benikea-daelim`) | Standard Double: 1 double bed (140×200 cm) | $48/night ($384 total) | ❌ **No** (Double bed below 150 cm; ~10-15 min to KTX) | [VisitKorea Official](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=85393) |
| 5 | **Le Stendal Hotel** (`daejeon-hotel-stendhal`) | Standard Double: 1 double bed (approx 140 cm) | $75/night ($600 total) | ❌ **No** (Double bed below 150 cm; Yuseong Spa district) | [Property site](http://stendhalhotel.co.kr/) |
| 6 | **Hotel Interciti** (`daejeon-hotel-interciti`) | Standard Double: 1 double bed (140×200 cm) | $72/night ($576 total) | ❌ **No** (Double bed below 150 cm; Yuseong Spa district) | [VisitKorea Official](https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=86274) |
| 7 | **Aank Air Hotel Daejeon Station** (`daejeon-aank-air`) | Standard Double: 1 double bed (approx 140 cm) | $45/night ($360 total) | ❌ **No** (Double bed below 150 cm; ~9 min walk to KTX) | [Booking](https://www.booking.com/hotel/kr/aank-daejeon-station.html) |

---

## 6. Flagged Irregularities & Sourcing Summary

1. **Hwangnamkwan Check-in Gate Closure:** The Gyeongju Hanok hotel locks its front gates/reception at **22:00**. Unannounced late arrivals will be completely locked out.
2. **Double Bed Size Standard:** Across Korean mid-tier business hotels (ibis, Toyoko Inn, Shilla Stay, Skypark), a standard "Double Room" utilizes a **140 cm wide mattress**, which represents a full/double bed, below our required 150 cm queen size. Only Deluxe or specific room choices provide true Queen/King bedding.
3. **No Subway Access:** Both Gyeongju and the beachfront areas of Songdo (Fairfield Songdo, Wyndham Grand) have **no metro stations within walking distance**. Taxis or local buses are mandatory.
4. **Metro Station Walk Times in Cheonan/Daejeon:** The business districts of Cheonan and Yuseong in Daejeon are located several kilometers away from their high-speed KTX stations, necessitating local transfers.
