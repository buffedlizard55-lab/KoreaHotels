# Hotel Identity & Duplicate Audit

**Audit date:** August 19, 2026
**Result:** **144 records · 144 sourced hotel identities · 0 duplicates**

## What was checked

- Every record has a canonical property name and a current official, government-tourism, or major trusted exact-property source.
- Hotel IDs, canonical names within each city, official URLs, verification URLs, and exact coordinates are unique.
- A fuzzy-name check catches likely duplicate spellings. Similar branch names (e.g. L7 Myeongdong / L7 Gangnam / L7 Hongdae, Sotetsu Splaisir Myeongdong / Dongdaemun, Novotel Gangnam / Dongdaemun / Yongsan, Shilla Stay Gwanghwamun / Seocho / Samsung / Yeoksam, Nine Tree branches, etc.) are explicitly cross-referenced via `distinctFrom`.
- Co-located or neighboring hotels are not treated as duplicates when their official property pages, names, and URLs differ.
- Independent hotels without a stable official booking page are retained only when a government-tourism authority or major trusted listing confirms the exact canonical name and street address.

## Automated safeguards

`python3 validate.py` enforces:

1. unique IDs and unique canonical names within each city;
2. unique official and verification source URLs;
3. unique coordinates;
4. complete, verified identity blocks (`existenceStatus: Verified operating property`);
5. mutual `distinctFrom` cross-checks for any same-city names exceeding 92% similarity.

## Complete identity register

### Seoul (90 hotels)

| Data ID | Canonical property | Identity source | Status |
|---|---|---|---|
| `seoul-l7-myeongdong` | L7 MYEONGDONG by LOTTE HOTELS | [Official hotel/brand](https://www.lottehotel.com/myeongdong-l7/en/main.html) | Verified operating property |
| `seoul-nine-tree` | Nine Tree by Parnas Seoul Myeongdong 1 | [Official hotel/brand](https://www.ninetreehotels.com/nth1/?lang=en) | Verified operating property |
| `seoul-ibis-styles` | Ibis Styles Ambassador Seoul Myeongdong | [Official hotel/brand](https://all.accor.com/hotel/9771/index.en.shtml) | Verified operating property |
| `seoul-ibis-insadong` | Ibis Ambassador Insadong (newly refurbished) | [Official hotel/brand](https://all.accor.com/hotel/8002/index.en.shtml) | Verified operating property |
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
| `seoul-four-points-seoul-station` | Four Points by Sheraton Josun, Seoul Station | [Official hotel/brand](https://www.marriott.com/en-us/hotels/selfp-four-points-josun-seoul-station/overview/) | Verified operating property |
| `seoul-the-plaza-autograph-collection` | THE PLAZA Seoul, Autograph Collection | [Official hotel/brand](https://www.marriott.com/en-us/hotels/selak-the-plaza-seoul-autograph-collection/overview/) | Verified operating property |
| `seoul-travelodge-myeongdong-euljiro` | Travelodge Myeongdong Euljiro | [Official hotel/brand](https://travelodgehotels.asia/travelodge-myeongdong-euljiro/) | Verified operating property |
| `seoul-sotetsu-fresa-inn-myeongdong` | Sotetsu Fresa Inn Seoul Myeong-dong | [Official hotel/brand](https://sotetsu-hotels.com/en/fresa-inn/myeong-dong/) | Verified operating property |
| `seoul-stanford-hotel-myeongdong` | Stanford Hotel Myeongdong | [Official hotel/brand](https://www.stanford-hotel.com/myeongdong/en/) | Verified operating property |
| `seoul-sotetsu-splaisir-myeongdong` | Sotetsu Hotels The Splaisir Seoul Myeongdong | [Official hotel/brand](https://sotetsu-hotels.com/en/splaisir/myeong-dong/) | Verified operating property |
| `seoul-hotel-vert` | Hotel Vert | [Major trusted booking platform](https://www.booking.com/hotel/kr/vert.html) | Verified operating property |
| `seoul-royal-hotel` | Royal Hotel Seoul | [Official hotel/brand](https://www.royal.co.kr/en/index.php) | Verified operating property |
| `seoul-sejong-hotel-myeongdong` | Sejong Hotel Seoul Myeongdong | [Official hotel/brand](http://www.sejong.co.kr/eng/) | Verified operating property |
| `seoul-orakai-insadong-suites` | Orakai Insadong Suites | [Official hotel/brand](https://orakai-insadong-suites.business.site/) | Verified operating property |
| `seoul-novotel-ambassador-gangnam` | Novotel Ambassador Seoul Gangnam | [Major trusted platform (Booking.com dated page) + brand site](https://www.booking.com/hotel/kr/ambassador-gangnam-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) | Verified operating property |
| `seoul-glad-gangnam-coex` | GLAD Gangnam COEX Center | [Major trusted platform (Booking.com dated page) + brand site](https://www.booking.com/hotel/kr/glad-gangnam-coex-center.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) | Verified operating property |
| `seoul-jw-marriott-seoul` | JW Marriott Hotel Seoul | [Major trusted platform (Booking.com dated page) + brand site](https://www.booking.com/hotel/kr/jw-marriott-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) | Verified operating property |
| `seoul-park-hyatt-seoul` | Park Hyatt Seoul | [Major trusted platform (Booking.com dated page) + brand site](https://www.booking.com/hotel/kr/park-hyatt-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) | Verified operating property |
| `seoul-josun-palace-gangnam` | Josun Palace, a Luxury Collection Hotel, Seoul Gangnam | [Major trusted platform (Booking.com dated page) + brand site](https://www.booking.com/hotel/kr/josun-palace-a-luxury-collection-seoul-gangnam.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) | Verified operating property |
| `seoul-grand-intercontinental-parnas` | Grand InterContinental Seoul Parnas by IHG | [Major trusted platform (Booking.com dated page) + brand site](https://www.booking.com/hotel/kr/grand-intercontinental-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) | Verified operating property |
| `seoul-oakwood-coex` | Oakwood Premier COEX Center Seoul | [Major trusted platform (Booking.com dated page) + brand site](https://www.booking.com/hotel/kr/oakwood-premier-coex-center-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) | Verified operating property |
| `seoul-ac-hotel-gangnam` | AC Hotel by Marriott Seoul Gangnam | [Major trusted platform (Booking.com dated page) + brand site](https://www.booking.com/hotel/kr/ac-hotel-by-marriott-seoul-gangnam.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) | Verified operating property |
| `seoul-dormy-inn-gangnam` | Dormy Inn SEOUL Gangnam | [Major trusted platform (Booking.com dated page) + brand site](https://www.booking.com/hotel/kr/dormyinn-seoul-gangnam.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) | Verified operating property |
| `seoul-shilla-stay-seocho` | Shilla Stay Seocho Gangnam Station | [Major trusted platform (Booking.com dated page) + brand site](https://www.booking.com/hotel/kr/shilla-stay-seocho.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) | Verified operating property |
| `seoul-novotel-dongdaemun` | Novotel Ambassador Seoul Dongdaemun Hotels & Residences | [Major trusted platform (Booking.com dated page) + brand site](https://www.booking.com/hotel/kr/novotel-ambassador-seoul-dongdaemun.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) | Verified operating property |
| `seoul-jw-marriott-dongdaemun` | JW Marriott Dongdaemun Square Seoul | [Major trusted platform (Booking.com dated page) + brand site](https://www.booking.com/hotel/kr/jw-marriott-dongdaemun-square-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) | Verified operating property |
| `seoul-nine-tree-dongdaemun` | Nine Tree by Parnas Seoul Dongdaemun | [Major trusted platform (Booking.com dated page) + brand site](https://www.booking.com/hotel/kr/nine-tree-dongdaemun.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) | Verified operating property |
| `seoul-sofitel-ambassador-seoul` | Sofitel Ambassador Seoul Hotel & Serviced Residences | [Major trusted platform (Booking.com dated page) + brand site](https://www.booking.com/hotel/kr/sofitel-ambassador-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) | Verified operating property |
| `seoul-hotel28-myeongdong` | Hotel28 Myeongdong (Small Luxury Hotels) | [Major trusted platform (Booking.com dated page) + brand site](https://www.booking.com/hotel/kr/hotel28-myeongdong.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) | Verified operating property |
| `seoul-hotel-gracery` | Hotel Gracery Seoul | [Major trusted platform (Booking.com dated page) + brand site](https://www.booking.com/hotel/kr/gracery-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) | Verified operating property |
| `seoul-ena-suite-namdaemun` | ENA Suite Hotel Namdaemun | [Major trusted platform (Booking.com dated page) + brand site](https://www.booking.com/hotel/kr/ena-suite-namdaemun.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) | Verified operating property |
| `seoul-l7-gangnam` | L7 GANGNAM by LOTTE HOTELS | [Official hotel/brand + Booking.com dated page](https://www.lottehotel.com/gangnam-l7/en.html) | Verified operating property |
| `seoul-fraser-place-namdaemun` | Fraser Place Namdaemun Seoul | [Official hotel/brand + Booking.com dated page](https://www.frasershospitality.com/en/south-korea/seoul/fraser-place-namdaemun-seoul/) | Verified operating property |
| `seoul-westin-parnas` | The Westin Seoul Parnas | [Official hotel/brand + Booking.com dated page](https://www.marriott.com/en-us/hotels/selwg-the-westin-seoul-parnas/overview/) | Verified operating property |
| `seoul-l7-hongdae` | L7 HONGDAE by LOTTE HOTELS | [Official hotel/brand](https://www.lottehotel.com/hongdae-l7/en.html) | Verified operating property |
| `seoul-ryse-autograph-collection` | RYSE, Autograph Collection, Seoul | [Official hotel/brand](https://www.marriott.com/en-us/hotels/seoak-ryse-autograph-collection/overview/) | Verified operating property |
| `seoul-mercure-hongdae` | Mercure Ambassador Seoul Hongdae | [Official hotel/brand](https://all.accor.com/hotel/B659/index.en.shtml) | Verified operating property |
| `seoul-holiday-inn-express-hongdae` | Holiday Inn Express Seoul Hongdae by IHG | [Official hotel/brand](https://www.ihg.com/holidayinnexpress/hotels/us/en/seoul/seohd/hoteldetail) | Verified operating property |
| `seoul-glad-mapo` | GLAD Mapo | [Official hotel/brand](https://www.glad-hotels.com/mapo/index.do) | Verified operating property |
| `seoul-grand-hyatt` | Grand Hyatt Seoul | [Official hotel/brand](https://www.hyatt.com/grand-hyatt/en-US/selrs-grand-hyatt-seoul) | Verified operating property |
| `seoul-mondrian-itaewon` | Mondrian Seoul Itaewon | [Official hotel/brand](https://all.accor.com/hotel/B2Y4/index.en.shtml) | Verified operating property |
| `seoul-hamilton` | Hamilton Hotel Seoul | [Official hotel/brand](https://www.hamilton.co.kr/) | Verified operating property |
| `seoul-novotel-yongsan` | Novotel Ambassador Seoul Yongsan | [Official hotel/brand](https://all.accor.com/hotel/9651/index.en.shtml) | Verified operating property |
| `seoul-sotetsu-splaisir-dongdaemun` | Sotetsu Hotels The Splaisir Seoul Dongdaemun | [Official hotel/brand](https://sotetsu-hotels.com/en/splaisir/dongdaemun/) | Verified operating property |
| `seoul-ramada-dongdaemun` | Ramada by Wyndham Seoul Dongdaemun | [Official hotel/brand](https://www.wyndhamhotels.com/ramada/seoul-south-korea/ramada-seoul-dongdaemun/overview) | Verified operating property |
| `seoul-toyoko-inn-dongdaemun2` | Toyoko Inn Seoul Dongdaemun II | [Official hotel/brand](https://www.toyoko-inn.com/eng/search/detail/00291/) | Verified operating property |
| `seoul-sunbee-insadong` | Hotel Sunbee Insadong | [Official hotel/brand](http://www.sunbeehotel.com/) | Verified operating property |
| `seoul-orakai-daehakro` | Orakai Daehakro Hotel, BW Signature Collection | [Official hotel/brand](http://dh.orakaihotels.com/en/default.asp) | Verified operating property |
| `seoul-amid-hotel` | Amid Hotel Seoul | [Official hotel/brand](https://www.amidhotel.co.kr/) | Verified operating property |
| `seoul-dormy-inn-insadong` | Dormy Inn EXPRESS SEOUL Insadong | [Official hotel/brand](https://www.hotespa.net/hotels/express_insadong/) | Verified operating property |
| `seoul-hotel-pj` | Hotel PJ Myeongdong | [Official hotel/brand](http://www.hotelpj.co.kr/) | Verified operating property |
| `seoul-klaven-city-hall` | Klaven Hotel Myeongdong City Hall | [Official hotel/brand](https://www.travelodgehotels.asia/travelodge-myeongdong-city-hall/) | Verified operating property |
| `seoul-voco-gangnam` | voco Seoul Gangnam by IHG | [Official hotel/brand](https://www.ihg.com/voco/hotels/us/en/seoul/seovc/hoteldetail) | Verified operating property |
| `seoul-hilton-garden-inn-gangnam` | Hilton Garden Inn Seoul Gangnam | [Official hotel/brand](https://www.hilton.com/en/hotels/seogagi-hilton-garden-inn-seoul-gangnam/) | Verified operating property |
| `seoul-amanti-hongdae` | Amanti Hotel Seoul Hongdae | [Official hotel/brand](http://www.amantihotel.com/) | Verified operating property |
| `seoul-the-designer-hongdae` | Hotel The Designers Hongdae | [Official hotel/brand](https://www.hotelthedesigners.com/hongdae/) | Verified operating property |
| `seoul-best-western-premier-garden` | Seoul Garden Hotel | [Official hotel/brand](http://www.seoulgarden.co.kr/en/) | Verified operating property |
| `seoul-imperial-palace-boutique` | Imperial Palace Boutique Hotel Itaewon | [Official hotel/brand](http://www.imperialpalaceboutique.co.kr/) | Verified operating property |
| `seoul-grand-mercure-yongsan` | Grand Mercure Ambassador Hotel and Residences Seoul Yongsan | [Official hotel/brand](https://all.accor.com/hotel/9652/index.en.shtml) | Verified operating property |
| `seoul-nine-tree-rokaus-yongsan` | Nine Tree Premier ROKAUS Hotel Seoul Yongsan | [Official hotel/brand](https://www.rokaushotel.com/) | Verified operating property |
| `seoul-skypark-dongdaemun1` | Hotel Skypark Dongdaemun I | [Official hotel/brand](https://www.skyparkhotel.com/html/accommdation/accom4_tab1_01.asp) | Verified operating property |
| `seoul-the-designers-dongdaemun` | Hotel The Designers Dongdaemun | [Official hotel/brand](https://www.hotelthedesigners.com/dongdaemun/) | Verified operating property |
| `seoul-mangrove-dongdaemun` | Mangrove Dongdaemun | [Official hotel/brand](https://mangrove.city/dongdaemun/) | Verified operating property |
| `seoul-moxy-insadong` | Moxy Seoul Insadong by Marriott | [Official hotel/brand](https://www.marriott.com/en-us/hotels/selon-moxy-seoul-insadong/overview/) | Verified operating property |
| `seoul-grid-inn` | Grid Inn Hotel Jongno | [Official hotel/brand](http://www.gridinn.com/) | Verified operating property |
| `seoul-lotte-city-myeongdong` | LOTTE City Hotel Myeongdong | [Official hotel/brand](https://www.lottehotel.com/myeongdong-city/en.html) | Verified operating property |
| `seoul-henn-na-myeongdong` | Henn na Hotel Seoul Myeongdong | [Official hotel/brand](https://www.hennnahotel.com/myeongdong/) | Verified operating property |
| `seoul-skypark-myeongdong2` | Hotel Skypark Myeongdong 2 | [Official hotel/brand](https://www.skyparkhotel.com/html/accommdation/accom2_tab1_01.asp) | Verified operating property |
| `seoul-hotel-entra` | Hotel Entra Gangnam | [Official hotel/brand](http://www.hotelentra.com/) | Verified operating property |
| `seoul-hotel-cappuccino` | Hotel Cappuccino | [Official hotel/brand](https://hotelcappuccino.co.kr/) | Verified operating property |
| `seoul-shilla-stay-samsung` | Shilla Stay Samsung COEX Center | [Official hotel/brand](https://www.shillastay.com/samsung/index.do) | Verified operating property |
| `seoul-shilla-stay-yeoksam` | Shilla Stay Gangnam Yeoksam | [Official hotel/brand](https://www.shillastay.com/yeoksam/index.do) | Verified operating property |
| `seoul-hotel-in-9` | HOTEL in 9 Gangnam | [Official hotel/brand](http://www.hotelin9.com/) | Verified operating property |
| `seoul-peyto-samseong` | Hotel Peyto Samseong | [Official hotel/brand](http://www.peytohotel.com/samseong/en/) | Verified operating property |

### Gyeongju (15 hotels)

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

### Busan (20 hotels)

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

### Cheonan (7 hotels)

| Data ID | Canonical property | Identity source | Status |
|---|---|---|---|
| `cheonan-shilla-stay` | Shilla Stay Cheonan | [Official hotel/brand](https://m.shillastay.com/cheonan/inquires/contactus/contactus.do) | Verified operating property |
| `cheonan-ramada-encore` | Ramada Encore by Wyndham CheonAn | [Official hotel/brand](https://www.wyndhamhotels.com/ramada/cheonan-si-south-korea/ramada-encore-cheonan/overview) | Verified operating property |
| `cheonan-on-city` | ON City Hotel | [Official property site](http://www.oncityhotel.com/web/eng/asp/index/index.asp) | Verified operating property |
| `cheonan-sono-belle` | SONO Belle Cheonan | [Official hotel/brand](https://www.sonohotelsresorts.com/belle_ca/roomsviewall) | Verified operating property |
| `cheonan-best-western-asan` | Best Western Asan Hotel | [Major trusted booking platform](https://www.booking.com/hotel/kr/surestay-plus-by-best-western.html) | Verified operating property |
| `cheonan-brown-dot` | Brown Dot Hotel Cheonan Dongnam | [Major trusted booking platform](https://www.trip.com/hotels/cheonan-si-hotel-detail-62705121/brown-dot-hotel-cheonan-dongnam/) | Verified operating property |
| `cheonan-mains` | The Mains Hotel | [Major trusted booking platform](https://www.booking.com/hotel/kr/the-mains.html) | Verified operating property |

### Daejeon (7 hotels)

| Data ID | Canonical property | Identity source | Status |
|---|---|---|---|
| `daejeon-toyoko-inn` | Toyoko Inn Daejeon Government Complex | [Official hotel/brand](https://www.toyoko-inn.com/eng/search/detail/00234/) | Verified operating property |
| `daejeon-ramada` | Ramada by Wyndham Daejeon | [Official hotel/brand](https://www.wyndhamhotels.com/ramada/daejeon-south-korea/ramada-daejeon/overview) | Verified operating property |
| `daejeon-lotte-city` | LOTTE City Hotel Daejeon | [Official hotel/brand](https://www.lottehotel.com/prerendered/daejeon-city/en/index.html) | Verified operating property |
| `daejeon-benikea-daelim` | BENIKEA Hotel Daelim | [Government tourism authority](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=85393) | Verified operating property |
| `daejeon-hotel-stendhal` | Le Stendal Hotel | [Official property site](http://stendhalhotel.co.kr/) | Verified operating property |
| `daejeon-hotel-interciti` | Hotel Interciti | [Official hotel + Korea Tourism Organization](https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=86274) | Verified operating property |
| `daejeon-aank-air` | Aank Air Hotel Daejeon Station | [Major trusted booking platform](https://www.booking.com/hotel/kr/aank-daejeon-station.html) | Verified operating property |

### Suwon (5 hotels)

| Data ID | Canonical property | Identity source | Status |
|---|---|---|---|
| `suwon-novotel-ambassador` | Novotel Ambassador Suwon | [Official hotel/brand](https://all.accor.com/hotel/8748/index.en.shtml) | Verified operating property |
| `suwon-four-points` | Four Points by Sheraton Suwon | [Official hotel/brand](https://www.marriott.com/en-us/hotels/selfo-four-points-suwon/overview/) | Verified operating property |
| `suwon-ramada-plaza` | Ramada Plaza by Wyndham Suwon | [Major trusted booking platform](https://www.booking.com/hotel/kr/ramada-plaza-suwon.html) | Verified operating property |
| `suwon-courtyard` | Courtyard by Marriott Suwon | [Official hotel/brand](https://www.marriott.com/en-us/hotels/selcw-courtyard-suwon/overview/) | Verified operating property |
| `suwon-ibis` | ibis Ambassador Suwon | [Official hotel/brand](https://all.accor.com/hotel/6528/index.en.shtml) | Verified operating property |

