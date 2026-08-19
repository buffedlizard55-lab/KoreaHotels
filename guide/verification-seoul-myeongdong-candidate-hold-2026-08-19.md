# Seoul / Myeongdong candidate hold log — dated verification pass (2026-08-19)

This is a **source-controlled candidate pass**, not a master-list expansion. It follows the Dongdaemun batch and deliberately records properties that were investigated but did **not** yet clear the project’s line-by-line admission rule. No rate from one window is reused in the other.

## Method and admission rule

- Search state for every link: **2 adults, 1 room**, USD display currency.
- A master entry requires a current dated result for the applicable window, refundable-status text, a room-level bed **count**, and a trusted source for the physical bed-size claim. A Booking `full`, `double`, `queen`, or `king` label alone is not treated as a published mattress measurement.
- Capture time: **2026-08-19 18:04–18:05 UTC** (the Booking URLs returned `chal_t` values in this interval). Totals below are Booking display totals; where stated, 10% tax is excluded.
- **Outcome: 0 additions in this hold pass.** This is intentional: inserting incomplete entries to reach a numerical target would violate the no-hallucination requirement.

## Table A — Nov 1–9, 2026 (8 nights)

| Candidate | Current dated finding | Room / bed count actually shown | Price and refundable evidence | Admission decision | Manual verification |
|---|---|---|---|---|---|
| Metro Hotel Myeongdong | Booking said reservations cannot be made at this time. The property text says a renovation is scheduled Jun. 16, 2026–Feb. 28, 2027. | No sellable room row. | No price or cancellation term. | **Hold — unavailable / renovation conflict.** | [Booking dated page](https://www.booking.com/hotel/kr/metro.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Solaria Nishitetsu Hotel Seoul Myeongdong | Sellable. | Standard Twin — **2 twin beds**, attached bathroom. | $297/night; $2,373 before tax; free cancellation before Oct. 30; payment due Oct. 28. | **Hold — the audited refundable row is two beds, not the required single bed.** | [Booking dated page](https://www.booking.com/hotel/kr/solaria-nishitetsu-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel Prince Seoul | Sellable; a refundable room was visible. | Refundable row captured was Twin Room A — **2 twin beds**. | $181/night; $1,619 before tax; free cancellation before Oct. 25; payment due Oct. 23. | **Hold — no refundable one-bed room was captured in this pass.** | [Booking dated page](https://www.booking.com/hotel/kr/hotel-prince-seoul.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| G2 Hotel Myeongdong | Sellable. | Standard Twin Room (No Parking) — **2 twin beds**, private bathroom. | Current displayed total was $1,990 before tax ($249 average/night); cancellation block was outside the captured text boundary. | **Hold — twin configuration and cancellation text incomplete.** | [Booking dated page](https://www.booking.com/hotel/kr/g2-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel Midcity Myeongdong | Booking showed no availability. | Standard Double exists in inventory as **1 queen bed**, but not sellable. | No price or cancellation term. | **Hold — unavailable.** | [Booking dated page](https://www.booking.com/hotel/kr/hotel-midcity-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel Thomas Myeongdong | Sellable. | Deluxe Twin Room — **2 twin beds**, attached bathroom. | The rate/cancellation block was not fully captured in the source response. | **Hold — twin configuration and incomplete rate capture.** | [Booking dated page](https://www.booking.com/hotel/kr/thomas-myeongdong.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |

## Table B — Nov 15–22, 2026 (7 nights)

| Candidate | Current dated finding | Room / bed count actually shown | Price and refundable evidence | Admission decision | Manual verification |
|---|---|---|---|---|---|
| Metro Hotel Myeongdong | Booking said reservations cannot be made at this time; the same renovation notice is displayed. | No sellable room row. | No price or cancellation term. | **Hold — unavailable / renovation conflict.** | [Booking dated page](https://www.booking.com/hotel/kr/metro.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Solaria Nishitetsu Hotel Seoul Myeongdong | Sellable. | Standard Double — **1 full bed**, attached bathroom. | $294/night; $2,055 before tax; free cancellation before Nov. 13; payment due Nov. 11. | **Hold — one bed is confirmed, but physical width is not established by the source used; do not call it queen/king.** | [Booking dated page](https://www.booking.com/hotel/kr/solaria-nishitetsu-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel Prince Seoul | Sellable. | Double Room A — **1 queen bed**, private/attached bathroom. | $167/night; $1,299 before tax; free cancellation before Nov. 8; payment due Nov. 6. | **Hold — Booking’s queen label is not a published physical dimension; official room-spec evidence still required.** | [Booking dated page](https://www.booking.com/hotel/kr/hotel-prince-seoul.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| G2 Hotel Myeongdong | Sellable. | Standard Twin Room (No Parking) — **2 twin beds**, private bathroom. | $180/night; $1,260 before tax; cancellation block was outside the captured text boundary. | **Hold — twin configuration and incomplete cancellation capture.** | [Booking dated page](https://www.booking.com/hotel/kr/g2-myeongdong.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel Midcity Myeongdong | Booking showed no availability. | Standard Double exists in inventory as **1 queen bed**, but not sellable. | No price or cancellation term. | **Hold — unavailable.** | [Booking dated page](https://www.booking.com/hotel/kr/hotel-midcity-myeongdong.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |
| Hotel Thomas Myeongdong | Sellable. | Superior Twin Room — **2 twin beds**, attached bathroom. | The rate/cancellation block was not fully captured in the source response. | **Hold — twin configuration and incomplete rate capture.** | [Booking dated page](https://www.booking.com/hotel/kr/thomas-myeongdong.html?checkin=2026-11-15&checkout=2026-11-22&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD) |

## Irregularities to carry forward

1. **Metro renovation:** Its own Booking property text places the published renovation across both requested windows. Do not present it as bookable without a new direct confirmation.
2. **Cancellation text is rate-plan specific:** G2 and Thomas had a visible dated inventory result but not a fully captured cancellation panel. Their prices are not treated as confirmed refundable prices.
3. **Do not convert labels into dimensions:** Solaria’s “1 full bed” and Prince’s “1 queen bed” establish what Booking calls the bed, not its millimetre width. Neither is in the master list yet.
4. **No cross-window carry-forward:** availability and rates above are specific to their respective table only.
