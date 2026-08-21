import json
CAP="2026-08-21T19:20:00Z"
SRC="Booking.com property page — dated rate table (live fetch 2026-08-21)"
def u(slug,extra=""):
    return ("https://www.booking.com/hotel/kr/%s.html?checkin=2026-11-09&checkout=2026-11-15"
            "&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD%s"%(slug,extra))

UP={
"busan-grand-josun": dict(slug="grand-josun-busan", available=True,
  room="Premier King Room with City View", beds="1 queen bed (Booking label) — 463 ft², sauna for 2 + Gran J lounge access",
  pricePerNight=327, totalStay=1965, currency="USD (display; 10% TAX excluded)", breakfastIncluded=True,
  freeCancellation="Free cancellation before November 7, 2026 — free until 2 days before arrival; ⚠️ inside 2 days AND no-show are charged the TOTAL price of the reservation",
  prepayment="No prepayment needed — pay at the property",
  note="LIVE 2026-08-21. Only 2 left. Buffet breakfast for 2 included. IRREGULARITY confirmed again: the room is sold as 'Premier King' but Booking states '1 queen bed' — same conflict the 2026-08-18 pass recorded. Kids Deluxe Twin (1 twin + 1 full) $266/$1,596. A Partner Offer row at $208/nt, $1,249 (KRW 173,803 tax excluded, free cancellation before Nov 5, PAY IN ADVANCE, no modifications) had its room label cut at a page-chunk boundary and is not recorded."),
"busan-lotte-hotel": dict(slug="lotte-busan", available=True,
  room="Premier Double with swimming pool, fitness, sauna access for 2pax",
  beds="1 full bed (397 ft²; Booking text: 'includes one double bed and has no capacity for an extra bed')",
  pricePerNight=197, totalStay=1313, currency="USD (display; 10% service charge INCLUDED; 10% TAX excluded)",
  breakfastIncluded=False,
  freeCancellation="Free cancellation before November 8, 2026 — free until 1 day before arrival; then the first night",
  prepayment="No prepayment needed — pay at the property",
  note="LIVE 2026-08-21. The same room also sells as a Partner Offer at $186/nt, $1,211 (KRW 132,107 service charge included, KRW 194,442 tax excluded) — free cancellation before Nov 8 but PAY IN ADVANCE with no modifications. Breakfast-inclusive variant $262/$1,742 ($50 pp otherwise). Deluxe Twin (2 twin) $163/$1,085. IRREGULARITY: the 2026-08-18 Nov 15–22 capture used a 'Deluxe Double Room' called 1 king bed at $162 — a different room tier from this one, so the two windows are not like-for-like."),
"busan-park-hyatt": dict(slug="park-hyatt-busan", available=True,
  room="King Room (refundable rate)", beds="1 king bed (452 ft², Busan Marina/city view)",
  pricePerNight=361, totalStay=2166, currency="USD (display; 10% TAX excluded)", breakfastIncluded=False,
  freeCancellation="Free cancellation before November 8, 2026 — free until 1 day before arrival; then the first night",
  prepayment="No prepayment needed — pay at the property",
  note="LIVE 2026-08-21. ⚠️ The cheaper $303/nt ($1,820) rate on the same King Room is NON-REFUNDABLE, pay online. King Room with Ocean View: $324/$1,945 non-refundable, $463/$2,779 refundable. Breakfast $45 pp."),
"busan-signiel": dict(slug="signiel-busan", available=True,
  room="Premier Double Room with City View (Salon de Signiel lounge access)",
  beds="1 king bed — Booking also lists 'Extra long beds (> 80 inches)'; balcony/terrace",
  pricePerNight=280, totalStay=1868,
  currency="USD (display; total before taxes $1,867.95 after a 7% property discount from $2,008.55; 10% service charge INCLUDED; 10% TAX excluded)",
  breakfastIncluded=False,
  freeCancellation="Free cancellation before November 4, 2026 — free until 5 days before arrival; then the first night",
  prepayment="Pay nothing until November 2, 2026 (payment then due, property time)",
  note="LIVE 2026-08-21. 4 left. Longest free-cancellation runway of any Busan record in this window (5 days). Breakfast-inclusive variant $356/$2,372."),
"busan-westin-josun": dict(slug="the-westin-chosun-busan", available=True,
  room="Deluxe Park King, 1 King, Dongbaek Park view",
  beds="⚠️ Booking bed label is '1 full bed' for this King-named room (312 ft²)",
  pricePerNight=220, totalStay=1467,
  currency="USD (display; 10% service charge INCLUDED; 10% VAT excluded)", breakfastIncluded=False,
  freeCancellation="Free cancellation before November 7, 2026 — free until 2 days before arrival; then the first night",
  prepayment="No prepayment needed — pay at the property",
  note="LIVE 2026-08-21, re-fetched with Booking's king-bed filter to resolve the earlier partial capture. 3 left. IRREGULARITY: Marriott sells this as a Deluxe King, but the Booking row states a full bed — same conflict as the 2026-08-18 capture. Breakfast-inclusive variant $285/$1,897. Low Floor Beach Family (1 twin + 1 full) $235/$1,562."),
"busan-fairfield-songdo": dict(slug="fairfield-by-marriott-busan-songdo-beach", available=True,
  room="Standard Room - Guest room, 1 King, Sea view", beds="1 king bed (323 ft², sea + landmark view)",
  pricePerNight=127, totalStay=761, currency="USD (display; 10% VAT excluded)", breakfastIncluded=False,
  freeCancellation="Free cancellation before November 9, 2026 — free until 12:00 AM on the day of arrival; then the first night",
  prepayment="No prepayment needed — pay at the property",
  note="LIVE 2026-08-21, re-fetched with Booking's king-bed filter — this resolves the earlier partial capture in which only the 2-twin sea-view room could be named at this price. 5 left. Breakfast-inclusive variant $147/$882."),
}

d=json.load(open('data/hotels.json',encoding='utf-8'))
by={h['id']:h for h in d['hotels']}
hist=json.load(open('data/pricing-history.json',encoding='utf-8'))

for hid,r in UP.items():
    slug=r.pop('slug')
    b={"capturedAtUtc":CAP,"source":SRC,"sourceUrl":u(slug),
       "stayCheckIn":"2026-11-09","stayCheckOut":"2026-11-15","nights":6}
    b.update(r)
    by[hid]['refundableRateNov9']=b
    hist['captures'].append({"captureId":"%s-%s-nov9"%(CAP,hid),"hotelId":hid,"capturedAtUtc":CAP,
      "sourceUrl":b["sourceUrl"],"refundableAvailable":True,
      "rates":[{"room":b["room"],"beds":b["beds"],"meetsOneBedNeed":None,
                "pricePerNightUsd":b["pricePerNight"],"totalStayUsd":b["totalStay"],
                "taxNote":b["currency"],"cancellationAsShown":b["freeCancellation"]}],
      "note":b["note"]})

# Ramada Encore Haeundae — verified SOLD OUT
b={"capturedAtUtc":CAP,"source":SRC,
   "sourceUrl":u("haeundae-ramada-encore"),
   "stayCheckIn":"2026-11-09","stayCheckOut":"2026-11-15","nights":6,
   "available":False,"room":None,"beds":"Room list shown but unbookable: 1 King Suite, 1 King Corner Suite, 1 Queen Mobility Accessible, 1 Queen + 1 Twin Family/Corner Suite, Superior 1 Queen",
   "pricePerNight":None,"totalStay":None,"currency":None,"breakfastIncluded":False,
   "freeCancellation":None,"prepayment":None,
   "note":"VERIFIED SOLD OUT 2026-08-21: Booking states 'We have no availability here between Mon, Nov 9, 2026 and Sun, Nov 15, 2026.' Every room type is marked 'Not available on our site for your dates'. Booking also tags this property 'Adults only'. Address 9, Gunam-ro, Haeundae-gu — distinct from Ramada Encore Busan Station."}
by['busan-ramada-encore-haeundae']['refundableRateNov9']=b
hist['captures'].append({"captureId":"%s-busan-ramada-encore-haeundae-nov9"%CAP,
  "hotelId":"busan-ramada-encore-haeundae","capturedAtUtc":CAP,"sourceUrl":b["sourceUrl"],
  "refundableAvailable":False,"rates":[],"note":b["note"]})

IBIS_NOTE=("Not distributable on Booking.com as of 2026-08-21. The guessed Booking slug redirected to the Busan "
 "search-results page, and Booking's own Busan brand filter for these dates lists no ibis/Accor brand at all. "
 "An independent listing (hotel.com.au) states the property 'isn't taking reservations on our site right now' and "
 "'may have changed name or is no longer bookable'. The property itself is still evidenced at 12 Haeundaehaebyeon-ro "
 "237beon-gil, Haeundae-gu (3-star, 24-hour reception). NO price, refundable status or bed count is recorded for "
 "Nov 9–15 — book direct through Accor and confirm the bed in writing.")
for hid,acc in (("busan-ibis-haeundae","https://all.accor.com/hotel/9643/index.en.shtml"),
                ("busan-ibis-budget-haeundae","https://all.accor.com/hotel/9106/index.en.shtml")):
    by[hid]['refundableRateNov9']={"capturedAtUtc":None,
      "source":"Checked 2026-08-21 — no dated OTA rate page reachable","sourceUrl":acc,
      "stayCheckIn":"2026-11-09","stayCheckOut":"2026-11-15","nights":6,
      "available":None,"room":None,"beds":None,"pricePerNight":None,"totalStay":None,
      "currency":None,"breakfastIncluded":False,"freeCancellation":None,"prepayment":None,
      "note":IBIS_NOTE}

m=d['meta']['refundableRateCaptures']['busanNov9Window']
m['capturedAtUtc']=CAP
m['fullyCaptured']=18
m['partial']=[]
m['soldOut']=["busan-ramada-encore-haeundae"]
m['notCaptured']=["busan-ibis-haeundae","busan-ibis-budget-haeundae"]
m['notCapturedReason']="Neither ibis Ambassador Busan Haeundae property is bookable on Booking.com; no dated rate page exists to quote."
d['meta']['pricingLastChecked']="2026-08-21"

json.dump(d,open('data/hotels.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
json.dump(hist,open('data/pricing-history.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
n9=[h for h in d['hotels'] if h['city']=='Busan']
print('busan records',len(n9),'| priced nov9',sum(1 for h in n9 if (h.get('refundableRateNov9') or {}).get('totalStay')),
      '| sold out',sum(1 for h in n9 if (h.get('refundableRateNov9') or {}).get('available') is False))
