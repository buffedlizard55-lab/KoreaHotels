# Hotel Identity & Duplicate Audit

**Audit date:** August 10, 2026
**Result:** **69 records · 69 sourced hotel identities · 0 duplicates**

## What was checked

- Every record has a canonical property name and a current official, government-tourism, or major trusted exact-property source.
- Hotel IDs, canonical names within each city, official URLs, verification URLs, and exact coordinates are unique.
- A fuzzy-name check catches likely duplicate spellings. The similar **Nine Tree Myeongdong 1 / Myeongdong 2** pair is explicitly cross-referenced because the official Parnas pages confirm two different branches.
- Co-located or neighboring hotels are not treated as duplicates when their official property pages, names, and URLs differ. For example, Moxy and Le Méridien Myeongdong are two separately bookable brands in one dual-brand building.
- Four independent hotels without a stable official booking page are retained only because a major trusted listing confirms the exact canonical name and street address: SureStay Plus Asan, Brown Dot Cheonan Dongnam, The Mains Hotel, and Aank Air Daejeon Station.

## Automated safeguards

`python3 validate.py` now fails when it finds:

1. duplicate IDs or sourced canonical names;
2. a reused official or identity-source URL;
3. exact duplicate coordinates;
4. an unverified/missing identity block;
5. a highly similar same-city name without a mutual `distinctFrom` cross-check.

## Complete identity register

### Seoul

| Data ID | Canonical property | Identity source | Status |
|---|---|---|---|
| `seoul-l7-myeongdong` | L7 MYEONGDONG by LOTTE HOTELS | [Official hotel/brand](https://www.lottehotel.com/myeongdong-l7/en/main.html) | Verified operating property |
| `seoul-nine-tree` | Nine Tree by Parnas Seoul Myeongdong 1 | [Official hotel/brand](https://www.ninetreehotels.com/nth1/?lang=en) | Verified operating property |
| `seoul-ibis-styles` | Ibis Styles Ambassador Seoul Myeongdong | [Official hotel/brand](https://all.accor.com/hotel/1976/index.en.shtml) | Verified operating property |
| `seoul-ibis-insadong` | Ibis Ambassador Insadong (newly refurbished) | [Official hotel/brand](https://all.accor.com/hotel/1888/index.en.shtml) | Verified operating property |
| `seoul-four-seasons` | Four Seasons Hotel Seoul | [Official hotel/brand](https://www.fourseasons.com/seoul/) | Verified operating property |
| `seoul-fairmont` | Fairmont Ambassador Seoul | [Official hotel/brand](https://www.fairmont.com/en/hotels/seoul/fairmont-ambassador-seoul.html) | Verified operating property |
| `seoul-skypark-myeongdong3` | Hotel Skypark Myeongdong 3 | [Official hotel/brand](https://www.skyparkhotel.com/html/accommdation/accom3_tab1_01.asp) | Verified operating property |
| `seoul-lescape` | L'Escape, A Luxury Collection Hotel, Seoul Myeongdong | [Official hotel/brand](https://www.marriott.com/en-us/hotels/sellm-lescape-a-luxury-collection-hotel-seoul-myeongdong/overview/) | Verified operating property |
| `seoul-somerset-palace` | Somerset Palace Seoul | [Official hotel/brand](https://www.discoverasr.com/en/somerset-serviced-residence/korea-south/somerset-palace-seoul) | Verified operating property |
| `seoul-ibis-ambassador-myeongdong` | ibis Ambassador Seoul Myeongdong | [Official hotel + Korea Tourism Organization](https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=96506) | Verified operating property |
| `seoul-moxy-myeongdong` | Moxy Seoul, Myeongdong | [Official hotel/brand](https://www.marriott.com/en-us/hotels/selmx-moxy-seoul-myeongdong/overview/) | Verified operating property |
| `seoul-le-meridien-myeongdong` | Le Méridien Seoul, Myeongdong | [Official hotel/brand](https://www.marriott.com/en-us/hotels/selmm-le-meridien-seoul-myeongdong/overview/) | Verified operating property |
| `seoul-aloft-myeongdong` | Aloft Seoul Myeongdong | [Official hotel/brand](https://www.marriott.com/en-us/hotels/selmo-aloft-seoul-myeongdong/overview/) | Verified operating property |
| `seoul-courtyard-myeongdong` | Courtyard by Marriott Seoul Myeongdong | [Official hotel/brand](https://www.marriott.com/en-us/hotels/selsn-courtyard-seoul-myeongdong/overview/) | Verified operating property |
| `seoul-four-points-myeongdong` | Four Points by Sheraton Josun, Seoul Myeongdong | [Official hotel/brand](https://www.marriott.com/en-us/hotels/selfd-four-points-josun-seoul-myeongdong/overview/) | Verified operating property |
| `seoul-nine-tree-myeongdong2` | Nine Tree by Parnas Seoul Myeongdong 2 | [Official hotel/brand](https://www.ninetreehotels.com/nth2/?lang=en) | Verified operating property |
| `seoul-nine-tree-insadong` | Nine Tree by Parnas Seoul Insadong | [Official hotel/brand](https://www.ninetreehotels.com/nth3/) | Verified operating property |
| `seoul-shilla-stay-gwanghwamun` | Shilla Stay Gwanghwamun Myeongdong | [Official hotel/brand](https://www.shillastay.com/gwanghwamun/accommodation/viewAccmo.do?contId=ST) | Verified operating property |
| `seoul-lotte-hotel` | LOTTE HOTEL SEOUL | [Official hotel/brand](https://www.lottehotel.com/seoul-hotel/en/rooms) | Verified operating property |
| `seoul-westin-josun` | The Westin Josun Seoul | [Official hotel/brand](https://www.marriott.com/en-us/hotels/selwi-the-westin-josun-seoul/overview/) | Verified operating property |

### Gyeongju

| Data ID | Canonical property | Identity source | Status |
|---|---|---|---|
| `gyeongju-hwangnamkwan` | Hwangnamkwan Hanok Hotel (황남관 한옥호텔) | [Korea Tourism Organization + property site](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=63039) | Verified operating property |
| `gyeongju-commodore` | Commodore Hotel Gyeongju | [Official hotel + Korea Tourism Organization](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=99034) | Verified operating property |
| `gyeongju-lahan` | Lahan Select Gyeongju | [Official hotel/brand](https://www.lahan.com/gyeongju/en/main.do) | Verified operating property |
| `gyeongju-hilton` | Hilton Gyeongju | [Official hotel + Korea Tourism Organization](https://www.hilton.com/en/hotels/kyjgyhi-hilton-gyeongju/) | Verified operating property |
| `gyeongju-gg-hotel` | GG Hotel Gyeongju | [Property site + established Korea tour operator](https://www.koreaetour.com/gyeongju-gg-hotel/) | Verified operating property |
| `gyeongju-kolon` | Kolon Hotel Gyeongju | [Official hotel + Korea Tourism Organization](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=99009) | Verified operating property |
| `gyeongju-the-k` | The-K Hotel Gyeongju | [Official hotel + Korea Tourism Organization](https://english.visitkorea.or.kr/enu/ATR/SI_EN_3_1_1_1.jsp?cid=1061398) | Verified operating property |
| `gyeongju-kinock` | KINOCK Gyeongju | [Official hotel/brand](https://www.kinock.co.kr/gj/ko/Home/Main) | Verified operating property |
| `gyeongju-swiss-rosen` | Benikea Swiss Rosen Hotel Gyeongju | [Korea Tourism Organization / BENIKEA](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=85181) | Verified operating property |
| `gyeongju-rivertain` | Rivertain Hotel Gyeongju | [Korea Tourism Organization — Korea Quality certified](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=60519) | Verified operating property |
| `gyeongju-hanokinn` | HanokInn | [Korea Tourism Organization + property site](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=45559) | Verified operating property |
| `gyeongju-wiyeonjae` | Wiyeonjae Hanok Stay | [Korea Tourism Organization + property site](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=45556) | Verified operating property |
| `gyeongju-nadul-hanok` | Nadul Hanok | [Korea Tourism Organization + property site](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=63076) | Verified operating property |
| `gyeongju-sono-calm` | SONO Calm Gyeongju | [Official hotel/brand](https://www.sonohotelsresorts.com/calm_gju/resort) | Verified operating property |
| `gyeongju-kensington` | Kensington Resort Gyeongju | [Official hotel/brand](https://www.kensington.co.kr/rgj) | Verified operating property |

### Busan

| Data ID | Canonical property | Identity source | Status |
|---|---|---|---|
| `busan-shilla-stay` | Shilla Stay Busan Haeundae | [Official hotel/brand](https://www.shillastay.com/haeundae/main.do?lang=en) | Verified operating property |
| `busan-l7-haeundae` | L7 HAEUNDAE by LOTTE HOTELS | [Official hotel/brand](https://www.lottehotel.com/haeundae-l7/en/main.html) | Verified operating property |
| `busan-asti` | ASTI Hotel Busan Station | [Official property site](https://www.astihotel.com) | Verified operating property |
| `busan-grand-josun` | Grand Josun Busan | [Official hotel/brand](https://gjb.josunhotel.com/main.do?locale=en) | Verified operating property |
| `busan-park-hyatt` | Park Hyatt Busan | [Official hotel/brand](https://www.hyatt.com/park-hyatt/en-US/busph-park-hyatt-busan) | Verified operating property |
| `busan-toyoko-haeundae2` | Toyoko Inn Busan Haeundae No.2 | [Official hotel/brand](https://www.toyoko-inn.com/eng/search/detail/00256/) | Verified operating property |
| `busan-ramada-encore-haeundae` | Ramada Encore by Wyndham Busan Haeundae | [Official hotel/brand](https://www.wyndhamhotels.com/ramada/busan-south-korea/ramada-encore-haeundae/overview) | Verified operating property |
| `busan-signiel` | SIGNIEL BUSAN | [Official hotel/brand](https://www.lottehotel.com/busan-signiel/en/rooms/signiel-premier-familytwin-ocean-view.html) | Verified operating property |
| `busan-paradise` | Paradise Hotel Busan | [Official hotel + Korea Tourism Organization](https://www.busanparadisehotel.co.kr/front/hotel/room/view?RR_ROOM_CATEGORY=PREMIUM_DELUXE&RR_ROOM_TYPE=PREMIUM_DELUXE_OCEAN_DOUBLE) | Verified operating property |
| `busan-westin-josun` | The Westin Josun Busan | [Official hotel/brand](https://www.marriott.com/en-us/hotels/puswi-the-westin-josun-busan/overview/) | Verified operating property |
| `busan-fairfield-haeundae` | Fairfield by Marriott Busan | [Official hotel/brand](https://www.marriott.com/en-us/hotels/pusfi-fairfield-busan/overview/) | Verified operating property |
| `busan-ibis-budget-haeundae` | ibis budget Ambassador Busan Haeundae | [Official hotel/brand](https://all.accor.com/hotel/9106/index.en.shtml) | Verified operating property |
| `busan-ibis-haeundae` | ibis Ambassador Busan Haeundae | [Official hotel/brand](https://all.accor.com/hotel/9643/index.en.shtml) | Verified operating property |
| `busan-lotte-hotel` | LOTTE HOTEL BUSAN | [Official hotel/brand](https://www.lottehotel.com/busan-hotel/en/rooms/premier-room.html) | Verified operating property |
| `busan-avani-central` | Avani Central Busan | [Official hotel/brand](https://www.avanihotels.com/en/central-busan) | Verified operating property |
| `busan-ramada-station` | Ramada Encore by Wyndham Busan Station | [Official hotel/brand](https://www.wyndhamhotels.com/ramada/busan-south-korea/ramada-encore-busan-station/overview) | Verified operating property |
| `busan-toyoko-station1` | Toyoko Inn Busan Station No.1 | [Official hotel/brand](https://www.toyoko-inn.com/eng/search/detail/00194/) | Verified operating property |
| `busan-crown-harbor` | Crown Harbor Hotel Busan | [Property site + established Korea tour operator](https://www.koreaetour.com/busan-crown-harbor-hotel/) | Verified operating property |
| `busan-fairfield-songdo` | Fairfield by Marriott Busan Songdo Beach | [Official hotel/brand](https://www.marriott.com/en-us/hotels/pusfb-fairfield-busan-songdo-beach/overview/) | Verified operating property |
| `busan-wyndham-grand` | Wyndham Grand Busan Ijin | [Official hotel/brand](https://www.wyndhamhotels.com/wyndham-grand/busan-south-korea/wyndham-grand-busan-ijin/overview) | Verified operating property |

### Cheonan

| Data ID | Canonical property | Identity source | Status |
|---|---|---|---|
| `cheonan-shilla-stay` | Shilla Stay Cheonan | [Official hotel/brand](https://m.shillastay.com/cheonan/inquires/contactus/contactus.do) | Verified operating property |
| `cheonan-ramada-encore` | Ramada Encore by Wyndham CheonAn | [Official hotel/brand](https://www.wyndhamhotels.com/ramada/cheonan-si-south-korea/ramada-encore-cheonan/overview) | Verified operating property |
| `cheonan-on-city` | ON City Hotel | [Official property site](http://www.oncityhotel.com/web/eng/asp/index/index.asp) | Verified operating property |
| `cheonan-sono-belle` | SONO Belle Cheonan | [Official hotel/brand](https://www.sonohotelsresorts.com/belle_ca/roomsviewall) | Verified operating property |
| `cheonan-best-western-asan` | SureStay Plus Hotel by Best Western Asan | [Major trusted booking platform](https://www.booking.com/hotel/kr/surestay-plus-by-best-western.html) | Verified operating property |
| `cheonan-brown-dot` | Brown Dot Hotel Cheonan Dongnam | [Major trusted booking platform](https://www.trip.com/hotels/cheonan-si-hotel-detail-62705121/brown-dot-hotel-cheonan-dongnam/) | Verified operating property |
| `cheonan-mains` | The Mains Hotel | [Major trusted booking platform](https://www.booking.com/hotel/kr/the-mains.html) | Verified operating property |

### Daejeon

| Data ID | Canonical property | Identity source | Status |
|---|---|---|---|
| `daejeon-toyoko-inn` | Toyoko Inn Daejeon Government Complex | [Official hotel/brand](https://www.toyoko-inn.com/eng/search/detail/00234/) | Verified operating property |
| `daejeon-ramada` | Ramada by Wyndham Daejeon | [Official hotel/brand](https://www.wyndhamhotels.com/ramada/daejeon-south-korea/ramada-daejeon/overview) | Verified operating property |
| `daejeon-lotte-city` | LOTTE City Hotel Daejeon | [Official hotel/brand](https://www.lottehotel.com/prerendered/daejeon-city/en/index.html) | Verified operating property |
| `daejeon-benikea-daelim` | BENIKEA Hotel Daelim | [Government tourism authority](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=85393) | Verified operating property |
| `daejeon-hotel-stendhal` | Le Stendal Hotel | [Official property site](http://stendhalhotel.co.kr/) | Verified operating property |
| `daejeon-hotel-interciti` | Hotel Interciti | [Official hotel + Korea Tourism Organization](https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=86274) | Verified operating property |
| `daejeon-aank-air` | Aank Air Hotel Daejeon Station | [Major trusted booking platform](https://www.booking.com/hotel/kr/aank-daejeon-station.html) | Verified operating property |

## Important scope note

This audit verifies that each entry is a real, distinct hotel property and that the source link belongs to that identity. It does **not** turn planning price estimates into live quotes or prove that every room category is available for the trip dates. Bed size, final price, cancellation terms, and late-arrival retention must still be confirmed before payment.

Only the five entries in the separate arrival-night block have been screened for the first-night 24-hour reception requirement.
