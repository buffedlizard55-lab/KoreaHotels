# 🇰🇷 South Korea Hotel Shortlist — verified date-window tables

**Three stay windows. Three separate tables. Never merged.**
Every row below comes from a dated Booking.com rate page that was actually fetched, with the UTC capture date shown.
Prices are the USD display price at capture time and, unless the note says otherwise, **exclude 10% tax**.
A blank or missing value means it was not verified — nothing here is estimated.

| Window | Nights | Planned city | Rows with a live dated quote | Line-by-line checklist |
|---|---:|---|---:|---|
| **Nov 1–9, 2026** | 8 | Seoul | 89 | [Seoul dual window](guide/verification-seoul-dual-window-nov1-and-nov15-2026.md) · [Dongdaemun batch 5](guide/verification-seoul-dongdaemun-batch5-2026-08-19.md) |
| **Nov 9–15, 2026** | 6 | **Busan** (this request) + Gyeongju alternates | 21 Busan + 9 Gyeongju | [Busan Nov 9–15 pass](guide/verification-busan-nov9-15-2026-08-21.md) |
| **Nov 15–22, 2026** | 7 | Busan (original plan) + Seoul alternates | 112 | [Seoul Nov 15 pass](guide/verification-seoul-nov15-2026.md) |

> 💰 **Do not multiply the $/night column by the number of nights.** A line-by-line audit of all **242 priced rows** (2026-08-22) found **184 arithmetically consistent**, but **57 where the displayed total sits ~11% ABOVE $/night × nights** (median ratio 1.111) — Booking's per-night *average* excludes a component its own total includes. Both figures are captured verbatim from the same dated page. **Budget from the Total column, then add the tax shown in that row.** One row runs the other way and is flagged in-record for re-fetch (`The Designers Dongdaemun`, Nov 15–22).

> ⚠️ **Do not compare a row in one table with a row in another.** They are different search lengths (8 / 6 / 7 nights) and different searches.
> ⚠️ The itinerary files still describe the *original* route (Gyeongju Nov 9–15, Busan Nov 15–22). This request treats **Busan as the Nov 9–15 stay**, so both sets of captures are kept and neither is deleted. The route itself has not been rewritten — that is a decision, not a verification.

---

## 🔍 Line-by-line audit — what was checked and what it caught (2026-08-22)

Every one of the **160 records** and all **242 priced rate rows** were machine-checked against ten rules. This is the "verify everything" pass, and it found real defects.

| Check | Result |
|---|---|
| `sourceUrl` check-in/check-out **must match** the row's stored stay dates | ✅ 0 mismatches |
| `nights` **must equal** the real span between the dates | ✅ 0 errors |
| Live rates must carry timestamp, source URL, room, beds, cancellation, prepayment, currency | ❌ **2 failures — fixed** |
| Capture timestamps must not be in the future | ✅ 0 |
| A price may not exist unless `available` is true | ✅ 0 after fix |
| No-rate records must carry a `distributionStatus` | ✅ all 20 |
| `officialUrl` must not point at an OTA | ✅ 0 |
| `verification.sourceUrl` present and valid | ✅ 160/160 |
| Window field name vs actual stay dates | ✅ 0 |
| `$/night × nights` vs stored total | ⚠️ **58 flagged** — 57 explained, 1 unresolved |

### ❌ What it caught — two unsourced prices

**`ibis Ambassador Busan Haeundae`** and **`ibis budget Ambassador Busan Haeundae`** each carried `available: true` with a room name, a bed count, a **price ($49/nt · $343 and $45/nt · $315)** and a cancellation date — **with no capture timestamp, no source and no source URL.** Nothing supported those numbers, and they directly contradicted the same records' own `distributionStatus` of *"Not distributed on Booking.com"*.

**Both have been nulled**, with the removed values preserved in the record's note for traceability. This is exactly the failure mode this project exists to prevent: numbers that look verified sitting next to numbers that are.

### ⚠️ One arithmetic outlier, isolated

`The Designers Dongdaemun`, Nov 15–22: **$73/night × 7 = $511, but the stored total is $464** — ~9% *below*. It is the **only** row of 242 running in that direction; the other 57 all run the opposite way. Flagged in-record as unresolved pending a re-fetch, not silently corrected.

### ⚠️ Two core-needs badges now show their own disagreement

`Grand Josun Busan` and `Avani Central Busan` are marked as core-needs matches on the strength of their **official** room pages (queen ~150×200 / king). But Booking states **1 queen bed** on the row actually sold at both. A queen still meets the ≥150 cm preference, so the badge stands — but `fitReason` on both now says plainly that the official page and the OTA disagree about the bed, so the badge is no longer quietly resting on one source.

---

## 🅰 Table A — Nov 9–15, 2026 · 6 nights · **BUSAN** (the focus of this pass)

Captured 2026-08-21/22, Booking.com dated pages, 2 adults · 1 room · USD.
**All 25 Busan records are resolved for this window — 21 live refundable rates, 2 verified sold out, 2 not distributed on Booking.** Nothing is estimated.

| Hotel | City · area | Room captured | Beds on the sold row | Refundable — free until | $/night | Total | Captured (UTC) | Verify |
|---|---|---|---|---|---:|---:|---|---|
| Toyoko Inn Busan Haeundae No.2 | Busan · Haeundae | Economy Double Room (No Parking) | 1 full bed | Free cancellation before November 8, 2026 | $55 | **$331** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/toyoko-inn-busan-haeundae-2.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Toyoko Inn Busan Station No.1 | Busan · Busan Station / Dong-gu | Economy Double Room | 1 full bed | Free cancellation before November 8, 2026 | $59 | **$355** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/toyoko-inn-busan-no-1.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| ASTI Hotel Busan Station | Busan · Busan Station (Dong-gu) | Standard Double Room with City View (Partner Offer) | 1 full bed (284 ft²) | Free cancellation before November 8, 2026 | $79 | **$471** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/asti-busan.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Ramada Encore by Wyndham Busan Station | Busan · Busan Station / Dong-gu | Superior Double Room | 1 full bed (208 ft²) | Free cancellation before November 7, 2026 | $79 | **$474** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/ramada-encore-by-wyndham-busan.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Crown Harbor Hotel Busan | Busan · Jungang / Nampo | [Busan Minibar] Executive Double City | 1 full bed (291 ft²) | Free cancellation before November 7, 2026 | $91 | **$548** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/crown-harbour-busan.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel Foret Premier Nampo | Busan · Nampo / BIFF Square (Jung-gu) | Family Twin Room | 1 twin bed AND 1 full bed (258 ft², landmark + city view) — NOT a one-bed room | Free cancellation before November 6, 2026 | $100 | **$601** | 2026-08-22 | [dated rate](https://www.booking.com/hotel/kr/foret-premier-nampo.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Fairfield by Marriott Busan | Busan · Haeundae | Standard Room - 1 King Bed with City View | 1 king bed (248 ft²) | Free cancellation before November 9, 2026 | $103 | **$617** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/fairfield-by-marriott-busan.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Fairfield by Marriott Busan Songdo Beach | Busan · Songdo Beach | Standard Room - Guest room, 1 King, Sea view | 1 king bed (323 ft², sea + landmark view) | Free cancellation before November 9, 2026 | $127 | **$761** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/fairfield-by-marriott-busan-songdo-beach.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Avani Central Busan | Busan · BIFC / Seomyeon | Deluxe King Room with Mountain View (refundable rate) | 1 queen bed (301 ft², high floor) | Free cancellation before November 6, 2026 | $132 | **$790** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/avani-central-busan.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hyatt Place Busan Yeonsan | Busan · Yeonsan (Yeonje-gu) | King Room with City View (refundable rate) | 1 king bed (320 ft², city view) | Free cancellation before November 8, 2026 | $134 | **$806** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/hyatt-place-busan-yeonsan.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Nongshim Hotel | Busan · Dongnae / Oncheonjang hot spr… | Queen Room - Two Welcome Drink Coupons per stay | ⚠️ Booking bed label: 1 full bed (305 ft²) despite the room being sold as a 'Qu… | Free cancellation before November 8, 2026 | $128 | **$862** | 2026-08-22 | [dated rate](https://www.booking.com/hotel/kr/nongshim.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Shilla Stay Busan Haeundae | Busan · Haeundae (beach) | Standard Double Room with City View | 1 full bed (312 ft²) | Free cancellation before November 6, 2026 | $148 | **$885** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/shilla-stay-haeundae.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| L7 HAEUNDAE by LOTTE HOTELS | Busan · Haeundae (beach) | Standard King Town View (4F–9F) | 1 king bed (248 ft²) | Free cancellation before November 6, 2026 | $181 | **$1,084** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/l7-haeundae-busan.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Ananti at Busan Cove (Ananti Hilton Busan) | Busan · Gijang / Ananti Cove (Gijang-… | Cabin S Forest View Twin Bed (14-day cancellation tier) | 2 twin beds (753 ft², balcony, terrace, spa tub, mountain + pool view, high flo… | Free cancellation before October 26, 2026 | $191 | **$1,144** | 2026-08-22 | [dated rate](https://www.booking.com/hotel/kr/hilton-busan.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| LOTTE HOTEL BUSAN | Busan · Seomyeon | Premier Double with swimming pool, fitness, sauna access for 2pax | 1 full bed (397 ft²; Booking text: 'includes one double bed and has no capacity… | Free cancellation before November 8, 2026 | $197 | **$1,313** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/lotte-busan.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| The Westin Josun Busan | Busan · Haeundae / Dongbaek | Deluxe Park King, 1 King, Dongbaek Park view | ⚠️ Booking bed label is '1 full bed' for this King-named room (312 ft²) | Free cancellation before November 7, 2026 | $220 | **$1,467** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/the-westin-chosun-busan.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Wyndham Grand Busan Ijin | Busan · Songdo / Amnam | Executive King Room - Non-Smoking | 1 king bed (401 ft², sea view, hot tub, lounge access) | Free cancellation before November 8, 2026 | $278 | **$1,666** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/wyndham-grand-busan.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| SIGNIEL BUSAN | Busan · Haeundae / Mipo | Premier Double Room with City View (Salon de Signiel lounge access) | 1 king bed — Booking also lists 'Extra long beds (> 80 inches)'; balcony/terrace | Free cancellation before November 4, 2026 | $280 | **$1,868** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/signiel-busan.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Grand Josun Busan | Busan · Haeundae (beachfront) | Premier King Room with City View | 1 queen bed (Booking label) — 463 ft², sauna for 2 + Gran J lounge access | Free cancellation before November 7, 2026 | $327 | **$1,965** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/grand-josun-busan.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Paradise Hotel Busan | Busan · Haeundae beachfront | Premium Double Room with Half Sea View - Annex | 1 king bed (581 ft²) | Free cancellation before November 7, 2026 | $324 | **$2,160** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/paradise-busan.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Park Hyatt Busan | Busan · Haeundae (marine city) | King Room (refundable rate) | 1 king bed (452 ft², Busan Marina/city view) | Free cancellation before November 8, 2026 | $361 | **$2,166** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/park-hyatt-busan.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |

**Also resolved, with no price to quote:**

| Hotel | Finding | Evidence |
|---|---|---|
| Ramada Encore by Wyndham Busan Haeundae | **Verified sold out.** Booking states *"We have no availability here between Mon, Nov 9, 2026 and Sun, Nov 15, 2026."* Every room type (1 King Suite, 1 King Corner Suite, 1 Queen Mobility Accessible, 1 Queen + 1 Twin Family/Corner, Superior 1 Queen) is marked *Not available on our site for your dates*. Booking also tags the property **Adults only**. | [dated Booking page](https://www.booking.com/hotel/kr/haeundae-ramada-encore.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| ibis Ambassador Busan Haeundae | **Not distributable on Booking.com.** Booking's own Busan brand filter for these dates lists no ibis/Accor brand, and an independent listing states the property *"isn't taking reservations on our site right now"*. The property itself is still evidenced at 12 Haeundaehaebyeon-ro 237beon-gil, Haeundae-gu (3-star, 24-hour reception). Book direct via Accor and confirm the bed in writing. | [official Accor 9643](https://all.accor.com/hotel/9643/index.en.shtml) |
| ibis budget Ambassador Busan Haeundae | Same finding as above. | [official Accor 9106](https://all.accor.com/hotel/9106/index.en.shtml) |

### Same window, alternate city — Gyeongju, Nov 9–15, 2026 (the original itinerary's leg)

The *same six nights*, kept in the same table group so the two cities can be compared like-for-like.

| Hotel | City · area | Room captured | Beds on the sold row | Refundable — free until | $/night | Total | Captured (UTC) | Verify |
|---|---|---|---|---|---:|---:|---|---|
| Rivertain Hotel Gyeongju | Gyeongju · City center / bus terminal | Standard Double Room | 1 full bed (307 ft², spa tub). Adults-only rooms. | Free cancellation before November 6, 2026 | $81 | **$484** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/rivertain-hotel-gyeongju.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Kolon Hotel Gyeongju | Gyeongju · Bulguksa / Tohamsan | Premier Double or Twin Room | 1 full bed OR 1 twin + 1 full (guest selects if available); 280 ft² | Free cancellation before November 6, 2026 | $82 | **$491** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/kolon.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Benikea Swiss Rosen Hotel Gyeongju | Gyeongju · Bomun / HICO | Deluxe Double Room | 1 full bed (323 ft², balcony/garden/pool/city view). Width unpublished. | Free cancellation before November 6, 2026 | $83 | **$556** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/swiss-rosen.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| The-K Hotel Gyeongju | Gyeongju · Bomun Lake Resort | Hwangnyoung View Room with Ondol Floor | 4 futon beds (334 ft²) — not a western one-bed | Free cancellation before November 6, 2026 | $125 | **$752** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/the-k-gyeong-ju.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| KINOCK Gyeongju | Gyeongju · North Bomun | KINOCK PKG — KINOCK PREMIER (pet-park package) | 1 queen bed (570 ft²) | Free cancellation before November 2, 2026 | $138 | **$827** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/the-suite-gyeongju.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Kensington Resort Gyeongju | Gyeongju · North Bomun | Kensington Deluxe - Fully Renovated Room | 2 full beds (746 ft² apartment) — not one-bed | Free cancellation before November 2, 2026 | $160 | **$957** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/kensington-resort-gyeongju.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Commodore Hotel Gyeongju | Gyeongju · Bomun Lake Resort | Imperial Suite with Mountain View (only isolated refundable row this … | 1 twin + 1 full (2 beds) — NOT one-bed | Free cancellation before November 8, 2026 | $186 | **$1,254** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/commodore-gyeongju.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hilton Gyeongju | Gyeongju · Bomun Lake Resort | Premium King Room (lake view) | 1 king bed | Free cancellation before November 7, 2026 | $257 | **$1,712** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/gyeongju-hilton.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Lahan Select Gyeongju | Gyeongju · Bomun Lake Resort | Deluxe King Suite | 1 queen bed (829 ft², lake-view balcony) — page says queen despite “King” name | Free cancellation before November 7, 2026 | $265 | **$1,764** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/hyundai-gyeongju.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |

### 🚩 Busan Nov 9–15 — irregularities to review before booking

1. **Four "King" rooms are not sold with a king bed.** Booking's bed label on the row you actually buy:
   - Westin Josun *Deluxe Park King* → **1 full bed**
   - Grand Josun *Premier King* → **1 queen bed**
   - Avani Central *Deluxe King* → **1 queen bed**
   - and in reverse, L7 Haeundae *Superior **Queen** Town View* → **1 full bed**
2. **"Free cancellation" ≠ "pay later".** ASTI, Grand Josun's cheapest row, Lotte Hotel Busan's cheapest row and the cheaper Shilla Stay row are **Partner Offers: pay in advance, no modifications**. Wyndham Grand requires payment to the property before arrival. Signiel, Avani and both Toyoko Inns have a fixed payment-due date.
3. **Six properties charge the TOTAL stay, not one night, inside the deadline.** Toyoko Inn Haeundae 2, Toyoko Inn Busan Station No.1 and Wyndham Grand inside 1 day; Crown Harbor and **Grand Josun** inside 2 days; **Avani's no-show fee** is the whole reservation. On 6 nights that is a much larger exposure than a first-night fee.
4. **Two headline prices are not refundable prices.** Park Hyatt's $303/night King Room and Avani's $100/night Deluxe King are **non-refundable**. The refundable equivalents are **$361** and **$132** (Avani's $108 is a Genius + pay-online member rate, not the public price).
5. **Low inventory on the good rooms.** Avani Deluxe King **1 left**; Crown Harbor and **Grand Josun Premier King** **2 left**; Paradise **2 left and only two rate rows offered at all**; Westin **3 left**; Signiel **4 left**.
6. **Room tiers differ between windows for two hotels.** Wyndham Grand's Nov 15–22 row was a *Premium King* ($147) but no Premium King is offered Nov 9–15 (Executive King, $278). Lotte Hotel Busan's Nov 15–22 row was a *Deluxe Double* called 1 king ($162); the Nov 9–15 row is a *Premier Double* stated as 1 full ($197). Those pairs are **not** like-for-like price movements.
7. **Longest and shortest cancellation runways.** Signiel is free until **Nov 4** (5 days out). Both Fairfields are free until **12:00 AM on Nov 9** — the day of arrival.
8. **Display bug found and fixed.** The site was labelling every `refundableRate` row "Nov 1–9" regardless of its real stay dates, so all 20 Busan (Nov 15–22) and 15 Gyeongju (Nov 9–15) captures were rendering under the wrong window. Windows are now derived from each row's own `stayCheckIn`/`stayCheckOut`.

Full line-by-line evidence: **[`guide/verification-busan-nov9-15-2026-08-21.md`](guide/verification-busan-nov9-15-2026-08-21.md)**

---

## 🅱 Table B — Nov 1–9, 2026 · 8 nights (Seoul window)

Kept completely separate from Table A and Table C. Capture dates are shown per row.

| Hotel | City · area | Room captured | Beds on the sold row | Refundable — free until | $/night | Total | Captured (UTC) | Verify |
|---|---|---|---|---|---:|---:|---|---|
| Mangrove Dongdaemun | Seoul · Dongdaemun (Jung-gu) | Budget Twin Room | 1 bunk bed | Free cancellation before October 29, 2026 | $100 | **$800** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/maenggeurobeu-dongdaemun-junggu.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel Cappuccino | Seoul · Gangnam / Eonju | Double Room | 1 king bed (custom 2x2m Super King) | Free cancellation before October 30, 2026 | $103 | **$824** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/cappuccino.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hamilton Hotel Seoul | Seoul · Itaewon (Yongsan-gu) | Standard Twin Room | 2 twin beds | Free cancellation before October 30, 2026 | $99 | **$888** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/hamilton.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel The Designers Hongdae | Seoul · Hongdae / Hapjeong | Standard Double Room | 1 full bed | Free cancellation before October 30, 2026 | $108 | **$972** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/the-designer-hongdae.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Dormy Inn SEOUL Gangnam | Seoul · Gangnam | Superior Double Room (10F-16F) | 1 full bed | Free cancellation before October 29, 2026 | $144 | **$1,152** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/dormyinn-seoul-gangnam.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Shilla Stay Seocho Gangnam Station | Seoul · Seocho / Gangnam | Standard Double Room | 1 full bed (Shilla double ≈140cm) | Free cancellation before October 29, 2026 | $153 | **$1,226** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/shilla-stay-seocho.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| GLAD Gangnam COEX Center | Seoul · Gangnam / COEX | Superior Double Room | 1 full bed | Free cancellation before October 29, 2026 | $167 | **$1,333** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/glad-gangnam-coex-center.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel Skypark Dongdaemun I | Seoul · Dongdaemun (Jung-gu) | Standard Twin Room (Double also $149/$1,340) | 2 twin beds | Free cancellation before October 29, 2026 | $149 | **$1,340** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/skypark-dongdaemun-i.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| HOTEL in 9 Gangnam | Seoul · Gangnam / COEX | Standard Double Room | 1 queen bed | Free cancellation before October 30, 2026 | $167 | **$1,340** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/in-9.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Henn na Hotel Seoul Myeongdong | Seoul · Myeongdong | Double Room With Complimentary Breakfast | 1 full bed | Free cancellation before October 30, 2026 | $170 | **$1,361** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/bian-nahoteru-souruming-dong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Travelodge Myeongdong Euljiro | Seoul · Myeongdong / Euljiro | Superior Queen Room | 1 queen bed (231 ft²) | Free cancellation before October 30, 2026 | $172 | **$1,377** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/holiday-inn-express-seoul-euljiro.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Shilla Stay Gangnam Yeoksam | Seoul · Gangnam / Yeoksam | Standard Double Room | 1 full bed | Free cancellation before October 29, 2026 | $174 | **$1,390** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/shilla-stay-yeoksam.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Sotetsu Fresa Inn Seoul Myeong-dong | Seoul · Myeongdong | Standard Double Room | 1 full bed | Free cancellation before October 30, 2026 | $180 | **$1,442** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/sotetsu-fresa-inn-seoul-myeong-dong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Ibis Styles Ambassador Seoul Myeongdong | Seoul · Myeongdong | Standard Double Room | 1 full bed (Accor /9771: 1 x Double bed(s), 16 m²; width unpublished) | Free cancellation before October 31, 2026 | $187 | **$1,499** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/ibis-styles-seoul-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Amid Hotel Seoul | Seoul · Insadong / Jongno | Standard Double Room | 1 full bed | Free cancellation before October 31, 2026 | $188 | **$1,506** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/centermark.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Klaven Hotel Myeongdong City Hall | Seoul · City Hall / Myeongdong | Superior Double Room | 1 queen bed | Free cancellation before October 29, 2026 | $188 | **$1,507** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/aropa.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel Gracery Seoul | Seoul · City Hall / Namdaemun | Superior Double Room (17–20F) | 1 full bed | Free cancellation before October 25, 2026 | $193 | **$1,545** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/gracery-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| GLAD Mapo | Seoul · Mapo / Gongdeok (transit hu… | Standard Double Room | 1 queen bed | Free cancellation before October 29, 2026 | $194 | **$1,553** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/geulraedeu-mapo.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Sotetsu Hotels The Splaisir Seoul Dongdaemun | Seoul · Dongdaemun (Jung-gu) | Standard Double Room | 1 queen bed | Free cancellation before October 30, 2026 | $173 | **$1,554** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/ky-heritage-dongdaemun.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Seoul Garden Hotel | Seoul · Mapo / Gongdeok | Superior Double Room | 1 full bed | Free cancellation before October 29, 2026 | $199 | **$1,595** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/best-western-premier-seoul-garden.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Shilla Stay Gwanghwamun Myeongdong | Seoul · Gwanghwamun / Jongno | Standard Double Room (high floor) | 1 full bed | Free cancellation before October 29, 2026 | $200 | **$1,600** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/shilla-stay-gwanghwamun.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Four Points by Sheraton Josun, Seoul Station | Seoul · Seoul Station (Yongsan-gu) | Superior Double, Guest room, 1 Double, High floor | 1 full bed | Free cancellation before November 1, 2026 | $181 | **$1,609** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/four-points-by-sheraton-seoul-namsan.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel Skypark Myeongdong 3 | Seoul · Myeongdong | Double Room | 1 full bed (prior hotel-confirmed 1400×2000 mm) | Free cancellation before October 29, 2026 | $180 | **$1,612** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/skypark-myeongdong-3.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Sotetsu Hotels The Splaisir Seoul Myeongdong | Seoul · Myeongdong | Deluxe High-Floor Double | 1 full bed | Free cancellation before October 30, 2026 | $204 | **$1,628** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/the-m-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Sejong Hotel Seoul Myeongdong | Seoul · Myeongdong | Deluxe Double Room with Bath | 1 queen bed (338 ft²; extra-long beds) | Free cancellation before October 29, 2026 | $207 | **$1,656** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/sejong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Nine Tree by Parnas Seoul Myeongdong 1 | Seoul · Myeongdong | Double Room | 1 full bed (official Nine Tree spec: 1,600×1,900 mm ≈ queen width) | Free cancellation before October 29, 2026 | $208 | **$1,661** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/nine-tree.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Shilla Stay Samsung COEX Center | Seoul · Gangnam / COEX | Standard Double Room | 1 full bed | Free cancellation before October 29, 2026 | $208 | **$1,661** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/shilla-stay-samsung.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel Entra Gangnam | Seoul · Gangnam / Cheongdam | Deluxe King | 1 king bed | Free cancellation before October 29, 2026 | $186 | **$1,662** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/entra.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel PJ Myeongdong | Seoul · Myeongdong / Euljiro | Deluxe Double Room | 1 king bed | Free cancellation before October 29, 2026 | $189 | **$1,694** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/pj.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| ENA Suite Hotel Namdaemun | Seoul · Namdaemun / City Hall | Deluxe Twin Room (Standard Double 1-king not listed in first rooms) | 2 twin beds | Free cancellation before October 29, 2026 | $213 | **$1,706** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/ena-suite-namdaemun.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| LOTTE CITY HOTEL Mapo | Seoul · Mapo / Gongdeok (Hongdae ca… | Double Room | 1 full bed (280 ft², city view) | Free cancellation before October 29, 2026 | $215 | **$1,723** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/lottecityhotel.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Mercure Ambassador Seoul Dongdaemun | Seoul · Dongdaemun / Euljiro 4-ga (… | Classic Double Room (refundable rate) | 1 full bed (216 ft², city view) | Free cancellation before 6:00 PM on October 31, 2026 | $216 | **$1,727** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/u5.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| L7 GANGNAM by LOTTE HOTELS | Seoul · Gangnam | Standard Double Room with Garden View | 1 queen bed | Free cancellation before October 29, 2026 | $216 | **$1,728** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/l7-gangnam.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel Prince Seoul | Seoul · Myeongdong / Toegye-ro (Jun… | Twin Room B | 2 twin beds (215 ft², high floor) — NOT a one-bed room | Free cancellation before October 25, 2026 | $195 | **$1,751** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/hotel-prince-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Moxy Seoul Insadong by Marriott | Seoul · Insadong / Jongno | Standard Double Room | 1 full bed | Free cancellation before November 1, 2026 | $225 | **$1,799** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/moxy-seoul-insadong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Somerset Palace Seoul | Seoul · Gwanghwamun / Insadong | Executive One-Bedroom | 1 queen bed | Free cancellation before October 30, 2026 | $228 | **$1,824** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/somerset-palace-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel Thomas Myeongdong | Seoul · Myeongdong / City Hall (Jun… | Family Twin Room | 1 twin bed AND 1 full bed (249 ft², city view) — NOT a one-bed room | Free cancellation before October 25, 2026 | $229 | **$1,833** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/thomas-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| G2 Hotel Myeongdong | Seoul · Myeongdong / Supyo-ro (Jung… | Standard Twin Room (No Parking) | 2 twin beds (269 ft², city view) — NOT a one-bed room | Free cancellation before October 18, 2026 | $230 | **$1,840** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/g2-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Nine Tree by Parnas Seoul Dongdaemun | Seoul · Dongdaemun / Euljiro | Semi Double Room | 1 full bed | Free cancellation before October 29, 2026 | $232 | **$1,856** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/nine-tree-dongdaemun.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Nine Tree by Parnas Seoul Insadong | Seoul · Insadong / Gwanghwamun | Deluxe Double w/ Jogyesa View, High Floor, Bath | 1 queen bed | Free cancellation before October 29, 2026 | $235 | **$1,881** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/nine-tree-premier-insadong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Aloft by Marriott Seoul Gangnam | Seoul · Gangnam / COEX (Yeongdong-d… | Aloft River, Guest room, 1 King, River view | ⚠️ Booking bed label: 1 queen bed (258 ft², river view) despite the '1 King' ro… | Free cancellation before October 31, 2026 | $218 | **$1,919** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/aloft-seoul-gangnam.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| L7 HONGDAE by LOTTE HOTELS | Seoul · Hongdae (Mapo-gu) | Standard Double Room | 1 full bed | Free cancellation before October 29, 2026 | $244 | **$1,950** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/l7-hongdae.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Holiday Inn Express Seoul Hongdae by IHG | Seoul · Hongdae (Mapo-gu) | Standard Queen Room with Inner Room - Free Breakfast | 1 queen bed | Free cancellation before 4:00 PM on October 31, 2026 | $255 | **$2,038** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/holiday-inn-express-seoul-hongdae.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel Sunbee Insadong | Seoul · Insadong / Jongno | Deluxe KOR Double Room | 1 queen bed + 1 futon bed | Free cancellation before October 29, 2026 | $233 | **$2,072** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/sunbee.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Four Points by Sheraton Josun, Seoul Myeongdong | Seoul · Myeongdong / Euljiro | Superior room with a double bed and city view | 1 full bed | Free cancellation before October 29, 2026 (row text began “Fre”… | $234 | **$2,081** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/four-points-by-sheraton-seoul-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Ramada by Wyndham Seoul Dongdaemun | Seoul · Dongdaemun (Jung-gu) | Queen Suite (Standard/Superior Double sold out) | 1 full bed | Free cancellation before October 30, 2026 | $236 | **$2,095** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/ramada-seoul-dongdaemun.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hilton Garden Inn Seoul Gangnam | Seoul · Gangnam / Seocho | King Guest Room | 1 king bed | Free cancellation before November 1, 2026 | $267 | **$2,137** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/hilton-garden-inn-seoul-gangnam.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Stanford Hotel Myeongdong | Seoul · Myeongdong | Family Twin Room (2 full beds) — one-bed Standard Double not isolated | 2 full beds | Free cancellation before October 29, 2026 | $269 | **$2,154** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/seutaenpodeuhotel-myeongdong-stanford-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel Skypark Myeongdong 2 | Seoul · Myeongdong | Standard Double Room | 1 full bed | Free cancellation before October 29, 2026 | $243 | **$2,179** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/skypark-myeongdong-2.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Mercure Ambassador Seoul Hongdae | Seoul · Hongdae (Mapo-gu) | Superior King Room | 1 queen bed | Free cancellation before October 31, 2026 | $274 | **$2,190** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/mercure-ambassador-seoul-hongdae.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| LOTTE City Hotel Myeongdong | Seoul · Myeongdong / Euljiro | Standard Double Room | 1 full bed | Free cancellation before October 29, 2026 | $282 | **$2,253** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/lotte-city-seoul-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| AC Hotel by Marriott Seoul Gangnam | Seoul · Gangnam | Queen Bed Room | 1 queen bed | Free cancellation before October 29, 2026 | $282 | **$2,257** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/ac-hotel-by-marriott-seoul-gangnam.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Fraser Place Namdaemun Seoul | Seoul · Namdaemun / City Hall | Premier Twin Room (Premier Double 1-queen NOT listed this window) | 2 twin beds | Free cancellation before October 29, 2026 | $285 | **$2,276** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/fraser-place-namdaemun.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Orakai Insadong Suites | Seoul · Insadong / Jongno (historic… | Two-Bedroom Premier Apartment (3 Adults) — 1 king + 1 twin (cheapest … | 1 king bed + 1 twin bed | Free cancellation before October 27, 2026 | $288 | **$2,302** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/orakai-insadong-suites.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| The Ambassador Seoul - A Pullman Hotel | Seoul · Jangchung / Dongdaemun frin… | Deluxe King Room | 1 king bed | Free cancellation before 6:00 PM on October 31, 2026 | $292 | **$2,336** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/grand-ambassador-seoul-associated-with-pullman.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| L7 MYEONGDONG by LOTTE HOTELS | Seoul · Myeongdong (central Seoul) | Standard Double Room | 1 full bed | Free cancellation before October 29, 2026 | $295 | **$2,358** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/l7-myeongdong-by-lotte.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Mondrian Seoul Itaewon | Seoul · Itaewon (Yongsan-gu) | Signature King Room | 1 king bed | Free cancellation before October 31, 2026 | $302 | **$2,414** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/mondrian-seoul-itaewon.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Nine Tree by Parnas Seoul Myeongdong 2 | Seoul · Myeongdong / Euljiro | Hollywood Double Room | 1 king bed | Free cancellation before October 29, 2026 | $303 | **$2,422** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/nine-tree-premier-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| L'Escape, A Luxury Collection Hotel, Seoul Myeongdong | Seoul · Myeongdong | Classic King Room with City View | 1 king bed | Free cancellation before November 1, 2026 | $305 | **$2,443** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/l-39-escape.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Solaria Nishitetsu Hotel Seoul Myeongdong | Seoul · Myeongdong (Jung-gu) | Casual Double - No Window | 1 full bed (237 ft², ⚠️ no window) | Free cancellation before October 30, 2026 | $306 | **$2,447** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/solaria-nishitetsu-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Moxy Seoul, Myeongdong | Seoul · Myeongdong | Queen Room with City View | 1 queen bed | Free cancellation before November 1, 2026 | $308 | **$2,460** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/moxy-seoul-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| ibis Ambassador Seoul Myeongdong | Seoul · Myeongdong | Standard Double Room | 1 full bed (Accor /6317: 1 x Double bed(s), 21 m²; width unpublished) | Free cancellation before 6:00 PM on October 31, 2026 | $313 | **$2,503** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/ibis-myeong-dong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel Naru Seoul - MGallery Collection | Seoul · Mapo / Hongdae catchment | Superior King Room - Disability Access - Floors 3-5 (No View) | 1 king bed | Free cancellation before 6:00 PM on October 31, 2026 | $314 | **$2,515** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/naru-seoul-mgallery-ambassador.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Royal Hotel Seoul | Seoul · Myeongdong | Premier Double Room | 1 queen bed (Booking; 237 ft²; NOT a king) | Free cancellation before October 30, 2026 | $320 | **$2,556** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/seoul-royal.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Aloft Seoul Myeongdong | Seoul · Myeongdong | Aloft Room, 1 King | 1 king bed | Free cancellation before October 31, 2026 | $323 | **$2,581** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/aloft-seoul-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Courtyard by Marriott Seoul Myeongdong | Seoul · Namdaemun / Myeongdong | Guest Room, 1 King | 1 king bed | Free cancellation before November 1, 2026 | $324 | **$2,595** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/courtyard-by-marriott-seoul-namdaemun.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel28 Myeongdong (Small Luxury Hotels) | Seoul · Myeongdong | Deluxe Double Room | 1 king bed | Free cancellation before October 31, 2026 | $326 | **$2,604** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/hotel28-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| RYSE, Autograph Collection, Seoul | Seoul · Hongdae (Mapo-gu) | Creator King Room | 1 queen bed (Marriott spec: 1 King) | Free cancellation before October 25, 2026 | $329 | **$2,631** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/ryse-autograph-collection-korea.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Novotel Ambassador Seoul Dongdaemun Hotels & Residences | Seoul · Dongdaemun | King Studio Residence | 1 king bed | Free cancellation before October 31, 2026 | $330 | **$2,644** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/novotel-ambassador-seoul-dongdaemun.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Novotel Ambassador Seoul Gangnam | Seoul · Gangnam | Deluxe Queen Room | 1 queen bed | Free cancellation before October 31, 2026 | $335 | **$2,678** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/ambassador-gangnam-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| voco Seoul Gangnam by IHG | Seoul · Gangnam / Sinsa | Premium King Room | 1 king bed | Free cancellation before 4:00 PM on October 31, 2026 | $342 | **$2,732** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/voco-seoul-gangnam-an-ihg.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Grand Mercure Ambassador Hotel and Residences Seoul Yongsan | Seoul · Yongsan (Seoul Dragon City) | Superior Suite | 1 king bed | Free cancellation before October 31, 2026 | $355 | **$2,840** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/grand-mercure-ambassador-seoul-yongsan.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Sofitel Ambassador Seoul Hotel & Serviced Residences | Seoul · Jamsil / Songpa | Luxury Room with 2 Single Beds (lead refundable; King studio also lis… | 2 twin beds | Free cancellation before 6:00 PM on October 31, 2026 | $376 | **$3,011** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/sofitel-ambassador-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Oakwood Premier COEX Center Seoul | Seoul · Gangnam / COEX | 1-Bedroom residence (king-size bed per Booking property text) | 1 king bed | Free cancellation before October 29, 2026 | $351 | **$3,118** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/oakwood-premier-coex-center-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| LOTTE HOTEL SEOUL | Seoul · Myeongdong / City Hall | Main Tower Grand Superior Double | 1 full bed | Free cancellation before October 29, 2026 | $364 | **$3,235** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/lotte-seoul-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| The Westin Seoul Parnas | Seoul · Gangnam / COEX | Club Lounge Access, Guest room, 1 King | 1 king bed | Free cancellation before October 25, 2026 | $392 | **$3,484** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/coex-intercontinental-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| The Westin Josun Seoul | Seoul · City Hall / Myeongdong | Deluxe King Room | 1 king bed | Free cancellation before November 1, 2026 | $398 | **$3,532** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/westin-chosun-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| JW Marriott Dongdaemun Square Seoul | Seoul · Dongdaemun | Deluxe Guest room, 1 King | 1 king bed | Free cancellation before November 1, 2026 | $425 | **$3,774** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/jw-marriott-dongdaemun-square-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| JW Marriott Hotel Seoul | Seoul · Seocho / Gangnam | Deluxe King, Guest room, 1 King, City view | 1 king bed | Free cancellation before November 1, 2026 | $460 | **$4,089** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/jw-marriott-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Grand Hyatt Seoul | Seoul · Itaewon / Namsan (Yongsan-g… | King Room | 1 king bed | Free cancellation before October 31, 2026 | $491 | **$4,317** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/grand-hyatt-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Fairmont Ambassador Seoul | Seoul · Yeouido (financial district… | Fairmont Twin Room (2-adult refundable rate; room attribution by tabl… | 2 twin beds | Free cancellation before 6:00 PM on October 31, 2026 | $583 | **$4,666** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/fairmont-ambassador-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Grand InterContinental Seoul Parnas by IHG | Seoul · Gangnam / COEX | Classic King Room - High Floor | 1 king bed | Free cancellation before October 30, 2026 | $539 | **$4,788** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/grand-intercontinental-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Josun Palace, a Luxury Collection Hotel, Seoul Gangnam | Seoul · Gangnam | State King Room with City View | 1 king bed | Free cancellation before November 1, 2026 | $611 | **$4,888** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/josun-palace-a-luxury-collection-seoul-gangnam.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Le Méridien Seoul, Myeongdong | Seoul · Myeongdong | Deluxe King Room with City View | 1 king bed | Free cancellation before November 1, 2026 | $624 | **$4,992** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/le-meridien-seoul-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Park Hyatt Seoul | Seoul · Gangnam / COEX | 1 King Bed, High Floor, Deluxe | 1 king bed | Free cancellation before October 31, 2026 | $701 | **$5,610** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/park-hyatt-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| ibis Ambassador Suwon | Suwon · Suwon City Hall / Paldal-gu | Standard/Superior Double Room | 1 full / Accor /6528: Standard & Superior = 1 x Double bed(s) (19–20 m²). Width… | Free cancellation before 6:00 PM on October 31, 2026 | $104 | **$834** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/ibis-suwon-ambassador.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Ramada Plaza by Wyndham Suwon | Suwon · Paldal-gu | Superior Double Room (cheapest isolated one-bed refundable this fetch) | 1 full bed (315 ft²) | Free cancellation before October 31, 2026 | $127 | **$1,018** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/ramada-plaza-suwon.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Four Points by Sheraton Suwon | Suwon · Ingye-dong / central Suwon | Premier King Room with City View | 1 king bed (official Marriott /rooms/: Premier Guest room, 1 King) | Free cancellation before November 1, 2026 | $157 | **$1,259** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/four-points-by-sheraton-suwon.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Courtyard by Marriott Suwon | Suwon · Gwanggyo New Town / Yeongto… | Comfortable, Guest room, 1 King | 1 king bed (official Marriott /rooms/: Guest room 1 King) | Free cancellation before November 1, 2026 | $177 | **$1,419** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/courtyard-by-marriott-suwon.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |

---

## 🅲 Table C — Nov 15–22, 2026 · 7 nights

Kept completely separate from Table A and Table B. Capture dates are shown per row.

| Hotel | City · area | Room captured | Beds on the sold row | Refundable — free until | $/night | Total | Captured (UTC) | Verify |
|---|---|---|---|---|---:|---:|---|---|
| Toyoko Inn Busan Station No.1 | Busan · Busan Station / Dong-gu | Economy Double Room | 1 full bed | Free cancellation before November 14, 2026 | $58 | **$406** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/toyoko-inn-busan-no-1.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| ASTI Hotel Busan Station | Busan · Busan Station (Dong-gu) | Standard Double with City View | 1 full bed | Free cancellation before November 14, 2026 (day before) | $78 | **$543** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/asti-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Avani Central Busan | Busan · BIFC / Seomyeon | Deluxe King with Mountain View (high floor) | 1 queen bed (page spec despite 'King' name) | Free cancellation before November 12, 2026 | $86 | **$599** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/avani-central-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Ramada Encore by Wyndham Busan Station | Busan · Busan Station / Dong-gu | Superior Double (Premier $2/nt more) | 1 full bed | Free cancellation before November 13, 2026 | $94 | **$655** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/ramada-encore-by-wyndham-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Crown Harbor Hotel Busan | Busan · Jungang / Nampo | [Busan Minibar] Executive Double City | 1 full bed (291 ft²) | Free cancellation before November 13, 2026 | $98 | **$688** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/crown-harbour-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Fairfield by Marriott Busan | Busan · Haeundae | Standard Room - 1 King Bed with City View | 1 king bed | Free cancellation before November 15, 2026 | $113 | **$793** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/fairfield-by-marriott-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Fairfield by Marriott Busan Songdo Beach | Busan · Songdo Beach | Standard Room - Guest room, 1 King, Sea view | 1 king bed | Free cancellation before November 15, 2026 | $130 | **$912** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/fairfield-by-marriott-busan-songdo-beach.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Wyndham Grand Busan Ijin | Busan · Songdo / Amnam | Premium King Room - Non-Smoking | 1 king bed (401 ft², sea view, hot tub) | Free cancellation before November 14, 2026 | $147 | **$1,027** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/wyndham-grand-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| LOTTE HOTEL BUSAN | Busan · Seomyeon | Deluxe Double Room (city view) | 1 king bed | Free cancellation before November 14, 2026 | $162 | **$1,256** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/lotte-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Shilla Stay Busan Haeundae | Busan · Haeundae (beach) | Standard Double with City View | 1 full bed | Free cancellation before November 12, 2026 | $184 | **$1,288** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/shilla-stay-haeundae.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| L7 HAEUNDAE by LOTTE HOTELS | Busan · Haeundae (beach) | Standard King Town View (4F–9F) | 1 king bed | Free cancellation before November 12, 2026 | $185 | **$1,294** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/l7-haeundae-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| The Westin Josun Busan | Busan · Haeundae / Dongbaek | Deluxe Park King (Dongbaek Park view) | 1 full bed (page spec) | Free cancellation before November 13, 2026 (penalty text cut at… | $224 | **$1,742** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/the-westin-chosun-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Paradise Hotel Busan | Busan · Haeundae beachfront | Deluxe Double City View (Main Building, pool+fitness incl.) | 1 king bed | Free cancellation before November 13, 2026 | $246 | **$1,915** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/paradise-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| SIGNIEL BUSAN | Busan · Haeundae / Mipo | Premier Double with City View (lounge access) | 1 king bed | Free cancellation before November 10, 2026 | $297 | **$2,306** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/signiel-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Grand Josun Busan | Busan · Haeundae (beachfront) | Premier King City View (sauna + private lounge) | 1 queen bed (page spec despite 'King' name) | Free cancellation before November 13, 2026 | $347 | **$2,431** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/grand-josun-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Park Hyatt Busan | Busan · Haeundae (marine city) | King Room with Ocean View | 1 king bed | Free cancellation before November 14, 2026 | $532 | **$3,721** | 2026-08-18 | [dated rate](https://www.booking.com/hotel/kr/park-hyatt-busan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel The Designers Dongdaemun | Seoul · Dongdaemun (Jung-gu) | Deluxe Double Room | 1 full bed | Free cancellation before November 12, 2026 | $73 | **$464** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/the-designers-dongdaemun.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Grid Inn Hotel Jongno | Seoul · Jongno (central) | Twin Room | 2 twin beds | Free cancellation before November 13, 2026 | $80 | **$560** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/grid-inn.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Mangrove Dongdaemun | Seoul · Dongdaemun (Jung-gu) | Budget Twin Room | 1 bunk bed | Free cancellation before November 12, 2026 | $93 | **$653** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/maenggeurobeu-dongdaemun-junggu.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel Cappuccino | Seoul · Gangnam / Eonju | Double Room | 1 king bed (custom 2x2m Super King) | Free cancellation before November 13, 2026 | $101 | **$708** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/cappuccino.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel Migliore Seoul | Seoul · Dongdaemun | Deluxe Double Room (Bathtub Random) | 1 queen bed | Free cancellation before November 12, 2026 | $105 | **$738** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/milreore-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel The Designers Hongdae | Seoul · Hongdae / Hapjeong | Standard Double Room | 1 full bed | Free cancellation before November 13, 2026 | $103 | **$805** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/the-designer-hongdae.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Orakai Daehakro Hotel, BW Signature Collection | Seoul · Jongno / Daehangno | Standard Double Room (Eco Stay & Save) | 1 queen bed | Free cancellation before November 13, 2026 | $117 | **$820** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/orakai-daehakro.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hamilton Hotel Seoul | Seoul · Itaewon (Yongsan-gu) | Standard Double Room | 1 full bed | Free cancellation before November 13, 2026 | $110 | **$863** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/hamilton.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Nine Tree by Parnas Seoul Dongdaemun | Seoul · Dongdaemun / Euljiro | Standard Double Room | 1 full bed | Free cancellation before November 12, 2026 | $129 | **$903** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/nine-tree-dongdaemun.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Dormy Inn EXPRESS SEOUL Insadong | Seoul · Insadong / Jongno | Standard Twin Room | 2 twin beds | Free cancellation before November 12, 2026 | $136 | **$949** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/dormyinnexpressseoulinsadong.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Ramada by Wyndham Seoul Dongdaemun | Seoul · Dongdaemun (Jung-gu) | Superior Double Room | 1 queen bed | Free cancellation before November 13, 2026 | $123 | **$956** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/ramada-seoul-dongdaemun.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Imperial Palace Boutique Hotel Itaewon | Seoul · Itaewon (Yongsan-gu) | Special Offer - Superior Double Room | 1 full bed | Free cancellation before November 14, 2026 | $124 | **$975** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/imperial-palace-boutique.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Seoul Garden Hotel | Seoul · Mapo / Gongdeok | Semi Double Room | 1 twin/full bed | Free cancellation before November 12, 2026 | $143 | **$999** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/best-western-premier-seoul-garden.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Dormy Inn SEOUL Gangnam | Seoul · Gangnam | Standard Queen Room (labeled) | 1 full bed (Booking bed line) | Free cancellation before November 12, 2026 | $143 | **$1,004** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/dormyinn-seoul-gangnam.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Shilla Stay Seocho Gangnam Station | Seoul · Seocho / Gangnam | Standard Double Room | 1 full bed (Shilla double ≈140cm) | Free cancellation before November 12, 2026 | $146 | **$1,019** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/shilla-stay-seocho.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel Peyto Samseong | Seoul · Gangnam / COEX | Deluxe Double Room | 1 full bed | Free cancellation before November 14, 2026 | $146 | **$1,025** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/peyto-samseong.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Ibis Styles Ambassador Seoul Myeongdong | Seoul · Myeongdong | Standard Double Room | 1 double bed (width unpublished; ≈140cm) | Free cancellation before November 14, 2026 | $147 | **$1,027** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/ibis-styles-seoul-myeongdong.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Ibis Ambassador Insadong (newly refurbished) | Seoul · Insadong / Jongno (historic… | Superior Double Room | 1 queen bed (Accor spec) | Free cancellation before November 14, 2026 | $148 | **$1,034** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/ibis-ambassador-insadong.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel Skypark Dongdaemun I | Seoul · Dongdaemun (Jung-gu) | Standard Twin Room | 2 twin beds | Free cancellation before November 12, 2026 | $146 | **$1,056** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/skypark-dongdaemun-i.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel Thomas Myeongdong | Seoul · Myeongdong / City Hall (Jun… | Deluxe Twin Room | 2 twin beds (249 ft², city view) — NOT a one-bed room | Free cancellation before November 8, 2026 | $158 | **$1,106** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/thomas-myeongdong.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Sotetsu Hotels The Splaisir Seoul Myeongdong | Seoul · Myeongdong | Superior Double Room | 1 full bed | Free cancellation before November 13, 2026 | $158 | **$1,108** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/the-m-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| GLAD Gangnam COEX Center | Seoul · Gangnam / COEX | Superior Double Room | 1 full bed | Free cancellation before November 12, 2026 | $162 | **$1,136** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/glad-gangnam-coex-center.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Sotetsu Fresa Inn Seoul Myeong-dong | Seoul · Myeongdong | Standard Double Room | 1 full bed | Free cancellation before November 13, 2026 | $164 | **$1,145** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/sotetsu-fresa-inn-seoul-myeong-dong.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Travelodge Myeongdong Euljiro | Seoul · Myeongdong / Euljiro | Superior Double Room | 1 full bed | Free cancellation before November 13, 2026 | $165 | **$1,152** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/holiday-inn-express-seoul-euljiro.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel Vert | Seoul · Myeongdong | Deluxe Twin Room (only bookable one-room type) | 2 twin beds | Free cancellation before November 12, 2026 | $166 | **$1,162** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/vert.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| GLAD Mapo | Seoul · Mapo / Gongdeok (transit hu… | Standard Double Room | 1 queen bed | Free cancellation before November 12, 2026 | $167 | **$1,168** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/geulraedeu-mapo.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| HOTEL in 9 Gangnam | Seoul · Gangnam / COEX | Standard Double Room | 1 queen bed | Free cancellation before November 13, 2026 | $167 | **$1,168** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/in-9.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Shilla Stay Samsung COEX Center | Seoul · Gangnam / COEX | Standard Double Room | 1 full bed | Free cancellation before November 12, 2026 | $170 | **$1,190** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/shilla-stay-samsung.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Amanti Hotel Seoul Hongdae | Seoul · Hongdae (Mapo-gu) | Standard Double Room | 1 full bed | Free cancellation before November 12, 2026 | $173 | **$1,211** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/amanti-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Shilla Stay Gangnam Yeoksam | Seoul · Gangnam / Yeoksam | Standard Double Room | 1 full bed | Free cancellation before November 12, 2026 | $174 | **$1,216** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/shilla-stay-yeoksam.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Nine Tree by Parnas Seoul Myeongdong 1 | Seoul · Myeongdong | Standard Double Room (1,600 mm queen per official spec) | 1 queen bed | Free cancellation before November 12, 2026 | $174 | **$1,221** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/nine-tree.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel Skypark Myeongdong 2 | Seoul · Myeongdong | Standard Double Room | 1 full bed | Free cancellation before November 12, 2026 | $175 | **$1,225** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/skypark-myeongdong-2.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| LOTTE CITY HOTEL Mapo | Seoul · Mapo / Gongdeok (Hongdae ca… | Double Room | 1 full bed (280 ft², city view) | Free cancellation before November 12, 2026 | $177 | **$1,242** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/lottecityhotel.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Sejong Hotel Seoul Myeongdong | Seoul · Myeongdong | Standard Double Room with Bath | 1 queen bed | Free cancellation before November 12, 2026 | $178 | **$1,244** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/sejong.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel Prince Seoul | Seoul · Myeongdong / Toegye-ro (Jun… | Double Room A (room block RD28644505) | 1 queen bed (high floor) | Free cancellation before November 8, 2026 | $159 | **$1,250** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/hotel-prince-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Henn na Hotel Seoul Myeongdong | Seoul · Myeongdong | Double Room With Complimentary Breakfast | 1 full bed | Free cancellation before November 13, 2026 | $180 | **$1,260** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/bian-nahoteru-souruming-dong.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Amid Hotel Seoul | Seoul · Insadong / Jongno | Standard Double Room | 1 full bed | Free cancellation before November 14, 2026 | $181 | **$1,269** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/centermark.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Sotetsu Hotels The Splaisir Seoul Dongdaemun | Seoul · Dongdaemun (Jung-gu) | Standard Double Room | 1 queen bed | Free cancellation before November 13, 2026 | $163 | **$1,282** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/ky-heritage-dongdaemun.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel Gracery Seoul | Seoul · City Hall / Namdaemun | Superior Double Room (17–20F) | 1 full bed | Free cancellation before November 8, 2026 | $184 | **$1,286** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/gracery-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Klaven Hotel Myeongdong City Hall | Seoul · City Hall / Myeongdong | Superior Double Room | 1 queen bed | Free cancellation before November 12, 2026 | $184 | **$1,289** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/aropa.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel Skypark Myeongdong 3 | Seoul · Myeongdong | Standard Double Room | 1 full bed (≈140cm) | Free cancellation before November 12, 2026 | $168 | **$1,319** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/skypark-myeongdong-3.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Shilla Stay Gwanghwamun Myeongdong | Seoul · Gwanghwamun / Jongno | Standard Double Room | 1 full bed (Shilla double ≈140cm) | Free cancellation before November 12, 2026 | $192 | **$1,341** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/shilla-stay-gwanghwamun.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| ENA Suite Hotel Namdaemun | Seoul · Namdaemun / City Hall | Standard Double Room | 1 king bed | Free cancellation before November 12, 2026 | $193 | **$1,351** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/ena-suite-namdaemun.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Somerset Palace Seoul | Seoul · Gwanghwamun / Insadong | Deluxe One-Bedroom | 1 queen bed | Free cancellation before November 13, 2026 | $193 | **$1,353** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/somerset-palace-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Nine Tree by Parnas Seoul Insadong | Seoul · Insadong / Gwanghwamun | Standard Double Room | 1 queen bed | Free cancellation before November 12, 2026 | $195 | **$1,366** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/nine-tree-premier-insadong.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Fraser Place Namdaemun Seoul | Seoul · Namdaemun / City Hall | Premier Double Room | 1 queen bed | Free cancellation before November 12, 2026 | $202 | **$1,411** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/fraser-place-namdaemun.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel PJ Myeongdong | Seoul · Myeongdong / Euljiro | PJ Signature Twin (Deluxe Double sold out) | 2 twin beds | Free cancellation before November 12, 2026 | $181 | **$1,420** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/pj.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Moxy Seoul Insadong by Marriott | Seoul · Insadong / Jongno | Standard Double Room | 1 full bed | Free cancellation before November 15, 2026 | $203 | **$1,424** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/moxy-seoul-insadong.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Nine Tree by Parnas Seoul Myeongdong 2 | Seoul · Myeongdong / Euljiro | Handicap Double Room (only single queen listed) | 1 queen bed | Free cancellation before November 1, 2026 | $209 | **$1,462** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/nine-tree-premier-myeongdong.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel Entra Gangnam | Seoul · Gangnam / Cheongdam | Deluxe King | 1 king bed | Free cancellation before November 12, 2026 | $187 | **$1,469** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/entra.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| L7 GANGNAM by LOTTE HOTELS | Seoul · Gangnam | Standard Double Room with Garden View | 1 queen bed | Free cancellation before November 12, 2026 | $211 | **$1,480** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/l7-gangnam.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Orakai Insadong Suites | Seoul · Insadong / Jongno (historic… | Two-Bedroom Deluxe Apartment (3 adults) | 1 king + 1 twin (2 bedrooms) | Free cancellation before November 10, 2026 | $213 | **$1,494** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/orakai-insadong-suites.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Mercure Ambassador Seoul Dongdaemun | Seoul · Dongdaemun / Euljiro 4-ga (… | Classic Double Room (refundable rate) | 1 full bed (216 ft², city view) | Free cancellation before 6:00 PM on November 14, 2026 | $218 | **$1,529** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/u5.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel Sunbee Insadong | Seoul · Insadong / Jongno | Deluxe Twin Room | 1 twin bed + 1 queen bed | Free cancellation before November 12, 2026 | $200 | **$1,552** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/sunbee.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| L7 HONGDAE by LOTTE HOTELS | Seoul · Hongdae (Mapo-gu) | Standard Double Room | 1 full bed | Free cancellation before November 12, 2026 | $229 | **$1,601** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/l7-hongdae.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Aloft by Marriott Seoul Gangnam | Seoul · Gangnam / COEX (Yeongdong-d… | Aloft River, Guest room, 1 King, River view | ⚠️ Booking bed label: 1 queen bed (258 ft², river view) despite the '1 King' ro… | Free cancellation before November 14, 2026 | $210 | **$1,619** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/aloft-seoul-gangnam.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Holiday Inn Express Seoul Hongdae by IHG | Seoul · Hongdae (Mapo-gu) | Standard Queen Room with Inner Room - Free Breakfast | 1 queen bed | Free cancellation before 4:00 PM on November 14, 2026 | $235 | **$1,642** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/holiday-inn-express-seoul-hongdae.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| AC Hotel by Marriott Seoul Gangnam | Seoul · Gangnam | Queen Bed Room | 1 queen bed | Free cancellation before November 12, 2026 | $240 | **$1,677** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/ac-hotel-by-marriott-seoul-gangnam.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Four Points by Sheraton Josun, Seoul Station | Seoul · Seoul Station (Yongsan-gu) | Deluxe King, 1 King high floor | 1 king bed | Free cancellation before November 15, 2026 | $219 | **$1,698** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/four-points-by-sheraton-seoul-namsan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| voco Seoul Gangnam by IHG | Seoul · Gangnam / Sinsa | Deluxe Room (Premium King sold out) | 1 full bed | Free cancellation before 4:00 PM on November 14, 2026 | $245 | **$1,713** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/voco-seoul-gangnam-an-ihg.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hilton Garden Inn Seoul Gangnam | Seoul · Gangnam / Seocho | King Guest Room | 1 king bed | Free cancellation before November 15, 2026 | $248 | **$1,734** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/hilton-garden-inn-seoul-gangnam.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| ibis Ambassador Seoul Myeongdong | Seoul · Myeongdong | Standard Double Room | 1 full bed | Free cancellation before 6:00 PM November 14, 2026 | $253 | **$1,771** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/ibis-myeong-dong.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Mercure Ambassador Seoul Hongdae | Seoul · Hongdae (Mapo-gu) | Standard King Room | 1 queen bed | Free cancellation before November 14, 2026 | $257 | **$1,802** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/mercure-ambassador-seoul-hongdae.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Royal Hotel Seoul | Seoul · Myeongdong | Premier Double Room | 1 queen bed | Free cancellation before November 13, 2026 | $268 | **$1,876** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/seoul-royal.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| LOTTE City Hotel Myeongdong | Seoul · Myeongdong / Euljiro | Standard Double Room | 1 full bed | Free cancellation before November 12, 2026 | $268 | **$1,877** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/lotte-city-seoul-myeongdong.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Stanford Hotel Myeongdong | Seoul · Myeongdong | Standard Double Room | 1 full bed | Free cancellation before November 12, 2026 | $277 | **$1,938** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/seutaenpodeuhotel-myeongdong-stanford-myeongdong.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Grand Mercure Ambassador Hotel and Residences Seoul Yongsan | Seoul · Yongsan (Seoul Dragon City) | Junior Suite | 1 king bed | Free cancellation before November 14, 2026 | $280 | **$1,958** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/grand-mercure-ambassador-seoul-yongsan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| L7 MYEONGDONG by LOTTE HOTELS | Seoul · Myeongdong (central Seoul) | Standard Double Room | 1 full bed | Free cancellation before November 12, 2026 | $287 | **$2,012** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/l7-myeongdong-by-lotte.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Aloft Seoul Myeongdong | Seoul · Myeongdong | Aloft Room, 1 King (high floor) | 1 king bed | Free cancellation before November 14, 2026 | $293 | **$2,054** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/aloft-seoul-myeongdong.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Novotel Ambassador Seoul Yongsan | Seoul · Yongsan (Seoul Dragon City) | Superior Double Room | 1 queen bed | Free cancellation before November 14, 2026 | $293 | **$2,054** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/novotel-ambassador-seoul-yongsan.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| The Ambassador Seoul - A Pullman Hotel | Seoul · Jangchung / Dongdaemun frin… | Deluxe King Room | 1 king bed | Free cancellation before 6:00 PM on November 14, 2026 | $296 | **$2,071** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/grand-ambassador-seoul-associated-with-pullman.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Moxy Seoul, Myeongdong | Seoul · Myeongdong | Queen Room with City View | 1 queen bed | Free cancellation before November 15, 2026 | $300 | **$2,097** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/moxy-seoul-myeongdong.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Novotel Ambassador Seoul Gangnam | Seoul · Gangnam | Superior Double Room | 1 queen bed | Free cancellation before November 14, 2026 | $305 | **$2,132** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/ambassador-gangnam-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Mondrian Seoul Itaewon | Seoul · Itaewon (Yongsan-gu) | Signature King Room | 1 king bed | Free cancellation before November 14, 2026 | $305 | **$2,137** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/mondrian-seoul-itaewon.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel28 Myeongdong (Small Luxury Hotels) | Seoul · Myeongdong | Deluxe Double Room | 1 full bed | Free cancellation before November 14, 2026 | $307 | **$2,150** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/hotel28-myeongdong.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| L'Escape, A Luxury Collection Hotel, Seoul Myeongdong | Seoul · Myeongdong | Amour King Room with City View | 1 king bed | Free cancellation before November 15, 2026 | $312 | **$2,187** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/l-39-escape.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| RYSE, Autograph Collection, Seoul | Seoul · Hongdae (Mapo-gu) | Creator King Room | 1 queen bed (Marriott spec: 1 King) | Free cancellation before November 8, 2026 | $316 | **$2,214** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/ryse-autograph-collection-korea.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel Naru Seoul - MGallery Collection | Seoul · Mapo / Hongdae catchment | Superior King Room - Disability Access - Floors 3-5 (No View) | 1 king bed | Free cancellation before 6:00 PM on November 14, 2026 | $319 | **$2,231** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/naru-seoul-mgallery-ambassador.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Solaria Nishitetsu Hotel Seoul Myeongdong | Seoul · Myeongdong (Jung-gu) | Standard Double Room (pay-later rate) | 1 full bed (269 ft², city view) | Free cancellation before November 13, 2026 | $327 | **$2,290** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/solaria-nishitetsu-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Novotel Ambassador Seoul Dongdaemun Hotels & Residences | Seoul · Dongdaemun | King Studio Residence (kitchenette, washer, rooftop pool) | 1 king bed | Free cancellation before November 14, 2026 | $334 | **$2,340** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/novotel-ambassador-seoul-dongdaemun.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Courtyard by Marriott Seoul Myeongdong | Seoul · Namdaemun / Myeongdong | Larger Guest room, 1 King | 1 king bed | Free cancellation before November 15, 2026 | $346 | **$2,423** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/courtyard-by-marriott-seoul-namdaemun.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Fraser Place Central Seoul | Seoul · Jung-gu / Seodaemun (Gwangh… | Super Deluxe Two-Bedroom Apartment | 1 king bed AND 1 queen bed (915 ft², private suite, private kitchen) — two beds… | Free cancellation before November 12, 2026 | $360 | **$2,520** | 2026-08-21 | [dated rate](https://www.booking.com/hotel/kr/fraser-place-central-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Four Points by Sheraton Josun, Seoul Myeongdong | Seoul · Myeongdong / Euljiro | Deluxe King Room with City View | 1 king bed | Free cancellation before November 15, 2026 | $339 | **$2,634** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/four-points-by-sheraton-seoul-myeongdong.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| LOTTE HOTEL SEOUL | Seoul · Myeongdong / City Hall | Main Tower Grand Superior Double | 1 full bed | Free cancellation before November 12, 2026 | $359 | **$2,788** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/lotte-seoul-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Oakwood Premier COEX Center Seoul | Seoul · Gangnam / COEX | 1-Bedroom Superior (king, full kitchen, washer) | 1 king bed | Free cancellation before November 12, 2026 | $359 | **$2,793** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/oakwood-premier-coex-center-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| The Westin Josun Seoul | Seoul · City Hall / Myeongdong | Deluxe King Room | 1 king bed | Free cancellation before November 15, 2026 | $360 | **$2,795** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/westin-chosun-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| JW Marriott Dongdaemun Square Seoul | Seoul · Dongdaemun | Deluxe Guest room, 1 King | 1 king bed | Free cancellation before November 15, 2026 | $390 | **$3,027** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/jw-marriott-dongdaemun-square-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Sofitel Ambassador Seoul Hotel & Serviced Residences | Seoul · Jamsil / Songpa | Luxury King Room (free-cancel tier) | 1 king bed | Free cancellation before 6:00 PM November 14, 2026 | $450 | **$3,152** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/sofitel-ambassador-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| The Westin Seoul Parnas | Seoul · Gangnam / COEX | Club Lounge Access, Guest room, 1 King | 1 king bed | Free cancellation before November 8, 2026 | $442 | **$3,436** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/coex-intercontinental-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| JW Marriott Hotel Seoul | Seoul · Seocho / Gangnam | Deluxe King, Guest room, 1 King, City view | 1 king bed | Free cancellation before November 15, 2026 | $486 | **$3,774** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/jw-marriott-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Le Méridien Seoul, Myeongdong | Seoul · Myeongdong | Club King Room with City View (club lounge) | 1 king bed | Free cancellation before November 15, 2026 | $576 | **$4,029** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/le-meridien-seoul-myeongdong.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Fairmont Ambassador Seoul | Seoul · Yeouido (financial district… | Fairmont King (free-cancel tier) | 1 king bed | Free cancellation before 6:00 PM November 14, 2026 | $587 | **$4,109** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/fairmont-ambassador-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Josun Palace, a Luxury Collection Hotel, Seoul Gangnam | Seoul · Gangnam | Masters King Room with City View | 1 king bed | Free cancellation before November 15, 2026 | $612 | **$4,286** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/josun-palace-a-luxury-collection-seoul-gangnam.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Grand Hyatt Seoul | Seoul · Itaewon / Namsan (Yongsan-g… | King Room with River View | 1 king bed | Free cancellation before November 14, 2026 | $669 | **$5,151** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/grand-hyatt-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Park Hyatt Seoul | Seoul · Gangnam / COEX | 1 King Bed, High Floor, Deluxe | 1 king bed | Free cancellation before November 14, 2026 | $757 | **$5,299** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/park-hyatt-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Grand InterContinental Seoul Parnas by IHG | Seoul · Gangnam / COEX | Grand Deluxe King (free-cancel tier) | 1 king bed | Free cancellation before November 13, 2026 | $920 | **$7,147** | 2026-08-19 | [dated rate](https://www.booking.com/hotel/kr/grand-intercontinental-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |

---

## 🆕 New entries — area-by-area batches (2026-08-21)

Added to the master list only after identity, coordinates, bed count **and** a dated refundable rate for every relevant window were all sourced from pages actually fetched.

### Round 13 — Dongnae hot springs + a Centum City minefield (1 added)

| New entry | Area | Room / bed count | Nov 9–15 (6 nt) refundable | Cancellation | Verify |
|---|---|---|---|---|---|
| **Nongshim Hotel** | Dongnae / Oncheonjang hot springs | Queen Room — ⚠️ Booking says **1 full bed**, 305 ft², **free hot-spring coupon for 2** | **$128/nt · $862** | Free until **1 day** out, then first night — ⚠️ but a **no-show costs the TOTAL stay** | [dated rate](https://www.booking.com/hotel/kr/nongshim.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [official Hotel Nongshim](https://www.hotelnongshim.com/kr/index.php?pCode=Hurshimchung) |

Opens **Dongnae / Oncheonjang**, and it's the only record in the project attached to a major Korean bathhouse — **Hurshimchung** is on site. It sits beside **Oncheonjang Station (Metro Line 1)**, so unlike the Gijang resort this is a genuine transit base, and it has **on-site laundry facilities**. A cheaper **Korean-Style Ondol Double** (underfloor heating, no carpet) is $117/nt · $788.

### ⚠️ Centum City is an identity minefield — nothing added there on purpose

Four separately-named listings resolve to just **two street addresses**:

| Listing | Address | Coordinates |
|---|---|---|
| Centum Business Hotel | 17 Centum 1-ro | 35.166935 / 129.13159 |
| Centum **Primus** Hotel | 17 Centum 1-ro | 35.166668 / 129.13153 |
| Centum **Premier** Hotel | 17 Centum 1-ro | 35.16693878 / 129.13160705 |
| Haeundae Centum Hotel | 20 Centum 3-ro | 35.16772 / 129.13297 |
| Centum **Convention** Hotel | 20 Centum 3-ro | 35.1678 / 129.13292 |

The page titled *"Centum Primus Hotel"* even **opens its description with "Centum Premier Hotel is a hotel situated in Busan"** — the third-party data is cross-contaminated. These are near-duplicate listings of at most **two** real properties.

**No Centum record was created.** This is precisely the duplicate scenario the validator exists to catch, and third-party data alone cannot separate them. Held out with coordinates recorded: **Haeundae Centum Hotel** (543 rooms, self-serve laundry, washing machine, airport transfer, walk to Shinsegae Centum City and BEXCO) is the most credible candidate but shares its address with the "Centum Convention Hotel" listing.

**🚩 Other flags on round 13:**

1. **Seventh room-name / bed-label conflict:** Nongshim's *"Queen Room"* is stated by Booking as **1 full bed**.
2. **No-show asymmetry:** in-window cancellation costs one night, but a **no-show costs the entire reservation**.
3. An older address form (*137-7 Onchun-Dong, Dongrae-gu*) appears on one aggregator — verified as the legacy lot-based form of the same site, consistent to 4 decimal places, **not** a second property.
4. Breakfast rated 6.5/10; check-in 14:00 is third-party, check-out not captured.

### Round 12 — Gijang / east coast (1 added · a rebrand untangled)

| New entry | Area | Room / bed count | Nov 9–15 (6 nt) refundable | Cancellation | Verify |
|---|---|---|---|---|---|
| **Ananti at Busan Cove (Ananti Hilton Busan)** | Gijang / Ananti Cove — east coast | Cabin S Forest View Twin — **2 twin beds**, **753 ft²**, balcony + terrace + in-room **spa tub** | **$191/nt · $1,144** | Free until **14 days** out, then the **first night only** | [dated rate](https://www.booking.com/hotel/kr/hilton-busan.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [official Hilton page](https://www.hilton.com/en/hotels/pushihi-ananti-hilton-busan/) |

Opens **Gijang-gun / the east coast**, a district the list had never touched, and it is the first Busan record pairing a genuine **first-party Hilton page** with a live dated rate.

### 🔀 Identity untangled: Hilton Busan = Ananti Hilton Busan = Ananti at Busan Cove

The Booking slug is literally `hilton-busan`, but the page now titles the property **"Ananti at Busan Cove"**, while Hilton's own site still markets it as **"Ananti Hilton Busan"**. Four independent signals confirm one site:

- identical address — 268-32 Gijanghaean-ro, Gijang-eup, 46083
- identical coordinates — 35.198 / 129.228864 (Hilton) vs 35.198 / 129.22886 (Michelin Guide)
- identical phone — +82 51-509-1111
- a third listing states outright *"Ananti At Busan Cove — ex. Ananti Hilton Busan"*

Recorded as **one** record, no duplicate. ⚠️ **Residual risk logged:** Ananti Cove is a resort *complex* that may contain more than one lodging product (hotel / penthouse / villas). If a second Ananti Cove product is ever added, cross-check address and room count first.

### ⚠️ The trap on this property: an inverted cancellation ladder

Three refundable tiers on the same Cabin S room, and **paying more buys you a shorter runway** — with the middle tier being the worst of both worlds:

| Rate | Free until | Penalty inside the window |
|---:|---|---|
| **$191/nt** | **14 days** out | first night only |
| $216/nt | 7 days out | ⚠️ **the TOTAL reservation** |
| $254/nt | 5 days out | first night only |

The cheapest option here is also the most flexible. The $216 tier costs more than $191 *and* exposes you to the entire stay. Anyone skim-reading "free cancellation" would pick badly.

**Other flags:** check-out conflict — Hilton's visible text says **11:00**, its own structured data says **12:00** · no single-bed room captured (a same-priced sibling row's header fell outside the fetched chunk and is deliberately not recorded) · resort location with **no walkable rail** and no airport shuttle · `stars: 5` is third-party.

### Rounds 10–11 — Busan batch (2 added · a whole district found *and closed*)

| New entry | Area | Room / bed count | Nov 9–15 (6 nt) refundable | Cancellation | Verify |
|---|---|---|---|---|---|
| **Hotel Foret Premier Nampo** | Nampo / BIFF Square (Jung-gu) | Family Twin — **1 twin + 1 full**, 258 ft² | **$100/nt · $601** | Free until **3 days** out — ⚠️ inside that, **and on a no-show, the fee is the TOTAL stay** | [dated rate](https://www.booking.com/hotel/kr/foret-premier-nampo.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |

**The cheapest verified Busan option for your window**, and only the second Nampo/BIFF Square record alongside Crown Harbor. Guests place it steps from Jagalchi Market, BIFF Square and the subway.

### 🔍 Gwangalli coverage gap — found **and closed**

Busan has two main beach districts. The list covered **Haeundae** heavily (11 records) plus Seomyeon, Busan Station, Nampo, Songdo and Yeonsan — but **not a single property in Gwangalli (Suyeong-gu)**, the quieter beach opposite Gwangan Bridge. That hole was invisible until this pass.

**It is now closed.** After `kent-hotel-gwangalli` 404'd, the correct Booking slug turned out to be **`kent-gwangalli`**:

| New entry | Area | Nov 9–15 (6 nt) | Verify |
|---|---|---|---|
| **Kent Hotel Gwangalli by Kensington** | Gwangalli Beach (Suyeong-gu) | ⚠️ **ZERO availability** — every room type marked *Not available on our site for your dates* | [dated Booking page](https://www.booking.com/hotel/kr/kent-gwangalli.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |

It is recorded **anyway**, with no price invented, so the option set represents the district instead of silently omitting it. Full room inventory captured: Executive Double Ocean View (1 queen) · Deluxe Twin City View (1 twin + 1 full) · Cinema Twin No View (2 twin) · Suite with Sea View (1 full + 1 sofa bed) · Twin Room (2 full). Beachfront, 15th-floor Sky Lounge, free parking, 24-hour desk; check-in 15:00–24:00 with photo ID **and** credit card required plus advance notice of arrival; children 6+ charged as adults.

### ⚠️ Second market signal — Busan is tightening too

Booking displayed on this property:

> *"Limited supply in Busan for your dates: **2 four-star hotels like this are already unavailable on our site**."*

That mirrors the Seoul five-star signal found in round 9 (*"2 five-star hotels like this are already unavailable"* for Nov 1–9). **Two independent tiers, two different cities, both windows** — inventory is visibly thinning. Combined with Ramada Encore Haeundae already verified sold out and Paradise showing only two rate rows, the Nov 9–15 Busan window is not as open as the 19-row table makes it look.

### Still held out in Gwangalli / Busan

| Candidate | Why |
|---|---|
| **H Avenue Gwangalli** | ⚠️ **Identity ambiguity — deliberately not added.** Sources disagree on the address (*29 Millaksubyeon-ro* vs *42 Gwanganhaebyeon-ro 278beon-gil*) and on coordinates, the name appears as "H Avenue Gwangalli", "…Gwangalli branch" and "…Gwangalli Beach", and guests report it occupies floors 8–10 of a building **housing four other hotels**. This may be more than one property. Needs an independent identity source first. |
| Hound Premier Hotel Nampo | Identity + coordinates confirmed (35.099094 / 129.02522); Booking slug still unresolved. |
| Toyoko Inn Busan Seomyeon | Identity confirmed; coordinates not yet obtained, and the chain's ~3-month direct-booking window makes a Booking rate unlikely. |

**🚩 Flags on round 10:**

1. **A separate CITY TAX is excluded on top of 10% TAX** at Foret Premier Nampo — only the second Busan record with a second tax line. The $601 is not the amount you pay.
2. **Cancellation inside 3 days *and* a no-show both cost the TOTAL stay.**
3. **Photo ID *and* credit card required at check-in**, and the property asks to be told your arrival time in advance.
4. **No single-bed room captured** — the named room is a twin + full. `fits: false`.
5. Only **2 rooms left** at capture; breakfast rated 6.7/10.
6. Booking's own address line wasn't in the captured chunk, so the street address rests on an independent listing.

### Round 9 — Re-verification round 2 · every no-rate record now has a *reason* (0 added)

Two more single-check negatives were re-tested, and — more importantly — **all 19 records without a live rate now carry an explicit `distributionStatus`**, so a blank price cell can never be misread as "sold out".

| Property | Finding on re-check (2026-08-21) |
|---|---|
| **Four Seasons Hotel Seoul** | ⚠️ **Confirmed zero inventory for Nov 1–9 — second independent negative.** All 13+ room types unbookable (Deluxe King, Club Double, Grand Family King, Premier Family King, Executive King Suites City/Palace View, King Suites, Two- and Three-Bedroom Suites…). **Booking also displayed a market signal: _"Limited supply in Seoul for your dates: 2 five-star hotels like this are already unavailable on our site."_** Luxury inventory for this window is tightening. |
| **Toyoko Inn Seoul Dongdaemun II** | Still not on sale — **and it is structural, not sold out.** Toyoko opens its own booking window ~3 months ahead and sells direct. Newly captured: check-in 15:00–24:00, **check-out 10:00**, minimum age 18, children 7+ charged as adults, no cribs or extra beds, cash accepted, licence 제2018-00012호. Guests place it ~20 m from Dongdaemun History & Culture Park station. Book at toyoko-inn.com. |

### Why a blank price is not one thing

Every no-rate record is now labelled with **why** it has no rate:

| `distributionStatus` | Records | What it means for you |
|---|---|---|
| **On Booking, no inventory for our window (verified)** | Four Seasons Seoul · THE PLAZA Autograph · Ramada Encore Busan Haeundae | Genuinely full for these dates on this channel. Try the brand direct. |
| **Direct-book only** | Toyoko Inn Dongdaemun II · Nine Tree ROKAUS Yongsan · Novotel Ambassador Suwon (Accor) · SONO Calm Gyeongju | The hotel is fine — it just doesn't sell this stay through Booking. Go to the operator. |
| **Not distributed on Booking.com** | ibis Ambassador Busan Haeundae · ibis budget Ambassador Busan Haeundae | Not on the platform at all. Accor direct only. |
| **Unclassified — not yet re-tested** | 10 records (6 Gyeongju incl. 3 hanoks · 2 Cheonan · 3 Daejeon minus overlap) | Carries an old negative but has **not** been re-checked. **Do not read the absence of a rate as "sold out."** |

That last row is the honest one: ten records are still unknown rather than unavailable, and the data now says so in the record itself instead of implying it by omission.

### Round 8 — Re-verification pass (0 added, 2 findings hardened)

No new entries this round. Two records that previously said "unavailable" on a **single** check were re-tested, because a one-off negative is not proof.

| Property | Finding on re-check (2026-08-21) |
|---|---|
| **THE PLAZA Seoul, Autograph Collection** | ⚠️ **Confirmed unavailable for Nov 1–9 — second independent negative, three days after the first.** All seven room types are marked *Not available on our site for your dates*: Premier Suite (1 king), Business King (1 king), Prestige Suite (1 king), Residential Suite w/ Club Lounge (1 king), Deluxe Guest room (1 twin + 1 king), Club Deluxe Twin (2 twin), Deluxe Twin (2 twin). Newly captured: check-in 15:00 / check-out 11:00, **photo ID *and* credit card required at check-in**; indoor pool, spa, airport shuttle; guests confirm it is connected to City Hall metro with the Incheon airport bus stopping outside. **Book Marriott/Autograph direct — Booking simply holds no inventory for this 8-night span.** |
| **Hotel Midcity Myeongdong** | Still no availability for Nov 1–9 — but with an important nuance. Booking served its **alternative-dates widget** instead of a rate table, and that widget shows the property **is** selling adjacent ranges: Nov 8–14 from $1,546, **Nov 9–15 from $1,641**, Nov 11–18 from $1,851, Nov 8–16 from $2,128. So this is **not** a closed or sold-out hotel — the exact **8-night Nov 1–9 span** is what fails. Those totals are for *other* date ranges and are deliberately **not** recorded as our-window rates. |

**Why this matters:** the repo previously carried THE PLAZA with the honest caveat *"negative result on one source at one moment — not proof the hotel is full."* It now has two negatives three days apart, so the caveat is retired. Midcity's result changes shape entirely: the property is open and selling, and a one-night shift in either direction would likely make it bookable.

**Still outstanding — 15 records carry no live rate in any window:** Four Seasons Seoul, Toyoko Inn Dongdaemun II, Nine Tree ROKAUS Yongsan, Novotel Ambassador Suwon, 2 Cheonan, 3 Daejeon and 6 Gyeongju properties. Several are structural rather than sold out (Toyoko only opens its booking window ~3 months ahead; the Gyeongju hanoks and SONO are direct-book inventory).

### Round 7 — Myeong-dong completed (1 added)

| New entry | Area | Nov 1–9 (8 nt) refundable | Nov 15–22 (7 nt) refundable | Cancellation | Verify |
|---|---|---|---|---|---|
| **Hotel Thomas Myeongdong** | Myeongdong / City Hall (Jung-gu) | Family Twin — **1 twin + 1 full**, 249 ft² — **$229/nt · $1,833** | Deluxe Twin — **2 twin**, 249 ft² — **$158/nt · $1,106** | Free until **7 days** out in both windows — ⚠️ inside that, **and on a no-show, the fee is the TOTAL stay** | [Nov 1–9](https://www.booking.com/hotel/kr/thomas-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Nov 15–22](https://www.booking.com/hotel/kr/thomas-myeongdong.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |

At **$158/night** this is the cheapest Seoul property verified in both windows anywhere in this series — but read the flags before treating that as a bargain.

**🚩 Flags on round 7:**

1. **Booking's own room data contradicts itself on the bathroom.** The amenity list for these rooms shows **both "Attached bathroom" and "Shared toilet"**. The private-bathroom requirement is therefore **not established**. Confirm before booking.
2. **No single-bed room exists in either window** — Family Twin is twin+full, Deluxe Twin is 2 twin. `fits: false`.
3. **The $158 and $229 are Genius member prices**, 38–43% below the displayed originals ($1,956.54 and $2,951.86). The public price is much higher.
4. **The two windows use different room codes**, so the price gap is not movement.
5. **Prepayment differs by window** — pay-at-property for Nov 1–9, payment due Nov 6 for Nov 15–22.
6. **Breakfast is rated 5.6/10** by Booking guests — the lowest of anything added in this series.

**Myeong-dong is now closed out**, except **Hotel Midcity Myeongdong** (URL known; showed no availability in either window on 2026-08-19, needs one re-check).

### Round 6 — Myeong-dong continued (1 added · 1 property eliminated outright)

| New entry | Area | Room / bed count | Nov 1–9 (8 nt) refundable | Nov 15–22 | Cancellation | Verify |
|---|---|---|---|---|---|---|
| **G2 Hotel Myeongdong** | Myeongdong / Supyo-ro (Jung-gu) | Standard Twin Room (No Parking) — **2 twin beds**, 269 ft² | **$230/nt · $1,840** | ⚠️ **not captured** — Booking truncated twice | Free until **14 DAYS** out — ⚠️ inside that, **and on a no-show, the fee is the TOTAL stay** | [Nov 1–9](https://www.booking.com/hotel/kr/g2-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Nov 15–22](https://www.booking.com/hotel/kr/g2-myeongdong.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |

Booking states a **7-minute walk to two different subway stations** — Myeongdong (Line 4) *and* Chungmuro (Lines 3 and 4) — and its own photo set shows a guest laundry room.

### ❌ Metro Hotel Myeongdong — eliminate from consideration

Its Booking page carries a property notice of a **renovation scheduled 2026-06-16 → 2027-02-28**, and Booking reports reservations cannot be made. **That window covers all three of our stays** (Nov 1–9, Nov 9–15 and Nov 15–22). This is not a "check back later" — it is closed for the entire trip.

**🚩 Flags on round 6:**

1. **G2 has the longest free-cancellation deadline in the dataset — 14 days — but the harshest penalty after it.** Cancel inside 14 days, or no-show, and you pay the **whole reservation**. A second rate tier is 7 days on the same total-price terms. Long runway, cliff edge at the end.
2. **G2 is twin-only on the evidence available.** The only named, priced room in the Nov 1–9 table is a 2-twin Standard Twin, and the 2026-08-19 audit also found only twins. `fits: false`.
3. **G2's Nov 15–22 window is genuinely missing.** Booking truncated before the rate table on two attempts. The 2026-08-19 audit recorded $180/nt · $1,260 for the same room, but that is a **prior-pass figure and is deliberately not stored as a live rate**.
4. **Four more G2 rate rows were captured without room names** ($207, $222, $300, $322/nt) because their headers fell outside the fetched chunks. Recorded in the note, not guessed into rows.
5. G2 has no `officialUrl` yet; `stars: 4` is from a third-party listing.

**Still open in Myeong-dong:** Hotel Thomas Myeongdong — **identity and coordinates now confirmed** (26 Sejong-daero 16-gil, 37.56312942 / 126.97834777, 3-star, check-in 15:00/out 12:00, laundry service, near City Hall metro) but rates not yet fetched. Hotel Midcity Myeongdong — URL known, showed no availability in either window on 2026-08-19, needs a re-check.

### Round 5 — Myeong-dong (2 added, recovered from the repo's own guide files)

I said last round that Myeong-dong would mostly yield rebrands. That was **wrong**, and here is the correction: the repo's older guide files already contained **working Booking URLs for six Myeongdong properties that were never attached to any master record**. No slug guessing was needed — they were sitting in `guide/`. Two of them are now fully verified in both windows.

| New entry | Area | Room / bed count | Nov 1–9 (8 nt) refundable | Nov 15–22 (7 nt) refundable | Cancellation | Verify |
|---|---|---|---|---|---|---|
| **Solaria Nishitetsu Hotel Seoul Myeongdong** | Myeongdong (Jung-gu) | Nov 1–9: Casual Double **No Window** — 1 full bed, 237 ft² · Nov 15–22: Standard Double — 1 full bed, 269 ft² | **$306/nt · $2,447** | **$327/nt · $2,290** | Free until **2 days** out — ⚠️ inside that, **and on a no-show, the fee is the TOTAL stay** | [Nov 1–9](https://www.booking.com/hotel/kr/solaria-nishitetsu-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Nov 15–22](https://www.booking.com/hotel/kr/solaria-nishitetsu-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| **Hotel Prince Seoul** | Myeongdong / Toegye-ro (Jung-gu) | Nov 1–9: Twin Room B — 2 twin, 215 ft² · Nov 15–22: **Double Room A — 1 queen bed** | **$195/nt · $1,751** | **$159/nt · $1,250** ⚠️ member price | Free until **SEVEN days** out — the longest runway in the entire dataset | [Nov 1–9](https://www.booking.com/hotel/kr/hotel-prince-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Nov 15–22](https://www.booking.com/hotel/kr/hotel-prince-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |

Both had been **held out by the 2026-08-19 Myeongdong audit** purely because the row captured then happened to be a twin. Single-bed rooms are confirmed sellable at both, so both now belong in the list.

**🚩 Flags on round 5:**

1. **Hotel Prince has the best cancellation terms in the whole project — free until 7 days before arrival**, in both windows. Every other record is 1–3 days. Worth knowing while plans are still moving.
2. **…but Prince's $159 is a members-only price.** The displayed stack is original $1,888.56 → bonus −$339.94 → Genius −$188.86 → pay-online −$110.25 → $1,249.51. Budget the public figure.
3. **Prince's no-show fee is the TOTAL reservation**, even though in-window cancellation is only the first night.
4. **Solaria's penalty is the harshest found so far:** inside 2 days *and* on a no-show, you are charged the **entire stay**.
5. **Solaria's only "king" row is a trap.** *Hollywood Double* — Booking says "1 king bed", but a Hollywood configuration is **two mattresses pushed together**. Sixth property in this series with a bed-label conflict.
6. **Solaria's Nov 1–9 room has no window.** The captured refundable row is literally *"Casual Double - No Window"*, 237 ft². Fine for a night, questionable for eight.
7. **Neither hotel's two windows are like-for-like** — different room codes in each window. Do not read the price gaps as movement.
8. **Prince's queen-row label was cut** in today's capture; the name *Double Room A* is carried from this repo's own 2026-08-19 audit of the **same Booking room block ID (RD28644505)** — matched, not invented.
9. Neither has an `officialUrl` yet; Solaria's `hasOnSiteLaundry: true` rests on a third-party amenity list.

**Still held out in Myeong-dong (URLs known, work remaining):** G2 Hotel Myeongdong (twin-only rows captured so far), Hotel Thomas Myeongdong (rate block never fully captured), Hotel Midcity Myeongdong (previously showed no availability in either window).

### Round 4 — Gangnam (1 added, 2 held out; 1 earlier hold-out re-verified)

| New entry | Area | Room / bed count | Nov 1–9 (8 nt) refundable | Nov 15–22 (7 nt) refundable | Cancellation | Verify |
|---|---|---|---|---|---|---|
| **Aloft by Marriott Seoul Gangnam** | Gangnam / COEX (Yeongdong-daero) | Aloft River, Guest room, 1 King, River view — ⚠️ Booking says **1 queen bed**, 258 ft² | **$218/nt · $1,919** | **$210/nt · $1,619** | Free until **1 day** before arrival in both windows; then the first night. **No prepayment — pay at the property.** | [Nov 1–9](https://www.booking.com/hotel/kr/aloft-seoul-gangnam.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Nov 15–22](https://www.booking.com/hotel/kr/aloft-seoul-gangnam.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |

Same room code in both windows, so these are comparable: **−4% in the later window**. This is the **first new entry in the series with `hasOnSiteLaundry: true`** and only the second with a genuine `officialUrl` (Marriott).

**🚩 Flags on round 4:**

1. **King name, queen label — again.** Marriott markets it as *"Guest room, 1 King"*; Booking states **1 queen bed** on the row actually sold. Unresolved, so `fits: false`.
2. **A Hollywood room is also sold here.** *Aloft Urban Hollywood, Guest room, 1 King* — a Hollywood bed is **two mattresses pushed together**, not a single king. Avoid if you want one mattress.
3. **The laundry claim is third-party.** `hasOnSiteLaundry: true` rests on an independent structured amenity list ("Self-serve laundry", "Washing machine"); Booking's captured facility list did not repeat it. Verify.
4. **`stars: 4` and the check-in/check-out times** come from independent listings, not the captured Booking page.
5. **A cheaper unnamed row exists** at $1,793 for 8 nights, above the Aloft River rows — its room name was cut at a page-chunk boundary, so it is recorded in the note rather than as a named row.

**Investigated, not added:**

| Candidate | Finding |
|---|---|
| **InterContinental Seoul COEX** (524 Bongeunsa-ro, Gangnam-gu) | Identity confirmed by two independent listings — address, coordinates 37.51286 / 127.05711, direct COEX Mall access, indoor pool. But **two Booking slug attempts both 404'd**, so no dated rate page could be reached. Not added without a rate. Note this is a **different hotel** from Grand InterContinental Seoul Parnas, which is already in the list. |
| **Andaz Seoul Gangnam, By Hyatt** | **Re-verified 2026-08-21 — still no sellable inventory for Nov 1–9.** Every room type (Premium King, Premium Twin, King Room High Floor, Twin Room High Floor) is marked *Not available on our site for your dates*. This confirms the 2026-08-19 batch-5 finding rather than leaving it stale. House rules captured: check-in 15:00, check-out 11:00, **minimum check-in age 20**, pets not allowed, children 13+ charged as adults. Guests consistently report a direct connection to **Apgujeong Station (Line 3)**. Direct-booking follow-up only. |

### Round 3 — Itaewon + Jongno (1 added, 2 held out with findings)

| New entry | Area | Room / bed count | Nov 1–9 (8 nt) | Nov 15–22 (7 nt) refundable | Cancellation | Verify |
|---|---|---|---|---|---|---|
| **Fraser Place Central Seoul** | Jung-gu / Seodaemun (Gwanghwamun–Jongno fringe) | Super Deluxe Two-Bedroom Apartment — **1 king + 1 queen** (two beds), 915 ft², **private kitchen** | ⚠️ **No availability at all** — every room type marked *Not available on our site for your dates* | **$360/nt · $2,520** | Free until **3 days** out (Nov 12); pay nothing until Nov 10 | [Nov 1–9](https://www.booking.com/hotel/kr/fraser-place-central-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Nov 15–22](https://www.booking.com/hotel/kr/fraser-place-central-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |

First entry in this project with a real **`officialUrl`** (Frasers Hospitality) rather than a Booking-only identity, and the first with a **private kitchen** in the unit — relevant on a 7-night leg.

**🚩 Flags on round 3:**

1. **Not a one-bed option.** Every unit captured — including the one called *One-Bedroom Family Apartment* — is listed by Booking as **1 king bed AND 1 queen bed**. `fits: false`.
2. **Window-specific availability.** Zero availability Nov 1–9; bookable and refundable Nov 15–22. No cross-window comparison is possible for this property.
3. **Address disagreement between sources.** Booking's own address line was not inside the captured chunks. Third-party listings give *78 Tongil-ro, Jung-gu 04517* (used here, with its coordinates), *1-202 Uiju-ro 1-ga, Jung-gu* (the old lot form of the same address) and *19-1 Sogong-ro 5-gil* (inconsistent). Confirm before travelling.
4. **A cheaper refundable row exists but is unnamed.** 732 ft², also 1 king + 1 queen with a private kitchen, 5 left, **$280/nt · $1,959** on identical terms — its room name was cut at a page-chunk boundary, so it is recorded in the note rather than as a named row.
5. **In-unit washer/dryer is guest-reported only**, so `hasOnSiteLaundry` stays `false`.
6. Distinct property from **Fraser Place Namdaemun Seoul**, which is already in the list.

**Investigated, not added — with the finding recorded:**

| Candidate | Finding |
|---|---|
| **Nouvelle Hotel Seoul Itaewon by Anook** (11 Usadan-ro 14-gil, Yongsan-gu) | Identity and coordinates confirmed, and the **entire Nov 1–9 rate table was read end to end** — **every single row is "Non-refundable, pay online."** There is no refundable rate to record. Cheapest row $110/nt ($881 Genius/pay-online member price off $1,064.03); Deluxe Twin (2 twin) $122/$979; Suite (2 full beds) $248/$1,988. Booking also states **children are not allowed** and the **minimum check-in age is 19**. Held out; the finding is logged in `data/pricing-history.json`. |
| **Hotel Aventree Jongno** (46 Ujeongguk-ro, Jongno-gu) | Identity solid — three independent listings agree on the address and coordinates 37.573027 / 126.98301, minutes on foot from Jonggak Station (Line 1). But **two Booking slug attempts both returned a 404**, so no dated rate page could be reached: no price, no bed count, no cancellation term. Star rating also disagrees across sources (3, 3.5, 4). Needs the correct slug before it can be added. |

### Round 2 — Dongdaemun + Mapo/Gongdeok (both Seoul windows captured)

| New entry | Area | Room / bed count | Nov 1–9 (8 nt) refundable | Nov 15–22 (7 nt) refundable | Cancellation | Verify |
|---|---|---|---|---|---|---|
| **Mercure Ambassador Seoul Dongdaemun** | Dongdaemun / Euljiro 4-ga (Jung-gu) | Classic Double Room — **1 full bed**, 216 ft² | **$216/nt · $1,727** | **$218/nt · $1,529** | Free until **6:00 PM the day before arrival** in both windows; then the first night. Pay nothing until 2 days before. | [Nov 1–9](https://www.booking.com/hotel/kr/u5.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Nov 15–22](https://www.booking.com/hotel/kr/u5.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| **LOTTE CITY HOTEL Mapo** | Mapo / Gongdeok (Hongdae catchment) | Double Room — **1 full bed**, 280 ft² | **$215/nt · $1,723** | **$177/nt · $1,242** | Free until **3 days** before arrival in both windows; then the first night. **No prepayment — pay at the property.** | [Nov 1–9](https://www.booking.com/hotel/kr/lottecityhotel.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) · [Nov 15–22](https://www.booking.com/hotel/kr/lottecityhotel.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |

Both rows use the **same room code in both windows**, so those two prices *are* comparable: Mercure is flat ($216 → $218/nt), LOTTE City Mapo is **~18% cheaper in the later window** ($215 → $177/nt).

**🚩 Flags on round 2:**

1. **Identity collision RESOLVED.** The 2026-08-19 batch flagged that `booking.com/hotel/kr/u5.html` ("Hotel U5") resolved to a different name. Confirmed: that URL now serves **Mercure Ambassador Seoul Dongdaemun** at 369 Dongho-ro. Recorded as **one** property under the Mercure name — **no duplicate "Hotel U5" record was created**.
2. **Neither hotel is a core-needs match.** Every one-bed room captured at both properties is labelled **"1 full bed"** by Booking, with no published width. `fits` is `false` on both.
3. **LOTTE Mapo has an unresolved full-vs-queen conflict.** A Booking room-type index lists *Run of House*, *Standard Double with Late Check-in 18:00* and *[Swimming Pool PKG for 2] Standard Double with Bath* as **1 queen bed**, while every dated rate row captured for our windows says **1 full bed** for the same room names. Settle this with the property before assuming a queen.
4. **Headline prices at Mercure are non-refundable.** $177/nt (Nov 1–9) and $179/nt (Nov 15–22) are pay-online, no-refund. The refundable rates are $216 and $218.
5. **Neither has an `officialUrl` yet.** The all.accor.com and lottehotel.com property URLs were not captured, so the field is deliberately absent rather than guessed; identity rests on Booking's dated page plus an independent structured listing agreeing on address, postal code and coordinates.
6. **Mercure room count disagrees between sources** (336 vs 297) and its check-in 16:00 / check-out 11:00 come from a third-party listing, not Accor.
7. **Mercure is brand new** — 2 Booking reviews at capture, so operational data is thin.

### Round 1 — Busan / Yeonsan

| New entry | Area | Room / bed count | Refundable | $/night | 6-night total | Verify |
|---|---|---|---|---|---:|---|
| **Hyatt Place Busan Yeonsan** | Busan · Yeonsan (Yeonje-gu) | King Room with City View — **1 king bed**, 320 ft² | **Yes** — free until Nov 8, 2026 (1 day); then the first night. No prepayment. | **$134** | **$806** (10% VAT excluded) | [dated Booking rate](https://www.booking.com/hotel/kr/hyatt-place-busan-yeonsan.html?checkin=2026-11-09&checkout=2026-11-15&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |

**🚩 Flags:** Booking tags it **Adults only**; no hyatt.com URL captured; `stars: 4` is a brand tier not an official rating; no published mattress width and no walkable-rail distance, so **not** a core-needs match; the **$107 headline is non-refundable**.

### Investigated, not added

| Candidate | Why it was held out |
|---|---|
| Shilla Stay Seobusan (Gangseo-gu, Busan) | Identity solid — 38 Myeongjigukje 7-ro, official `shillastay.com/seobusan` page, coordinates 35.096675 / 128.905259 — but the Booking property slug could not be resolved, so there is **no dated rate page**. No price, bed count or cancellation term exists to record. |

Full evidence and the queue for the next rounds: **[`guide/verification-new-entries-2026-08-21.md`](guide/verification-new-entries-2026-08-21.md)**.

Next up: re-tries that need a working Booking slug — **Hotel Aventree Jongno**, **InterContinental Seoul COEX**, **Shilla Stay Seobusan** — plus Hongdae proper. **Myeong-dong is deliberately skipped**: with 25+ records already, new candidates there are overwhelmingly rebrands rather than genuinely new properties — each needing both the Nov 1–9 and Nov 15–22 windows plus coordinates before it can enter the master list.

---

## How to re-verify any row yourself

1. Open the row's **dated rate** link — it already contains `checkin`, `checkout`, `group_adults=2`, `no_rooms=1`, `selected_currency=USD`.
2. Read the **room name and bed line** on that exact row (Booking states the bed count explicitly, e.g. "1 king bed", "2 twin beds").
3. Read the **cancellation sentence verbatim**, including what happens *inside* the free window (first night vs. total stay) and the **prepayment** line.
4. For bed **size** in centimetres, use the hotel's **official** page — a Booking "queen"/"king" label proves the category, not a width. Korean hotels frequently list a 160 cm double as a "full".
5. Anything that disagrees with a table above is a flag, not a correction — record it rather than overwriting.

The append-only capture log is [`data/pricing-history.json`](data/pricing-history.json). Rate blocks live on each hotel record as `refundableRate` (its own stay dates), `refundableRateNov9` (Nov 9–15) and `refundableRateNov15` (Nov 15–22); `meta.dateWindows` in [`data/hotels.json`](data/hotels.json) documents which field holds which window.

---

# About this planner

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
- **Expanded city lists** — browse 101 Seoul, 15 Gyeongju, 25 Busan, 7 Cheonan, 7 Daejeon, and 5 Suwon hotels. Seoul has two date tables (planned Nov 1–9 vs alternate Nov 15–22) in [`guide/verification-seoul-dual-window-nov1-and-nov15-2026.md`](guide/verification-seoul-dual-window-nov1-and-nov15-2026.md); the latest strictly verified Dongdaemun additions and held-out candidates are in [`guide/verification-seoul-dongdaemun-batch5-2026-08-19.md`](guide/verification-seoul-dongdaemun-batch5-2026-08-19.md). The Busan **Nov 9–15** pass is [`guide/verification-busan-nov9-15-2026-08-21.md`](guide/verification-busan-nov9-15-2026-08-21.md).
- **Quick filters** — view all stays, only core-needs matches, or stays with laundry; search within the current city.
- **Useful details at a glance** — estimated nightly range, recommended room, bed setup, bathroom/transport fit, normal check-in/out time, canonical identity source, and rate-comparison link.
- **Timestamped refundable pricing** — hotel cards show a ♻️ badge with the captured refundable rate, cancellation deadline, and UTC capture time; the append-only log lives in [`data/pricing-history.json`](data/pricing-history.json). The four-city (Suwon / Gyeongju / Cheonan / Daejeon) 2026-08-18T19:16Z checklist is [`guide/verification-suwon-gyeongju-cheonan-daejeon-2026-08-18.md`](guide/verification-suwon-gyeongju-cheonan-daejeon-2026-08-18.md). The earlier same-day Seoul-inclusive pass is [`guide/verification-checklist-2026-08-18-line-by-line.md`](guide/verification-checklist-2026-08-18-line-by-line.md).
- **Duplicate protection** — all 160 records are source verified; similarly named branches are cross-checked as distinct properties.

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
| Seoul | 101 | First-night shortlist + Myeongdong / Jongno / Dongdaemun / Hongdae / Itaewon / Gangnam (dual date windows) |
| Gyeongju | 15 | Heritage / hanok, Old Town, Bulguksa, and Bomun Lake stays |
| Busan | 25 | Haeundae, Seomyeon, Busan Station, Nampo, and Songdo options |
| Cheonan | 7 | KTX-corridor alternative |
| Daejeon | 7 | KTX-corridor alternative |
| Suwon | 5 | Seoul-area base (Suwon Station + Hwaseong Fortress) |
| **Planned cities** | **141** | Seoul + Gyeongju + Busan |
| **Total** | **160** | Full city-by-city comparison set |

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
│   ├── hotels.json         # 160 city hotels + five-option arrivalNight shortlist and source links
│   └── itinerary.json      # Dates, city order, and alternatives
├── guide/
│   ├── arrival-night.md    # 24-hour reception research + late-arrival workflow
│   ├── verification-audit.md # Canonical identity and duplicate audit
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

- Arrival-night evidence and **all 160 hotel records** were identity-checked (Seoul/Gyeongju/Busan/Cheonan/Daejeon on August 10, 2026; the Suwon shortlist on August 18, 2026; expanded Seoul batches on August 19, 2026). Every card shows a canonical property source, source type, date, and verification note. The validator rejects duplicate IDs, sourced names, official URLs, identity-source URLs, and exact coordinates; similar branch names require an explicit distinct-property cross-check.
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
