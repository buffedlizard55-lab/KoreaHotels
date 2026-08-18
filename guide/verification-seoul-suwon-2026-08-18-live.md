# Seoul · Myeongdong · Suwon — Full Line-by-line Re-verification (2026-08-18, live run)

**Method:** 2 fetches per hotel — (1) **Booking.com dated rate table** for live price + refundable status + bed count; (2) **official brand page** for bed size + identity. All 25 in-scope hotels completed.
**Dates:** Seoul/Myeongdong + Suwon all priced for **Nov 1–9, 2026** (8 nights, 2 adults, 1 room, USD).
**Captured:** 2026-08-18, live Booking.com + official-page fetches.

> Prices below are a **snapshot taken today** from Booking.com. They change continuously — re-open the linked page before paying. "Free cancellation" = the row explicitly labelled free-cancellation on Booking; the inside-window penalty (usually "first night") is noted where visible.

---

## 1. Live results — all 25 hotels (price / refundable / bed count / bed size)

| # | Hotel | Cheapest refundable one-bed (live) | Beds (count → size) | Refundable? | Source |
|---|---|---|---|---|---|
| 1 | L7 MYEONGDONG | Standard Double $295/nt ($2,358) | 1 **full** bed (no queen exists) | ✅ free-cancel Oct 29 | [Booking](https://www.booking.com/hotel/kr/l7-myeongdong-by-lotte.html) |
| 2 | Nine Tree MD1 | Double Room $205/nt ($1,643) | 1 bed 160×190 cm (**queen-width**) | ✅ free-cancel Oct 29 | [Booking](https://www.booking.com/hotel/kr/nine-tree.html) · [spec](https://www.ninetreehotels.com/nth1/room_standard_double.php) |
| 3 | ibis Styles Myeongdong | Standard 1 Double $187/nt ($1,499) | 1 **double** (16 m²) | ✅ free-cancel Oct 31 | [Booking](https://www.booking.com/hotel/kr/ibis-styles-seoul-myeongdong.html) · [Accor](https://all.accor.com/hotel/9771/index.en.shtml) |
| 4 | ibis Ambassador Insadong | — (no Booking avail Nov 1–9) | Superior = 1 **queen** (Accor) | ⚠️ book Accor direct | [Accor](https://all.accor.com/hotel/8002/index.en.shtml) |
| 5 | Four Seasons Seoul | — (no Booking avail Nov 1–9) | Deluxe/Premier = **king** | ⚠️ book direct | [four seasons](https://www.fourseasons.com/seoul/) |
| 6 | Fairmont Ambassador Seoul | $583/nt ($4,666) free-cancel ⚠️ room attribution | Deluxe King exists (official) | ⚠️ $583 row is likely 2-twin (see flag) | [Booking](https://www.booking.com/hotel/kr/fairmont-ambassador-seoul.html) |
| 7 | Hotel Skypark MD3 | Double Room $180/nt ($1,612) | 1 **double** (1400×2000 mm) | ✅ free-cancel Oct 29 | [Booking](https://www.booking.com/hotel/kr/skypark-myeongdong-3.html) |
| 8 | L'Escape Myeongdong | Classic King $305/nt ($2,443) | 1 **king** (Classic = lead-in) | ✅ free-cancel day-of-arrival | [Booking](https://www.booking.com/hotel/kr/l-39-escape.html) |
| 9 | Somerset Palace Seoul | **Executive One-Bedroom $228/nt ($1,824)** ✅ fixed | 1 **queen** | ✅ free-cancel Oct 30 | [Booking](https://www.booking.com/hotel/kr/somerset-palace-seoul.html) |
| 10 | ibis Ambassador Myeongdong | Standard 1 Double $313/nt ($2,503) | 1 **double** (21 m²) | ✅ free-cancel Oct 31 | [Booking](https://www.booking.com/hotel/kr/ibis-myeong-dong.html) |
| 11 | Moxy Myeongdong | **Queen w/ City View $308/nt ($2,460)** ✅ fixed | 1 **queen** | ✅ free-cancel day-of-arrival | [Booking](https://www.booking.com/hotel/kr/moxy-seoul-myeongdong.html) |
| 12 | Le Méridien Myeongdong | Deluxe King $624/nt ($4,992) | 1 **king** | ✅ free-cancel | [Booking](https://www.booking.com/hotel/kr/le-meridien-seoul-myeongdong.html) |
| 13 | Aloft Myeongdong ✅ NEW | **Aloft Room, 1 King $323/nt ($2,581)** | 1 **king** | ✅ free-cancel Oct 31 | [Booking](https://www.booking.com/hotel/kr/aloft-seoul-myeongdong.html) |
| 14 | Courtyard Seoul Myeongdong | Guest Room 1 King $324/nt ($2,595) | 1 **king** | ✅ free-cancel day-of-arrival | [Booking](https://www.booking.com/hotel/kr/courtyard-by-marriott-seoul-namdaemun.html) |
| 15 | Four Points Josun MD ✅ NEW | **Superior double $234/nt ($2,081)** | 1 **full** bed (not king) ⚠️ | ✅ free-cancel Oct 29 | [Booking](https://www.booking.com/hotel/kr/four-points-by-sheraton-seoul-myeongdong.html) |
| 16 | Nine Tree MD2 | Hollywood Double $303/nt ($2,422) | **2 singles joined** ⚠️ | ✅ free-cancel Oct 29 | [Booking](https://www.booking.com/hotel/kr/nine-tree-premier-myeongdong.html) |
| 17 | Nine Tree Insadong | Deluxe Double $235/nt ($1,881) | 1 **queen-width** (width unpub.) | ✅ free-cancel Oct 29 | [Booking](https://www.booking.com/hotel/kr/nine-tree-premier-insadong.html) |
| 18 | Shilla Stay Gwanghwamun | Standard Double $200/nt ($1,600) | 1 **full** (Hollywood=joined) ⚠️ | ✅ free-cancel Oct 29 | [Booking](https://www.booking.com/hotel/kr/shilla-stay-gwanghwamun.html) |
| 19 | LOTTE HOTEL SEOUL | Grand Superior Double $364/nt ($3,235) | 1 **full** bed (not king) | ✅ free-cancel Oct 29 | [Booking](https://www.booking.com/hotel/kr/lotte-seoul-seoul.html) |
| 20 | Westin Josun Seoul | Deluxe King $398/nt ($3,532) | 1 **king** | ✅ free-cancel day-of-arrival | [Booking](https://www.booking.com/hotel/kr/westin-chosun-seoul.html) |
| 21 | Novotel Ambassador Suwon ✅ NEW | **No Booking availability Nov 1–9** | Superior/Deluxe/Executive = 1 **king** (Accor) | ⚠️ book Accor direct | [Accor](https://all.accor.com/hotel/8748/index.en.shtml) |
| 22 | Four Points Suwon ✅ NEW | **Premier King $157/nt ($1,259)** | 1 **king** | ✅ free-cancel day-of-arrival | [Booking](https://www.booking.com/hotel/kr/four-points-by-sheraton-suwon.html) |
| 23 | Ramada Plaza Suwon ✅ NEW | **Deluxe King $139/nt ($1,114)** | 1 **queen** (named "King") ⚠️ | ✅ free-cancel Oct 31 | [Booking](https://www.booking.com/hotel/kr/ramada-plaza-suwon.html) |
| 24 | Courtyard Suwon ✅ NEW | **Comfortable King ≈ $177/nt ($1,419)** | 1 **king** | ✅ free-cancel day-of-arrival | [Booking](https://www.booking.com/hotel/kr/courtyard-by-marriott-suwon.html) |
| 25 | ibis Suwon ✅ NEW | **Standard/Superior Double ≈ $104/nt ($834)** | 1 **full** bed (king = suite only) | ✅ free-cancel Oct 31 | [Booking](https://www.booking.com/hotel/kr/ibis-suwon-ambassador.html) |

---

## 2. Changes applied to `data/hotels.json` this run

1. **Added 7 missing `refundableRate` blocks** (live Booking reads): Aloft MD, Four Points Josun MD, Novotel Suwon (no-availability finding), Four Points Suwon, Ramada Plaza Suwon, Courtyard Suwon, ibis Suwon.
2. **Corrected Somerset Palace** — the captured "$249 2-queen" room replaced with the true one-bed **"Executive One-Bedroom = 1 queen, $228/nt"**.
3. **Corrected Moxy Myeongdong** — the captured "$296 2-queen" room replaced with the true one-bed **"Queen Room with City View = 1 queen, $308/nt"**.
4. Updated `meta.refundableRateCaptures` (26 entries now; Suwon 5/5).

`validate.py` ✅ 74/74, `build.py` ✅ rebuilt.

---

## 3. Irregularities flagged for review

**New / resolved this run:**
1. **Somerset + Moxy "refundable" captures were 2-bed rooms** → **fixed** to the real 1-queen rooms ($228 and $308/nt respectively).
2. **Four Points Josun Myeongdong**: Booking's lead-in one-bed is a **1 full/double bed ($234/nt)**, not the "Deluxe King" the data lists. The king does not surface on Booking's unauthenticated view → the "fits:true" king claim is not backed by the cheapest refundable room.
3. **Novotel Suwon**: **zero Booking availability** Nov 1–9 — must be booked on Accor direct (king rooms confirmed there).
4. **Ramada Plaza Suwon "Deluxe King" = 1 queen bed** — live-confirmed naming mismatch (data already noted this; now evidenced with a price).
5. **Fairmont**: the $583/nt free-cancellation row is **attributed to the Fairmont Twin (2 twin)** in the prior capture; the one-bed King free-cancel rate was not cleanly isolated this fetch (room-name header cut). Re-verify before booking a king.

**Carried (still open):**
6. **"Hollywood Double" = joined mattresses** (Nine Tree MD2 $303, Shilla Gwanghwamun) — not a single queen/king. Shilla's captured $200 row is a 1-full Standard Double, not the Hollywood.
7. **Korean "double" ≠ 140 cm** — Nine Tree MD1 Standard Double is 160 cm (queen-width) per official spec; Booking labels it "full".
8. **ibis Suwon / Four Points Josun MD / Shilla / LOTTE Seoul / L7 / ibis Styles** lead-in one-bed rooms are **1 full/double**, not queen/king — correct per the repo's own "double ≠ queen" rule (`fits:false`).

---

## 4. Honesty boundaries (unchanged)

- **Prices are a snapshot.** Every figure above was read from Booking.com today, but rates move per-rate-plan and continuously. Re-open the link before purchasing.
- **Bed *size* comes only from official sources** (Accor bedding fields, Nine Tree mm specs, Marriott roomPoolCode). Booking's "full/queen/king" is a count/size *label* that is unreliable for Korean hotels — hence "double ≠ queen" is judged on the official spec, not Booking's word.
- **Official-site live prices** (Accor/Marriott/Hyatt direct) remain JS/login-gated; Booking (with Agoda as a second OTA) is the machine-readable price+refundable source.

*Run completed 2026-08-18. All Booking figures and official specs live-fetched this session; links above are the manual-verification references.*
