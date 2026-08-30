# Data Schema — KoreaHotels

This document describes the two source files used to build the static planner:

- `data/hotels.json` — trip context, the normal city-hotel list, and the special late-arrival shortlist
- `data/itinerary.json` — dates, planned legs, and alternative cities

Run `python3 validate.py` after changing either file, then run `python3 build.py` to regenerate `index.html`.

---

## `hotels.json`

### Top-level structure

```json
{
  "trip": { "...": "..." },
  "split": { "...": "..." },
  "hotels": [ { "...": "..." } ],
  "meta": { "...": "..." },
  "arrivalNight": { "...": "..." }
}
```

### `trip`

| Field | Purpose |
|---|---|
| `title` | Display title for the trip |
| `checkIn`, `checkOut`, `nights` | Overall itinerary dates and number of nights |
| `note` | Season / pricing context |

### `split`

| Field | Purpose |
|---|---|
| `recommended` | Default city-night split |
| `rationale` | Why that split is suggested |
| `alternatives` | Other possible splits |

### `hotels[]`

Each standard hotel record is shown in the city shortlist.

#### Required core fields

- `id`: unique slug, such as `seoul-l7-myeongdong`
- `city`: city name (currently Seoul, Gyeongju, Busan, Cheonan, or Daejeon)
- `name`: full property name
- `tier`: `budget`, `mid`, or `premium`
- `stars`: numeric star rating
- `area`, `neighborhood`: readable location descriptions
- `priceFrom`, `priceTo`, `currency`: planning price range
- `checkIn`, `checkOut`, `policies`
- `rooms`, `promos`, `amenities`, `hasOnSiteLaundry`
- `officialLabel`, `compareUrl`, `compareLabel`
- `why`, `highlights`, `fits`, `fitReason`, `lat`, `lng`

`officialUrl` may be `null` only where a reliable official booking page is not available.

#### `verification` (every hotel entry)

All 69 records carry an auditable property-identity block:

```json
{
  "lastChecked": "2026-08-10",
  "sourceType": "Official hotel/brand",
  "sourceUrl": "https://official.example/property",
  "canonicalName": "Official Property Name",
  "existenceStatus": "Verified operating property",
  "note": "What the linked identity source confirms"
}
```

`sourceUrl` must identify that exact hotel through an official property/brand page, a government tourism authority, or a major trusted booking platform. It must be unique across the dataset. A `distinctFrom` array is required when two legitimate branches have highly similar canonical names. The website shows the status, source, date, and note on every card.

#### `secondarySource` (Agoda — the second official verified source)

Every record must state, explicitly, where the same property stands on Agoda. A blank is never acceptable as a *silently omitted* check; `validate.py` fails records without the block so the un-checked backlog stays visible as a queue.

```json
"secondarySource": {
  "platform": "Agoda",
  "status": "verified",
  "url": "https://www.agoda.com/signiel-seoul/hotel/seoul-kr.html",
  "lastCheckedUtc": "2026-08-30",
  "checkMethod": "search-index",
  "linkType": "property-page",
  "note": "How the page was located, what matched (address/score), and any caveat."
}
```

- `status: "verified"` — an `https://www.agoda.com/` property or reviews page was located and its indexed copy corroborates the same identity (address/score). URLs must be unique across records. `linkType` is machine-readable and must be `"property-page"` (canonical `/hotel/` page) or `"reviews-page"` (`/reviews/` page); a `travel-guides`, `city`, or `maps` URL is rejected as `"other"` because those pages only prove the property was *mentioned* by Agoda, not that it has an Agoda booking page. `checkMethod` records how: `"property-page-fetched"` (the page itself was read) or `"search-index"` (its own snippet in search results — weaker; the audit emits a CHECK telling you to fetch and harden it). Locale-prefixed URLs (`/en-gb/…`) may be stored canonicalized **only** with a note saying so.
- `status: "not-found"` — an index search was run on `lastCheckedUtc` and no Agoda page surfaced. **This is a recorded result, not a claim the property is absent from Agoda**; the note must keep that framing. No URL field.
- `status: "unresolved"` — an Agoda listing is *known to exist* (aggregator deal lines or provider scores cite it) but no URL could be surfaced. No URL, dated note, and the audit emits a CHECK for manual lookup. Never upgrade to `verified` by guessing a slug — guessed Agoda URLs 404 and that mistake is unrecoverable in a trusted dataset.
- Rate rows: `refundableRate*` / `refundableRateNov9` / `refundableRateNov15` `source` strings must name exactly one platform (Booking.com or Agoda) so a labeled rate can never be attributed to the wrong site. Agoda-sourced prices need the same dated evidence standard as Booking ones; while no dated page can be fetched, records carry no priced rows at all plus a `distributionStatus` explaining the blank.

#### `rooms[]`

Each room needs:

```json
{
  "name": "Deluxe Double",
  "price": "$150–185/night",
  "note": "Short room note",
  "bed": "queen",
  "bedType": "queen",
  "bedSize": "Queen (approx 150x200cm)",
  "oneBed": true,
  "oneBedOnly": true,
  "privateBathroom": true,
  "bedNote": "Single queen bed (not two beds pushed together)"
}
```

The frontend chooses the first one-bed, private-bath queen/king room as the **“Best room to compare.”** It falls back to another one-bed private-bath room only when no queen/king option is recorded.

#### Core-needs fields

- `fits`: `true` only when the planner has verified a suitable one-bed room for two, a private bathroom, and practical walkable rail/subway access.
- `fitReason`: concise reason shown in older guide data.
- `stationWalkTime`: optional readable station distance used in the new cards.

Do not mark a property `fits: true` solely because it has a 24-hour desk; the arrival-night criterion is separate.

### `arrivalNight`

`arrivalNight` is a special block because its rules apply only to the first booked night after the late ICN arrival. It is embedded into the built page alongside the normal hotels.

#### Required block fields

```json
{
  "title": "First night in Seoul — late-arrival shortlist",
  "airport": "Incheon International Airport (ICN)",
  "arrivalTime": "21:00",
  "arrivalCity": "Seoul",
  "firstNightOnly": true,
  "lastVerified": "2026-08-10",
  "requirement": "...",
  "definition": "...",
  "recommendedId": "seoul-l7-myeongdong",
  "decision": { "recommended": "...", "why": "...", "airportFallback": "..." },
  "steps": [ { "title": "...", "body": "..." } ],
  "candidates": [ { "...": "..." } ]
}
```

#### `arrivalNight.candidates[]`

Each candidate must include:

| Field | Purpose |
|---|---|
| `id`, `rank`, `label` | Stable identifier and display order |
| `hotelId` | Optional link to an item in `hotels[]`; use `null` for an airport-only fallback not in the general hotel list |
| `location`, `tier`, `checkIn`, `checkOut` | Plain-language comparison fields |
| `frontDesk` | The specific 24-hour / anytime evidence signal; do not make an unsourced claim here |
| `room`, `privateBathroom`, `station`, `estimatedRate` | Booking / transport comparison fields |
| `why`, `tradeoff`, `bookingNote` | Human decision guidance |
| `officialUrl` | Where to book directly |
| `evidenceType` | `Official hotel/brand page`, `Government tourism authority`, `Major trusted booking platform`, or the allowed official + platform combination |
| `evidenceUrl`, `evidenceLabel`, `evidenceQuote` | Auditable source for the late-arrival claim |

The validator requires an HTTP(S) official-booking link, evidence link, accepted evidence type, and unique rank for every arrival candidate. The recommended candidate must use direct official hotel/brand evidence. Keep `lastVerified` current whenever the evidence is rechecked.

**Important:** `frontDesk` means the property currently shows a 24-hour staffed reception or an equivalent late-check-in signal. It must never be represented as a guarantee that an unannounced post-midnight reservation will be retained. The `definition`, `steps`, and `bookingNote` should always tell the traveler to notify the hotel.

### `meta`

- `pricingLastChecked`: pricing-research date
- `pricingSource`: note about price research

---

## `itinerary.json`

### `trip`

- `name`, `checkIn`, `checkOut`, `note`

### `legs[]`

Each planned leg uses:

- `city`, `nights`, `dates`
- `locations`: area ideas
- `hotelChoice`: `null` or a hotel ID
- `note`: transit / city caveat

### `alternatives[]`

Optional alternative legs use the same structure. The UI shows them as **Alternative stop** rather than silently mixing them with the primary route.

---

## Validation rules

`validate.py` checks:

- standard hotels have all required fields, unique IDs, and room detail fields
- all rooms include `bedType`, `oneBedOnly`, and `privateBathroom`
- every hotel has a complete, dated `verification` block and `Verified operating property` status
- every hotel has a `secondarySource` block for Agoda with a valid status (`verified` / `not-found` / `unresolved`); verified entries need a unique `agoda.com` URL whose path is a `property-page` (`/hotel/`) or `reviews-page` (`/reviews/`) and a matching `linkType`, the other two statuses must carry **no** URL plus a dated note; rate-row `source` strings must name exactly one platform
- canonical names are unique within a city
- official URLs and exact-property verification URLs are not reused by another hotel
- exact coordinates are not duplicated
- highly similar same-city names are rejected unless both records explicitly cross-reference each other as distinct branches
- the expanded primary-city baseline remains at least 20 Seoul, 15 Gyeongju, and 20 Busan records
- the `arrivalNight` block exists and has a non-empty candidate set
- every arrival candidate has a unique ID and rank, 24-hour / anytime front-desk signal, accepted evidence type, valid booking link, valid evidence link, and (if supplied) a valid `hotelId`
- `recommendedId` points to a candidate backed by direct official hotel/brand evidence
- `itinerary.json` includes a `legs` array

```bash
python3 validate.py
python3 build.py
```
