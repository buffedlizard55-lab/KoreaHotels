# Agoda as a main verified source — 185/185 hotels

**Agoda.com is a main official verified source** for property identity. **Booking.com remains the only dated USD rate capture.** No Agoda prices were stored. No slugs were guessed in this pass.

- Hotels: **185**
- Unique Agoda URLs: **185**
- Page types: **150** `/hotel/` property pages, **35** `/reviews/` pages
- GitHub README tables label every link **Agoda** vs **Booking.com**.

## Line-by-line FLAG list (from stored notes, not new claims)

| City | Hotel | Agoda | Flag (as recorded) |
|---|---|---|---|
| Seoul | L7 MYEONGDONG by LOTTE HOTELS | [Agoda property-page](https://www.agoda.com/l7-myeongdong-by-lotte/hotel/seoul-kr.html) | FLAG: KAYAK-era Agoda quote 9. |
| Seoul | Ibis Styles Ambassador Seoul Myeongdong | [Agoda property-page](https://www.agoda.com/ibis-styles-ambassador-seoul-myeongdong/hotel/seoul-kr.html) | FLAG: Agoda's 'About' copy (marked Generative-AI-assisted) mentions hot-spring bath/outdoor pool — not promoted to amenities; Expedia copy mentions free basement laundry — neither is Agoda-confirmed facility line. |
| Seoul | Four Seasons Hotel Seoul | [Agoda property-page](https://www.agoda.com/four-seasons-hotel-seoul/hotel/seoul-kr.html) | FLAG: KAYAK-era Agoda line 9. |
| Seoul | Fairmont Ambassador Seoul | [Agoda property-page](https://www.agoda.com/fairmont-ambassador/hotel/seoul-kr.html) | FLAG: KAYAK-era Agoda 9. |
| Busan | Grand Josun Busan | [Agoda property-page](https://www.agoda.com/novotel-ambassador-busan_8/hotel/busan-kr.html) | FLAG: Agoda's URL slug is a stale legacy string ('novotel-ambassador-busan_8') whose text does NOT name Grand Josun; the live page content is unambiguously Grand Josun Busan. |
| Cheonan | Shilla Stay Cheonan | [Agoda property-page](https://www.agoda.com/shilla-stay-cheonan/hotel/cheonan-si-kr.html) | FLAG: Agoda's display name includes 'Asan - Samsung Display City'. |
| Cheonan | ON City Hotel | [Agoda property-page](https://www.agoda.com/on-city-hotel/hotel/cheonan-si-kr.html) | FLAG: canonical slug is 'on-city-hotel' (not 'on-city-hotel-cheonan'). |
| Cheonan | SureStay Plus Hotel by Best Western Asan | [Agoda property-page](https://www.agoda.com/best-western-asan-hotel/hotel/asan-si-kr.html) | FLAG: property has been rebranded/upgraded from 'SureStay Plus Hotel by Best Western Asan' to 'Best Western Asan Hotel' (older Agoda listing slug 'surestay-plus-hotel-by-best-western-asan' id 35318569 redirects here); city file is asan-si-kr. |
| Daejeon | Ramada by Wyndham Daejeon | [Agoda property-page](https://www.agoda.com/ramada-daejeon-hotel/hotel/daejeon-kr.html) | FLAG: canonical slug is 'ramada-daejeon-hotel'. |
| Daejeon | Le Stendal Hotel | [Agoda property-page](https://www.agoda.com/hotel-stendhal-h10573875/hotel/daejeon-kr.html) | FLAG: canonical slug is the hybrid 'hotel-stendhal-h10573875' form because the natural slug 'le-stendal-hotel' 404s; the reviews route slug is 'stendhal-hotel'. |
| Daejeon | Aank Air Hotel Daejeon Station | [Agoda property-page](https://www.agoda.com/aank-hotel-daejeon-station/hotel/daejeon-kr.html) | FLAG: Agoda romanizes the Korean brand '아늑에어(Aank Air)' as 'Anook Air'; canonical slug is 'aank-hotel-daejeon-station' (loses the 'Air'); a second duplicate Hangul-named listing id 64267301 (8. |
| Seoul | Hotel Skypark Myeongdong 3 | [Agoda reviews-page](https://www.agoda.com/hotel-skypark-myeongdong-iii/reviews/seoul-kr.html) | FLAG: at least four Myeongdong-adjacent Skyparks exist (MD I at 15 Myeongdong 8na-gil verified separately, MD II 'Central', MD III, Dongdaemun I) — this block cites only the -iii page. |
| Gyeongju | KINOCK Gyeongju | [Agoda property-page](https://www.agoda.com/the-suite-hotel-gyeongju/hotel/gyeongju-si-kr.html) | FLAG: Agoda's property name is The Suite Hotel Gyeongju [KINOCK] - same property as repo KINOCK Gyeongju; legacy Agoda slug 'the-suite-hotel-gyeongju'. |
| Gyeongju | Nadul Hanok | [Agoda property-page](https://www.agoda.com/nadul-hanok_2/hotel/gyeongju-si-kr.html) | FLAG: canonical slug is collision-disambiguated as 'nadul-hanok_2' (the '_2' suffix is part of the real Agoda URL). |
| Busan | ibis budget Ambassador Busan Haeundae | [Agoda property-page](https://www.agoda.com/ibis-budget-ambassador-busan-haeundae/hotel/busan-kr.html) | FLAG: property has been de-flagged/rebranded on Agoda - formerly 'ibis budget Ambassador Busan Haeundae', now marketed as 'Ambassador Busan Haeundae'; the URL slug still carries the old ibis-budget name. |
| Busan | ibis Ambassador Busan Haeundae | [Agoda property-page](https://www.agoda.com/ibis-ambassador-busan-haeundae-h15814986/hotel/busan-kr.html) | FLAG: canonical URL uses Agoda's hybrid mobile form 'ibis-ambassador-busan-haeundae-h15814986' because the plain slug 'ibis-ambassador-busan-haeundae' is owned by a DIFFERENT property (id 1254424, 'Busan Haeundae'); the h-id hybrid resolves to the correct ibis listing. |
| Suwon | Novotel Ambassador Suwon | [Agoda property-page](https://www.agoda.com/novotel-ambassador-suwon-hotel/hotel/suwon-si-kr.html) | FLAG: suggest API returns a second duplicate listing id 68658955 with no image - ignore, 745644 is the canonical page. |
| Seoul | Travelodge Myeongdong Euljiro | [Agoda property-page](https://www.agoda.com/holiday-inn-express-seoul-euljiro_2/hotel/seoul-kr.html) | FLAG: legacy Agoda slug 'holiday-inn-express-seoul-euljiro_2' (rebranded to Travelodge); URL verified by page title/address, not slug text. |
| Seoul | Sotetsu Hotels The Splaisir Seoul Myeongdong | [Agoda property-page](https://www.agoda.com/sotetsu-hotels-the-splaisir-seoul-myeong-dong/hotel/seoul-kr.html) | FLAG: canonical slug uses '. |
| Seoul | GLAD Gangnam COEX Center | [Agoda property-page](https://www.agoda.com/glad-gangnam-coex-center_2/hotel/seoul-kr.html) | FLAG: canonical slug disambiguated '_2'. |
| Seoul | Park Hyatt Seoul | [Agoda property-page](https://www.agoda.com/park-hyatt-seoul-hotel/hotel/seoul-kr.html) | FLAG: canonical slug is 'park-hyatt-seoul-hotel'; the reviews-route slug is 'park-hyatt-seoul'. |
| Seoul | AC Hotel by Marriott Seoul Gangnam | [Agoda property-page](https://www.agoda.com/mercure-ambassador-seoul-gangnam-sodowe_6/hotel/seoul-kr.html) | FLAG: legacy Agoda slug 'mercure-ambassador-seoul-gangnam-sodowe_6' (property rebranded Mercure Sodowe -> AC Hotel by Marriott; verified by page title; do NOT confuse with AC PALACE HOTEL & RESIDENCE id 75959291 which is a different hotel). |
| Seoul | Ramada by Wyndham Seoul Dongdaemun | [Agoda reviews-page](https://www.agoda.com/ramada-by-wyndham-seoul-dongdaemun/reviews/seoul-kr.html) | FLAG: 'Ramada Hotel & Suites Seoul Namdaemun' is a different property; do not conflate. |
| Seoul | Dormy Inn EXPRESS SEOUL Insadong | [Agoda property-page](https://www.agoda.com/hotel-kuretakeso-insadong_3/hotel/seoul-kr.html) | FLAG: legacy Agoda slug 'hotel-kuretakeso-insadong_3' (Kuretakeso = pre-Dormy branding); verified by title/address. |
| Seoul | Klaven Hotel Myeongdong City Hall | [Agoda property-page](https://www.agoda.com/hotel-aropa_3/hotel/seoul-kr.html) | FLAG: legacy slug 'hotel-aropa_3'; rebrand already captured in repo note. |
| Seoul | The Ambassador Seoul - A Pullman Hotel | [Agoda property-page](https://www.agoda.com/grand-ambassador-seoul/hotel/seoul-kr.html) | FLAG: Agoda slug retains legacy 'grand-ambassador-seoul' (Grand Ambassador → The Ambassador/Pullman renaming) — same pattern as sono-belle-gyeongju. |
| Seoul | Hotel Migliore Seoul | [Agoda reviews-page](https://www.agoda.com/hotel-migliore-seoul/reviews/seoul-kr.html) | FLAG: 'Migliore Hotel Seoul Myeongdong' (featured on Agoda's Myeongdong-Station guide) is a DIFFERENT property — its card on the Myeong-dong district page was not attached here. |
| Busan | Hyatt Place Busan Yeonsan | [Agoda property-page](https://www.agoda.com/hotel-hlb/hotel/busan-kr.html) | FLAG: legacy Agoda slug 'hotel-hlb'. |
| Seoul | Mercure Ambassador Seoul Dongdaemun | [Agoda property-page](https://www.agoda.com/hotel-u5/hotel/seoul-kr.html) | FLAG: very new Agoda listing, review count 1. |
| Busan | Nongshim Hotel | [Agoda property-page](https://www.agoda.com/hotel-nongshim_2/hotel/busan-kr.html) | FLAG: canonical slug disambiguated '_2'. |
| Busan | Shilla Stay Seobusan - Gimhae Airport | [Agoda property-page](https://www.agoda.com/shilla-stay-seobusan/hotel/busan-kr.html) | FLAG: Agoda's display name is 'Shilla Stay busan Gimhae Airport (Noksan)'; canonical slug remains 'shilla-stay-seobusan'. |
| Busan | Benikea Hotel Haeundae | [Agoda property-page](https://www.agoda.com/benikea-premier-hotel-haeundae/hotel/busan-kr.html) | FLAG: Agoda lists the property as 'Benikea PREMIER Hotel Haeundae' while the repo name is 'Benikea Hotel Haeundae' - same address (317 Haeundaehaebyeon-ro); title difference recorded for review. |
| Busan | The Coolest Hotel | [Agoda property-page](https://www.agoda.com/songjeong-the-coolist-hotel/hotel/busan-kr.html) | FLAG: Agoda's canonical slug MISSPELLS the name as 'songjeong-the-coolist-hotel' ('coolist') - the typo is part of the real URL; the reviews route also accepts the correct spelling 'songjeong-the-coolest-hotel'. |

## Hotels with Agoda but no Booking.com URL in catalog fields

These still have a verified Agoda page. Booking.com identity/rate URL was not present in the rate/verification URL fields used to build the directory.

- **Brown Dot Hotel Cheonan Dongnam (Cheonan Station)** (Cheonan) — [Agoda](https://www.agoda.com/brown-dot-hotel-cheonan-dongnam/hotel/cheonan-si-kr.html)
- **Wiyeonjae Hanok Stay** (Gyeongju) — [Agoda](https://www.agoda.com/wiyeonjae-hanok-stay/hotel/gyeongju-si-kr.html)
- **Nadul Hanok** (Gyeongju) — [Agoda](https://www.agoda.com/nadul-hanok_2/hotel/gyeongju-si-kr.html)
- **ibis budget Ambassador Busan Haeundae** (Busan) — [Agoda](https://www.agoda.com/ibis-budget-ambassador-busan-haeundae/hotel/busan-kr.html)
- **ibis Ambassador Busan Haeundae** (Busan) — [Agoda](https://www.agoda.com/ibis-ambassador-busan-haeundae-h15814986/hotel/busan-kr.html)
- **Hotel J-TOP Cheonan** (Cheonan) — [Agoda](https://www.agoda.com/hotel-j-top-cheonan_2/hotel/cheonan-kr.html)


## Dual-source directory — Agoda.com (main verified source) + Booking.com (dated rates)

Every hotel in `data/hotels.json` (185/185) has a unique **Agoda.com** URL as a **main verified source**, labeled `Agoda`. Booking.com remains the source of **dated USD rate captures**. A blank price is not an Agoda price. Links say which site they open.

| City | Hotel | Agoda (main verified source) | Booking.com (dated-rate source) | Agoda page type |
|---|---|---|---|---|
| Seoul | L7 MYEONGDONG by LOTTE HOTELS | [Agoda](https://www.agoda.com/l7-myeongdong-by-lotte/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/l7-myeongdong-by-lotte.html) | property-page |
| Seoul | Nine Tree by Parnas Seoul Myeongdong 1 | [Agoda](https://www.agoda.com/nine-tree-hotel-myeong-dong/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/nine-tree.html) | property-page |
| Seoul | Ibis Styles Ambassador Seoul Myeongdong | [Agoda](https://www.agoda.com/ibis-styles-ambassador-seoul-myeongdong/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/ibis-styles-seoul-myeongdong.html) | property-page |
| Seoul | Ibis Ambassador Insadong (newly refurbished) | [Agoda](https://www.agoda.com/ibis-ambassador-seoul-insadong-hotel/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/ibis-ambassador-insadong.html) | property-page |
| Seoul | Four Seasons Hotel Seoul | [Agoda](https://www.agoda.com/four-seasons-hotel-seoul/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/four-seasons-seoul.html) | property-page |
| Seoul | Fairmont Ambassador Seoul | [Agoda](https://www.agoda.com/fairmont-ambassador/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/fairmont-ambassador-seoul.html) | property-page |
| Seoul | Hotel Skypark Myeongdong 3 | [Agoda](https://www.agoda.com/hotel-skypark-myeongdong-iii/reviews/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/skypark-myeongdong-3.html) | reviews-page |
| Seoul | L'Escape, A Luxury Collection Hotel, Seoul Myeongdong | [Agoda](https://www.agoda.com/l-escape-hotel_6/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/l-39-escape.html) | property-page |
| Seoul | Somerset Palace Seoul | [Agoda](https://www.agoda.com/somerset-palace-seoul/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/somerset-palace-seoul.html) | property-page |
| Seoul | ibis Ambassador Seoul Myeongdong | [Agoda](https://www.agoda.com/ibis-ambassador-seoul-myeongdong/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/ibis-myeong-dong.html) | property-page |
| Seoul | Moxy Seoul, Myeongdong | [Agoda](https://www.agoda.com/moxy-seoul-myeongdong/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/moxy-seoul-myeongdong.html) | property-page |
| Seoul | Le Méridien Seoul, Myeongdong | [Agoda](https://www.agoda.com/le-meridien-seoul-myeongdong/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/le-meridien-seoul-myeongdong.html) | property-page |
| Seoul | Aloft Seoul Myeongdong | [Agoda](https://www.agoda.com/aloft-seoul-myeongdong/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/aloft-seoul-myeongdong.html) | property-page |
| Seoul | Courtyard by Marriott Seoul Myeongdong | [Agoda](https://www.agoda.com/courtyard-seoul-namdaemun_8/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/courtyard-by-marriott-seoul-namdaemun.html) | property-page |
| Seoul | Four Points by Sheraton Josun, Seoul Myeongdong | [Agoda](https://www.agoda.com/four-points-by-sheraton-josun-seoul-myeongdong/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/four-points-by-sheraton-seoul-myeongdong.html) | property-page |
| Seoul | Nine Tree by Parnas Seoul Myeongdong 2 | [Agoda](https://www.agoda.com/nine-tree-premier-hotel-myeong-dong-2/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/nine-tree-premier-myeongdong.html) | property-page |
| Seoul | Nine Tree by Parnas Seoul Insadong | [Agoda](https://www.agoda.com/nine-tree-premier-hotel-insadong/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/nine-tree-premier-insadong.html) | property-page |
| Seoul | Shilla Stay Gwanghwamun Myeongdong | [Agoda](https://www.agoda.com/shilla-stay-gwanghwamun/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/shilla-stay-gwanghwamun.html) | property-page |
| Seoul | LOTTE HOTEL SEOUL | [Agoda](https://www.agoda.com/lotte-hotel-seoul/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/lotte-seoul-seoul.html) | property-page |
| Seoul | The Westin Josun Seoul | [Agoda](https://www.agoda.com/the-westin-chosun-seoul/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/westin-chosun-seoul.html) | property-page |
| Seoul | Four Points by Sheraton Josun, Seoul Station | [Agoda](https://www.agoda.com/four-points-by-sheraton-seoul-namsan/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/four-points-by-sheraton-seoul-namsan.html) | property-page |
| Seoul | THE PLAZA Seoul, Autograph Collection | [Agoda](https://www.agoda.com/the-plaza-seoul-autograph-collection/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/theplaza.html) | property-page |
| Seoul | Travelodge Myeongdong Euljiro | [Agoda](https://www.agoda.com/holiday-inn-express-seoul-euljiro_2/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/holiday-inn-express-seoul-euljiro.html) | property-page |
| Seoul | Sotetsu Fresa Inn Seoul Myeong-dong | [Agoda](https://www.agoda.com/sotetsu-fresa-inn-seoul-myeong-dong/reviews/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/sotetsu-fresa-inn-seoul-myeong-dong.html) | reviews-page |
| Seoul | Stanford Hotel Myeongdong | [Agoda](https://www.agoda.com/stanford-hotel-myeongdong/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/seutaenpodeuhotel-myeongdong-stanford-myeongdong.html) | property-page |
| Seoul | Sotetsu Hotels The Splaisir Seoul Myeongdong | [Agoda](https://www.agoda.com/sotetsu-hotels-the-splaisir-seoul-myeong-dong/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/the-m-seoul.html) | property-page |
| Seoul | Hotel Vert | [Agoda](https://www.agoda.com/hotel-vert/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/vert.html) | property-page |
| Seoul | Royal Hotel Seoul | [Agoda](https://www.agoda.com/royal-hotel-seoul/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/seoul-royal.html) | property-page |
| Seoul | Sejong Hotel Seoul Myeongdong | [Agoda](https://www.agoda.com/sejong-hotel-seoul-myeongdong/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/sejong.html) | property-page |
| Seoul | Orakai Insadong Suites | [Agoda](https://www.agoda.com/orakai-insadong-suites/reviews/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/orakai-insadong-suites.html) | reviews-page |
| Seoul | Novotel Ambassador Seoul Gangnam | [Agoda](https://www.agoda.com/novotel-ambassador-seoul-gangnam/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/ambassador-gangnam-seoul.html) | property-page |
| Seoul | GLAD Gangnam COEX Center | [Agoda](https://www.agoda.com/glad-gangnam-coex-center_2/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/glad-gangnam-coex-center.html) | property-page |
| Seoul | JW Marriott Hotel Seoul | [Agoda](https://www.agoda.com/jw-marriott-hotel-seoul/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/jw-marriott-seoul.html) | property-page |
| Seoul | Park Hyatt Seoul | [Agoda](https://www.agoda.com/park-hyatt-seoul-hotel/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/park-hyatt-seoul.html) | property-page |
| Seoul | Josun Palace, a Luxury Collection Hotel, Seoul Gangnam | [Agoda](https://www.agoda.com/josun-palace-a-luxury-collection-hotel-seoul-gangnam/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/josun-palace-a-luxury-collection-seoul-gangnam.html) | property-page |
| Seoul | Grand InterContinental Seoul Parnas by IHG | [Agoda](https://www.agoda.com/grand-intercontinental-seoul-parnas/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/grand-intercontinental-seoul.html) | property-page |
| Seoul | Oakwood Premier COEX Center Seoul | [Agoda](https://www.agoda.com/oakwood-premier-coex-center/reviews/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/oakwood-premier-coex-center-seoul.html) | reviews-page |
| Seoul | AC Hotel by Marriott Seoul Gangnam | [Agoda](https://www.agoda.com/mercure-ambassador-seoul-gangnam-sodowe_6/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/ac-hotel-by-marriott-seoul-gangnam.html) | property-page |
| Seoul | Dormy Inn SEOUL Gangnam | [Agoda](https://www.agoda.com/dormy-inn-seoul-gangnam/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/dormyinn-seoul-gangnam.html) | property-page |
| Seoul | Shilla Stay Seocho Gangnam Station | [Agoda](https://www.agoda.com/shilla-stay-seocho/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/shilla-stay-seocho.html) | property-page |
| Seoul | Novotel Ambassador Seoul Dongdaemun Hotels & Residences | [Agoda](https://www.agoda.com/novotel-ambassador-seoul-dongdaemun-hotels-residences/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/novotel-ambassador-seoul-dongdaemun.html) | property-page |
| Seoul | JW Marriott Dongdaemun Square Seoul | [Agoda](https://www.agoda.com/jw-marriott-dongdaemun-square-seoul/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/jw-marriott-dongdaemun-square-seoul.html) | property-page |
| Seoul | Nine Tree by Parnas Seoul Dongdaemun | [Agoda](https://www.agoda.com/nine-tree-hotel-dongdaemun/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/nine-tree-dongdaemun.html) | property-page |
| Seoul | Sofitel Ambassador Seoul Hotel & Serviced Residences | [Agoda](https://www.agoda.com/sofitel-ambassador-seoul-serviced-residences/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/sofitel-ambassador-seoul.html) | property-page |
| Seoul | Hotel28 Myeongdong (Small Luxury Hotels) | [Agoda](https://www.agoda.com/hotel-28-myeongdong/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/hotel28-myeongdong.html) | property-page |
| Seoul | Hotel Gracery Seoul | [Agoda](https://www.agoda.com/hotel-gracery-seoul/reviews/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/gracery-seoul.html) | reviews-page |
| Seoul | ENA Suite Hotel Namdaemun | [Agoda](https://www.agoda.com/ena-suite-hotel-namdaemun/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/ena-suite-namdaemun.html) | property-page |
| Seoul | L7 GANGNAM by LOTTE HOTELS | [Agoda](https://www.agoda.com/l7-gangnam-by-lotte/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/l7-gangnam.html) | property-page |
| Seoul | Fraser Place Namdaemun Seoul | [Agoda](https://www.agoda.com/fraser-place-namdaemun-seoul/reviews/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/fraser-place-namdaemun.html) | reviews-page |
| Seoul | The Westin Seoul Parnas | [Agoda](https://www.agoda.com/intercontinental-coex-hotel/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/coex-intercontinental-seoul.html) | property-page |
| Seoul | L7 HONGDAE by LOTTE HOTELS | [Agoda](https://www.agoda.com/l7-hongdae/reviews/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/l7-hongdae.html) | reviews-page |
| Seoul | RYSE, Autograph Collection, Seoul | [Agoda](https://www.agoda.com/ryse-autograph-collection_2/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/ryse-autograph-collection-korea.html) | property-page |
| Seoul | Mercure Ambassador Seoul Hongdae | [Agoda](https://www.agoda.com/mercure-ambassador-seoul-hongdae/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/mercure-ambassador-seoul-hongdae.html) | property-page |
| Seoul | Holiday Inn Express Seoul Hongdae by IHG | [Agoda](https://www.agoda.com/holiday-inn-express-seoul-hongdae/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/holiday-inn-express-seoul-hongdae.html) | property-page |
| Seoul | GLAD Mapo | [Agoda](https://www.agoda.com/glad-mapo/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/geulraedeu-mapo.html) | property-page |
| Seoul | Grand Hyatt Seoul | [Agoda](https://www.agoda.com/grand-hyatt-seoul/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/grand-hyatt-seoul.html) | property-page |
| Seoul | Mondrian Seoul Itaewon | [Agoda](https://www.agoda.com/mondrian-seoul-itaewon/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/mondrian-seoul-itaewon.html) | property-page |
| Seoul | Hamilton Hotel Seoul | [Agoda](https://www.agoda.com/hamilton-hotel-itaewon/reviews/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/hamilton.html) | reviews-page |
| Seoul | Novotel Ambassador Seoul Yongsan | [Agoda](https://www.agoda.com/novotel-ambassador-seoul-yongsan/reviews/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/novotel-ambassador-seoul-yongsan.html) | reviews-page |
| Seoul | Sotetsu Hotels The Splaisir Seoul Dongdaemun | [Agoda](https://www.agoda.com/sotetsu-hotels-the-splaisir-seoul-dongdaemun/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/ky-heritage-dongdaemun.html) | property-page |
| Seoul | Ramada by Wyndham Seoul Dongdaemun | [Agoda](https://www.agoda.com/ramada-by-wyndham-seoul-dongdaemun/reviews/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/ramada-seoul-dongdaemun.html) | reviews-page |
| Seoul | Toyoko Inn Seoul Dongdaemun II | [Agoda](https://www.agoda.com/toyoko-inn-seoul-dongdaemun-ii/reviews/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/toyoko-inn-seoul-dongdaemun-ii.html) | reviews-page |
| Seoul | Hotel Sunbee Insadong | [Agoda](https://www.agoda.com/sunbee-hotel-insadong-seoul/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/sunbee.html) | property-page |
| Seoul | Orakai Daehakro Hotel, BW Signature Collection | [Agoda](https://www.agoda.com/orakai-daehakro-hotel/reviews/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/orakai-daehakro.html) | reviews-page |
| Seoul | Amid Hotel Seoul | [Agoda](https://www.agoda.com/center-mark-hotel/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/centermark.html) | property-page |
| Seoul | Dormy Inn EXPRESS SEOUL Insadong | [Agoda](https://www.agoda.com/hotel-kuretakeso-insadong_3/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/dormyinnexpressseoulinsadong.html) | property-page |
| Seoul | Hotel PJ Myeongdong | [Agoda](https://www.agoda.com/hotel-pj-myeongdong/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/pj.html) | property-page |
| Seoul | Klaven Hotel Myeongdong City Hall | [Agoda](https://www.agoda.com/hotel-aropa_3/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/aropa.html) | property-page |
| Seoul | voco Seoul Gangnam by IHG | [Agoda](https://www.agoda.com/voco-seoul-gangnam/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/voco-seoul-gangnam-an-ihg.html) | property-page |
| Seoul | Hilton Garden Inn Seoul Gangnam | [Agoda](https://www.agoda.com/hilton-garden-inn-seoul-gangnam/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/hilton-garden-inn-seoul-gangnam.html) | property-page |
| Seoul | Amanti Hotel Seoul Hongdae | [Agoda](https://www.agoda.com/amanti-hotel-seoul/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/amanti-seoul.html) | property-page |
| Seoul | Hotel The Designers Hongdae | [Agoda](https://www.agoda.com/hotel-the-designers-hongdae/reviews/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/the-designer-hongdae.html) | reviews-page |
| Seoul | Seoul Garden Hotel | [Agoda](https://www.agoda.com/best-western-premier-seoul-garden-hotel/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/best-western-premier-seoul-garden.html) | property-page |
| Seoul | Imperial Palace Boutique Hotel Itaewon | [Agoda](https://www.agoda.com/imperial-palace-boutique-hotel/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/imperial-palace-boutique.html) | property-page |
| Seoul | Grand Mercure Ambassador Hotel and Residences Seoul Yongsan | [Agoda](https://www.agoda.com/grand-mercure-ambassador-seoul-yongsan_3/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/grand-mercure-ambassador-seoul-yongsan.html) | property-page |
| Seoul | Nine Tree Premier ROKAUS Hotel Seoul Yongsan | [Agoda](https://www.agoda.com/h36845586/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/nine-tree-premier-rokaus-seoul-yongsan-seoul.html) | property-page |
| Seoul | Hotel Skypark Dongdaemun I | [Agoda](https://www.agoda.com/skypark-dongdaemun-i-h68856392/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/skypark-dongdaemun-i.html) | property-page |
| Seoul | Hotel The Designers Dongdaemun | [Agoda](https://www.agoda.com/hotel-the-designers-dongdaemun/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/the-designers-dongdaemun.html) | property-page |
| Seoul | Mangrove Dongdaemun | [Agoda](https://www.agoda.com/mangrove-dongdaemun/reviews/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/maenggeurobeu-dongdaemun-junggu.html) | reviews-page |
| Seoul | Moxy Seoul Insadong by Marriott | [Agoda](https://www.agoda.com/moxy-seoul-insadong/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/moxy-seoul-insadong.html) | property-page |
| Seoul | Grid Inn Hotel Jongno | [Agoda](https://www.agoda.com/grid-inn/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/grid-inn.html) | property-page |
| Seoul | LOTTE City Hotel Myeongdong | [Agoda](https://www.agoda.com/lotte-city-hotel-myeongdong/reviews/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/lotte-city-seoul-myeongdong.html) | reviews-page |
| Seoul | Henn na Hotel Seoul Myeongdong | [Agoda](https://www.agoda.com/h22615631/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/bian-nahoteru-souruming-dong.html) | property-page |
| Seoul | Hotel Skypark Myeongdong 2 | [Agoda](https://www.agoda.com/hotel-skypark-myeongdong-ii/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/skypark-myeongdong-2.html) | property-page |
| Seoul | Hotel Entra Gangnam | [Agoda](https://www.agoda.com/hotel-entra-gangnam/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/entra.html) | property-page |
| Seoul | Hotel Cappuccino | [Agoda](https://www.agoda.com/hotel-cappuccino-seoul/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/cappuccino.html) | property-page |
| Seoul | Shilla Stay Samsung COEX Center | [Agoda](https://www.agoda.com/shilla-stay-samsung/reviews/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/shilla-stay-samsung.html) | reviews-page |
| Seoul | Shilla Stay Gangnam Yeoksam | [Agoda](https://www.agoda.com/shilla-stay-yeoksam/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/shilla-stay-yeoksam.html) | property-page |
| Seoul | HOTEL in 9 Gangnam | [Agoda](https://www.agoda.com/hotel-in-9-coex-center-gangnam/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/in-9.html) | property-page |
| Seoul | Hotel Peyto Samseong | [Agoda](https://www.agoda.com/hotel-peyto-samseong/reviews/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/peyto-samseong.html) | reviews-page |
| Seoul | The Ambassador Seoul - A Pullman Hotel | [Agoda](https://www.agoda.com/grand-ambassador-seoul/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/grand-ambassador-seoul-associated-with-pullman.html) | property-page |
| Seoul | Hotel Migliore Seoul | [Agoda](https://www.agoda.com/hotel-migliore-seoul/reviews/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/milreore-seoul.html) | reviews-page |
| Seoul | Hotel Naru Seoul - MGallery Collection | [Agoda](https://www.agoda.com/hotel-naru-seoul-mgallery-ambassador/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/naru-seoul-mgallery-ambassador.html) | property-page |
| Seoul | Mercure Ambassador Seoul Dongdaemun | [Agoda](https://www.agoda.com/hotel-u5/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/u5.html) | property-page |
| Seoul | LOTTE CITY HOTEL Mapo | [Agoda](https://www.agoda.com/lotte-city-hotel-mapo/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/lottecityhotel.html) | property-page |
| Seoul | Fraser Place Central Seoul | [Agoda](https://www.agoda.com/fraser-place-central-seoul-residence/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/fraser-place-central-seoul.html) | property-page |
| Seoul | Aloft by Marriott Seoul Gangnam | [Agoda](https://www.agoda.com/aloft-seoul-gangnam/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/aloft-seoul-gangnam.html) | property-page |
| Seoul | Solaria Nishitetsu Hotel Seoul Myeongdong | [Agoda](https://www.agoda.com/solaria-nishitetsu-hotel-seoul-myeongdong/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/solaria-nishitetsu-seoul.html) | property-page |
| Seoul | Hotel Prince Seoul | [Agoda](https://www.agoda.com/prince-hotel-myeongdong/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/hotel-prince-seoul.html) | property-page |
| Seoul | G2 Hotel Myeongdong | [Agoda](https://www.agoda.com/g2-hotel-myeongdong/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/g2-myeongdong.html) | property-page |
| Seoul | Hotel Thomas Myeongdong | [Agoda](https://www.agoda.com/hotel-thomas-myeongdong_2/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/thomas-myeongdong.html) | property-page |
| Seoul | Signiel Seoul | [Agoda](https://www.agoda.com/signiel-seoul/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/signiel-seoul.html) | property-page |
| Seoul | Lotte Hotel World | [Agoda](https://www.agoda.com/lotte-hotel-world/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/lotte-world.html) | property-page |
| Seoul | The Classic 500 Pentaz Executive Residence | [Agoda](https://www.agoda.com/the-classic-500-executive-residence-pentaz/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/the-classic-500.html) | property-page |
| Seoul | voco Seoul Myeongdong by IHG (former Tmark Grand) | [Agoda](https://www.agoda.com/tmark-grand-hotel-myeongdong_12/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/voco-seoul-myeongdong.html) | property-page |
| Seoul | Crown Park Hotel Seoul Myeongdong | [Agoda](https://www.agoda.com/crown-park-hotel-myeongdong-seoul/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/crown-park.html) | property-page |
| Seoul | Toyoko Inn Seoul Gangnam | [Agoda](https://www.agoda.com/toyoko-inn-gangnam-seoul/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/toyoko-inn-seoul-gangnam.html) | property-page |
| Seoul | Best Western Premier Gangnam Hotel | [Agoda](https://www.agoda.com/best-western-premier-gangnam_10/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/bestwestern-premier-gangnam.html) | property-page |
| Seoul | Must Stay Hotel Myeongdong | [Agoda](https://www.agoda.com/must-stay-hotel-myeongdong/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/seoul-backpackers.html) | property-page |
| Seoul | Shilla Stay Seodaemun Seoul Station | [Agoda](https://www.agoda.com/shilla-stay-seodaemun/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/shilla-stay-seodaemun.html) | property-page |
| Seoul | Toyoko Inn Seoul Yeongdeungpo | [Agoda](https://www.agoda.com/toyoko-inn-seoul-yeongdeungpo/hotel/seoul-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/toyoko-inn-seoul-yeongdeungpo.html) | property-page |
| Gyeongju | Hwangnamkwan Hanok Hotel (황남관 한옥호텔) | [Agoda](https://www.agoda.com/hwangnamkwan-hanok-guesthouse/hotel/gyeongju-si-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/hwangnamguan-hanok-village-gyeongjusi.html) | property-page |
| Gyeongju | Commodore Hotel Gyeongju | [Agoda](https://www.agoda.com/commodore/hotel/gyeongju-si-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/commodore-gyeongju.html) | property-page |
| Gyeongju | Lahan Select Gyeongju | [Agoda](https://www.agoda.com/lahan-select-gyeongju/reviews/gyeongju-si-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/hyundai-gyeongju.html) | reviews-page |
| Gyeongju | Hilton Gyeongju | [Agoda](https://www.agoda.com/hilton-gyeongju/hotel/gyeongju-si-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/gyeongju-hilton.html) | property-page |
| Gyeongju | GG Hotel Gyeongju | [Agoda](https://www.agoda.com/gyeongju-tourist-hotel-gg/hotel/gyeongju-si-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/gyeongju-dy-tourist.html) | property-page |
| Gyeongju | Kolon Hotel Gyeongju | [Agoda](https://www.agoda.com/kolon-hotel/hotel/gyeongju-si-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/kolon.html) | property-page |
| Gyeongju | The-K Hotel Gyeongju | [Agoda](https://www.agoda.com/the-k-hotel-gyeongju_3/hotel/gyeongju-si-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/the-k-gyeong-ju.html) | property-page |
| Gyeongju | KINOCK Gyeongju | [Agoda](https://www.agoda.com/the-suite-hotel-gyeongju/hotel/gyeongju-si-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/the-suite-gyeongju.html) | property-page |
| Gyeongju | Benikea Swiss Rosen Hotel Gyeongju | [Agoda](https://www.agoda.com/benikea-swiss-rosen-hotel/reviews/gyeongju-si-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/swiss-rosen.html) | reviews-page |
| Gyeongju | Rivertain Hotel Gyeongju | [Agoda](https://www.agoda.com/rivertain-hotel-gyeongju/reviews/gyeongju-si-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/rivertain-hotel-gyeongju.html) | reviews-page |
| Gyeongju | HanokInn | [Agoda](https://www.agoda.com/h36825033/hotel/gyeongju-si-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/hanogin.html) | property-page |
| Gyeongju | Wiyeonjae Hanok Stay | [Agoda](https://www.agoda.com/wiyeonjae-hanok-stay/hotel/gyeongju-si-kr.html) | — | property-page |
| Gyeongju | Nadul Hanok | [Agoda](https://www.agoda.com/nadul-hanok_2/hotel/gyeongju-si-kr.html) | — | property-page |
| Gyeongju | SONO Calm Gyeongju | [Agoda](https://www.agoda.com/sono-belle-gyeongju/reviews/gyeongju-si-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/daemyung-resort-gyeongju.html) | reviews-page |
| Gyeongju | Kensington Resort Gyeongju | [Agoda](https://www.agoda.com/kensington-resort-gyeongju/hotel/gyeongju-si-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/kensington-resort-gyeongju.html) | property-page |
| Busan | Shilla Stay Busan Haeundae | [Agoda](https://www.agoda.com/shilla-stay-haeundae/hotel/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/shilla-stay-haeundae.html) | property-page |
| Busan | L7 HAEUNDAE by LOTTE HOTELS | [Agoda](https://www.agoda.com/l7-haeundae/hotel/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/l7-haeundae-busan.html) | property-page |
| Busan | ASTI Hotel Busan Station | [Agoda](https://www.agoda.com/asti-hotel-busan-station/hotel/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/asti-busan.html) | property-page |
| Busan | Grand Josun Busan | [Agoda](https://www.agoda.com/novotel-ambassador-busan_8/hotel/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/grand-josun-busan.html) | property-page |
| Busan | Park Hyatt Busan | [Agoda](https://www.agoda.com/park-hyatt-busan/reviews/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/park-hyatt-busan.html) | reviews-page |
| Busan | Toyoko Inn Busan Haeundae No.2 | [Agoda](https://www.agoda.com/toyoko-inn-busan-haeundae-2_6/hotel/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/toyoko-inn-busan-haeundae-2.html) | property-page |
| Busan | Ramada Encore by Wyndham Busan Haeundae | [Agoda](https://www.agoda.com/ramada-encore-by-wyndham-busan-haeundae/reviews/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/haeundae-ramada-encore.html) | reviews-page |
| Busan | SIGNIEL BUSAN | [Agoda](https://www.agoda.com/signiel-busan/hotel/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/signiel-busan.html) | property-page |
| Busan | Paradise Hotel Busan | [Agoda](https://www.agoda.com/paradise-hotel-busan/reviews/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/paradise-busan.html) | reviews-page |
| Busan | The Westin Josun Busan | [Agoda](https://www.agoda.com/the-westin-josun-busan/reviews/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/the-westin-chosun-busan.html) | reviews-page |
| Busan | Fairfield by Marriott Busan | [Agoda](https://www.agoda.com/fairfield-by-marriott-busan_3/hotel/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/fairfield-by-marriott-busan.html) | property-page |
| Busan | ibis budget Ambassador Busan Haeundae | [Agoda](https://www.agoda.com/ibis-budget-ambassador-busan-haeundae/hotel/busan-kr.html) | — | property-page |
| Busan | ibis Ambassador Busan Haeundae | [Agoda](https://www.agoda.com/ibis-ambassador-busan-haeundae-h15814986/hotel/busan-kr.html) | — | property-page |
| Busan | LOTTE HOTEL BUSAN | [Agoda](https://www.agoda.com/lotte-hotel-busan/reviews/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/lotte-busan.html) | reviews-page |
| Busan | Avani Central Busan | [Agoda](https://www.agoda.com/avani-central-busan/reviews/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/avani-central-busan.html) | reviews-page |
| Busan | Ramada Encore by Wyndham Busan Station | [Agoda](https://www.agoda.com/ramada-encore-by-wyndham-busan-station/hotel/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/ramada-encore-by-wyndham-busan.html) | property-page |
| Busan | Toyoko Inn Busan Station No.1 | [Agoda](https://www.agoda.com/toyoko-inn-busan-station-no-1/reviews/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/toyoko-inn-busan-no-1.html) | reviews-page |
| Busan | Crown Harbor Hotel Busan | [Agoda](https://www.agoda.com/crown-harbor-hotel-busan/hotel/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/crown-harbour-busan.html) | property-page |
| Busan | Fairfield by Marriott Busan Songdo Beach | [Agoda](https://www.agoda.com/fairfield-by-marriott-busan-songdo-beach/reviews/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/fairfield-by-marriott-busan-songdo-beach.html) | reviews-page |
| Busan | Wyndham Grand Busan Ijin | [Agoda](https://www.agoda.com/wyndham-grand-busan-ijin/hotel/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/wyndham-grand-busan.html) | property-page |
| Busan | Hyatt Place Busan Yeonsan | [Agoda](https://www.agoda.com/hotel-hlb/hotel/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/hyatt-place-busan-yeonsan.html) | property-page |
| Busan | Hotel Foret Premier Nampo | [Agoda](https://www.agoda.com/hotel-foret-premier-nampo/reviews/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/foret-premier-nampo.html) | reviews-page |
| Busan | Kent Hotel Gwangalli by Kensington | [Agoda](https://www.agoda.com/kent-hotel-gwangalli-by-kensington/hotel/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/kent-gwangalli.html) | property-page |
| Busan | Ananti at Busan Cove (Ananti Hilton Busan) | [Agoda](https://www.agoda.com/ananti-hilton-busan/reviews/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/hilton-busan.html) | reviews-page |
| Busan | Nongshim Hotel | [Agoda](https://www.agoda.com/hotel-nongshim_2/hotel/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/nongshim.html) | property-page |
| Busan | Haeundae Centum Hotel | [Agoda](https://www.agoda.com/haeundae-centum-hotel/hotel/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/haeundae-centum.html) | property-page |
| Busan | Nampo Hound Hotel Premier | [Agoda](https://www.agoda.com/hound-hotel-premier-nampo/hotel/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/hound-bupyeong.html) | property-page |
| Busan | Toyoko Inn Busan Seomyeon | [Agoda](https://www.agoda.com/toyoko-inn-busan-seomyeon_4/hotel/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/toyoko-inn-seomyeon.html) | property-page |
| Busan | Shilla Stay Seobusan - Gimhae Airport | [Agoda](https://www.agoda.com/shilla-stay-seobusan/hotel/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/shillastay-seobusan.en-gb.html) | property-page |
| Busan | Benikea Hotel Haeundae | [Agoda](https://www.agoda.com/benikea-premier-hotel-haeundae/hotel/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/benikea-haeundae.html) | property-page |
| Busan | H Avenue Hotel Gwangalli branch | [Agoda](https://www.agoda.com/h-avenue-hotel-gwangalli-branch/hotel/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/h-avnue.html) | property-page |
| Busan | The Coolest Hotel | [Agoda](https://www.agoda.com/songjeong-the-coolist-hotel/hotel/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/the-coolest.html) | property-page |
| Busan | Grab The Ocean Songdo | [Agoda](https://www.agoda.com/best-western-plus-busan-songdo/hotel/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/busan-songdo-hotel.html) | property-page |
| Busan | Stanford Hotel Busan | [Agoda](https://www.agoda.com/stanford-inn-busan_2/hotel/busan-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/stanford-inn-busan.html) | property-page |
| Cheonan | Shilla Stay Cheonan | [Agoda](https://www.agoda.com/shilla-stay-cheonan/hotel/cheonan-si-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/shilla-cheonan.html) | property-page |
| Cheonan | Ramada Encore by Wyndham Cheonan | [Agoda](https://www.agoda.com/ramada-encore-hotel-cheonan/reviews/cheonan-si-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/ramada-encore-cheonan.html) | reviews-page |
| Cheonan | ON City Hotel | [Agoda](https://www.agoda.com/on-city-hotel/hotel/cheonan-si-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/on-city.html) | property-page |
| Cheonan | Sono Belle Cheonan | [Agoda](https://www.agoda.com/sono-belle-cheonan/reviews/cheonan-si-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/i2i-eeae-i-degi.html) | reviews-page |
| Cheonan | SureStay Plus Hotel by Best Western Asan | [Agoda](https://www.agoda.com/best-western-asan-hotel/hotel/asan-si-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/surestay-plus-by-best-western.html) | property-page |
| Cheonan | Brown Dot Hotel Cheonan Dongnam (Cheonan Station) | [Agoda](https://www.agoda.com/brown-dot-hotel-cheonan-dongnam/hotel/cheonan-si-kr.html) | — | property-page |
| Cheonan | The Mains Hotel | [Agoda](https://www.agoda.com/cheonan-a1-h78508786/hotel/cheonan-si-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/the-mains.html) | property-page |
| Cheonan | Hotel J-TOP Cheonan | [Agoda](https://www.agoda.com/hotel-j-top-cheonan_2/hotel/cheonan-kr.html) | — | property-page |
| Daejeon | Toyoko Inn Daejeon Government Complex | [Agoda](https://www.agoda.com/toyoko-inn-daejeon-government-complex/reviews/daejeon-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/toyoko-inn-daejeon-government-complex.html) | reviews-page |
| Daejeon | Ramada by Wyndham Daejeon | [Agoda](https://www.agoda.com/ramada-daejeon-hotel/hotel/daejeon-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/ramada-daejeon.html) | property-page |
| Daejeon | LOTTE City Hotel Daejeon | [Agoda](https://www.agoda.com/lotte-city-hotel-daejeon/hotel/daejeon-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/lotte-city-daejeon.html) | property-page |
| Daejeon | BENIKEA Hotel Daelim | [Agoda](https://www.agoda.com/benikea-hotel-daelim/hotel/daejeon-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/daelim.html) | property-page |
| Daejeon | Le Stendal Hotel | [Agoda](https://www.agoda.com/hotel-stendhal-h10573875/hotel/daejeon-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/seutangdalhotel.html) | property-page |
| Daejeon | Hotel Interciti | [Agoda](https://www.agoda.com/hotel-interciti/hotel/daejeon-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/hotelinterciti.html) | property-page |
| Daejeon | Aank Air Hotel Daejeon Station | [Agoda](https://www.agoda.com/aank-hotel-daejeon-station/hotel/daejeon-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/aank-daejeon-station.html) | property-page |
| Daejeon | Hotel Onoma, Daejeon, Autograph Collection | [Agoda](https://www.agoda.com/hotel-onoma-daejeon-autograph-collection/hotel/daejeon-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/onoma-daejeon-autograph-collection.html) | property-page |
| Daejeon | Skypark Daejeon 1 | [Agoda](https://www.agoda.com/hotel-skypark-daejeon-i/hotel/daejeon-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/skypark-daejeoni.html) | property-page |
| Daejeon | Hotel ICC | [Agoda](https://www.agoda.com/hotel-icc/hotel/daejeon-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/icc.html) | property-page |
| Daejeon | Dunsan Graytone Hotel | [Agoda](https://www.agoda.com/dunsan-graytone-hotel/hotel/daejeon-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/dunsan-graytone.html) | property-page |
| Suwon | Novotel Ambassador Suwon | [Agoda](https://www.agoda.com/novotel-ambassador-suwon-hotel/hotel/suwon-si-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/novotel-ambassador-suwon.html) | property-page |
| Suwon | Four Points by Sheraton Suwon | [Agoda](https://www.agoda.com/four-points-by-sheraton-suwon/hotel/suwon-si-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/four-points-by-sheraton-suwon.html) | property-page |
| Suwon | Ramada Plaza by Wyndham Suwon | [Agoda](https://www.agoda.com/ramada-plaza/hotel/suwon-si-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/ramada-plaza-suwon.html) | property-page |
| Suwon | Courtyard by Marriott Suwon | [Agoda](https://www.agoda.com/courtyard-by-marriott-suwon/hotel/suwon-si-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/courtyard-by-marriott-suwon.html) | property-page |
| Suwon | ibis Ambassador Suwon | [Agoda](https://www.agoda.com/ibis-ambassador-suwon/hotel/suwon-si-kr.html) | [Booking.com](https://www.booking.com/hotel/kr/ibis-suwon-ambassador.html) | property-page |
| Suwon | Hotel Biz Suwon | [Agoda](https://www.agoda.com/hotel-biz-suwon/hotel/suwon-kr.html) | [Booking.com](https://www.booking.com/reviews/kr/hotel/biz-suwon.html) | property-page |

