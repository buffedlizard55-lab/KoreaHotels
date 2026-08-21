import sys; sys.path.insert(0,'.')
import json
from findings import build_findings
h=json.load(open('data/hotels.json',encoding='utf-8'))
it=json.load(open('data/itinerary.json',encoding='utf-8'))
f=build_findings(h,it)
def esc(s): return (str(s or '')).replace('|','\\|').replace('\n',' ').strip()
def short(s,n=110):
    s=esc(s); return s if len(s)<=n else s[:n-1]+'…'
def cancel(s):
    s=esc(s)
    for sep in (' — ','—'):
        if sep in s: s=s.split(sep)[0]
    return short(s,64)
def table(window,cities=None):
    rows=[q for q in f['quotes'] if q['windowKey']==window]
    if cities: rows=[q for q in rows if q['city'] in cities]
    rows.sort(key=lambda q:(q['city'],q['totalStay']))
    out=['| Hotel | City · area | Room captured | Beds on the sold row | Refundable — free until | $/night | Total | Captured (UTC) | Verify |',
         '|---|---|---|---|---|---:|---:|---|---|']
    for q in rows:
        out.append('| %s | %s · %s | %s | %s | %s | $%s | **$%s** | %s | [dated rate](%s) |'%(
            esc(q['name']),esc(q['city']),short(q['area'],28),short(q['room'],70),short(q['beds'],80),
            cancel(q['freeCancellation']) or '—',q['pricePerNight'],f"{q['totalStay']:,}",
            esc((q['capturedAtUtc'] or '')[:10]),q['sourceUrl']))
    return '\n'.join(out),len(rows)
for k,n in (('nov1',None),('nov15',None)):
    t,c=table(k); open('.work/t_%s.md'%k,'w').write(t); print(k,c)
t,c=table('nov9',{'Busan'}); open('.work/t_nov9.md','w').write(t); print('nov9 busan',c)
t,c=table('nov9',{'Gyeongju'}); open('.work/t_nov9_gj.md','w').write(t); print('nov9 gyeongju',c)
