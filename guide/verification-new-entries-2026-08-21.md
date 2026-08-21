# New-entry batch, round 1 — area-by-area (2026-08-21)

**Method:** a candidate enters `data/hotels.json` only when *all* of the following are sourced from a page actually fetched in this pass:

1. **Identity** — exact property name and street address,
2. **Coordinates** — real lat/lng (the validator rejects records without them and rejects duplicates),
3. **Bed count and Booking's bed label** on the specific room row being quoted,
4. **A dated refundable rate** — price, tax line, cancellation sentence, prepayment terms,
5. **No collision** with an existing record (ID, name, official URL, source URL, coordinates).

Anything missing means the candidate is **held out and documented**, not added with a placeholder.

---

## Added: 9 (round 1 Busan · round 2 Dongdaemun + Mapo · round 3 Jongno fringe · round 4 Gangnam · rounds 5–7 Myeong-dong)

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

## Round 3 — Itaewon + Jongno (added 2026-08-21 ~21:00 UTC)

**Result: 1 added, 2 held out.** Both hold-outs produced a real, recorded finding rather than a blank.

### Fraser Place Central Seoul — `seoul-fraser-place-central`

| Field | Value | Source |
|---|---|---|
| Address | 78, Tongil-ro, Jung-gu, 04517 Seoul | Independent structured listing (**not** Booking — see flags) |
| Coordinates | 37.562393 / 126.969406 | Same listing |
| Official site | `http://seoul-central.frasershospitality.com/` | Independent listing's `sameAs` field |
| Property type | Serviced apartments, 271 units | Independent listing |
| House rules | Check-in 15:00–24:00 · check-out 01:00–11:00 · minimum age 19 · pets on request · crib free, extra bed KRW 44,000 pp/night | Booking.com, captured page |
| Facilities | Indoor swimming pool, fitness center, restaurant "First Floor", room service, bar, free parking, **private kitchen in unit** | Booking.com |
| **Nov 1–9, 2026 (8 nt)** | ⚠️ **NO AVAILABILITY.** Every room type marked *"Not available on our site for your dates"* — Suite (1 king + 1 queen), Suite (2 twin + 1 king), One-Bedroom Family Apartment (1 king + 1 queen) | Booking.com, dated page |
| **Nov 15–22, 2026 (7 nt)** | Super Deluxe Two-Bedroom Apartment — **1 king + 1 queen**, 915 ft², private suite, private kitchen. **$360/night · $2,520**, 10% VAT excluded. **2 left.** | Booking.com, dated page |
| — cancellation | Free cancellation before **November 12, 2026** (3 days); then the first night. **Pay nothing until November 10, 2026.** | Booking.com, verbatim |
| Cheaper row, same window | 732 ft², also 1 king + 1 queen with private kitchen, 5 left, **$280/nt · $1,959**, identical terms — **room name cut at a page-chunk boundary**, so recorded in the note only | Booking.com |

**Manual verification:** [Nov 1–9](https://www.booking.com/hotel/kr/fraser-place-central-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Nov 15–22](https://www.booking.com/hotel/kr/fraser-place-central-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [official Frasers site](http://seoul-central.frasershospitality.com/)

**Flags:**

1. **Not a one-bed option.** Every unit — including the one *named* "One-Bedroom Family Apartment" — is listed by Booking as **1 king bed AND 1 queen bed**. `fits: false`.
2. **Booking's address line was not in the captured chunks**, so the street address rests on a third-party listing.
3. **Third-party sources disagree on the address:** *78 Tongil-ro, Jung-gu* (used here), *1-202 Uiju-ro 1-ga, Jung-gu* (old lot form of the same address) and *19-1 Sogong-ro 5-gil* (inconsistent). Confirm before travelling.
4. `stars: 4` is not an official Korean classification.
5. **In-unit washer/dryer is guest-reported only** — no official or OTA facility line confirmed it, so `hasOnSiteLaundry` stays `false`.
6. Distinct from **Fraser Place Namdaemun Seoul**, already in the list under a separate address.
7. This is the **first new record in this batch series with a genuine `officialUrl`**.


---

## Round 4 — Gangnam (added 2026-08-21 ~21:40 UTC)

**Result: 1 added, 2 held out, and one earlier hold-out re-verified instead of left stale.**

### Aloft by Marriott Seoul Gangnam — `seoul-aloft-gangnam`

| Field | Value | Source |
|---|---|---|
| Address | 736 Yeongdong-daero, Gangnam-gu, 06075 Seoul | Independent structured listing |
| Coordinates | 37.52362 / 127.05569 | Same listing |
| Official site | `https://www.marriott.com/en-us/hotels/selal-aloft-seoul-gangnam/overview/` | Independent listing's `sameAs` field |
| Room quoted | Aloft River, Guest room, **1 King**, River view — ⚠️ Booking bed label **1 queen bed**, 258 ft², river view | Booking.com rate table |
| **Nov 1–9, 2026 (8 nt)** | **$218/night · $1,919** — 10% service charge included, 10% VAT excluded. 5 left. | Booking.com |
| — cancellation | Free cancellation before **October 31, 2026** (1 day); then the first night. **No prepayment — pay at the property.** | Booking.com, verbatim |
| **Nov 15–22, 2026 (7 nt)** | **$210/night · $1,619** — same terms. 5 left. | Booking.com |
| — cancellation | Free cancellation before **November 14, 2026** (1 day); then the first night. **No prepayment.** | Booking.com, verbatim |
| Other rows | Breakfast-inclusive $243/$2,134 (Nov 1–9) and $235/$1,807 (Nov 15–22); Chic River (also queen-labelled) $225/$1,983 and $217/$1,675 | Booking.com |

**Manual verification:** [Nov 1–9](https://www.booking.com/hotel/kr/aloft-seoul-gangnam.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Nov 15–22](https://www.booking.com/hotel/kr/aloft-seoul-gangnam.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [official Marriott page](https://www.marriott.com/en-us/hotels/selal-aloft-seoul-gangnam/overview/)

**Like-for-like:** the same room code was captured in both windows — $218/nt over 8 nights vs $210/nt over 7 nights, **−4% in the later window**.

**Flags:**

1. **King name, queen label.** Marriott markets *"Guest room, 1 King"*; Booking states **1 queen bed** on the row sold. Unresolved → `fits: false`.
2. **A Hollywood room is also sold here** — *Aloft Urban Hollywood, Guest room, 1 King* is two mattresses pushed together, not a single king.
3. **`hasOnSiteLaundry: true` is third-party.** It rests on an independent structured amenity list ("Self-serve laundry", "Washing machine"); Booking's captured facility list did not repeat it. This is the first record in the series with the flag set true — verify it before relying on it.
4. `stars: 4` and check-in 15:00 / check-out 12:00 come from independent listings, not the captured Booking page.
5. **A cheaper unnamed row** at $1,793 for 8 nights sits above the Aloft River rows; its room name was cut at a page-chunk boundary and is recorded in the note only.
6. Distinct from **Aloft Seoul Myeongdong**, already in the list.







---

## Rounds 10–11 — Busan batch (2026-08-22)

**2 added. A whole Busan district was found missing and then represented.**

### Round 10 · Hotel Foret Premier Nampo — `busan-foret-premier-nampo`

Nampo / BIFF Square (Jung-gu), 54-1 Gudeok-ro, 48953 · coords 35.098415 / 129.02971.

**Nov 9–15, 2026 (6 nt):** Family Twin Room — **1 twin + 1 full**, 258 ft², only **2 left**. **$100/night · $601.34** before taxes (51% off an original $1,227.22). Free cancellation before **November 6, 2026** (3 days); ⚠️ inside 3 days **and** on a no-show the fee is the **TOTAL stay**. **No prepayment — pay at the property.**

The cheapest verified Busan option for the window, and only the second Nampo/BIFF Square record alongside Crown Harbor.

**Flags:** ⚠️ a separate **CITY TAX** is excluded on top of 10% TAX — only the second Busan record with a second tax line, so $601 is not what you pay · photo ID **and** credit card required at check-in with advance notice of arrival time · no single-bed room captured (`fits: false`) · breakfast 6.7/10 · Booking's own address line was not in the captured chunk.

[Dated Booking page](https://www.booking.com/hotel/kr/foret-premier-nampo.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD)

### The gap: Gwangalli had zero records

Working Busan **by district** rather than hotel-by-hotel exposed something no amount of per-hotel verification would have: the list covered Haeundae with **11 records**, plus Seomyeon, Busan Station, Nampo, Songdo and Yeonsan — and had **nothing at all in Gwangalli (Suyeong-gu)**, one of Busan's two main beach areas.

### Round 11 · Kent Hotel Gwangalli by Kensington — `busan-kent-gwangalli-kensington`

229 Gwanganhaebyeon-ro, Suyeong-gu, 48303 · coords 35.154232 / 129.11925 · phone +82 1670 7464.

Booking slug resolved as **`kent-gwangalli`** (after `kent-hotel-gwangalli` returned 404).

**Nov 9–15, 2026: ZERO availability.** Every room type is marked *"Not available on our site for your dates"*:

| Room | Bed |
|---|---|
| Executive Double with Ocean View | 1 queen bed |
| Deluxe Twin Room with City View (1 Double + 1 Single) | 1 twin + 1 full |
| Cinema Twin - No View (2 Single) | 2 twin beds |
| Suite with Sea View | 1 full bed + 1 sofa bed |
| Twin Room | 2 full beds |

**It is recorded anyway, with no price invented**, so the district is represented rather than silently absent. Captured: beachfront opposite Gwangan Bridge, 15th-floor Sky Lounge restaurant, bar, room service, free parking, 24-hour front desk; check-in 15:00–24:00 with photo ID **and** credit card required plus advance notice of arrival; check-out 11:00; children 6+ charged as adults; extra bed KRW 33,000.

**Flags:** ⚠️ **bed conflict** — Booking says the Executive Double Ocean View has **1 queen**, while another major platform lists the same 313 sqft room as **1 King** · star rating disputed (4 vs 3.5) · no Kensington official URL captured · third-party aggregators quote ~$45–$73/night for **other** dates, explicitly not stored as our-window rates.

[Dated Booking page](https://www.booking.com/hotel/kr/kent-gwangalli.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD)

### ⚠️ Second market signal — Busan is tightening

Booking displayed on this property: *"Limited supply in Busan for your dates: **2 four-star hotels like this are already unavailable on our site**."*

This mirrors the Seoul five-star signal from round 9. **Two different cities, two different star tiers, two different windows** — both showing inventory thinning. Combined with Ramada Encore Haeundae verified sold out and Paradise Hotel Busan offering only two rate rows for Nov 9–15, the Busan window is materially tighter than a 19-row table suggests.

### Held out — with reasons

| Candidate | Why |
|---|---|
| **H Avenue Gwangalli** | ⚠️ **Identity ambiguity.** Address given as *29 Millaksubyeon-ro, Suyeong-gu 48283* (coords 35.1532/129.12468) by two sources and *42 Gwanganhaebyeon-ro 278beon-gil* (coords 35.1539709/129.1245349) by another. Name appears as "H Avenue Gwangalli", "H Avenue Hotel Gwangalli branch" and "H Avenue Hotel Gwangalli Beach". Guests report it occupies floors 8–10 of a building **housing four other hotels**. This may be more than one property under near-identical names — exactly the duplicate risk this project's validator exists to prevent. No record created. |
| Hound Premier Hotel Nampo | 24 Bosu-daero, Jung-gu 48980; coords 35.099094 / 129.02522 confirmed. Booking slug unresolved (`hound-premier-nampo` 404s). |
| Toyoko Inn Busan Seomyeon | 39 Seojeon-ro, Busanjin-gu 47247; +82 51-638-1045. Coordinates not obtained. Chain sells direct on a ~3-month window, so a Booking rate for these dates is unlikely. |

---

## Round 9 — Re-verification round 2 (2026-08-22 ~00:45 UTC)

**0 added. Two more negatives hardened, and every no-rate record given an explicit reason.**

### Four Seasons Hotel Seoul — confirmed zero inventory, twice

Re-fetched 2026-08-21 for **Nov 1–9, 2026**. Every room type is marked *"Not available on our site for your dates"*:

Deluxe King (1 king) · Club Double (2 full) · Grand Family Room King (1 king) · Grand Family Room Double Bed (2 full) · Premier Family King (1 king) · Executive King Suite City View (1 king) · Executive King Suite Palace View (1 king) · Executive Double Suite City View (2 full) · King Suite (1 king) · King Suite (2 full) · Two-Bedroom Suite (1 king + 1 king) · Two-Bedroom Suite (1 king + 2 full) · Three-Bedroom Suite

This is a **second independent negative three days after 2026-08-18**, so the record's caveat is retired.

**Market signal worth acting on:** Booking displayed *"Limited supply in Seoul for your dates: **2 five-star hotels like this are already unavailable on our site**."* Combined with THE PLAZA also showing zero inventory, the five-star tier for the **Nov 1–9** window is visibly tightening. If a luxury Seoul stay matters, that is the window to lock first — and to book brand-direct rather than via an OTA.

[Dated Booking page](https://www.booking.com/hotel/kr/four-seasons-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD)

### Toyoko Inn Seoul Dongdaemun II — structural, not sold out

Re-fetched 2026-08-21: the page renders **no rate table at all** for Nov 1–9. Second check, three days after 2026-08-19.

This is a **distribution fact**: Toyoko Inn opens its own booking window roughly 3 months ahead and sells direct. Newly captured house rules: check-in **15:00–24:00**, check-out **10:00** (unusually early — plan the last morning around it), minimum check-in age 18, children 7+ charged as adults, **no cribs or extra beds**, pets not allowed, cash accepted, licence 제2018-00012호. Guests place the hotel about **20 m from Dongdaemun History & Culture Park station** and consistently praise the free breakfast.

**Book direct at toyoko-inn.com.**

[Dated Booking page](https://www.booking.com/hotel/kr/toyoko-inn-seoul-dongdaemun-ii.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD)

### New field: `distributionStatus`

A blank price cell was previously ambiguous — it could mean sold out, not on the platform, or simply not yet checked. Every record without a live rate now carries a `distributionStatus` block with a status, an `asOf` date, the evidence, and a `bookVia` channel where known.

| Status | Records | Meaning |
|---|---|---|
| `On Booking, no inventory for our window (verified)` | seoul-four-seasons · seoul-the-plaza-autograph-collection · busan-ramada-encore-haeundae | Genuinely full on this channel for these dates, each verified on two separate days (or, for Ramada Encore, with Booking's explicit no-availability statement). |
| `Direct-book only` / `Direct-book (Accor)` / `Direct-book (resort inventory)` | seoul-toyoko-inn-dongdaemun2 · seoul-nine-tree-rokaus-yongsan · suwon-novotel-ambassador · gyeongju-sono-calm | The property is operating and sellable — just not through Booking for this stay. |
| `Not distributed on Booking.com` | busan-ibis-haeundae · busan-ibis-budget-haeundae | Absent from the platform entirely. Accor direct only. |
| `Unclassified — no live rate and no distribution check yet` | gyeongju-hwangnamkwan · gyeongju-gg-hotel · gyeongju-hanokinn · gyeongju-wiyeonjae · gyeongju-nadul-hanok · cheonan-on-city · cheonan-brown-dot · daejeon-ramada · daejeon-hotel-stendhal · daejeon-hotel-interciti | **Genuinely unknown.** Each carries an old dated negative but has not been re-tested and no direct channel has been confirmed. The evidence text says explicitly: *do not read the absence of a rate as "sold out."* |

Ten records remain unclassified. They are all Gyeongju / Cheonan / Daejeon — the alternate-route cities, not Seoul or Busan — which is why they sit at the bottom of the priority list rather than blocking anything.

---

## Round 8 — Re-verification pass (2026-08-22 ~00:10 UTC)

**0 added. Two "unavailable" findings hardened from a single check to a verified result.**

A negative result from one source at one moment is not proof a hotel is full. This round re-tested the two most decision-relevant records that carried exactly that caveat.

### THE PLAZA Seoul, Autograph Collection — confirmed unavailable, twice

Re-fetched 2026-08-21 for **Nov 1–9, 2026**. Every room type is marked *"Not available on our site for your dates"*:

| Room | Bed |
|---|---|
| Premier Suite | 1 king bed |
| Business King Room | 1 king bed |
| Prestige Suite | 1 king bed |
| Residential Suite, Club Lounge access | 1 king bed |
| Deluxe Guest room | 1 twin + 1 king |
| Club Deluxe Twin, Club lounge access | 2 twin beds |
| Deluxe Twin, Guest room | 2 twin beds |

This is a **second independent negative three days after the 2026-08-18 check**, so the record's previous caveat — *"negative result on one source at one moment — not proof the hotel is full"* — is now retired and replaced with a verified result.

Newly captured this pass: check-in from **15:00**, check-out until **11:00**, and **a photo ID *and* credit card are required at check-in**. Facilities: indoor swimming pool, spa and wellness centre, fitness centre, airport shuttle, room service, restaurant "The Seven Square". Guests repeatedly confirm the hotel is **connected to City Hall metro station** with the Incheon airport bus stopping directly outside.

**Action:** book Marriott / Autograph Collection direct. Booking.com holds no inventory for this 8-night span; that is a distribution fact, not evidence the hotel is full.

[Dated Booking page](https://www.booking.com/hotel/kr/theplaza.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD)

### Hotel Midcity Myeongdong — the finding changed shape

Re-checked 2026-08-21 for **Nov 1–9, 2026**: still no rate table. But Booking served its **alternative-dates widget**, and that widget proves the property is **open and actively selling**:

| Alternative range shown by Booking | Nights | From |
|---|---:|---:|
| Nov 8 – Nov 14 | 6 | $1,546 |
| **Nov 9 – Nov 15** | 6 | $1,641 |
| Nov 10 – Nov 16 | 6 | $1,641 |
| Nov 11 – Nov 17 | 6 | $1,631 |
| Nov 8 – Nov 15 | 7 | $1,889 |
| Nov 11 – Nov 18 | 7 | $1,851 |
| Nov 8 – Nov 16 | 8 | $2,128 |

So Midcity is **not** sold out or closed — the specific **Nov 1–9 eight-night span** is what fails. A one- or two-night shift would likely make it bookable.

⚠️ **Those "from" totals are for OTHER date ranges.** They are recorded here as context only and are deliberately **not** stored as rates for any of our three windows. Nov 15–22 was not re-checked this pass.

[Dated Booking page](https://www.booking.com/hotel/kr/hotel-midcity-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD)

### Still outstanding — 15 records with no live rate in any window

| Group | Records | Likely reason |
|---|---|---|
| Seoul | Four Seasons Seoul · Toyoko Inn Dongdaemun II · Nine Tree ROKAUS Yongsan | Toyoko is structural — the chain only opens its booking window ~3 months ahead. ROKAUS is direct-book. Four Seasons has one untested negative. |
| Suwon | Novotel Ambassador Suwon | Accor direct-book; official page already confirms 1 × King size bed, 28 m², direct KTX/subway access. |
| Cheonan / Daejeon | 2 + 3 records | Corridor alternates, lower priority. |
| Gyeongju | 6 records incl. 3 hanoks and SONO Calm | Mostly direct-book or resort inventory not distributed on Booking. |

These are the highest-value remaining work: they are **already on the shortlist**, so confirming whether each is genuinely unavailable or merely undistributed matters more than adding further new properties.

---

## Round 7 — Myeong-dong completed (added 2026-08-21 ~23:40 UTC)

### Hotel Thomas Myeongdong — `seoul-hotel-thomas-myeongdong`

| Field | Value | Source |
|---|---|---|
| Address | 26, Sejong-daero 16-gil, Jung-gu, 04526 Seoul | Three independent structured listings, in agreement |
| Coordinates | 37.56312942 / 126.97834777 (others: 37.563175/126.978264, 37.563277/126.978348) | Same listings, agreeing to 3–4 dp |
| Star / hours | 3-star; check-in 15:00, check-out 12:00 | Independent listings |
| **Nov 1–9, 2026 (8 nt)** | Family Twin Room — **1 twin + 1 full**, 249 ft², city view, 6 left. **$229/night · $1,833.11** before taxes (38% off $2,951.86), 10% TAX excluded | Booking.com |
| — terms | Free cancellation before **October 25, 2026** (7 days); ⚠️ inside 7 days **and** on a no-show the fee is the **TOTAL reservation**. **No prepayment — pay at the property.** | Booking.com, verbatim |
| **Nov 15–22, 2026 (7 nt)** | Deluxe Twin Room — **2 twin beds**, 249 ft², city view, 6 left. **$158/night · $1,105.66** before taxes (43% off $1,956.54), 10% TAX excluded | Booking.com |
| — terms | Free cancellation before **November 8, 2026** (7 days), same total-price penalty. **Pay nothing until November 6, 2026.** | Booking.com, verbatim |
| Other rows | Nov 1–9 breakfast-inclusive $243/$1,944.02; an unnamed cheaper room at $194/$1,553.52 and $208/$1,664.43; a "Triple Room - Bath" with no captured price. Nov 15–22 breakfast-inclusive $171/$1,193.97; unnamed cheaper room $147/$1,031.02 and $160/$1,119.33 | Booking.com |

**Manual verification:** [Nov 1–9](https://www.booking.com/hotel/kr/thomas-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Nov 15–22](https://www.booking.com/hotel/kr/thomas-myeongdong.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD)

**Flags:**

1. **⚠️ Bathroom status is contradictory.** Booking's per-room amenity list contains **both "Attached bathroom" and "Shared toilet"** for the same rooms. The private-bathroom requirement is **not established**. This is the single most important thing to confirm before booking here.
2. **No single-bed room in either window** — Family Twin (twin + full) and Deluxe Twin (2 twin). `fits: false`.
3. **Prices are Genius member + Early Booker Deal rates**, 38–43% below the displayed originals. The public price is much higher.
4. **Different room codes in the two windows** — not a like-for-like comparison.
5. **Prepayment structure differs by window** (pay-at-property vs payment due Nov 6).
6. **Breakfast rated 5.6/10** by Booking guests — the lowest of any property added in this series.
7. No official property URL captured, so `officialUrl` is absent.

This property was held out by the 2026-08-19 audit because its rate/cancellation block was never fully captured. Both windows now have verbatim terms, so it is added — with the bathroom contradiction recorded rather than smoothed over.

### Myeong-dong status after round 7

| Property | Status |
|---|---|
| Solaria Nishitetsu Hotel Seoul Myeongdong | ✅ Added (round 5) |
| Hotel Prince Seoul | ✅ Added (round 5) |
| G2 Hotel Myeongdong | ✅ Added (round 6) |
| Hotel Thomas Myeongdong | ✅ Added (round 7) |
| Metro Hotel Myeongdong | ❌ Eliminated — closed for renovation 2026-06-16 → 2027-02-28, covering all three trip windows |
| Hotel Midcity Myeongdong | ⏳ Last open item — URL known, showed no availability in either window on 2026-08-19, needs one re-check |

Five of the six unattached Myeongdong Booking URLs found in this repo's own guide files are now resolved.

---

## Round 6 — Myeong-dong continued (added 2026-08-21 ~23:05 UTC)

### G2 Hotel Myeongdong — `seoul-g2-hotel-myeongdong`

| Field | Value | Source |
|---|---|---|
| Address | 24, Supyo-ro, Jung-gu, 04555 Seoul | Booking.com |
| Coordinates | 37.563287 / 126.990345 | Independent structured listing (same street address, 147 rooms, phone +82 2-2277-9700) |
| Transport | **7-minute walk to Myeongdong (Line 4) AND Chungmuro (Lines 3 and 4)**; ~2,657 ft from the Myeongdong shopping area | Booking.com property description |
| Facilities | On-site restaurant, free fitness center, rooftop patio, 24-hour front desk, luggage storage, currency exchange, concierge, laundry and dry cleaning. Booking's photo set shows a **guest laundry room with washing machines**. | Booking.com |
| **Nov 1–9, 2026 (8 nt)** | Standard Twin Room (No Parking) — **2 twin beds**, 269 ft², city view. **$230/night · $1,839.68** before taxes (37% off $2,902.25), 10% TAX excluded | Booking.com |
| — cancellation | Free cancellation before **October 18, 2026** — **14 days** before arrival. ⚠️ Inside 14 days the fee is the **TOTAL price of the reservation**; no-show the same. | Booking.com, verbatim |
| — prepayment | Pay nothing until October 16, 2026 | Booking.com |
| **Nov 15–22, 2026** | ⚠️ **NOT CAPTURED.** Booking truncated before the rate table on two attempts. | — |

**Manual verification:** [Nov 1–9](https://www.booking.com/hotel/kr/g2-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Nov 15–22](https://www.booking.com/hotel/kr/g2-myeongdong.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD)

**Flags:**

1. **Longest free-cancellation deadline in the dataset (14 days) with the harshest penalty after it** — the whole reservation, and the same on a no-show. A second rate tier runs 7 days on identical total-price terms.
2. **Twin-only on available evidence.** The only named, priced room is a 2-twin Standard Twin; the 2026-08-19 audit also captured only twins. `fits: false`.
3. **Nov 15–22 is genuinely missing.** The 2026-08-19 audit recorded $180/nt · $1,260 before tax for the same room, but that is a **prior-pass figure**, stored in the field's note and explicitly NOT as a live rate.
4. **Four further rate rows were captured without room names** — $207/nt ($1,655.71) and breakfast-inclusive $222/nt ($1,774.88) on the 14-day tier; $300/nt ($2,403.07) and $322/nt ($2,576.03) on the 7-day tier. Their headers fell outside the fetched chunks, so the names are not guessed.
5. No official G2 URL captured; `stars: 4` is third-party.

---

## Round 6 eliminations and open items

### ❌ Metro Hotel Myeongdong — eliminated, not merely held out

The property text on its Booking page states a **renovation scheduled 2026-06-16 to 2027-02-28**, and Booking reports that reservations cannot be made. **That window covers Nov 1–9, Nov 9–15 and Nov 15–22, 2026 — the entire trip.** This is a permanent exclusion for these dates, not a re-try. Logged in `data/pricing-history.json`.

### Hotel Thomas Myeongdong — identity resolved, rates pending

Confirmed this round: 26, Sejong-daero 16-gil, Jung-gu, 04526 Seoul; coordinates **37.56312942 / 126.97834777** (two further listings give 37.563175 / 126.978264 and 37.563277 / 126.978348, agreeing to 3–4 decimal places); 3-star; check-in 15:00, check-out 12:00; laundry service, 24-hour front desk, banquet room; near City Hall metro, one stop from Seoul Station. Booking URL `/hotel/kr/thomas-myeongdong.html`. **Only the dated rate capture is outstanding** — everything else needed for a master record is now in hand.

### Hotel Midcity Myeongdong — re-check pending

Booking URL `/hotel/kr/hotel-midcity-myeongdong.html`. The 2026-08-19 audit found **no availability in either Seoul window**, with a Standard Double listed as 1 queen bed but not sellable. Not re-checked this round.

---

## Round 5 — Myeong-dong (added 2026-08-21 ~22:20 UTC)

### How these were found — no slug guessing

Rounds 3 and 4 lost time guessing Booking slugs. Round 5 changed method: every Booking URL mentioned anywhere in this repo's `guide/` files was extracted and diffed against the URLs already attached to master records. That surfaced **six Myeongdong properties with known-good Booking URLs that had never been added**:

`g2-myeongdong` · `hotel-midcity-myeongdong` · `hotel-prince-seoul` · `metro` · `solaria-nishitetsu-seoul` · `thomas-myeongdong`

All six had been **held out by the 2026-08-19 Myeongdong audit**, mostly because the row captured at the time happened to be a twin — which is not a valid reason to exclude a property from a checklist whose stated goal is *"not cheapest refundable but fully understanding all our options."* Two are now fully verified in both windows.

### Solaria Nishitetsu Hotel Seoul Myeongdong — `seoul-solaria-nishitetsu-myeongdong`

| Field | Value | Source |
|---|---|---|
| Booking property name | "Solaria Nishitetsu Hotel Seoul Myeongdong - **Renovated in 2025**" | Booking.com |
| Address | 27, Myeong-dong 8-gil, Jung-gu, 04536 Seoul | Booking.com |
| Coordinates | 37.5624504 / 126.9853668 (a second listing gives 37.5626 / 126.98516) | Independent structured listings |
| **Nov 1–9, 2026 (8 nt)** | Casual Double **- No Window** — 1 full bed, 237 ft², **1 left**. **$306/night · $2,446.67** before taxes (23% off $3,165.98), 10% TAX excluded | Booking.com |
| **Nov 15–22, 2026 (7 nt)** | Standard Double Room — 1 full bed, 269 ft², **3 left**. **$327/night · $2,289.55** before taxes (24% off $3,012.57), 10% TAX excluded | Booking.com |
| Cancellation, both windows | Free until **2 days** before arrival. ⚠️ **Inside 2 days the fee is the TOTAL stay price, and the no-show fee is also the TOTAL stay price.** | Booking.com, verbatim |
| Prepayment | Pay nothing until Oct 28 / Nov 11 | Booking.com |
| Other rows | Nov 1–9 Standard Twin (2 twin) $308/$2,464.68 · Nov 15–22 Partner Offer Standard Double $304/$2,128 (pay in advance, no modifications) · Hollywood Double $313/$2,193 | Booking.com |

**Flags:** the only "king"-labelled row is **Hollywood Double** (two joined mattresses — the sixth bed-label conflict in this series) · the Nov 1–9 refundable room **has no window** · the two windows use different room codes so they are **not** like-for-like · harshest penalty terms found so far · no official Nishitetsu URL captured · `stars: 3` and `hasOnSiteLaundry: true` both rest on third-party listings.

### Hotel Prince Seoul — `seoul-hotel-prince-myeongdong`

| Field | Value | Source |
|---|---|---|
| Address | 130 Toegye-ro, Jung-gu, 100-042 Seoul | Independent structured listings |
| Coordinates | 37.56064987 / 126.98625183 (second listing 37.560732 / 126.986238) | Independent structured listings |
| **Nov 1–9, 2026 (8 nt)** | Twin Room B — **2 twin beds**, 215 ft², high floor, 2 left. **$195/night · $1,750.51** before taxes (26% off $2,358.09), 10% service charge included, 10% TAX excluded | Booking.com |
| **Nov 15–22, 2026 (7 nt)** | Double Room A (block RD28644505) — **1 queen bed**, high floor, 3 left. **$159/night · $1,249.51** before taxes, 10% service charge included, 10% TAX excluded | Booking.com |
| Cancellation, both windows | Free until **SEVEN days** before arrival; then the first night. ⚠️ **No-show fee is the TOTAL reservation price.** | Booking.com, verbatim |
| Prepayment | Pay nothing until Oct 23 / Nov 6 | Booking.com |

**The headline finding:** a **7-day free-cancellation window** in both date windows. Every other record in this dataset is 1–3 days. On a trip that is still being planned, that is a materially different risk profile.

**Flags:**

- **$159/night is a members-only price.** Displayed stack: original $1,888.56 → bonus savings −$339.94 → Genius −$188.86 → Booking.com pays −$110.25 → **$1,249.51**. The public price is higher.
- **No-show = the whole reservation**, even though in-window cancellation is only the first night.
- **The queen row's label was cut** in today's capture. The name *Double Room A* is carried from this repo's own 2026-08-19 audit of the **same Booking room block ID (RD28644505)** — matched, not invented.
- The two windows use **different room codes** (twin vs queen) — not a like-for-like comparison.
- Star rating disagrees across sources (3 and 4).
- No official `hotelprinceseoul.co.kr` URL captured, so `officialUrl` is absent.

### Still held out in Myeong-dong

| Candidate | Booking URL known | Why still out |
|---|---|---|
| G2 Hotel Myeongdong | `g2-myeongdong` | Only twin rows captured so far; the cancellation block fell outside the captured text in the earlier pass. |
| Hotel Thomas Myeongdong | `thomas-myeongdong` | Rate/cancellation block never fully captured; only twin rooms seen. |
| Hotel Midcity Myeongdong | `hotel-midcity-myeongdong` | Earlier pass found **no availability in either window**; a Standard Double exists in inventory as 1 queen but was not sellable. Needs a re-check. |

---

## Round 4 hold-outs

### InterContinental Seoul COEX — held out

- **Address:** 524 Bongeunsa-ro, Gangnam-gu, 06164 Seoul. **Coordinates:** 37.51286 / 127.05711. Two independent listings agree, and both describe direct COEX Mall access, an indoor pool, spa and indoor golf range, opposite Bongeunsa Temple.
- **Why held out:** two Booking property-slug attempts — `intercontinental-seoul-coex` and `intercontinental-coex` — both returned Booking's 404 page. **No dated rate page could be reached.**
- **Important:** this is a **different hotel** from *Grand InterContinental Seoul Parnas*, which is already in the master list. Do not merge them.

### Andaz Seoul Gangnam, By Hyatt — re-verified, still held out

The 2026-08-19 batch-5 report held this out for "no availability". Rather than leave that stale, it was re-fetched on 2026-08-21:

- **Still no sellable inventory for Nov 1–9, 2026.** Every room type is marked *"Not available on our site for your dates"*: Premium King (1 king), Premium Twin (2 twin), King Room – High Floor (1 king), Twin Room – High Floor (2 twin).
- **House rules captured:** check-in 15:00, check-out 11:00, **minimum check-in age 20**, pets not allowed, children 13+ charged as adults, crib free, extra bed free for 17+.
- **Location note:** guests consistently report the hotel is directly connected to **Apgujeong Station (Line 3)**.
- **Status:** direct-booking follow-up on hyatt.com. No price row will be invented.

---

## Round 3 hold-outs

### Nouvelle Hotel Seoul Itaewon by Anook — held out

- **Address:** 2-7F, 11, Usadan-ro 14-gil, Yongsan-gu, 04405 Seoul. **Coordinates:** 37.5341115 / 126.996318. Both confirmed.
- **Name discrepancy flagged:** search results call it "by **Aank**"; Booking's own page title says "by **Anook**".
- **The finding:** the Nov 1–9 rate table was read **end to end** (all three page chunks). **Every rate row on the property is "Non-refundable — pay online."** There is no refundable rate at any price point.
  - Cheapest row **$110/nt · $881** (Genius + pay-online member price off an original $1,064.03)
  - Same room with breakfast **$129/nt · $1,028**
  - Deluxe Twin (2 twin beds, 165 ft²) **$122/nt · $978.91**
  - Suite (2 full beds, 489 ft²) **$248/nt · $1,987.84**, 2 left
- **Also recorded:** check-in 16:00, check-out 12:00, **children are not allowed**, minimum check-in age **19**, no cribs or extra beds, pets not allowed.
- **Why held out:** this project's core requirement is a verifiable refundable rate. A property with no refundable inventory is a legitimate *finding*, not a master-list row. The capture is logged in `data/pricing-history.json` so the work is not lost.

### Hotel Aventree Jongno — held out

- **Address:** 46, Ujeongguk-ro, Jongno-gu, Seoul. **Coordinates:** 37.573027 / 126.98301 (three independent listings agree to ~4 decimal places). Minutes on foot from **Jonggak Station (Line 1)**; laundry service and 24-hour reception listed.
- **Why held out:** two Booking property-slug attempts — `aventree-jongno` and `aventree-hotel-jongno` — both returned Booking's 404/sign-in page. **No dated rate page could be reached**, so there is no price, no bed count on a sold row, and no cancellation term.
- **Also flagged:** the star rating disagrees across sources (3, 3.5 and 4).
- **Next step:** find the correct Booking slug (or another dated, fetchable rate source) and re-run both windows.

---

## Earlier hold-out (round 1)

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
| Itaewon | **Round 3 worked** — no property added. The candidate investigated (Nouvelle by Anook) sells **only non-refundable** rates. The four existing Itaewon records (Grand Hyatt, Mondrian, Hamilton, Imperial Palace Boutique) already cover the area's refundable tier. |
| Jongno / Insadong | **Round 3 partially worked** — Fraser Place Central Seoul added on the Jung-gu/Seodaemun fringe; **Hotel Aventree Jongno held out** pending a working Booking slug. |
| Myeong-dong | **Round 5 complete — the earlier "skip it" call was wrong.** Six unattached Booking URLs were found inside this repo's own guide files; Solaria Nishitetsu and Hotel Prince Seoul are now added, three remain held out with known URLs. |
| Gangnam | **Round 4 complete** — Aloft by Marriott Seoul Gangnam added; InterContinental Seoul COEX held out (slug 404); Andaz Seoul Gangnam re-verified as still unavailable for Nov 1–9. |
| Busan | Round 1 complete: 1 added, 1 held out. |

**Running total across all eleven rounds: 11 added, 14 held out (each with a recorded finding), 1 identity collision resolved, 5 earlier findings re-verified on a second independent check, 1 property eliminated outright (Metro Hotel Myeongdong — closed for renovation across the whole trip), 20 records given an explicit `distributionStatus`, 1 whole district gap (Gwangalli) found and represented, 0 duplicates created.**

### Open re-tries — all blocked on the same thing

Three candidates have solid identity and coordinates but **no reachable dated rate page** because the Booking property slug could not be guessed:

| Candidate | Coordinates | Slugs already tried |
|---|---|---|
| Hotel Aventree Jongno | 37.573027 / 126.98301 | `aventree-jongno`, `aventree-hotel-jongno` |
| InterContinental Seoul COEX | 37.51286 / 127.05711 | `intercontinental-seoul-coex`, `intercontinental-coex` |
| Shilla Stay Seobusan | 35.096675 / 128.905259 | `shilla-stay-seobusan` |

Each needs the correct slug (or another dated, fetchable rate source) before it can enter the master list.

Run `python3 validate.py && python3 build.py` after any edit.
