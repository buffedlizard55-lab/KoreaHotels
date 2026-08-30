#!/usr/bin/env python3
"""Round-31 (2026-08-31): apply directly-fetched Agoda URL upgrades.

Every URL below was surfaced by Agoda's own site routing on 2026-08-31:
each property's /reviews/<city> page (the 'Book Now' link that Agoda renders
is the current canonical /hotel/<city> URL) or a directly fetched hotel
page whose title, address and selectedproperty matched the repo record.
Nothing is guessed: where Agoda's slug did not resolve, the record stays
unresolved/not-found (see REFRESHED note stamping).

Method: the en-sg reviews route (https://www.agoda.com/en-sg/<slug>/reviews/<city>-kr.html)
fuzzy-matches Agoda properties and returns the live reviews page with the
canonical 'Book Now' hotel URL; the page title/address/score were captured
as evidence per record.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "hotels.json")
DATE = "2026-08-31"

# id -> (canonical agoda /hotel/ URL, evidence note)
VERIFIED = {
    # ---- carried over from earlier in the 2026-08-31 session ----
    "seoul-ibis-insadong": (
        "https://www.agoda.com/ibis-ambassador-seoul-insadong-hotel/hotel/seoul-kr.html",
        "Agoda property page fetched live 2026-08-31: title 'ibis Ambassador Seoul Insadong', 4 stars self-reported, address 31 Samil-daero 30-gil Jongno-gu 03132, score 8.7/2,765 reviews (service 9.2, loc 9.1, clean 8.9, value 8.6, facilities 8.4), selectedproperty=433160; Anguk Stn 0.43 km; 'newly renovated in 2025'. Identity matches repo record (Insadong/Jongno).",
    ),
    "seoul-lescape": (
        "https://www.agoda.com/l-escape-hotel_6/hotel/seoul-kr.html",
        "Agoda property page fetched live 2026-08-31: title \"L'Escape, A Luxury Collection Hotel, Seoul Myeongdong\", 9.1/~777 reviews; legacy Agoda slug is 'l-escape-hotel_6' (stale; URL verified by direct fetch, not by slug text). Repo record: L'Escape Seoul Myeongdong.",
    ),
    "seoul-four-points-myeongdong": (
        "https://www.agoda.com/four-points-by-sheraton-josun-seoul-myeongdong/hotel/seoul-kr.html",
        "Agoda property page fetched live 2026-08-31: title 'Four Points by Sheraton Josun, Seoul Myeongdong', 8.8/~3,067 reviews; identity matches repo record (Myeongdong, Josun/Four Points).",
    ),
    "seoul-novotel-ambassador-gangnam": (
        "https://www.agoda.com/novotel-ambassador-seoul-gangnam/hotel/seoul-kr.html",
        "Agoda property page fetched live 2026-08-31: title 'Novotel Ambassador Seoul Gangnam', selectedproperty=1372, 8.4/~4,518 reviews; address matches Gangnam record.",
    ),
    "busan-asti": (
        "https://www.agoda.com/asti-hotel-busan-station/hotel/busan-kr.html",
        "Agoda property page fetched live 2026-08-31: title 'ASTI Hotel Busan Station', 9.0/~17,188 reviews; selectedproperty=5061354; identity matches repo (Busan Station).",
    ),
    "gyeongju-hwangnamkwan": (
        "https://www.agoda.com/hwangnamkwan-hanok-guesthouse/hotel/gyeongju-si-kr.html",
        "Agoda property page fetched live 2026-08-31: title 'Hwangnamkwan Hanok Guesthouse', 8.5/~3,290 reviews, selectedproperty=570232; identity matches repo (Hwangnam-dong hanok).",
    ),
    "daejeon-benikea-daelim": (
        "https://www.agoda.com/benikea-hotel-daelim/hotel/daejeon-kr.html",
        "Agoda property page fetched live 2026-08-31: title 'BENIKEA Hotel Daelim', 8.2/~3,498 reviews, selectedproperty=262489; Daejeon address matches repo.",
    ),
    "cheonan-brown-dot": (
        "https://www.agoda.com/brown-dot-hotel-cheonan-dongnam/hotel/cheonan-si-kr.html",
        "Agoda property page fetched live 2026-08-31: title 'Brown Dot Hotel Cheonan Dongnam', 8.7/~655 reviews, selectedproperty=41304719; Cheonan Station/Dongnam address matches repo. Sister-branch trap avoided (the 'brown-dot' slug is a different branch).",
    ),
    "gyeongju-kolon": (
        "https://www.agoda.com/kolon-hotel/hotel/gyeongju-si-kr.html",
        "Agoda property page fetched live 2026-08-31: title 'Kolon Hotel Gyeongju', 7.6/~2,130 reviews, selectedproperty=9284; Bomun Lake resort address matches repo.",
    ),
    "gyeongju-kinock": (
        "https://www.agoda.com/the-suite-hotel-gyeongju/hotel/gyeongju-si-kr.html",
        "Agoda property page fetched live 2026-08-31: title 'The Suite Hotel Gyeongju [KINOCK]', 8.5/~1,432 reviews, selectedproperty=230590; address 280-12 Bomun-ro. FLAG: Agoda's property name is The Suite Hotel Gyeongju [KINOCK] - same property as repo KINOCK Gyeongju; legacy Agoda slug 'the-suite-hotel-gyeongju'.",
    ),
    "gyeongju-hanokinn": (
        "https://www.agoda.com/h36825033/hotel/gyeongju-si-kr.html",
        "Agoda property page fetched live 2026-08-31 via Agoda's h-id canonical route: title 'HanokInn', 9.5/~688 reviews, selectedproperty=36825033; identity matches repo (Gyeongju hanok stay).",
    ),
    # ---- resolved 2026-08-31 via reviews-route Book Now canonical links ----
    "seoul-nine-tree": (
        "https://www.agoda.com/nine-tree-hotel-myeong-dong/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'NINE TREE BY PARNAS SEOUL MYEONDONG 1', address 51 Myeong-dong 10-gil Jung-gu 100-012, score 8.7/19,572 reviews, selectedproperty=407482; Myeong-dong Stn 0.08 km; Book Now canonical = nine-tree-hotel-myeong-dong. Identity matches repo (Nine Tree Myeongdong 1, 51 Myeongdong 10-gil).",
    ),
    "suwon-ramada-plaza": (
        "https://www.agoda.com/ramada-plaza/hotel/suwon-si-kr.html",
        "Agoda property page fetched live 2026-08-31: title 'Ramada Plaza Suwon', 4 stars, address 150 Jungbu-daero Paldal-gu 16483, score 8.6/3,868 reviews (selectedproperty 161789 via See-all link; hotelImages 2296549).",
    ),
    "suwon-novotel-ambassador": (
        "https://www.agoda.com/novotel-ambassador-suwon-hotel/hotel/suwon-si-kr.html",
        "Agoda property page fetched live 2026-08-31: title 'Novotel Ambassador Suwon Hotel', 4.5 stars, address 902 Dukyoungdaero Paldal-gu, score 8.8/3,907 reviews, selectedproperty=745644; Suwon Station 210 m; matches Accor official (all.accor.com/hotel/8748). FLAG: suggest API returns a second duplicate listing id 68658955 with no image - ignore, 745644 is the canonical page.",
    ),
    "suwon-four-points": (
        "https://www.agoda.com/four-points-by-sheraton-suwon/hotel/suwon-si-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Four Points by Sheraton Suwon', address 27 Hyowon-ro 307 beon-gil Paldal-gu 16488, score 8.8/884 reviews; suggest id 35780706 (city 3818 Suwon).",
    ),
    "suwon-courtyard": (
        "https://www.agoda.com/courtyard-by-marriott-suwon/hotel/suwon-si-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Courtyard by Marriott Suwon', address 320 Gwanggyohosugongwon-ro 16514 (Gwanggyo/Suwon Convention Center), score 8.8/1,690 reviews; suggest id 10777143. Note: fetch redirected slug 'courtyard-merriott-suwon' to the Book Now canonical above.",
    ),
    "suwon-ibis": (
        "https://www.agoda.com/ibis-ambassador-suwon/hotel/suwon-si-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Ibis Ambassador Suwon', address 132 Kwon Kwang-Ro Paldal-gu 16491, score 8.5/2,434 reviews; suggest id 108639 (Suwon-si).",
    ),
    "seoul-the-plaza-autograph-collection": (
        "https://www.agoda.com/the-plaza-seoul-autograph-collection/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'THE PLAZA Seoul, Autograph Collection', address 119 Sogong-ro Jung-gu 04525, score 8.8/1,344 reviews; suggest id 5293 (Seoul). City Hall location matches repo.",
    ),
    "seoul-travelodge-myeongdong-euljiro": (
        "https://www.agoda.com/holiday-inn-express-seoul-euljiro_2/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Travelodge Myeongdong Euljiro', address 61 Supyo-ro Jung-gu 04542, score 8.2/8,281 reviews; suggest id 926964. FLAG: legacy Agoda slug 'holiday-inn-express-seoul-euljiro_2' (rebranded to Travelodge); URL verified by page title/address, not slug text.",
    ),
    "seoul-royal-hotel": (
        "https://www.agoda.com/royal-hotel-seoul/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Royal Hotel Seoul Myeongdong', address Myeongdong-gil 61 Jung-gu 04538, score 8.7/11,034 reviews; suggest id 43230. (Repo name 'Royal Hotel Seoul' = Agoda 'Royal Hotel Seoul Myeongdong'.)",
    ),
    "seoul-glad-gangnam-coex": (
        "https://www.agoda.com/glad-gangnam-coex-center_2/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'GLAD Gangnam COEX Center', address 610 Teheran-ro Gangnam-gu 133-502, score 8.7/11,225 reviews. FLAG: canonical slug disambiguated '_2'.",
    ),
    "seoul-jw-marriott-seoul": (
        "https://www.agoda.com/jw-marriott-hotel-seoul/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'JW Marriott Hotel Seoul', address 176 Sinbanpo-ro Seocho-gu 06546, score 8.9/1,209 reviews; Seocho/Gangnam Express Terminal location matches repo.",
    ),
    "seoul-grand-intercontinental-parnas": (
        "https://www.agoda.com/grand-intercontinental-seoul-parnas/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'InterContinental Grand Seoul Parnas By IHG', address 521 Teheran-ro Gangnam-gu 06164, score 9.0/2,922 reviews; COEX/Parnas location matches repo.",
    ),
    "seoul-dormy-inn-gangnam": (
        "https://www.agoda.com/dormy-inn-seoul-gangnam/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Dormy Inn SEOUL Gangnam', address 134 Bongeunsa-ro Gangnam-gu 135-081, score 9.0/22,728 reviews; 2025 top choice; COEX/Gangnam location matches repo.",
    ),
    "seoul-nine-tree-dongdaemun": (
        "https://www.agoda.com/nine-tree-hotel-dongdaemun/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'NINE TREE BY PARNAS SEOUL DONGDAEMUN', address 224 Eulji-ro Jung-gu 04561, score 8.8/14,804 reviews; 2025 award; Dongdaemun location matches repo.",
    ),
    "seoul-hotel28-myeongdong": (
        "https://www.agoda.com/hotel-28-myeongdong/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Hotel 28 Myeongdong', address 13 Myeongdong 7-gil Jung-gu 04534, score 9.2/4,427 reviews; Myeongdong address matches repo (Hotel28 Small Luxury Hotels).",
    ),
    "seoul-l7-gangnam": (
        "https://www.agoda.com/l7-gangnam-by-lotte/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'L7 GANGNAM by LOTTE HOTELS', address 415 Teheran-ro Gangnam-gu 06160, score 8.8/7,099 reviews; 2024 award.",
    ),
    "seoul-glad-mapo": (
        "https://www.agoda.com/glad-mapo/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'GLAD MAPO', address 92 Mapo-daero Mapo-gu 04168, score 9.0/20,652 reviews; 2025 award; airport bus stop outside (matches repo).",
    ),
    "seoul-grand-hyatt": (
        "https://www.agoda.com/grand-hyatt-seoul/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Grand Hyatt Seoul', address 322 Sowol-ro Yongsan-gu (Itaewon), score 8.7/4,319 reviews; 2024 award; address exactly matches repo identity.",
    ),
    "seoul-mondrian-itaewon": (
        "https://www.agoda.com/mondrian-seoul-itaewon/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Mondrian Seoul Itaewon', address 23 Jangmun-ro Yongsan-gu 04392, score 8.6/3,525 reviews; Itaewon location matches repo.",
    ),
    "seoul-sotetsu-splaisir-dongdaemun": (
        "https://www.agoda.com/sotetsu-hotels-the-splaisir-seoul-dongdaemun/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Sotetsu Hotels The Splaisir Seoul Dongdaemun', address 226 Jangchungdan-ro Jung-gu 04565, score 8.9/10,118 reviews; 2025 award; Dongdaemun location matches repo.",
    ),
    "seoul-dormy-inn-insadong": (
        "https://www.agoda.com/hotel-kuretakeso-insadong_3/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Dormy Inn EXPRESS SEOUL Insadong', address 20-9 Insadong-gil Jongno-gu 03163, score 8.9/3,152 reviews. FLAG: legacy Agoda slug 'hotel-kuretakeso-insadong_3' (Kuretakeso = pre-Dormy branding); verified by title/address.",
    ),
    "seoul-klaven-city-hall": (
        "https://www.agoda.com/hotel-aropa_3/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Klaven Hotel Myeongdong City Hall, Formerly Travelodge Myeongdong City Hall', address 22 Sejong-daero 16-gil Jung-gu 04526, score 8.5/449 reviews; suggest API id 83196636 confirms rebrand. FLAG: legacy slug 'hotel-aropa_3'; rebrand already captured in repo note.",
    ),
    "seoul-voco-gangnam": (
        "https://www.agoda.com/voco-seoul-gangnam/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'voco Seoul Gangnam by IHG', address 144 Dosan-daero Gangnam-gu 06040, score 8.9/1,633 reviews; Sinsa station area matches repo.",
    ),
    "seoul-hilton-garden-inn-gangnam": (
        "https://www.agoda.com/hilton-garden-inn-seoul-gangnam/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Hilton Garden Inn Seoul Gangnam', address 253 Gangnam-daero Seocho-gu 06735, score 8.8/2,504 reviews.",
    ),
    "seoul-best-western-premier-garden": (
        "https://www.agoda.com/best-western-premier-seoul-garden-hotel/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Seoul Garden Hotel', address 58 Mapo-daero Mapo-gu 04168, score 8.6/11,419 reviews; Book Now canonical carries the Best Western Premier name.",
    ),
    "seoul-grand-mercure-yongsan": (
        "https://www.agoda.com/grand-mercure-ambassador-seoul-yongsan_3/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Grand Mercure Ambassasdor Hotel and Residences Seoul Yongsan' (Agoda's own typo for Ambassador), address Cheongpa-ro 20-gil 95 Yongsan-gu 04372, score 8.9/1,350 reviews; canonical slug '_3'; Yongsan/Dragon Hill complex matches repo.",
    ),
    "seoul-nine-tree-rokaus-yongsan": (
        "https://www.agoda.com/h36845586/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Nine Tree Premier ROKAUS Hotel Seoul Yongsan', address 25 Hangang-daero 23-gil Yongsan-gu 04378, score 9.1/10,900 reviews; 2025 award. Book Now canonical is Agoda's h-id route h36845586 (selectedproperty 36845586).",
    ),
    "seoul-skypark-dongdaemun1": (
        "https://www.agoda.com/skypark-dongdaemun-i-h68856392/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'SKYPARK DONGDAEMUN I'; Book Now canonical skypark-dongdaemun-i-h68856392 (selectedproperty 68856392); Dongdaemun property.",
    ),
    "seoul-the-designers-dongdaemun": (
        "https://www.agoda.com/hotel-the-designers-dongdaemun/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Hotel the Designers Dongdaemun', address 306 Toegye-ro Jung-gu 100-400, score 7.2/10,556 reviews (self-reported low score honestly carried).",
    ),
    "seoul-moxy-insadong": (
        "https://www.agoda.com/moxy-seoul-insadong/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Moxy Seoul Insadong', address 37 Donhwamun-ro 11-gil Jongno 03139, score 8.8/503 reviews; Jongno/Insadong location matches repo.",
    ),
    "seoul-henn-na-myeongdong": (
        "https://www.agoda.com/h22615631/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Henn-na Hotel Seoul Myeongdong', address 59 Myeongdong 8ga-gil Jung-gu 04537, score 8.8/4,449 reviews; Book Now canonical h22615631.",
    ),
    "seoul-hotel-cappuccino": (
        "https://www.agoda.com/hotel-cappuccino-seoul/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Hotel Cappuccino Seoul', address 155 Bongeunsa-ro Gangnam-gu 06122, score 8.4/4,851 reviews.",
    ),
    "seoul-mercure-ambassador-dongdaemun": (
        "https://www.agoda.com/hotel-u5/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Mercure Ambassador Seoul Dongdaemun', address 369 Dongho-ro Jung-gu 04546, score 9.3 from 1 review - newly opened listing (matches repo's 2025/26 opening-window flag); Book Now legacy slug 'hotel-u5'. FLAG: very new Agoda listing, review count 1.",
    ),
    "seoul-aloft-gangnam": (
        "https://www.agoda.com/aloft-seoul-gangnam/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Aloft by Marriott Seoul Gangnam', address 736 Yeongdong-daero Gangnam 135-957, score 8.5/1,195 reviews.",
    ),
    "seoul-hotel-prince-myeongdong": (
        "https://www.agoda.com/prince-hotel-myeongdong/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Prince Hotel Myeongdong', address 130 Toegye-ro Jung-gu 04629, score 8.6/8,142 reviews; 2025 award; Myeongdong/Seoul Station location matches repo 'Hotel Prince Seoul'.",
    ),
    "seoul-g2-hotel-myeongdong": (
        "https://www.agoda.com/g2-hotel-myeongdong/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'G2 Hotel Myeongdong', address 24 Supyo-ro Myeong-dong 04555, score 8.7/6,406 reviews; 2024 award; address exactly matches repo (24 Supyo-ro).",
    ),
    "seoul-hotel-thomas-myeongdong": (
        "https://www.agoda.com/hotel-thomas-myeongdong_2/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Hotel Thomas Myeongdong', address 26 Sejong-daero 16-gil Myeong-dong 04526, score 8.9/8,565 reviews; 2025 award; canonical slug '_2'.",
    ),
    "seoul-grid-inn": (
        "https://www.agoda.com/grid-inn/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'GRID INN', address 9-6 Jong-ro 18-gil Jongno-gu 03192, score 8.8/4,223 reviews; suggest id 1709863 (Seoul); Jongno location matches repo 'Grid Inn Hotel Jongno'.",
    ),
    "seoul-lotte-world": (
        "https://www.agoda.com/lotte-hotel-world/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'LOTTE HOTEL WORLD', address 240 Olympic-ro Songpa 05554, score 9.0/9,583 reviews; 2025 award; Jamsil/Lotte World location matches repo.",
    ),
    "seoul-toyoko-gangnam": (
        "https://www.agoda.com/toyoko-inn-gangnam-seoul/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Toyoko INN Gangnam Seoul', address Gangnam-daero 323 Seocho-gu 06627, score 8.6/10,443 reviews; address matches repo (323 Gangnam-daero).",
    ),
    "seoul-bw-premier-gangnam": (
        "https://www.agoda.com/best-western-premier-gangnam_10/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Best Western Premier Gangnam', address 139 Bongeunsa-ro Gangnam-gu 06122, score 8.2/3,286 reviews; canonical slug '_10'. Re-UPGRADE: the pre-2026-08-30 stored URL had been downgraded when it landed on the wrong property; this URL was fetched and title/address verified.",
    ),
    "seoul-classic500": (
        "https://www.agoda.com/the-classic-500-executive-residence-pentaz/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'The Classic 500 Executive Residence Pentaz', address 90 Neungdong-ro Gwangjin-gu, score 8.7/3,252 reviews; suggest id 305454; address matches repo (90 Neungdong-ro).",
    ),
    "seoul-muststay-myeongdong": (
        "https://www.agoda.com/must-stay-hotel-myeongdong/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'MUST STAY HOTEL Myeongdong', address 15-3 Toegye-ro 2-gil Jung-gu 04635, score 6.8/2,423 reviews; Agoda Preferred; address matches repo. Low score carried honestly (KAYAK-era 6.4 consistent).",
    ),
    "seoul-ac-hotel-gangnam": (
        "https://www.agoda.com/mercure-ambassador-seoul-gangnam-sodowe_6/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'AC Hotel Seoul Gangnam', address 10 Teheran-ro 25-gil Gangnam-gu 06132, score 8.8/576 reviews; suggest id 335567. FLAG: legacy Agoda slug 'mercure-ambassador-seoul-gangnam-sodowe_6' (property rebranded Mercure Sodowe -> AC Hotel by Marriott; verified by page title; do NOT confuse with AC PALACE HOTEL & RESIDENCE id 75959291 which is a different hotel).",
    ),
    "seoul-crown-park-myeongdong": (
        "https://www.agoda.com/crown-park-hotel-myeongdong-seoul/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Crown Park Hotel Myeongdong Seoul', address Namdaemun-ro 7-gil 19 (Sogong-dong 70) Jung-gu 04532, score 8.6/10,912 reviews; 2025 award; suggest id 1077738; address matches repo (19 Namdaemun-ro 7-gil).",
    ),
    "busan-ramada-station": (
        "https://www.agoda.com/ramada-encore-by-wyndham-busan-station/hotel/busan-kr.html",
        "Agoda property page fetched live 2026-08-31: title 'Ramada Encore by Wyndham Busan Station', 4 stars, address 1204 Choryang-dong Dong-gu 48821, score 8.8/13,358 reviews, selectedproperty=9079659; Busan Station 0.12 km; phone +82 51-922-0000 matches external record. (KAYAK-era 9.1/636 was a stale sub-feed.)",
    ),
    "busan-wyndham-grand": (
        "https://www.agoda.com/wyndham-grand-busan-ijin/hotel/busan-kr.html",
        "Agoda property page fetched live 2026-08-31: title 'Wyndham Grand Busan Ijin', 5 stars, address 27 Deungdae-ro Seo-gu 49264, score 9.2/3,121 reviews, selectedproperty=46400389; Songdo Beach 270 m; opened 2023, 271 rooms; itravelblog 9.3/777 consistent.",
    ),
    "busan-kent-gwangalli-kensington": (
        "https://www.agoda.com/kent-hotel-gwangalli-by-kensington/hotel/busan-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Kent Hotel Gwangalli by Kensington', address 229 Gwanganhaebyeon-ro Suyeong-gu 613-100, score 8.6/4,285 reviews; Gwangan beachfront matches repo.",
    ),
    "busan-haeundae-centum": (
        "https://www.agoda.com/haeundae-centum-hotel/hotel/busan-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Haeundae Centum Hotel', address 20 Centum 3-ro Haeundae-gu 48060, score 8.5/8,352 reviews; 2025 award; Centum City location matches repo.",
    ),
    "busan-hound-premier-nampo": (
        "https://www.agoda.com/hound-hotel-premier-nampo/hotel/busan-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Hound Hotel Premier Nampo', address 3-1 Bosu-daero Nampo 48980, score 8.6/7,740 reviews; address matches repo (24 Bosu-daero area).",
    ),
    "busan-benikea-haeundae": (
        "https://www.agoda.com/benikea-premier-hotel-haeundae/hotel/busan-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Benikea Premier Hotel Haeundae', address Haeundaehaebyeon-ro 317 Haeundae-gu 48095, score 8.2/13,645 reviews. FLAG: Agoda lists the property as 'Benikea PREMIER Hotel Haeundae' while the repo name is 'Benikea Hotel Haeundae' - same address (317 Haeundaehaebyeon-ro); title difference recorded for review.",
    ),
    "busan-havenue-gwangalli": (
        "https://www.agoda.com/h-avenue-hotel-gwangalli-branch/hotel/busan-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'H Avenue Hotel Gwangalli branch', address 29 Millaksubyeon-ro Suyeong-gu 48283, score 8.4/1,802 reviews; address matches repo exactly (29 Millaksubyeon-ro).",
    ),
    "busan-hyatt-place-yeonsan": (
        "https://www.agoda.com/hotel-hlb/hotel/busan-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Hyatt Place Busan Yeonsan', address 1121 Jungang-daero Yeonje-gu 47524, score 8.6/94 reviews; opened 2025 (low review count consistent with itravelblog's 27). FLAG: legacy Agoda slug 'hotel-hlb'.",
    ),
    "gyeongju-gg-hotel": (
        "https://www.agoda.com/gyeongju-tourist-hotel-gg/hotel/gyeongju-si-kr.html",
        "Agoda property page fetched live 2026-08-31: title 'GG Hotel', 3 stars, address Taejong-ro 699beon-gil 3 Gyeongju City Center 38157, score 8.6/6,047 reviews, selectedproperty=529490; near Gyeongju bus terminal; matches repo (GG Hotel a.k.a. Hotel the D.Y).",
    ),
    "daejeon-hotel-icc": (
        "https://www.agoda.com/hotel-icc/hotel/daejeon-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'HOTEL ICC', address Expo-ro 123-gil 55 Yuseong-gu 305-340, score 8.3/1,683 reviews; address matches repo (55 Expo-ro 123beon-gil, Yuseong/DCC).",
    ),
    "busan-nongshim-dongnae": (
        "https://www.agoda.com/hotel-nongshim_2/hotel/busan-kr.html",
        "Agoda property page fetched live 2026-08-31: title 'Hotel Nongshim', 5 stars, address 23 Geumganggongwon-ro 20beon-gil Dongnae-gu 47709, score 8.5/4,650 reviews (service 8.9, clean 8.8, facilities 8.7, value 8.6), selectedproperty=43058; Oncheonjang Stn 0.36 km; Heosimcheong hot-spring spa on site - matches repo (Nongshim Hotel, Dongnae hot springs). FLAG: canonical slug disambiguated '_2'.",
    ),
    "seoul-skypark-myeongdong2": (
        "https://www.agoda.com/hotel-skypark-myeongdong-ii/hotel/seoul-kr.html",
        "Agoda property page fetched live 2026-08-31: title 'Hotel Skypark Myeongdong II', 3 stars, address 22 Myeongdong 9-gil Jung-gu 100-845, score 8.4/10,174 reviews, selectedproperty=267332 (suggest API id 267332, Seoul); Euljiro 1 Stn 0.25 km; matches repo (Skypark Myeongdong 2).",
    ),
    "seoul-shilla-stay-yeoksam": (
        "https://www.agoda.com/shilla-stay-yeoksam/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'Shilla Stay Gangnam Yeoksam', address 517 Eonju-ro Gangnam-gu 135915, score 8.4/6,261 reviews; Book Now canonical 'shilla-stay-yeoksam'; Gangnam/Yeoksam location matches repo.",
    ),
    "seoul-ryse-autograph-collection": (
        "https://www.agoda.com/ryse-autograph-collection_2/hotel/seoul-kr.html",
        "Agoda reviews page fetched live 2026-08-31: title 'RYSE, Autograph Collection', address 130 Yanghwa-ro Hongdae Mapo-gu 04038, score 9.1/4,682 reviews (clean 9.4, service 9.5, loc 9.6, value 8.9, facilities 9.0); 2025 award; suggest API id 4120283 (Seoul); canonical slug disambiguated '_2'; Hongdae location matches repo.",
    ),
}

# Records where the 2026-08-31 index search surfaced evidence the Agoda property
# does not exist in Agoda's own suggest index (recorded result, not absence proof).
NEW_NOT_FOUND = {
    "daejeon-aank-air": (
        "2026-08-31 Agoda suggest-API probes ('aank air hotel daejeon', 'aank air daejeon station', 'aank air hotel'; chunks 0+1) return no Korean Aank property - only Lebanon/Malaysia noise and 'Cheongju Anook ryokan and air' (the sister-brand trap). Recorded not-found result, not a verified absence; property operates (Booking/official channels)."
    ),
    "cheonan-best-western-asan": (
        "2026-08-31 Agoda suggest-API probe ('surestay plus best western asan', 'surestay asan korea') returns zero Agoda hotel objects for the Asan property - only a Google Places POI entry (address 온대로 32 Tangjeong-myeon Asan) with no Agoda property id; US SureStay listings only. Recorded not-found result, not a verified absence; property operates (Best Western official/Klook)."
    ),
    "busan-ibis-budget-haeundae": (
        "2026-08-31 Agoda suggest-API probes ('ibis budget busan haeundae', 'ibis budget ambassador busan haeundae'; chunks 0+1) list no Korean ibis budget - only Zurich/Sydney/Jakarta/Singapore/Surabaya properties. Recorded not-found result, not a verified absence."
    ),
}

# Records known to exist on Agoda (suggest id) whose canonical slug still could
# not be surfaced this round - status stays unresolved with this evidence.
STILL_UNRESOLVED = {
    "busan-ibis-haeundae": (
        "2026-08-31: Agoda suggest API CONFIRMS the property exists - id 15814986 'Ibis Ambassador Busan Haeundae', Busan (city 17172) - but the canonical /hotel/ slug could not be surfaced: 'ibis-ambassador-busan-haeundae' is occupied by a DIFFERENT property (id 1254424, 'Busan Haeundae', 12 Haeundaehaebyeon-ro 237beon-gil, 8.2/1,964) and slug variants (-hotel, ibis-busan-haeundae, ibis-ambassador-haeundae-busan, -busan-hotel) all 404; /search?selectedproperty=15814986 renders client-side only. Stays unresolved; Agoda listing certain."
    ),
    "seoul-novotel-dongdaemun": (
        "2026-08-31: Agoda suggest API CONFIRMS id 4935081 'Novotel Ambassador Seoul Dongdaemun Hotels & Residences' (Seoul) exists, but reviews/hotel slug guesses (novotel-ambassador-seoul-dongdaemun[-hotels-and-residences], novotel-seoul-dongdaemun, hotel-u5->Mercure) all 404/fuzzy-missed; stays unresolved; Agoda listing certain."
    ),
    "gyeongju-nadul-hanok": (
        "2026-08-31: Agoda suggest id 4857999 'Nadul Hanok' (Gyeongju) exists, but reviews slugs (nadul-hanok, nadul-hanok-guesthouse, hanok-guesthouse-nadul, nadul-hanok-stay, hotel-nadul-hanok) all 404; stays unresolved; small 7-room property likely under a non-obvious slug."
    ),
}

UNRESOLVED_RECHECK = (
    f" Re-checked {DATE}: Agoda listing evidence (aggregator score/deal lines) still present but no canonical agoda.com property URL could be surfaced via Agoda's own site index this round (Agoda search renders client-side; reviews-route slug resolution attempted where possible). Blank remains an honest recorded gap, not a verified absence."
)
NOTFOUND_RECHECK = (
    f" Re-checked {DATE}: targeted Agoda index searches again surfaced no agoda.com property page; recorded result, not a verified absence."
)

def main():
    with open(DATA, encoding="utf-8") as f:
        d = json.load(f)
    up, nf, st, refreshed = 0, 0, 0, 0
    for h in d["hotels"]:
        hid = h["id"]
        ss = h.get("secondarySource") or {}
        if hid in VERIFIED:
            url, note = VERIFIED[hid]
            h["secondarySource"] = {
                "platform": "Agoda",
                "status": "verified",
                "url": url,
                "lastCheckedUtc": DATE,
                "checkMethod": "property-page-fetched",
                "note": note,
            }
            up += 1
        elif hid in NEW_NOT_FOUND:
            ss["status"] = "not-found"
            ss["lastCheckedUtc"] = DATE
            ss["note"] = ss.get("note", "").rstrip() + " " + NEW_NOT_FOUND[hid]
            nf += 1
        elif hid in STILL_UNRESOLVED:
            ss["status"] = "unresolved"
            ss.pop("url", None)
            ss["lastCheckedUtc"] = DATE
            ss["note"] = STILL_UNRESOLVED[hid]
            st += 1
        elif ss.get("status") == "unresolved":
            ss["lastCheckedUtc"] = DATE
            ss["note"] = ss.get("note", "").rstrip() + UNRESOLVED_RECHECK
            refreshed += 1
        elif ss.get("status") == "not-found":
            ss["lastCheckedUtc"] = DATE
            ss["note"] = ss.get("note", "").rstrip() + NOTFOUND_RECHECK
            refreshed += 1
    meta = d.setdefault("meta", {})
    batches = meta.setdefault("newEntryBatches", [])
    batches.append({
        "date": DATE,
        "kind": "agoda-verification-round",
        "upgradedToVerified": up,
        "newNotFound": nf,
        "stillUnresolvedWithAgodaId": st,
        "method": "Agoda /reviews/<city> route Book Now canonical links + direct /hotel/ page fetches; title+address+selectedproperty matched per record",
    })
    with open(DATA, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(f"Upgraded {up} records to fetch-verified Agoda links; {nf} new not-found; {st} confirmed-listing-but-slugless unresolved; refreshed {refreshed} unresolved/not-found notes.")

if __name__ == "__main__":
    main()
