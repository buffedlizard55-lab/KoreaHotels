# New-entry batch, round 1 — area-by-area (2026-08-21)

**Method:** a candidate enters `data/hotels.json` only when *all* of the following are sourced from a page actually fetched in this pass:

1. **Identity** — exact property name and street address,
2. **Coordinates** — real lat/lng (the validator rejects records without them and rejects duplicates),
3. **Bed count and Booking's bed label** on the specific room row being quoted,
4. **A dated refundable rate** — price, tax line, cancellation sentence, prepayment terms,
5. **No collision** with an existing record (ID, name, official URL, source URL, coordinates).

Anything missing means the candidate is **held out and documented**, not added with a placeholder.

---

## Added: 3 (round 1 Busan · round 2 Dongdaemun + Mapo)

### Hyatt Place Busan Yeonsan — `busan-hyatt-place-yeonsan`

| Field | Value | Source |
|---|---|---|
| Address | 1121, Jungang-daero, Yeonje-gu, 47524 Busan | Booking.com dated property page |
| Coordinates | 35.187756 / 129.08073 | Independent structured listing (same address, postal code, phone +82 51-713-6000) |
| Brand | Hyatt Place | Booking.com "Hotel chain/brand" field |
| Room quoted | King Room with City View — **1 king bed**, 320 ft², city view, attached bathroom | Booking.com rate table (king-bed filter) |
| Refundable rate, Nov 9–15, 2026 (6 nt) | **$134/night · $806 total**, 10% VAT excluded | Booking.com rate table |
| Cancellation | Free cancellation before **November 8, 2026** — free until 1 day before arrival; then the first night | Booking.com, verbatim |
| Prepayment | No prepayment needed — pay at the property | Booking.com, verbatim |
| Other rows captured | Non-refundable King $107/$645 · breakfast-inclusive refundable King $177/$1,064 · Twin (2 twin) $113/$679 non-ref, $141/$849 refundable | Booking.com rate table |

**Manual verification:** [dated Booking rate page](https://www.booking.com/hotel/kr/hyatt-place-busan-yeonsan.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD)

**Why it earns a place:** it adds a mid-tier international-brand **one-king** option to Busan at $134/night refundable, against $361 for the refundable Park Hyatt Busan King Room over the identical six nights. It is inland (Yeonje-gu), not on the Haeundae beach strip, so it widens the option set rather than duplicating it.

### Flags recorded on this entry

1. **Booking tags the property "Adults only."** Confirm before booking if that matters.
2. **No `officialUrl`.** The hyatt.com property URL was not captured in this pass, so the field is deliberately absent rather than guessed. Identity rests on Booking.com's dated page **plus** an independent structured listing agreeing on address, postal code, phone and coordinates.
3. **`stars: 4` is a brand-tier label, not an official rating.** No star rating appeared on the captured page.
4. **Not a core-needs match.** Booking says "1 king bed" with a private bathroom, but no source checked publishes a **mattress width**, and no **walkable-rail distance** was captured. `fits` is `false` until both exist.
5. **The headline price is not the refundable price.** $107/night is non-refundable, pay online. $134 is the refundable rate.
6. **Very few reviews (13 at capture)** — consistent with a recently opened property, so operational data is thin.


---

## Round 2 — Dongdaemun + Mapo/Gongdeok (added 2026-08-21 ~20:15 UTC)

Both properties were captured in **both** Seoul windows, using the **same room code in each window**, so the two prices are genuinely comparable per property.

### Mercure Ambassador Seoul Dongdaemun — `seoul-mercure-ambassador-dongdaemun`

| Field | Value | Source |
|---|---|---|
| Address | 369, Dongho-ro, Jung-gu, 04546 Seoul | Booking.com dated property page |
| Coordinates | 37.567348 / 127.0018 | Two independent structured listings, same address + postal code |
| Brand | Mercure (Accor) | Booking.com "Hotel chain/brand" field |
| Transport | Adjacent to **Euljiro 4-ga Station (Lines 2 and 5)**; an independent listing states 5 min to Euljiro 4-ga and 5 min to Jongno 5-ga | Independent listing |
| Room quoted | Classic Double Room — **1 full bed**, 216 ft², city view | Booking.com rate table |
| **Nov 1–9, 2026 (8 nt)** | **$216/night · $1,727**, 10% VAT excluded | Booking.com |
| — cancellation | Free cancellation before **6:00 PM on October 31, 2026**; then the first night. Pay nothing until **October 29, 2026**. | Booking.com, verbatim |
| **Nov 15–22, 2026 (7 nt)** | **$218/night · $1,529**, 10% VAT excluded | Booking.com |
| — cancellation | Free cancellation before **6:00 PM on November 14, 2026**; then the first night. Pay nothing until **November 12, 2026**. | Booking.com, verbatim |
| Other rows | Non-refundable $177/$1,416 (Nov 1–9) and $179/$1,254 (Nov 15–22); refundable + breakfast $245/$1,957 and $247/$1,731; Classic Twin (2 twin beds) prices identically | Booking.com |

**Manual verification:** [Nov 1–9](https://www.booking.com/hotel/kr/u5.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Nov 15–22](https://www.booking.com/hotel/kr/u5.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD)

**Identity collision resolved.** The 2026-08-19 Dongdaemun batch held out "Hotel U5" because its historic Booking URL resolved to a different name at the same address. That is now confirmed: `booking.com/hotel/kr/u5.html` serves **Mercure Ambassador Seoul Dongdaemun**. It is recorded as **one** property under the Mercure name — no separate "Hotel U5" record was created, and the duplicate-identity validator passes.

**Flags:** `1 full bed` only (not a core-needs match) · no all.accor.com URL captured, so `officialUrl` is absent · `stars: 4` is the Mercure brand tier · check-in 16:00 / check-out 11:00 come from a third-party listing, not Accor · **room count disagrees between sources (336 vs 297)** · brand new, only 2 Booking reviews at capture · the headline price is non-refundable.

### LOTTE CITY HOTEL Mapo — `seoul-lotte-city-mapo`

| Field | Value | Source |
|---|---|---|
| Address | 109, Mapo-daero, Mapo-gu, 04146 Seoul | Booking.com dated property page |
| Coordinates | 37.544891 / 126.950607 | Independent structured listing, same address |
| Brand | Lotte City Hotels | Booking.com "Hotel chain/brand" field |
| Transport | **Connected to Gongdeok Station Exit 2 by an internal passageway** — airport railway (AREX) plus Subway Lines 5 and 6; ~15 min by subway to Hongdae, Sinchon and Myeongdong | Booking.com property description |
| Room quoted | Double Room — **1 full bed**, 280 ft², city view | Booking.com rate table |
| **Nov 1–9, 2026 (8 nt)** | **$215/night · $1,723**, 10% TAX excluded. 7 left. | Booking.com |
| **Nov 15–22, 2026 (7 nt)** | **$177/night · $1,242.09** before taxes (7% property discount from $1,335.58), 10% TAX excluded | Booking.com |
| — cancellation, both windows | Free cancellation until **3 days** before arrival (Oct 29 / Nov 12); then the first night. **No prepayment — pay at the property.** | Booking.com, verbatim |
| Other rows | Nov 1–9: Standard Double with Bath $208/$1,666, breakfast-inclusive $240/$1,917, Superior Double City View $223/$1,781. Nov 15–22: Superior Double City View $184/$1,288.84; Standard Double with Bath **total $1,195** (per-night cell outside the captured chunk) | Booking.com |

**Manual verification:** [Nov 1–9](https://www.booking.com/hotel/kr/lottecityhotel.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Nov 15–22](https://www.booking.com/hotel/kr/lottecityhotel.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD)

**Flags:**

- **Unresolved full-vs-queen labelling.** A Booking room-type index retrieved by search on 2026-08-21 lists *Run of House*, *Standard Double Room with Late Check-in 18:00* and *[Swimming Pool PKG for 2] Standard Double Room with Bath* as **1 queen bed**, while every dated rate row captured for our two windows says **1 full bed** for the same room names. Unresolved — do not assume a queen.
- No lottehotel.com URL captured, so `officialUrl` is absent.
- `stars: 4` comes from independent listings, not the captured Booking page.
- Guest reviews mention a coin laundry, but no official or OTA facility line confirmed it, so `hasOnSiteLaundry` stays `false`.
- Check-in/check-out times were not on the captured page.
- Not a core-needs match: every one-bed room captured is a **full** bed.

### Like-for-like window comparison

Because the same room code was captured in both windows for both properties:

| Property | Nov 1–9 (8 nt) | Nov 15–22 (7 nt) | Movement |
|---|---:|---:|---|
| Mercure Ambassador Seoul Dongdaemun | $216/nt | $218/nt | flat (+1%) |
| LOTTE CITY HOTEL Mapo | $215/nt | $177/nt | **−18% in the later window** |

---

## Investigated, not added: 1

### Shilla Stay Seobusan (Gangseo-gu, Busan)

Identity is solid: 38, Myeongjigukje 7-ro, Gangseo-gu, Busan; an official `shillastay.com/seobusan` page exists; coordinates 35.096675 / 128.905259; phone +82-51-661-9000. Booking's own Busan brand filter also shows **two** Shilla Stay properties in Busan, and only one (Haeundae) is currently in the master list.

**Held out because** the Booking property slug could not be resolved in this pass — the guessed URL returned Booking's 404/sign-in page — so there is **no dated rate page**, and therefore no price, no bed count on a sold row, and no cancellation term. Adding it would mean a record with an empty rate, which is what this project avoids. It is also ~17 km from Busan KTX station in the far west of the city, so it is a low-priority re-try.

---

## Queued for the next rounds

Each Seoul candidate needs **two** dated captures (Nov 1–9 and Nov 15–22) plus coordinates before it can enter the master list, which is roughly three fetches per property:

| Area | Status |
|---|---|
| Dongdaemun | **Round 2 complete** — Mercure Ambassador Seoul Dongdaemun added; the Hotel U5 identity collision is resolved. |
| Hongdae / Mapo | **Round 2 complete** — LOTTE CITY HOTEL Mapo added (Gongdeok, Hongdae catchment). Hongdae proper (Mapo-gu core) still has room for candidates. |
| Itaewon | Queued |
| Jongno / Insadong | Queued |
| Myeong-dong | Queued — already the densest area in the list (25+ records), so new candidates must be genuinely new properties, not rebrands. |
| Gangnam | Queued — Andaz Seoul Gangnam remains held out from batch 5 (no sellable availability in either window). |
| Busan | Round 1 complete: 1 added, 1 held out. |

**Running total across both rounds: 3 added, 1 held out, 1 identity collision resolved, 0 duplicates created.**

Run `python3 validate.py && python3 build.py` after any edit.
