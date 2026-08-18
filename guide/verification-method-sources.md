# How to verify every requirement line-by-line — sources & method (proven 2026-08-18)

**Purpose:** answer "is there another way to verify refundable status, current pricing, bed size, and bed count for every hotel — from sources we can actually access?"

**Bottom line:** Yes. The dynamic requirements (price + refundable) CAN be read machine-readably from **Booking.com's server-rendered dated rate table**, and bed **size** is best read from **official brand pages** (which expose structured bedding fields). A ~2-fetch-per-hotel method covers all four requirements.

---

## 0. What's actually reachable from this sandbox

- **Raw `curl`/HTTP from `bash` is blocked** — DNS resolves but outbound connections return HTTP 000, even to `example.com`. Only the sandbox's `fetch_page`, `web_search`, and `image_search` tools have web access. So "other sources" means *pages those tools can fetch*.
- `fetch_page` successfully renders **Booking.com, Accor, Marriott, Hyatt, Nine Tree, Agoda, Ascott (JSON-LD)** and others.
- **Blocked / not usable:** Expedia (bot wall → "Show us your human side"), Google Hotels (JS-only), Trip.com (needs a correct per-hotel ID; a wrong ID silently returns a different property), and **all official-site *live prices*** (Accor/Marriott/Hyatt load rates via JS or behind login — the static render shows availability/bedding but no dollar figure).

---

## 1. Requirement → best source (proven this session)

| Requirement | Primary source (works) | Cross-check | Notes / caveat |
|---|---|---|---|
| **Refundable status + current price** | **Booking.com dated URL** | Agoda (reachable) | Returns per-room: `$`/night, total before tax, **"Free cancellation before [date]" + penalty**, "No prepayment needed", units-left |
| **Bed count** | Booking.com ("1 full bed"/"2 twin beds") + official | — | Booking states count explicitly per room |
| **Bed size (mm/cm / queen vs king vs double)** | **Official brand page** (structured bedding field) | Korean official pages (exact mm) | Booking's "full/queen" labels are unreliable for Korean hotels (160 cm "double" is often shown as "full") |
| **Identity / star / address / room names** | Accor fact-sheet, Marriott, Hyatt, Nine Tree, Lotte, Josun, Ascott | — | — |

### Why Booking.com is the key unlock
A dated URL like
`https://www.booking.com/hotel/kr/l7-myeongdong-by-lotte.html?checkin=2026-11-01&checkout=2026-11-09&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD`
renders a full rate table. Verified live this session for L7 Myeongdong, e.g.:

| Room | Beds | $/night | Total (before tax) | Cancellation |
|---|---|---|---|---|
| Standard Twin | 2 twin | $287 | $2,297 | Free cancellation before Oct 29, 2026 (else first night) |
| Standard Double | 1 full | $295 | $2,358 | Free cancellation before Oct 29, 2026 |
| Superior Double City View | 1 full | $308 | $2,465 | Free cancellation before Oct 29, 2026 |

These figures **match the repo's 2026-08-18 captures exactly** (Standard Double $295 / $2,358), confirming the method is reliable and reproducible. Cancellation text is explicit: "Free cancellation before [date] … if you cancel within 3 days, fee = first night … no-show fee = same."

### Why official pages are the key unlock for bed *size*
- **Marriott `/rooms/` page** (e.g. `…/selmx-moxy-seoul-myeongdong/rooms/`) lists every `roomPoolCode` with exact bed config: "Guest room, **1 Queen**", "**2 Double**", "**2 Queen**", "**4 Twin bunk**", "1 Bedroom Suite, 1 Queen". This is more precise than the `/overview/` page used previously.
- **Accor** fact-sheet + direct-booking URL expose bedding fields: "1 x **Double** bed(s)", "1 x **Queen size** bed(s)", "1 x **King size** bed(s)".
- **Nine Tree** Korean room pages give **exact mm** (e.g. Standard Double = 더블 160×190 cm; Hollywood Double = 싱글 110×190 cm ×2).

---

## 2. Method — line-by-line, 2 fetches per hotel

For each of the 25 in-scope hotels:

1. **Fetch Booking dated URL** (Nov 1–9 for Seoul/Suwon; the hotel's own window otherwise) →
   record the **cheapest refundable one-bed room**: name, bed count, $/night, total, "Free cancellation before [date]", prepayment, units-left.
2. **Fetch official brand page** (Accor fact-sheet/booking, Marriott `/rooms/`, Nine Tree room page, Hyatt, Lotte, Josun, Ascott JSON-LD, Shilla) →
   record **bed size/type** (queen/king/double + mm where published), star, address, room names.
3. **Reconcile**: bed count (Booking) vs bed size (official) vs repo data → flag mismatches. Confirm the captured "refundable" room is actually the **one-bed** room, not a 2-bed room (the known Fairmont/Somerset/Moxy issue).

Estimated effort: ~50 fetches for 25 hotels, all proven feasible.

---

## 3. Known gaps / things that still can't be fully automated

- **Official-site live price** (Accor/Marriott/Hyatt direct) is JS/login-gated — Booking (and Agoda as a second OTA) are the machine-readable price+refundable sources, but an OTA rate can differ from direct-booking member rates. Always note the source.
- **Exact bed mm** is published only by a subset of hotels (Accor "queen/king size", Nine Tree mm, some Korean sites). For hotels that only say "double/full" with no width, bed *size* remains "not published" — must be flagged, not guessed.
- **Booking "full bed" ≠ authoritative width** for Korean hotels (a 160 cm bed is commonly labeled "full"). This is exactly why bed size must come from the official source, not Booking.

---

## 4. Source-URL templates (reusable)

- **Booking (price + refundable + bed count):**
  `https://www.booking.com/hotel/kr/{slug}.html?checkin={in}&checkout={out}&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD`
- **Accor fact-sheet (bedding + star + address):** `https://all.accor.com/hotel/{code}/index.en.shtml`
- **Accor direct booking (bedding + availability):** `https://all.accor.com/booking/en/accor/hotel/{code}?productCode={roomCode}&dateIn={in}&nights={n}&compositions=2`
- **Marriott rooms (bed config per roomPoolCode):** `https://www.marriott.com/en-us/hotels/{marshaCode}/rooms/`
- **Nine Tree room specs (exact mm):** `https://www.ninetreehotels.com/{nth1|nth2|nth3}/room_{type}.php`
- **Ascott/Ascott JSON-LD (bed + amenities):** `https://www.discoverasr.com/en/…/{property}/{room-slug}`
- **Agoda (second OTA cross-check):** `https://www.agoda.com/{slug}/hotel/{city}-kr.html?checkIn={in}&los={n}&adults=2&rooms=1`

### Known slug/id issues to resolve before a full run
- **Shilla Stay** official site has migrated: `shillastay.com/…` now redirects to **`shillahotels.com/ko/shillastay/…`** — the repo's Shilla URLs should be updated.
- **Booking slugs** for some hotels were 404 in prior passes (e.g. Courtyard Seoul Myeongdong, Nine Tree MD2/Insadong). Correct slugs must be resolved per hotel (the repo already stores the working `refundableRate.sourceUrl` for the 18 Seoul captures).
- **Trip.com** requires the correct `hotel-detail-{id}` per property; wrong IDs silently return a different hotel — use only as last resort.

---

## 5. Next step (ready to execute)

Run the 2-fetch-per-hotel method over all **25 in-scope hotels** (20 Seoul/Myeongdong + 5 Suwon), record results in a single line-by-line table with source URLs + UTC capture timestamps, and update `refundableRate` blocks + bed fields where the official source contradicts the data. The 7 hotels currently missing `refundableRate` (Aloft MD, Four Points Josun MD, + all 5 Suwon) are the priority.
