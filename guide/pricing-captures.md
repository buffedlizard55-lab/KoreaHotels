# Timestamped Refundable Pricing — Method & Log

**Stay windows priced (per city):** Seoul **Nov 1–9** (8 nights) · Gyeongju **Nov 9–15** (6 nights) · Busan **Nov 15–22** (7 nights). All at 2 adults, 1 room.
**Decision log:** the Oct 31 arrival night (ICN lands 21:00) is intentionally left **unbooked** for now.

This guide documents exactly how refundable, dated, timestamped prices are obtained for the Seoul shortlist, what is already captured, and what is not. The append-only data lives in [`data/pricing-history.json`](../data/pricing-history.json); hotels with a completed capture also show a **♻️ Refundable rate** badge on the planner card.

---

## The method (what makes it non-hallucinated)

1. **Dated source URL.** Each hotel's Booking.com property page is loaded with the stay baked into the URL:

   ```
   https://www.booking.com/hotel/kr/<property-slug>.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD
   ```

   The page that comes back is the hotel's **real rate table for those exact dates** — room name, bed count, per-night price, 8-night total, tax note, and per-rate cancellation/prepayment text.

2. **Identity verification before recording.** A capture is only recorded if the page's own hotel name (H1) and address match the hotel in our data. Slug guesses that 404 or pages that name a different property are logged as failures, never as data. (Example: `l7-myeongdong` 404s; the verified slug is `l7-myeongdong-by-lotte`.)

3. **Timestamping.** Every capture stores `capturedAtUtc`, corroborated by two independent clocks: the local UTC clock at fetch time and the `chal_t`/`srepoch` epoch parameter Booking.com embeds in the served URL (e.g. `chal_t=1787032350` → `2026-08-18T05:52:30Z`).

4. **Verbatim terms.** Cancellation and prepayment text is copied as shown ("Free cancellation before October 30, 2026…"), never summarized into a claim. The authoritative terms are always whatever the checkout page shows at the moment you book.

5. **Append-only history.** New captures are appended, never edited, so re-running on any later date builds a real price history for the same stay window.

### Honest limits of this method

- **Snapshot, not a feed.** Prices are valid as of the timestamp. There is no background scheduler; captures happen when a run is executed.
- **One source.** Booking.com display prices (USD conversion, usually "before taxes / 10% tax excluded"). Official brand sites can differ — a hotel with no availability here may still be bookable direct.
- **Free-cancellation filter vs. page truth.** The refundable badge reflects rates whose rows explicitly said "Free cancellation" / "Non-refundable" on the page. Per-rate inventory (e.g. "We have 5 left") changes constantly.

### Anyone can re-run a capture manually

Open the URL pattern above in a normal browser (replace `<property-slug>`, e.g. `somerset-palace-seoul`) and you get the same dated rate table; save/screenshot it with the time visible, or append the numbers to `data/pricing-history.json` with a fresh `capturedAtUtc`.

---

## Captured so far (run 1: 2026-08-18 ~05:52 UTC · run 2: 2026-08-18 ~13:03–13:05 UTC)

| Hotel (verified on page) | Refundable? | Room | $/night | 8-night total | Free cancellation until | Prepay |
|---|---|---|---:|---:|---|---|
| Somerset Palace Seoul | ✅ | Deluxe Queen (2 queens, incl. breakfast) | $249 | $1,994 | **Oct 30, 2026** (2 days out; then 1st night) | Pay nothing until Oct 28 |
| L7 MYEONGDONG by LOTTE | ✅ | Standard Double (1 full bed) | $295 | $2,358 | **Oct 29, 2026** (3 days out; then 1st night) | No prepayment — pay at property |
| Nine Tree by Parnas Myeongdong 1 | ✅ | Double (1 full bed) | $205 | $1,643 | **Oct 29, 2026** (3 days; then 1st night) | Pay nothing until Oct 27 |
| Nine Tree by Parnas MD 1 — cheaper rate ⚠️ | ✅* | Double (1 full bed) | $197 | $1,577 | **Oct 18, 2026 only**; inside 14 days the penalty is the **total stay price** | Pay nothing until Oct 16 |
| Hotel Skypark Myeongdong 3 | ✅ | Double (1 full bed) | $180 | $1,612 | **Oct 29, 2026** (3 days; then 1st night) | Pay nothing until Oct 27 |
| Hotel Skypark M3 — non-refundable comparison | ❌ (rate choice) | Double (1 full bed) | $178 | $1,594 | — none (one free date change until Oct 25) | Charged at booking |
| Moxy Seoul Myeongdong | ✅ | Queen w/ Two Queens & City View | $296 | $2,367 | **Nov 1, 2026 — day of arrival (12:00 AM)**; then 1st night | No prepayment — pay at property |
| THE GRAND LOTTE SEOUL (ex-Lotte Hotel Seoul) | ✅ | Main Tower Grand Superior Double (1 full bed) | $364 | $3,235 | **Oct 29, 2026** (3 days; then 1st night) | No prepayment — pay at property |
| Fairmont Ambassador Seoul | ✅ | Fairmont Twin (2 twins; 2-adult rate) | $583 | $4,666 | **6:00 PM Oct 31, 2026** (day before arrival; then 1st night) | Pay nothing until Oct 29 |
| Fairmont — cheaper "partially refundable" ⚠️ | ✅* | Fairmont Twin (2 twins) | $467 | $3,733 | *Not free cancellation*: first-night fee from booking moment, charged upfront | Pay online at booking |
| Le Méridien Seoul Myeongdong | ✅ | Deluxe King w/ City View (1 king, breakfast incl.) | $624 | $4,992 | **Nov 1, 2026 — day of arrival (12:00 AM)**; then 1st night | No prepayment — pay at property |
| Westin Josun Seoul | ✅ | Deluxe King (1 king) | $398 | $3,532 | **Nov 1, 2026 — day of arrival (12:00 AM)** | No prepayment — pay at property |
| L'Escape (Luxury Collection) | ✅ | Classic King w/ City View (1 king) | $305 | $2,443 | **Nov 1, 2026 — day of arrival (12:00 AM)**; then 1st night | No prepayment — pay at property |
| Shilla Stay Gwanghwamun | ✅ | Standard Double high floor (1 full bed) | $200 | $1,600 | **Oct 29, 2026** (3 days; then 1st night) | No prepayment — pay at property |
| Nine Tree by Parnas Myeongdong 2 | ✅ | Hollywood Double (1 KING bed) | $303 | $2,422 | **Oct 29, 2026** (3 days; then 1st night) | Pay nothing until Oct 27 |
| Nine Tree MD 2 — Partner Offer ⚠️ | ✅* | Hollywood Double (1 king) | $214 | $1,714 | Oct 29, 2026 (3 days) — but pay-in-advance, NO modifications | Pay in advance at booking |
| Grand Hyatt Incheon (arrival fallback) | ✅ | King Room High Floor | $253 | $2,023 | **Oct 31, 2026** (1 day out; then 1st night) | No prepayment — pay at property |
| Grand Hyatt Incheon — non-refundable rate | ❌ (rate choice) | King Room High Floor | $221 | $1,767 | — none (full forfeit) | Charged at booking |
| ibis Styles Ambassador Myeongdong | ✅ | Standard Double (1 full bed) | $187 | **$1,499** | **Oct 31, 2026** (1 day out; then 1st night) | No prepayment — pay at property |
| ibis Styles MD — non-refundable rate | ❌ (rate choice) | Standard Double (1 full bed) | $178 | $1,424 | — none | Charged at booking |
| ibis Ambassador Myeongdong | ✅ | Standard Double (1 full bed) | $313 | $2,503 | **6:00 PM Oct 31, 2026** (day before arrival) | No prepayment — pay at property |
| ibis Ambassador MD — non-refundable rate | ❌ (rate choice) | Standard Double (1 full bed) | $266 | $2,127 | — none | Charged at booking |
| Nine Tree by Parnas Seoul Insadong | ✅ | Deluxe Double w/ Jogyesa View (1 queen) | $235 | $1,881 | **Oct 29, 2026** (3 days; then 1st night) | Pay nothing until Oct 27 |
| Nine Tree Insadong — cheaper rate ⚠️ | ✅* | Same room | $226 | $1,805 | **Oct 18, 2026 only**; inside 14 days the penalty is the **total stay price** | Pay nothing until Oct 16 |
| Courtyard by Marriott Myeongdong | ✅ | Guest Room, 1 King | $324 | $2,595 | **Nov 1, 2026 — day of arrival (12:00 AM)** | No prepayment — pay at property |
| Four Seasons Hotel Seoul | 🚫 via this source | — | — | — | Booking.com showed **no availability** for Nov 1–9 |
| ibis Ambassador Insadong | 🚫 via this source | — | — | — | Booking.com showed **no availability** for Nov 1–9 |

✅* = labeled refundable but with materially worse terms than the alternative row — read the cancellation column carefully.

All prices: Booking.com USD display, taxes as noted per row (most exclude 10% tax; Skypark/Grand Lotte include 10% service charge). Full verbatim rows: [`data/pricing-history.json`](../data/pricing-history.json).

**Market snapshot (run 1 timestamp):** a Seoul-wide search with the *Free cancellation* filter for Nov 1–9, 2026 returned **2,044 refundable properties**, so refundable inventory for these dates is plentiful; e.g. Lake Tourist Hotel (Songpa) showed $46/night, $365 total, free cancellation + no prepayment.

**Notes worth knowing (all from the captured pages):**
- **Cheapest verified refundable 1-bed TOTAL: ibis Styles Ambassador Myeongdong at $1,499 for 8 nights** ($187/night, free cancel until 1 day before arrival, no prepayment). Runners-up: Shilla Stay Gwanghwamun $1,600, Skypark M3 $1,612, Nine Tree MD1 $1,643.
- **Best cancellation terms: Le Méridien, Westin Josun, L'Escape, Courtyard, and Moxy** — free cancellation until 12:00 AM on the day of arrival itself, no prepayment.
- **Beware cheap "free cancellation" rates:** Nine Tree MD1's $197 and Insadong's $226 rates close their windows Oct 18 and charge the whole stay inside 14 days; Fairmont's $467 rate is "partially refundable" (first-night fee always) with upfront charge; Nine Tree MD2's $214 partner offer takes payment upfront with no modifications.
- **Biggest refundability premium to avoid overpaying:** ibis Ambassador Myeongdong ($266 non-refundable vs $313 refundable = $376/stay premium). Smallest: Skypark M3 ($18/stay) and ibis Styles ($75/stay).
- **Rebrands/legacy slugs spotted:** Lotte Hotel Seoul → **"THE GRAND LOTTE SEOUL"**; Westin Josun → slug `westin-chosun-seoul`; Courtyard Myeongdong → slug `courtyard-by-marriott-seoul-namdaemun` (ex-Namdaemun); L'Escape → slug `l-39-escape`; ibis Ambassador Myeongdong → slug `ibis-myeong-dong`.

---

## Sweep closeout (2026-08-18)

**All 20 Seoul hotels are accounted for.** 18 captured with data (16 refundable rates + 2 no-availability negatives on this source), plus the Grand Hyatt Incheon arrival fallback. Two could not be priced via Booking.com this session, recorded as such (no estimates substituted):

- **Aloft Myeongdong** — property and slug verified (coin laundry confirmed), but the rate table failed to render before capture on three attempts. Price it on Marriott direct or retry the capture later.
- **Four Points by Sheraton Josun Myeongdong** — no Booking.com property page surfaced across three searches (TripAdvisor/HRS/Priceline/Trip.com only). Price it on FourPoints.com/Marriott direct; third-party snapshots around capture time showed ~$232–268 refundable rates for *other* dates, which are **not** recorded as data for Nov 1–9.

**Not bookable for Nov 1–9 via this source at capture time:** Four Seasons, ibis Ambassador Insadong — check official sites before ruling them out.

---

## Gyeongju — Nov 9–15, 2026 (6 nights) — in progress

**Market snapshot (2026-08-18 ~13:23 UTC):** 174 Gyeongju properties with free cancellation for the exact window (37 hotels, 61 guesthouses; 47 four-star, 2 five-star; queen-bed rooms in 43, king in 11). Hilton and Kensington are each confirmed listed on Booking.com with exactly one Gyeongju property. Cheapest verified refundable example card: Aventa Hotel, Standard Double (1 queen, breakfast included), $78/night, $469 total.

| Hotel (verified on page) | Refundable? | Room | $/night | 6-night total | Free cancellation until | Prepay |
|---|---|---|---:|---:|---|---|
| Rivertain Hotel Gyeongju ⭐ | ✅ | Standard Double (1 full bed, spa tub, **breakfast incl.**) | $82 | **$490** | **Nov 6, 2026** (3 days; ⚠️ inside = **total stay**) | Nothing until Nov 4 |
| Kensington Resort Gyeongju | ✅ | Kensington Deluxe (2 full beds, **breakfast incl.**) | $160 | **$957** | **Nov 2, 2026** ⚠️ 7-day-out cutoff (penalty text cut at capture) | No prepayment — pay at property |
| Benikea Swiss Rosen | ✅ | Standard Twin (twin + full) | $83 | **$556** | **Nov 6, 2026** (penalty text cut at capture) | Nothing until Nov 4 |
| Lahan Select (slug `hyundai-gyeongju`) | ✅ | Deluxe King Suite (1 queen, lake view) | $265 | $1,764 | **Nov 7, 2026** (penalty text cut at capture) | Pay at property, refundable in window |
| Commodore Hotel Gyeongju | ✅ | Imperial Suite Mtn View (2 beds) | $205 | $1,365 | **Nov 8, 2026** (1 day out; then 1st night) | Pay nothing until Nov 6 |
| The K Hotel Gyeongju | ✅ | Hwangnyoung View Ondol (4 futons) | $125 | $752 | **Nov 6, 2026** — ⚠️ inside 3 days the penalty is the **total stay** | Full stay charged 3 days out |
| Kinock (pet hotel) | ✅ | PKG room, **private pool**, 1 queen | $171 | $1,028 | **Nov 2, 2026** (7 days; inside = **first night only** — friendliest penalty) | Nothing until Oct 31 |
| SONO Calm (slug `daemyung-resort-gyeongju`) | 🚫 full window | — | — | — | **No availability Nov 9–15** on Booking.com | — |
| Nadul Hanok | 🚫 not listed | — | — | — | Books via gjhanok.com / hanok platforms, not Booking (like Wiyeonjae) | — |
| Hilton Gyeongju (slug `gyeongju-hilton`) | ⏳ | Premium King (1 king, lake view) — rate table render-failed ×2 + HTTP 500; identity + dates verified | — | — | retry next run | — |
| ~~Kinock pending~~ | — | captured above | — | — | — | — |
| Hwangnamkwan ("Hwangnamguan Hanok Village") | 🚫 full window | — | — | — | **No availability Nov 9–15**; only 3-night slices (e.g. Nov 14–17 from $294) | — |
| HanokInn | 🚫 full window | — | — | — | **No availability Nov 9–15** on Booking.com | — |
| Wiyeonjae Hanok Stay | 🚫 not listed | — | — | — | No Booking.com listing found (books direct at wiyeonjae.kr) | — |

**⚠️ The Gyeongju pattern so far:** the heritage/hanok tier does **not** stretch across the full 6-night window — both hanok options in the shortlist show no availability for Nov 9–15, the 4–5★ refundable filter returns just 49 properties with an "86% unavailable" warning, and only 12 no-prepayment rates exist. If a hanok stay matters, either book direct immediately, split the stay, or shift dates. Available 4–5★ free-cancellation properties that ARE bookable for the whole window are largely *not* on the repo shortlist (e.g. Hanok stay Mokhyang $233/nt w/ breakfast, 1 left; Muuun — recorded in the history file as market context only).

**Record-vs-page checks (Gyeongju so far):** The-K name matches (page "The K"); Commodore matches (page also says "Chosun"; pools temporarily closed; 8.0/10); Hwangnamkwan = Booking "Hwangnamguan Hanok Village," same property, **check-in ends 22:00**; HanokInn matches (9.6/10, staff 9.9).

**Record-vs-page check (The K):** name matches (repo "The-K" / page "The K"); address 45 Expo-ro is the Expo/HICO zone adjacent to the repo's "Bomun Lake Resort" area label — compatible. New data point: Booking guest score 7.1/10 (66 reviews), low for the shortlist. 24-hour front desk confirmed on-page.

**Gyeongju terms warning:** the first capture already shows a harsher pattern than Seoul — total-price cancellation penalties (not first-night) and full prepayment charged days before arrival. Read every Gyeongju rate's fine print twice.

**Slug log (do not retry):** `hilton-gyeongju`, `hwangnamkwan`, `commodore-hotel-gyeongju`, `lahan-select-gyeongju`, `sono-calm-gyeongju` all 404. `the-k-gyeong-ju` resolved. Remaining 14 Gyeongju properties need search-resolved slugs: Hilton, Commodore, Lahan Select, Hwangnamkwan, SONO Calm, Kolon, GG, KINOCK, Benikea Swiss Rosen, Rivertain, HanokInn, Wiyeonjae, Nadul, Kensington.

## Busan — Nov 15–22, 2026 (7 nights) — not yet started

20 properties queued; same method, dates `checkin=2026-11-15&checkout=2026-11-22`.
