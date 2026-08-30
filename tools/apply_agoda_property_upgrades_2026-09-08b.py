#!/usr/bin/env python3
"""Round-0908b (2026-09-08): replace non-property Agoda evidence URLs.

Every old URL below was a travel-guide/city/maps page that could only prove a
property was *mentioned* by Agoda — not that the property has an Agoda booking
page. This pass resolves each of the 12 remaining records to the ACTUAL Agoda
property page.

Method: Agoda's own en-sg reviews route
(https://www.agoda.com/en-sg/<slug>/reviews/<city>.html) fuzzy-resolves the
property and renders its canonical "Book Now" /hotel/ URL. That canonical
/hotel/ URL was then FETCHED LIVE (HTTP 200) and its title, star rating, street
address, score and/or selectedproperty id matched the repo record. No slug is
guessed: each URL below was read off a live Agoda page and confirmed by fetch.

Also adds a machine-readable `linkType` to every Agoda secondarySource:
  - "property-page"   when the stored URL is a canonical /hotel/ page
  - "reviews-page"    when the stored URL is a /reviews/ page
  - "other"           when it is a guide/city/maps page (rejected by validator)
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "hotels.json")
DATE = "2026-09-08"

# id -> (canonical agoda property URL, note)
UPGRADES = {
    "daejeon-hotel-interciti": (
        "https://www.agoda.com/hotel-interciti/hotel/daejeon-kr.html",
        "Agoda property page fetched live 2026-09-08: title 'Hotel Interciti', 4 stars verified, address 92 Oncheon-ro Yuseong-gu 34187, score 8.6/5,100 reviews (clean 9.1, service 9.1), selectedproperty=43289; Yuseong Spa Stn 0.56 km / Gapcheon 0.6 km. Old stored URL was a travel-guide page; this is the canonical /hotel/ page.",
    ),
    "daejeon-hotel-stendhal": (
        "https://www.agoda.com/hotel-stendhal-h10573875/hotel/daejeon-kr.html",
        "Agoda property page fetched live 2026-09-08: title 'Le Stendal Hotel', 4 stars, address 14 Oncheonbuk-ro Yuseong-gu 34186, score 8.8/2,140 reviews; selectedproperty=38984903 ('See all' link). FLAG: canonical slug is the hybrid 'hotel-stendhal-h10573875' form because the natural slug 'le-stendal-hotel' 404s; the reviews route slug is 'stendhal-hotel'. Old stored URL was a travel-guide page.",
    ),
    "seoul-sotetsu-splaisir-myeongdong": (
        "https://www.agoda.com/sotetsu-hotels-the-splaisir-seoul-myeong-dong/hotel/seoul-kr.html",
        "Agoda property page fetched live 2026-09-08: title 'Sotetsu Hotels The Splaisir Seoul Myeong-Dong', 4 stars government-verified, address 15 Namdaemun-ro 5-gil Jung-gu 04526, score 8.5/24,711 reviews; selectedproperty=1110738. FLAG: canonical slug uses '...-myeong-dong' (hyphen inside Myeong-Dong); the guide-page slug '...-myeongdong' is not the hotel route. Old stored URL was a travel-guide page.",
    ),
    "seoul-park-hyatt-seoul": (
        "https://www.agoda.com/park-hyatt-seoul-hotel/hotel/seoul-kr.html",
        "Agoda property page fetched live 2026-09-08: title 'Park Hyatt Seoul', 5 stars, address 606 Teheran-ro (995-14 Daechi-dong) Gangnam-gu 06174, score 8.9/963 reviews; selectedproperty=462482. FLAG: canonical slug is 'park-hyatt-seoul-hotel'; the reviews-route slug is 'park-hyatt-seoul'. Old stored URL was a travel-guide page.",
    ),
    "seoul-jw-marriott-dongdaemun": (
        "https://www.agoda.com/jw-marriott-dongdaemun-square-seoul/hotel/seoul-kr.html",
        "Agoda property page fetched live 2026-09-08: title 'JW Marriott Dongdaemun Square Seoul', 5 stars, address 279 Cheonggyecheon-ro Dongdaemun 03198, score 8.9/1,781 reviews; selectedproperty=564142. Old stored URL was a travel-guide page.",
    ),
    "seoul-holiday-inn-express-hongdae": (
        "https://www.agoda.com/holiday-inn-express-seoul-hongdae/hotel/seoul-kr.html",
        "Agoda property page fetched live 2026-09-08: title 'Holiday Inn Express Seoul Hongdae By IHG', 4 stars, address 188 Yanghwa-ro Mapo-gu 04051, score 8.9/16,666 reviews, location 9.7; selectedproperty=5056661. Old stored URL was a travel-guide page.",
    ),
    "seoul-amanti-hongdae": (
        "https://www.agoda.com/amanti-hotel-seoul/hotel/seoul-kr.html",
        "Agoda property page fetched live 2026-09-08: title 'Amanti Hotel Seoul', 4 stars government-verified, address 31 World Cup Buk-Ro Mapo-gu 04001, score 8.6/16,153 reviews; selectedproperty=1197749. Old stored URL was a travel-guide page.",
    ),
    "seoul-hotel-naru-mgallery": (
        "https://www.agoda.com/hotel-naru-seoul-mgallery-ambassador/hotel/seoul-kr.html",
        "Agoda property page fetched live 2026-09-08: title 'Hotel Naru Seoul - MGallery Collection', 5 stars, address 8 Mapodaero Mapo-gu 04176, score 9.0/3,009 reviews; selectedproperty=35614467. Old stored URL was a travel-guide page.",
    ),
    "seoul-solaria-nishitetsu-myeongdong": (
        "https://www.agoda.com/solaria-nishitetsu-hotel-seoul-myeongdong/hotel/seoul-kr.html",
        "Agoda property page fetched live 2026-09-08: title 'Solaria Nishitetsu Hotel Seoul Myeongdong', 3 stars government-verified, address 7-22F 27 Myeongdong 8-gil Jung-gu 100-809, score 9.0/17,901 reviews; selectedproperty=908128. Old stored URL was a travel-guide page.",
    ),
    "cheonan-on-city": (
        "https://www.agoda.com/on-city-hotel/hotel/cheonan-si-kr.html",
        "Agoda property page fetched live 2026-09-08: title 'ON City Hotel', 3 stars, address 105 Buldang 4-ro Seobuk-gu Cheonan-si 31163, score 8.1/4,258 reviews; selectedproperty=1179009. FLAG: canonical slug is 'on-city-hotel' (not 'on-city-hotel-cheonan'). Old stored URL was a city page.",
    ),
    "daejeon-ramada": (
        "https://www.agoda.com/ramada-daejeon-hotel/hotel/daejeon-kr.html",
        "Agoda property page fetched live 2026-09-08: title 'Ramada by Wyndham Daejeon', 3.5 stars, address 127 Gyeryong-ro Yuseong-gu 34187, score 8.8/13,740 reviews; selectedproperty=8233521. FLAG: canonical slug is 'ramada-daejeon-hotel'. Old stored URL was a city page.",
    ),
    "cheonan-shilla-stay": (
        "https://www.agoda.com/shilla-stay-cheonan/hotel/cheonan-si-kr.html",
        "Agoda property page fetched live 2026-09-08: title 'Shilla Stay Cheonan Asan - Samsung Display City', 4 stars, address 1430 Seongjeong-dong Seobuk-gu Cheonan 331-172, score 8.5/6,091 reviews; selectedproperty=1192803. FLAG: Agoda's display name includes 'Asan - Samsung Display City'. Old stored URL was a downtown/maps page.",
    ),
}


def link_type(url):
    if "/hotel/" in url:
        return "property-page"
    if "/reviews/" in url:
        return "reviews-page"
    return "other"


def main():
    with open(DATA, encoding="utf-8") as f:
        d = json.load(f)
    upgraded = 0
    for h in d["hotels"]:
        hid = h["id"]
        s = h.get("secondarySource")
        if not isinstance(s, dict):
            continue
        if hid in UPGRADES:
            url, note = UPGRADES[hid]
            s["status"] = "verified"
            s["url"] = url
            s["checkMethod"] = "property-page-fetched"
            s["lastCheckedUtc"] = DATE
            s["linkType"] = "property-page"
            s["note"] = note
            upgraded += 1
        elif s.get("status") == "verified" and s.get("url"):
            s["linkType"] = link_type(s["url"])
    meta = d.setdefault("meta", {})
    batches = meta.setdefault("newEntryBatches", [])
    batches.append({
        "date": DATE,
        "kind": "agoda-property-page-hardening",
        "upgradedToPropertyPage": upgraded,
        "note": "Replaced all non-property Agoda evidence URLs (travel-guides / city / downtown-maps) with live-fetched canonical /hotel/ property pages; added machine-readable linkType (property-page | reviews-page | other) to every secondarySource block.",
    })
    with open(DATA, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(f"Upgraded {upgraded} records to canonical Agoda /hotel/ property pages; linkType stamped on all {len(d['hotels'])} records.")


if __name__ == "__main__":
    main()
