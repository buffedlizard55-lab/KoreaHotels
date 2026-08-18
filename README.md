# 🇰🇷 South Korea Hotel Shortlist

A small, static hotel planner for choosing stays in **Seoul, Gyeongju, and Busan** (with Cheonan and Daejeon alternatives). It is designed to make the decision readable instead of burying it in a spreadsheet.

## Start here: the first night is handled differently

The flight is scheduled to reach **Incheon International Airport (ICN) at 21:00**. For the **first booked night only**, the site shows a separate shortlist with a currently listed **24-hour staffed front desk / reception**.

### Recommended first night

**Somerset Palace Seoul — Studio Executive**

- Central palace / Insadong area, about three minutes from Anguk Station
- One queen bed, private bathroom, kitchen, and in-room washer/dryer
- The **official Somerset / Ascott property page lists 24-hour reception**
- Strongest combination of an official reception source, the preferred bed, useful long-stay facilities, and a central Seoul base

The first screen now compares five source-checked options:

1. **Somerset Palace Seoul** — strongest direct official evidence and the top recommendation.
2. **L7 MYEONGDONG by LOTTE** — preferred Myeongdong room/location; 24-hour evidence is on a major trusted property listing.
3. **ibis Ambassador Seoul Myeongdong** — government tourism authority confirms 24-hour reception, but the cited room is a smaller double.
4. **Nine Tree by Parnas Seoul Myeongdong 1** — value-oriented queen-room alternative with trusted listing evidence.
5. **Grand Hyatt Incheon** — airport-area fallback when avoiding a late city transfer is more important than waking up in Seoul.

> A 24-hour desk does not mean the hotel can safely assume an unannounced no-show. Book the date you land, send your flight number, and get written confirmation that a possible after-midnight arrival will be held. The site has a one-click message you can copy for this.

Read the source links, trade-offs, and exact booking workflow in [`guide/arrival-night.md`](guide/arrival-night.md).

---

## What the website does

Open [`index.html`](index.html) in a browser to use the planner. The top of the page is a **verified findings dashboard** (coverage table, charts, recommendations, and sample price totals) built only from UTC-stamped quotes. It is intentionally simple:

- **Arrival night** — five source-checked late-arrival options, evidence links, trade-offs, and a copyable message to send the hotel.
- **Expanded city lists** — browse 30 Seoul, 15 Gyeongju, 20 Busan, 7 Cheonan, 7 Daejeon, and 5 Suwon hotels.
- **Quick filters** — view all stays, only core-needs matches, or stays with laundry; search within the current city.
- **Useful details at a glance** — estimated nightly range, recommended room, bed setup, bathroom/transport fit, normal check-in/out time, canonical identity source, and rate-comparison link.
- **Timestamped refundable pricing** — hotel cards show a ♻️ badge with the captured refundable rate, cancellation deadline, and UTC capture time; the append-only log lives in [`data/pricing-history.json`](data/pricing-history.json). The four-city (Suwon / Gyeongju / Cheonan / Daejeon) 2026-08-18T19:16Z checklist is [`guide/verification-suwon-gyeongju-cheonan-daejeon-2026-08-18.md`](guide/verification-suwon-gyeongju-cheonan-daejeon-2026-08-18.md). The earlier same-day Seoul-inclusive pass is [`guide/verification-checklist-2026-08-18-line-by-line.md`](guide/verification-checklist-2026-08-18-line-by-line.md).
- **Duplicate protection** — all 84 records are source verified; similarly named branches are cross-checked as distinct properties.

There is no account, tracker, or backend. It is a static planning document that can be hosted with GitHub Pages or opened locally.

---

## Core room requirements

For regular stays, a green **“Core needs match”** badge means the research has a room suitable for two people with:

| Requirement | Meaning |
|---|---|
| **One bed** | A single queen or king bed (approximately 150 cm wide or greater), not two beds pushed together |
| **Private bathroom** | An en-suite bathroom in the room |
| **Transport access** | Walkable subway or KTX access where that is practical |

**Gyeongju is the planned-route exception:** Singyeongju KTX station is outside the Old Town/Bomun hotel districts, so no realistic central Gyeongju hotel is walkable to rail. The audited Cheonan/Daejeon alternatives are also conservatively unmarked until both exact queen/king width and walkable rail access are established.

---

## Current coverage

| City | Hotels | Planning use |
|---|---:|---|
| Seoul | 30 | Five-option first-night shortlist + Myeongdong and palace-area bases |
| Gyeongju | 15 | Heritage / hanok, Old Town, Bulguksa, and Bomun Lake stays |
| Busan | 20 | Haeundae, Seomyeon, Busan Station, Nampo, and Songdo options |
| Cheonan | 7 | KTX-corridor alternative |
| Daejeon | 7 | KTX-corridor alternative |
| Suwon | 5 | Seoul-area base (Suwon Station + Hwaseong Fortress) |
| **Planned cities** | **65** | Seoul + Gyeongju + Busan |
| **Total** | **84** | Full city-by-city comparison set |

Prices are planning estimates for the 2026 autumn itinerary, not live inventory. Always verify a live rate and exact room configuration before paying.

---

## Run it locally

No package install is needed.

```bash
# check the hotel, arrival-night, and itinerary data
python3 validate.py

# regenerate index.html after editing the data or template
python3 build.py

# optional: open it through a local static server
python3 -m http.server 8000
```

Then visit `http://localhost:8000` in a local browser, or open `index.html` directly.

---

## Project structure

```text
├── index.template.html     # Site shell; data is embedded at build time
├── index.html              # Generated static planner
├── data/
│   ├── hotels.json         # 84 city hotels + five-option arrivalNight shortlist and source links
│   └── itinerary.json      # Dates, city order, and alternatives
├── guide/
│   ├── arrival-night.md    # 24-hour reception research + late-arrival workflow
│   ├── verification-audit.md # Canonical identity and duplicate audit for all 74 records
│   ├── seoul.md            # City notes
│   ├── gyeongju.md
│   ├── busan.md
│   └── ...
├── build.py                # Rebuilds index.html
└── validate.py             # Protects data quality and arrival-night evidence fields
```

`data/hotels.json` is the source of truth for the page. The `arrivalNight` block is deliberately separate from the normal hotel list because the 24-hour-reception rule applies to **night one only**.

---

## Research and booking guardrails

- Arrival-night evidence and **all 74 hotel records** were identity-checked (Seoul/Gyeongju/Busan/Cheonan/Daejeon on August 10, 2026; the Suwon shortlist on August 18, 2026). Every card shows a canonical property source, source type, date, and verification note. The validator rejects duplicate IDs, sourced names, official URLs, identity-source URLs, and exact coordinates; similar branch names require an explicit distinct-property cross-check.
- No duplicate hotel entries remain. Five independent hotels without a stable official page are retained only because a government-tourism or major trusted booking source confirms the exact property and address. See [`guide/verification-audit.md`](guide/verification-audit.md).
- A 24-hour front desk covers the **hotel-arrival** risk, not the **airport-transfer** risk. Check live public-transport / shuttle timing on the day; take a taxi when the final connection is tight.
- Use the exact recommended room type. A property may list a lower-priced twin or smaller double that does not meet the one-queen/king preference.
- Use official booking sites where possible, then cross-check a reputable OTA for the current total and cancellation terms.

## Updating the planner

1. Edit `data/hotels.json` or `data/itinerary.json`.
2. Preserve each hotel's `verification.canonicalName`, `existenceStatus`, unique `sourceUrl`, source description, and (for arrival candidates) reception evidence.
3. Run `python3 validate.py`; duplicate identity checks are automatic.
4. Run `python3 build.py`.
5. Review the generated `index.html` before publishing.
