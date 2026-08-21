# New-entry batch, round 1 — area-by-area (2026-08-21)

**Method:** a candidate enters `data/hotels.json` only when *all* of the following are sourced from a page actually fetched in this pass:

1. **Identity** — exact property name and street address,
2. **Coordinates** — real lat/lng (the validator rejects records without them and rejects duplicates),
3. **Bed count and Booking's bed label** on the specific room row being quoted,
4. **A dated refundable rate** — price, tax line, cancellation sentence, prepayment terms,
5. **No collision** with an existing record (ID, name, official URL, source URL, coordinates).

Anything missing means the candidate is **held out and documented**, not added with a placeholder.

---

## Added: 1

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

## Investigated, not added: 1

### Shilla Stay Seobusan (Gangseo-gu, Busan)

Identity is solid: 38, Myeongjigukje 7-ro, Gangseo-gu, Busan; an official `shillastay.com/seobusan` page exists; coordinates 35.096675 / 128.905259; phone +82-51-661-9000. Booking's own Busan brand filter also shows **two** Shilla Stay properties in Busan, and only one (Haeundae) is currently in the master list.

**Held out because** the Booking property slug could not be resolved in this pass — the guessed URL returned Booking's 404/sign-in page — so there is **no dated rate page**, and therefore no price, no bed count on a sold row, and no cancellation term. Adding it would mean a record with an empty rate, which is what this project avoids. It is also ~17 km from Busan KTX station in the far west of the city, so it is a low-priority re-try.

---

## Queued for the next rounds

Each Seoul candidate needs **two** dated captures (Nov 1–9 and Nov 15–22) plus coordinates before it can enter the master list, which is roughly three fetches per property:

| Area | Status |
|---|---|
| Dongdaemun | Queued — note the known Hotel U5 / Mercure Ambassador Seoul Dongdaemun identity collision recorded in batch 5. |
| Hongdae / Mapo | Queued |
| Itaewon | Queued |
| Jongno / Insadong | Queued |
| Myeong-dong | Queued — already the densest area in the list (25+ records), so new candidates must be genuinely new properties, not rebrands. |
| Gangnam | Queued — Andaz Seoul Gangnam remains held out from batch 5 (no sellable availability in either window). |
| Busan | Round 1 complete: 1 added, 1 held out. |

Run `python3 validate.py && python3 build.py` after any edit.
