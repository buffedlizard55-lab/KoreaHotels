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

## Captured so far (2026-08-18, ~05:52 UTC)

| Hotel (verified on page) | Refundable? | Room | $/night | 8-night total | Free cancellation until | Prepay |
|---|---|---|---:|---:|---|---|
| Somerset Palace Seoul | ✅ | Deluxe Queen (2 queens, incl. breakfast) | $249 | $1,994 | **Oct 30, 2026** (2 days out; then 1st night) | Pay nothing until Oct 28 |
| L7 MYEONGDONG by LOTTE | ✅ | Standard Double (1 full bed) | $295 | $2,358 | **Oct 29, 2026** (3 days out; then 1st night) | No prepayment — pay at property |
| Grand Hyatt Incheon (arrival fallback) | ✅ | King Room High Floor | $253 | $2,023 | **Oct 31, 2026** (1 day out; then 1st night) | No prepayment — pay at property |
| Grand Hyatt Incheon — same room, non-refundable rate | ❌ (rate choice) | King Room High Floor | $221 | $1,767 | — none (full price forfeit) | Charged at booking |
| Four Seasons Hotel Seoul | 🚫 via this source | — | — | — | — | Booking.com showed **no availability** for Nov 1–9 |

All prices: Booking.com USD display, 10% tax excluded unless noted. Full verbatim rows: [`data/pricing-history.json`](../data/pricing-history.json).

**Market snapshot (same timestamp):** a Seoul-wide search with the *Free cancellation* filter for Nov 1–9, 2026 returned **2,044 refundable properties**, so refundable inventory for these dates is plentiful; e.g. Lake Tourist Hotel (Songpa) showed $46/night, $365 total, free cancellation + no prepayment.

---

## Still to capture (next passes)

Slug guesses that failed (do not retry): `lotte-hotel-seoul`, `ibis-ambassador-seoul-myeongdong`, `nine-tree-by-parnas-seoul-myeongdong`, `l7-myeongdong`.

Hotels awaiting a verified capture: Nine Tree by Parnas Myeongdong 1 / 2 / Insadong · ibis Styles Ambassador Myeongdong · ibis Ambassador Myeongdong · ibis Ambassador Insadong · Hotel Skypark Myeongdong 3 · L'Escape · Moxy Myeongdong · Le Méridien Myeongdong · Aloft Myeongdong · Courtyard Myeongdong · Four Points Josun Myeongdong · Shilla Stay Gwanghwamun · LOTTE HOTEL SEOUL · Westin Josun Seoul · Fairmont Ambassador.
