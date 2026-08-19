# Seoul / Dongdaemun — verified new-entry batch 5 (captured 2026-08-19)

## Scope and decision rule

This is the first **area-by-area** pass after the existing Seoul list. It begins in **Dongdaemun / Jangchung**. Search was performed for **two adults, one room**, with Booking.com set to USD. Each window was queried separately; rows below must not be compared as if they were the same stay length.

A candidate entered the master list only after the dated live rate page, property identity, room bed count, and bed-size evidence had been reconciled. A Booking “queen” or “king” label verifies the OTA’s stated bed category, but **does not establish a physical millimetre width**. Where an official page did not publish a dimension, this report says so rather than inferring one.

**Result:** 5 candidates were investigated. **2 passed identity + dated-rate review and were added to `data/hotels.json` and the append-only pricing history.** This is intentionally not padded to 20: the remaining candidates below are held for the reason recorded in the irregularities section.

**Capture time:** 2026-08-19 18:00 UTC. Prices are Booking USD display prices and, where shown, exclude 10% VAT. They are not direct-booking prices and are subject to live change.

## Table A — Nov 1–9, 2026 (8 nights)

| New master entry | Area | selected room / bed count | bed-size verification | refundable status | live price | Manual verification |
|---|---|---|---|---|---:|---|
| The Ambassador Seoul – A Pullman Hotel | Jangchung / Dongdaemun fringe | Deluxe King Room — **1 king bed** | Official Pullman room inventory says “Deluxe Room with 1 King bed”, 28 m². Exact mattress dimensions were not published. | **Yes** — free cancellation before **18:00 Oct 31**; then first-night fee. Payment due Oct 29. | **$292/night; $2,336 / 8 nights** (10% VAT excluded) | [dated Booking rate](https://www.booking.com/hotel/kr/grand-ambassador-seoul-associated-with-pullman.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [official Pullman room page](https://pullman.accor.com/en/hotels/seoul/0966.html) · [official Accor identity page](https://all.accor.com/hotel/0966/index.en.shtml) |
| Hotel Migliore Seoul | Dongdaemun / DDP | Economy Double is listed as **1 queen bed**, but is not sellable | Exact width for the sellable target room was not published by the official hotel page reviewed. | **No Booking inventory** for this window; no rate or cancellation term recorded. | — | [dated Booking availability](https://www.booking.com/hotel/kr/milreore-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [official hotel page](https://www.migliorehotel.co.kr/homepage/ENG/index/index) |

## Table B — Nov 15–22, 2026 (7 nights)

| New master entry | Area | selected room / bed count | bed-size verification | refundable status | live price | Manual verification |
|---|---|---|---|---|---:|---|
| The Ambassador Seoul – A Pullman Hotel | Jangchung / Dongdaemun fringe | Deluxe King Room — **1 king bed** | Official Pullman room inventory says “Deluxe Room with 1 King bed”, 28 m². Exact mattress dimensions were not published. | **Yes** — free cancellation before **18:00 Nov 14**; then first-night fee. Payment due Nov 12. | **$296/night; $2,071 / 7 nights** (10% VAT excluded) | [dated Booking rate](https://www.booking.com/hotel/kr/grand-ambassador-seoul-associated-with-pullman.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [official Pullman room page](https://pullman.accor.com/en/hotels/seoul/0966.html) · [official Accor identity page](https://all.accor.com/hotel/0966/index.en.shtml) |
| Hotel Migliore Seoul | Dongdaemun / DDP | Deluxe Double Room (Bathtub Random) — **1 queen bed**; private/attached bathroom shown | Booking’s bed label is queen. The official hotel page reviewed did **not** publish an exact dimension for this specific room, so it is **not** marked a strict ≥150 cm match. | **Yes** — free cancellation before **Nov 12**. **Partner Offer: pay in advance; no modifications.** | **$105/night; $738 / 7 nights** (plus separately displayed KRW 104,155 tax) | [dated Booking rate](https://www.booking.com/hotel/kr/milreore-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [official hotel page](https://www.migliorehotel.co.kr/homepage/ENG/index/index) |

## Irregularities / candidates held out of the master list

1. **Hotel U5 was not added.** Its historic Booking URL (`/hotel/kr/u5.html`) presently resolves to **Mercure Ambassador Seoul Dongdaemun** at the same address, not to a property called Hotel U5. This is an identity collision / rebrand ambiguity. Adding “Hotel U5” would risk a duplicate or wrong-property rate; it needs an independent, current identity source before inclusion.
2. **Hotel Skypark Kingstown Dongdaemun was not added.** The trusted Booking property URL was located, but the live rate fetch failed twice with HTTP 500 in this research environment. No price, cancellation status, or current room configuration was copied from a failed fetch.
3. **Andaz Seoul Gangnam was checked as a Gangnam candidate, not added.** Booking showed no availability for either requested window. It showed king rooms exist (one king bed) but did not provide a sellable price/refundable rate. It remains a direct-booking follow-up, not an invented price row.
4. **Migliore has a window split.** The Nov 1–9 page was unavailable, while Nov 15–22 showed the refundable 1-queen-labelled Partner Offer. The first-window table therefore has no carried-forward alternate-window price.
5. **Migliore’s payment/cancellation combination needs care.** “Free cancellation” is displayed before Nov 12, but the selected Booking Partner Offer is also “pay in advance” and “no modifications.” Those terms should be rechecked at checkout rather than simplified to “pay later.”

## Files updated

- `data/hotels.json`: added the two verified records with **separate** `refundableRate` (Nov 1–9) and `refundableRateNov15` (Nov 15–22) blocks.
- `data/pricing-history.json`: appended four immutable rate/availability captures, including the unavailable Migliore first window.
- `index.html`: rebuilt from source data.

Run `python3 validate.py` to confirm identity uniqueness and schema checks.
