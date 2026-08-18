# Timestamped Refundable Pricing — Method & Log

**Stay priced:** Seoul, **check-in Sun Nov 1, 2026 → check-out Mon Nov 9, 2026** (8 nights, 2 adults, 1 room).
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
| Four Seasons Hotel Seoul | 🚫 via this source | — | — | — | Booking.com showed **no availability** for Nov 1–9 |
| ibis Ambassador Insadong | 🚫 via this source | — | — | — | Booking.com showed **no availability** for Nov 1–9 |

✅* = labeled refundable but with materially worse terms than the alternative row — read the cancellation column carefully.

All prices: Booking.com USD display, taxes as noted per row (most exclude 10% tax; Skypark/Grand Lotte include 10% service charge). Full verbatim rows: [`data/pricing-history.json`](../data/pricing-history.json).

**Market snapshot (run 1 timestamp):** a Seoul-wide search with the *Free cancellation* filter for Nov 1–9, 2026 returned **2,044 refundable properties**, so refundable inventory for these dates is plentiful; e.g. Lake Tourist Hotel (Songpa) showed $46/night, $365 total, free cancellation + no prepayment.

**Notes worth knowing (all from the captured pages):**
- **Cheapest verified refundable 1-bed TOTAL: Shilla Stay Gwanghwamun at $1,600 for 8 nights** ($200/night high-floor double, no prepayment). Skypark M3 is close at $1,612.
- **Best cancellation terms: Le Méridien, Westin Josun, L'Escape, and Moxy** — free cancellation until 12:00 AM on the day of arrival itself, no prepayment.
- **Beware cheap "free cancellation" rates:** Nine Tree MD1's $197 rate closes its window Oct 18 and charges the whole stay inside 14 days; Fairmont's $467 rate is "partially refundable" (first-night fee always) with upfront charge; Nine Tree MD2's $214 partner offer takes payment upfront with no modifications.
- **Rebrands/legacy slugs spotted:** Booking.com now titles Lotte Hotel Seoul as **"THE GRAND LOTTE SEOUL"**; Westin Josun is served under legacy slug `westin-chosun-seoul`; L'Escape's slug is `l-39-escape`.

---

## Still to capture (next passes)

Slug guesses that failed (do not retry): `lotte-hotel-seoul`, `ibis-ambassador-seoul-myeongdong`, `nine-tree-by-parnas-seoul-myeongdong`, `l7-myeongdong`, `the-westin-josun-seoul`, `ibis-styles-ambassador-seoul-myeongdong`, `ibis-ambassador-myeongdong`, `courtyard-by-marriott-seoul-myeongdong`.

Hotels awaiting a verified capture: Aloft Myeongdong (slug `aloft-seoul-myeongdong` verified, coin laundry confirmed; rate table failed to render twice — rerun) · Courtyard by Marriott Myeongdong · Four Points by Sheraton Josun Myeongdong · ibis Styles Ambassador Myeongdong · ibis Ambassador Seoul Myeongdong · Nine Tree by Parnas Seoul Insadong.

**Status: 14 of 20 Seoul hotels captured (12 refundable rates + 2 no-availability negatives), plus the Grand Hyatt Incheon arrival fallback.**
