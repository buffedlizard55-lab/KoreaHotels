#!/usr/bin/env python3
"""Line-by-line consistency audit for data/hotels.json.

Run:  python3 tools/audit_records.py
Ten checks: window naming, sourceUrl dates vs stay dates, night counts,
price arithmetic, live-rate completeness, future timestamps, price-without-
availability, distributionStatus coverage, OTA-as-officialUrl, verification source.
"""
import json,re,sys
from urllib.parse import urlparse,parse_qs
d=json.load(open('data/hotels.json',encoding='utf-8'))
H=d['hotels']
issues=[]
def add(sev,hid,msg): issues.append((sev,hid,msg))

RATE_FIELDS=[('refundableRate',None),('refundableRateNov9',('2026-11-09','2026-11-15')),
             ('refundableRateNov15',('2026-11-15','2026-11-22'))]
TODAY='2026-08-22'

for h in H:
    hid=h['id']
    for f,expect in RATE_FIELDS:
        r=h.get(f)
        if not isinstance(r,dict): continue
        ci,co,n=r.get('stayCheckIn'),r.get('stayCheckOut'),r.get('nights')
        ppn,tot=r.get('pricePerNight'),r.get('totalStay')
        url=r.get('sourceUrl') or ''
        cap=r.get('capturedAtUtc')

        # 1. field-name vs actual stay dates
        if expect and (ci,co)!=expect and r.get('available') is not None:
            add('HIGH',hid,f"{f}: stay dates {ci}->{co} do not match the field's window {expect[0]}->{expect[1]}")

        # 2. URL dates must match the stay dates
        if 'booking.com' in url:
            q=parse_qs(urlparse(url).query)
            uci=(q.get('checkin') or [None])[0]; uco=(q.get('checkout') or [None])[0]
            if uci and ci and uci!=ci: add('HIGH',hid,f"{f}: sourceUrl checkin {uci} != stayCheckIn {ci}")
            if uco and co and uco!=co: add('HIGH',hid,f"{f}: sourceUrl checkout {uco} != stayCheckOut {co}")

        # 3. nights vs date span
        if ci and co and n:
            from datetime import date
            a=date(*map(int,ci.split('-'))); b=date(*map(int,co.split('-')))
            if (b-a).days!=n: add('HIGH',hid,f"{f}: nights={n} but {ci}->{co} is {(b-a).days} nights")

        # 4. arithmetic sanity
        if isinstance(ppn,(int,float)) and isinstance(tot,(int,float)) and n:
            implied=ppn*n
            if implied>0 and abs(implied-tot)/max(tot,1) > 0.06:
                add('CHECK',hid,f"{f}: {ppn}/nt x {n} = {implied} but totalStay={tot} (diff {abs(implied-tot)/tot*100:.1f}%) — verify it is a discounted total")

        # 5. live rate completeness
        live = r.get('available') is True and isinstance(ppn,(int,float))
        if live:
            for req in ('capturedAtUtc','sourceUrl','room','beds','freeCancellation','prepayment','currency'):
                if not r.get(req): add('HIGH',hid,f"{f}: live rate missing '{req}'")
        # 6. capture date sanity
        if cap and cap[:10] > TODAY: add('HIGH',hid,f"{f}: capturedAtUtc {cap} is in the future vs {TODAY}")
        # 7. available true but no price
        if r.get('available') is True and not isinstance(ppn,(int,float)):
            add('CHECK',hid,f"{f}: available=true but no pricePerNight (partial capture?)")
        # 8. price present but available not true
        if isinstance(ppn,(int,float)) and r.get('available') is not True:
            add('HIGH',hid,f"{f}: has a price but available is {r.get('available')}")

    # 9. no rate anywhere -> must have distributionStatus
    def livef(f):
        r=h.get(f) or {}
        return bool(r.get('capturedAtUtc') and r.get('pricePerNight'))
    if not any(livef(f) for f,_ in RATE_FIELDS) and not h.get('distributionStatus'):
        add('HIGH',hid,"no live rate in any window and no distributionStatus")

    # 10. bed-conflict rows must not be fits=true
    blob=json.dumps(h,ensure_ascii=False)
    if h.get('fits') and ('CONFLICT' in blob or 'despite' in blob.lower()):
        add('HIGH',hid,"fits=true but the record contains a bed-label conflict")

    # 11. officialUrl must not be an OTA
    ou=h.get('officialUrl') or ''
    if ou and ('booking.com' in ou or 'agoda' in ou or 'kayak' in ou or 'tripadvisor' in ou):
        add('HIGH',hid,f"officialUrl points at an OTA: {ou}")

    # 12. verification sourceUrl present & http
    v=h.get('verification') or {}
    if not (v.get('sourceUrl','').startswith('http')): add('HIGH',hid,"verification.sourceUrl missing/invalid")

print("=== RECORD-LEVEL AUDIT ===")
for sev in ('HIGH','CHECK'):
    sel=[i for i in issues if i[0]==sev]
    print(f"\n--- {sev}: {len(sel)} ---")
    for s,hid,m in sel[:60]: print(f"  [{hid}] {m}")
    if len(sel)>60: print(f"  ... +{len(sel)-60} more")
