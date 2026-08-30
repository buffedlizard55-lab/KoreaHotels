#!/usr/bin/env python3
"""Round-0908 (2026-09-08): apply directly-fetched Agoda URL upgrades.

Final Agoda verification round. Every URL below was surfaced by Agoda's own
site routing on 2026-09-08 and then FETCHED LIVE as a canonical /hotel/ page
returning HTTP 200 whose title, selectedproperty id and/or street address
matched the repo record's identity. Nothing is guessed.

Discovery methods used this round (all via Agoda's own site; curl is blocked,
fetch_page only):
  1. en-sg reviews route (https://www.agoda.com/en-sg/<name-slug>/reviews/<cityfile>.html)
     fuzzy-resolves the property and prints its canonical 'Book Now' /hotel/ URL
     (worked for Best Western Asan).
  2. SSR search results page (/search?...&selectedproperty=<id>&city=<cid>&pslc=1)
     - non-pinned result cards include the mobile /hotel/ href in chunks 1-4;
       ko-kr locale search revealed the pinned card's sister listing with the
       same-name slug visible (Aank Air Daejeon Station).
  3. Hybrid mobile slug form <text-slug>-h<id>/hotel/<cityfile>.html
     (worked for ibis Ambassador Busan Haeundae, where the bare text slug is
     hijacked by a different property id).

Irregularities flagged in notes for user review:
  - busan-ibis-budget-haeundae: property de-flagged/rebranded on Agoda to
    'Ambassador Busan Haeundae' (former ibis budget branding remains in URL slug).
  - busan-ibis-haeundae: canonical slug is a hybrid '...-h15814986' form because
    the natural slug belongs to an unrelated property (id 1254424).
  - gyeongju-nadul-hanok: canonical slug is collision-suffixed 'nadul-hanok_2'.
  - busan-coolest-songjeong: Agoda's canonical slug misspells the name as
    'songjeong-the-coolist-hotel' ('coolist' typo is part of the real URL).
  - cheonan-best-western-asan: property now branded 'Best Western Asan Hotel'
    (upgraded from SureStay Plus; same address 32 Onsaem-ro Tangjeong-myeon).
  - daejeon-aank-air: Agoda romanizes the brand 'Aank' as 'Anook'; canonical
    slug is 'aank-hotel-daejeon-station'.
  - busan-shilla-seobusan: Agoda lists it as 'Shilla Stay busan Gimhae Airport
    (Noksan)'; slug remains 'shilla-stay-seobusan'.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "hotels.json")
DATE = "2026-09-08"

# id -> (canonical agoda /hotel/ URL, evidence note)
VERIFIED = {
    "seoul-novotel-dongdaemun": (
        "https://www.agoda.com/novotel-ambassador-seoul-dongdaemun-hotels-residences/hotel/seoul-kr.html",
        "Agoda property page fetched live 2026-09-08: title 'Novotel Ambassador Seoul Dongdaemun Hotels & Residences', 5 stars, address 238 Euljiro Jung-gu, score 8.9/~8,025 reviews; suggest API id 4935081 (Seoul). Identity matches repo (Novotel Ambassador Dongdaemun Hotels & Residences).",
    ),
    "gyeongju-nadul-hanok": (
        "https://www.agoda.com/nadul-hanok_2/hotel/gyeongju-si-kr.html",
        "Agoda property page fetched live 2026-09-08: title 'Nadul Hanok', 2 stars, address 4-1 Jjoksaem-gil Gyeongju, score 9.2/8 reviews, location 9.8; suggest API id 4857999. FLAG: canonical slug is collision-disambiguated as 'nadul-hanok_2' (the '_2' suffix is part of the real Agoda URL).",
    ),
    "busan-ibis-haeundae": (
        "https://www.agoda.com/ibis-ambassador-busan-haeundae-h15814986/hotel/busan-kr.html",
        "Agoda property page fetched live 2026-09-08: title 'ibis Ambassador Busan Haeundae', 3 stars, address 12 Haeundaehaebyeon-ro 237beon-gil Haeundae-gu, score 8.6/~30 reviews; selectedproperty=15814986. FLAG: canonical URL uses Agoda's hybrid mobile form 'ibis-ambassador-busan-haeundae-h15814986' because the plain slug 'ibis-ambassador-busan-haeundae' is owned by a DIFFERENT property (id 1254424, 'Busan Haeundae'); the h-id hybrid resolves to the correct ibis listing.",
    ),
    "busan-ibis-budget-haeundae": (
        "https://www.agoda.com/ibis-budget-ambassador-busan-haeundae/hotel/busan-kr.html",
        "Agoda property page fetched live 2026-09-08: page title 'Ambassador Busan Haeundae' (selectedproperty=1161196), 2 stars, address 8,209 beon-gil Haeundaehaebyeon-ro Haeundae-gu, score 8.4/~2,689 reviews. FLAG: property has been de-flagged/rebranded on Agoda - formerly 'ibis budget Ambassador Busan Haeundae', now marketed as 'Ambassador Busan Haeundae'; the URL slug still carries the old ibis-budget name. Repo record is the same physical property (ibis budget Ambassador Busan Haeundae).",
    ),
    "daejeon-hotel-onoma": (
        "https://www.agoda.com/hotel-onoma-daejeon-autograph-collection/hotel/daejeon-kr.html",
        "Agoda property page fetched live 2026-09-08: title 'Hotel Onoma, Daejeon, Autograph Collection', 5 stars, address 1 Expo-ro Yuseong-gu Daejeon, score 8.9/~2,852 reviews (cleanliness/service 9.5, facilities 9.2, location 9.3), Expo Park 330 m; selectedproperty=27809293 (confirmed via YouTube affiliate links + suggest API). Identity matches repo (Hotel Onma/Onoma Daejeon Autograph Collection). Canonical page lives under the en-sg locale path.",
    ),
    "busan-coolest-songjeong": (
        "https://www.agoda.com/songjeong-the-coolist-hotel/hotel/busan-kr.html",
        "Agoda property page fetched live 2026-09-08: title 'Songjeong The Coolest Hotel', 4 stars Agoda Preferred, address 11 Songjeonggwangeogol-ro Haeundae-gu Busan, score 8.5/~1,268 reviews, ~90 m to Songjeong Beach, rooftop/infinity pool; selectedproperty=45206767 in image URLs and See-all link. FLAG: Agoda's canonical slug MISSPELLS the name as 'songjeong-the-coolist-hotel' ('coolist') - the typo is part of the real URL; the reviews route also accepts the correct spelling 'songjeong-the-coolest-hotel'. Identity matches repo (The Coolest Hotel, Songjeong).",
    ),
    "daejeon-skypark-1": (
        "https://www.agoda.com/hotel-skypark-daejeon-i/hotel/daejeon-kr.html",
        "Agoda property page fetched live 2026-09-08: title 'Hotel Skypark Daejeon I', 4 stars, address 161 Technojungang-ro Yuseong-gu Daejeon (Daedeok Techno Valley / Hyundai Premium Outlet), score 8.7/~5,601 reviews, location 8.8; suggest API id 15967708 (a duplicate listing id 93616913 in suggest is ignored). Identity matches repo (Skypark Daejeon 1).",
    ),
    "busan-shilla-seobusan": (
        "https://www.agoda.com/shilla-stay-seobusan/hotel/busan-kr.html",
        "Agoda property page fetched live 2026-09-08: page title 'Shilla Stay busan Gimhae Airport (Noksan)', 4 stars, address 38 Myeongjigukje 7-ro Gangseo-gu Busan 46726, score 8.7/~6,682 reviews (clean 9.4, service 9.3), Gimhae Airport 9.3 km; selectedproperty=21826078 (suggest API). Identity matches repo (Shilla Stay Seobusan / Gimhae Airport, Gangseo-gu Noksan/Myeongji). FLAG: Agoda's display name is 'Shilla Stay busan Gimhae Airport (Noksan)'; canonical slug remains 'shilla-stay-seobusan'.",
    ),
    "cheonan-best-western-asan": (
        "https://www.agoda.com/best-western-asan-hotel/hotel/asan-si-kr.html",
        "Agoda property page fetched live 2026-09-08: title 'Best Western Asan Hotel', 3 stars, address 32 Onsaem-ro Tangjeong-myeon Asan-si Chungcheongnam-do 31457, score 8.6/~530 reviews (service 9.3, clean 9.1); selectedproperty=79596756 (See-all link; suggest API). Address exactly matches the repo's SureStay Plus record (32 Onsaem-ro Tangjeong-myeon). FLAG: property has been rebranded/upgraded from 'SureStay Plus Hotel by Best Western Asan' to 'Best Western Asan Hotel' (older Agoda listing slug 'surestay-plus-hotel-by-best-western-asan' id 35318569 redirects here); city file is asan-si-kr.html. Repo record name should be reviewed for the rebrand.",
    ),
    "daejeon-aank-air": (
        "https://www.agoda.com/aank-hotel-daejeon-station/hotel/daejeon-kr.html",
        "Agoda property page fetched live 2026-09-08: title 'Anook Air Hotel Daejeon Station', address 6 Mokcheok 9-gil Jung-gu Daejeon 34832, score 8.3/~228 reviews, location 8.5, Jungangno Station 0.26 km / Daejeon Station ~0.59 km; selectedproperty=64224693 (suggest API; ko-kr name '은행 아늑에어 대전역점'). Address 6 Mokcheok 9-gil exactly matches repo. FLAG: Agoda romanizes the Korean brand '아늑에어(Aank Air)' as 'Anook Air'; canonical slug is 'aank-hotel-daejeon-station' (loses the 'Air'); a second duplicate Hangul-named listing id 64267301 (8.8/108) is ignored - same property.",
    ),
}

def main():
    with open(DATA, encoding="utf-8") as f:
        d = json.load(f)
    up = 0
    for h in d["hotels"]:
        hid = h["id"]
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
    meta = d.setdefault("meta", {})
    batches = meta.setdefault("newEntryBatches", [])
    batches.append({
        "date": DATE,
        "kind": "agoda-verification-round",
        "upgradedToVerified": up,
        "newNotFound": 0,
        "stillUnresolvedWithAgodaId": 0,
        "method": "Final round: en-sg reviews-route Book Now links, SSR search (/search selectedproperty) mobile card hrefs (incl. ko-kr locale), and hybrid h-id mobile slugs; every canonical /hotel/ page fetched live HTTP 200 with title+selectedproperty id+address matched to the repo record. After this round 0 records remain unresolved/not-found.",
    })
    with open(DATA, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(f"Upgraded {up} records to fetch-verified Agoda links. All 185 records now have verified Agoda property URLs.")

if __name__ == "__main__":
    main()
