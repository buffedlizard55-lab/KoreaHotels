# Agoda property-page hardening round — 2026-09-08

**Scope:** the 12 records whose `secondarySource` pointed at an Agoda **guide / city / maps** page instead of a real Agoda property page. A guide/city/maps page only proves Agoda *mentions* a hotel; it cannot be used as the hotel's secondary verified source. This round replaces each one with the actual Agoda `/hotel/` property page.

**Method (no guessing):** Agoda's own en-sg reviews route
(`https://www.agoda.com/en-sg/<slug>/reviews/<city>.html`) fuzzy-resolves a property and renders its canonical **"Book Now" `/hotel/` URL**. That canonical URL was then **fetched live** (HTTP 200) and its title, star rating, street address, score and/or `selectedproperty` id were compared to the repo record. Each URL below was read off a live Agoda page and confirmed by fetch.

Manual review recipe for one line:
1. Open the new **Agoda `/hotel/` link**.
2. Confirm the displayed property name and street address match the hotel record.
3. Record any disagreement as a flag — do not silently overwrite.

> Irregularities found in this round are kept as `FLAG:` notes in `data/hotels.json` (e.g. hybrid `-h<id>` slugs, slug spelling differences, and Agoda display names that include a second brand/branch word).

| id | Hotel | Old stored URL (type) | New Agoda property page | Evidence matched on fetch |
|---|---|---|---|---|
| `daejeon-hotel-interciti` | Hotel Interciti | travel-guide | [property page](https://www.agoda.com/hotel-interciti/hotel/daejeon-kr.html) | title `Hotel Interciti` · 92 Oncheon-ro, Yuseong-gu 34187 · 8.6/5,100 · selectedproperty=43289 |
| `daejeon-hotel-stendhal` | Le Stendal Hotel | travel-guide | [property page](https://www.agoda.com/hotel-stendhal-h10573875/hotel/daejeon-kr.html) | title `Le Stendal Hotel` · 14 Oncheonbuk-ro, Yuseong-gu 34186 · 8.8/2,140 · selectedproperty=38984903 · **FLAG: hybrid slug** (`hotel-stendhal-h10573875`) because `le-stendal-hotel` 404s |
| `seoul-sotetsu-splaisir-myeongdong` | Sotetsu Hotels The Splaisir Seoul Myeongdong | travel-guide | [property page](https://www.agoda.com/sotetsu-hotels-the-splaisir-seoul-myeong-dong/hotel/seoul-kr.html) | title `Sotetsu Hotels The Splaisir Seoul Myeong-Dong` · 15 Namdaemun-ro 5-gil, Jung-gu 04526 · 8.5/24,711 · selectedproperty=1110738 · **FLAG: slug uses `...-myeong-dong`** |
| `seoul-park-hyatt-seoul` | Park Hyatt Seoul | travel-guide | [property page](https://www.agoda.com/park-hyatt-seoul-hotel/hotel/seoul-kr.html) | title `Park Hyatt Seoul` · 606 Teheran-ro, Gangnam-gu 06174 · 8.9/963 · selectedproperty=462482 · **FLAG: slug is `park-hyatt-seoul-hotel`**, reviews-route slug is `park-hyatt-seoul` |
| `seoul-jw-marriott-dongdaemun` | JW Marriott Dongdaemun Square Seoul | travel-guide | [property page](https://www.agoda.com/jw-marriott-dongdaemun-square-seoul/hotel/seoul-kr.html) | title `JW Marriott Dongdaemun Square Seoul` · 279 Cheonggyecheon-ro, Dongdaemun 03198 · 8.9/1,781 · selectedproperty=564142 |
| `seoul-holiday-inn-express-hongdae` | Holiday Inn Express Seoul Hongdae by IHG | travel-guide | [property page](https://www.agoda.com/holiday-inn-express-seoul-hongdae/hotel/seoul-kr.html) | title `Holiday Inn Express Seoul Hongdae By IHG` · 188 Yanghwa-ro, Mapo-gu 04051 · 8.9/16,666 · selectedproperty=5056661 |
| `seoul-amanti-hongdae` | Amanti Hotel Seoul Hongdae | travel-guide | [property page](https://www.agoda.com/amanti-hotel-seoul/hotel/seoul-kr.html) | title `Amanti Hotel Seoul` · 31 World Cup Buk-Ro, Mapo-gu 04001 · 8.6/16,153 · selectedproperty=1197749 |
| `seoul-hotel-naru-mgallery` | Hotel Naru Seoul - MGallery Collection | travel-guide | [property page](https://www.agoda.com/hotel-naru-seoul-mgallery-ambassador/hotel/seoul-kr.html) | title `Hotel Naru Seoul - MGallery Collection` · 8 Mapodaero, Mapo-gu 04176 · 9.0/3,009 · selectedproperty=35614467 |
| `seoul-solaria-nishitetsu-myeongdong` | Solaria Nishitetsu Hotel Seoul Myeongdong | travel-guide | [property page](https://www.agoda.com/solaria-nishitetsu-hotel-seoul-myeongdong/hotel/seoul-kr.html) | title `Solaria Nishitetsu Hotel Seoul Myeongdong` · 7-22F 27 Myeongdong 8-gil, Jung-gu 100-809 · 9.0/17,901 · selectedproperty=908128 |
| `cheonan-on-city` | ON City Hotel | city | [property page](https://www.agoda.com/on-city-hotel/hotel/cheonan-si-kr.html) | title `ON City Hotel` · 105 Buldang 4-ro, Seobuk-gu, Cheonan-si 31163 · 8.1/4,258 · selectedproperty=1179009 · **FLAG: slug is `on-city-hotel`**, not `on-city-hotel-cheonan` |
| `daejeon-ramada` | Ramada by Wyndham Daejeon | city | [property page](https://www.agoda.com/ramada-daejeon-hotel/hotel/daejeon-kr.html) | title `Ramada by Wyndham Daejeon` · 127 Gyeryong-ro, Yuseong-gu 34187 · 8.8/13,740 · selectedproperty=8233521 · **FLAG: slug is `ramada-daejeon-hotel`** |
| `cheonan-shilla-stay` | Shilla Stay Cheonan | downtown-maps | [property page](https://www.agoda.com/shilla-stay-cheonan/hotel/cheonan-si-kr.html) | title `Shilla Stay Cheonan Asan - Samsung Display City` · 1430 Seongjeong-dong, Seobuk-gu 331-172 · 8.5/6,091 · selectedproperty=1192803 · **FLAG: Agoda display name includes `Asan - Samsung Display City`** |

## Result

- Agoda secondary sources: **185 verified**, all now an Agoda URL.
- Page types: **150 canonical `/hotel/` property pages**, **35 `/reviews/` property-reviews pages** (each still Agoda's own page for the exact property; those 35 carry the `⚑ agoda-reviews-route` flag in the checklist).
- **0** guide / city / maps URLs remain — the `other` page type is now rejected by `validate.py`.
- `linkType` (`property-page` / `reviews-page`) is stamped on every `secondarySource` block so the frontend and checklist can label each Agoda link by what it opens.
