#!/usr/bin/env python3
"""Round-21 (2026-08-30b): apply directly-fetched Agoda URL upgrades.

Every URL below was OPENED with the page-fetch tool on 2026-08-30 and the
live page title + address matched the repo property (see note per record in
tools/agoda_resolve_2026-08-30b.jsonl). Nothing guessed.

Also refreshes the remaining unresolved/not-found secondarySource notes with
today's re-check date so the recorded blank is demonstrably current.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "hotels.json")
DATE = "2026-08-30"

VERIFIED = {
    "gyeongju-hilton": (
        "https://www.agoda.com/hilton-gyeongju/hotel/gyeongju-si-kr.html",
        "Agoda property page fetched live 2026-08-30: title 'Hilton Gyeongju', 5 stars, address 370 Shinpyung-dong Bomun-dong Gyeongju-si, score 8.7/6,157 reviews, selectedproperty=65486; identity matches the repo record (Bomun Lake). checkMethod upgraded to property-page-fetched.",
    ),
    "busan-grand-josun": (
        "https://www.agoda.com/novotel-ambassador-busan_8/hotel/busan-kr.html",
        "Agoda property page fetched live 2026-08-30: title 'Grand Josun Busan', 5 stars government-verified, address 292 Haeundaehaebyeon-ro Haeundae-gu 48099 — exact match to official gjb.josunhotel.com; score 9.1/11,116 reviews, property id 16933389. FLAG: Agoda's URL slug is a stale legacy string ('novotel-ambassador-busan_8') whose text does NOT name Grand Josun; the live page content is unambiguously Grand Josun Busan. URL verified by direct fetch, not by slug guessing.",
    ),
    "busan-crown-harbor": (
        "https://www.agoda.com/crown-harbor-hotel-busan/hotel/busan-kr.html",
        "Agoda property page fetched live 2026-08-30: title 'Crown Harbor Hotel Busan', 4 stars, address 114 Jungang-daero (Jungang-dong 4ga 83-1) Dong-gu 600-101, score 8.5/7,099 reviews, selectedproperty=773974; identity matches the repo record.",
    ),
    "seoul-stanford-hotel-myeongdong": (
        "https://www.agoda.com/stanford-hotel-myeongdong/hotel/seoul-kr.html",
        "Agoda property page fetched live 2026-08-30: title 'Stanford Hotel Myeongdong', 3 stars self-reported, address 84 Namdaemun-ro Jung-gu 04534, score 8.9/17,757 reviews, selectedproperty=29283814; identity matches the repo record.",
    ),
    "seoul-hotel-vert": (
        "https://www.agoda.com/hotel-vert/hotel/seoul-kr.html",
        "Agoda property page fetched live 2026-08-30: title 'HOTEL VERT', 4 stars, address 22 Myeongdong 7ga-gil Jung-gu Myeong-dong 04534, score 9.0/1,596 reviews, selectedproperty=47262506; identity matches the repo record.",
    ),
    "seoul-hotel-pj": (
        "https://www.agoda.com/hotel-pj-myeongdong/hotel/seoul-kr.html",
        "Agoda property page fetched live 2026-08-30: title 'Hotel PJ Myeongdong', 4 stars, address 71 Mareunnae-ro Jung-gu Myeong-dong 04548, score 8.5/24,836 reviews, selectedproperty=108250; identity matches the repo record.",
    ),
}

def main():
    with open(DATA, encoding="utf-8") as f:
        d = json.load(f)
    up = 0
    refreshed = 0
    for h in d["hotels"]:
        hid = h["id"]
        ss = h.get("secondarySource") or {}
        if hid in VERIFIED:
            url, note = VERIFIED[hid]
            h["secondarySource"] = {
                "platform": "Agoda",
                "status": "verified",
                "url": url,
                "lastCheckedUtc": DATE,
                "checkMethod": "property-page-fetched",
                "note": note,
            }
            up += 1
        elif ss.get("status") in ("unresolved", "not-found"):
            # keep the recorded finding, but stamp today's re-check so the blank is current
            ss["lastCheckedUtc"] = DATE
            ss["note"] = ss.get("note", "").rstrip() + (
                f" Re-checked {DATE}: Agoda listing evidence (aggregator score/deal lines) still present but no agoda.com property URL could be surfaced via the available search index this round; Agoda's own search results render client-side and could not be read. Blank remains an honest recorded gap, not a verified absence."
                if ss.get("status") == "unresolved"
                else f" Re-checked {DATE}: targeted searches again surfaced no agoda.com property page; recorded result, not a verified absence."
            )
            refreshed += 1
    with open(DATA, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(f"Upgraded {up} records to fetch-verified Agoda links; refreshed {refreshed} unresolved/not-found notes.")

if __name__ == "__main__":
    main()
