#!/usr/bin/env python3
"""
Build script: generates index.html from the template + data files.

Why this exists (improvement #3 — "one source of truth"):
  - Hotel, arrival-night, itinerary, and trip data lives in data/*.json
  - index.template.html holds the HTML/JS shell with a __DATA__ placeholder
  - Running this script regenerates index.html so the embedded data never
    falls out of sync with the JSON files.

Usage:
    python3 build.py
"""
import json

from findings import build_findings

HOTELS = 'data/hotels.json'
ITINERARY = 'data/itinerary.json'
TEMPLATE = 'index.template.html'
OUTPUT = 'index.html'


def load(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def html_escape(value):
    return (str(value or '')
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;'))


def booking_url(hotel):
    for key in ('refundableRate', 'refundableRateNov9', 'refundableRateNov15'):
        url = (hotel.get(key) or {}).get('sourceUrl') or ''
        if 'booking.com' in url:
            return url.split('?')[0]
    v = ((hotel.get('verification') or {}).get('sourceUrl') or '')
    if 'booking.com' in v:
        return v.split('?')[0]
    return ''


def agoda_directory_html(hotels):
    city_order = ['Seoul', 'Gyeongju', 'Busan', 'Cheonan', 'Daejeon', 'Suwon']
    rows = []
    for city in city_order:
        for hotel in [h for h in hotels if h.get('city') == city]:
            ss = hotel.get('secondarySource') or {}
            agoda = ss.get('url') or ''
            kind = ss.get('linkType') or ''
            booking = booking_url(hotel)
            agoda_cell = (
                f'<a href="{html_escape(agoda)}" target="_blank" rel="noopener noreferrer"><strong>Agoda</strong> ↗</a>'
                if agoda else '—'
            )
            booking_cell = (
                f'<a href="{html_escape(booking)}" target="_blank" rel="noopener noreferrer"><strong>Booking.com</strong> ↗</a>'
                if booking else '—'
            )
            rows.append(
                '<tr>'
                f'<td>{html_escape(hotel.get("city"))}</td>'
                f'<td>{html_escape(hotel.get("name"))}</td>'
                f'<td>{agoda_cell}</td>'
                f'<td>{booking_cell}</td>'
                f'<td>{html_escape(kind)}</td>'
                '</tr>'
            )
    body = '\n'.join(rows)
    return (
        '<table class="data-table">'
        '<caption class="source-line" style="caption-side:top;text-align:left">'
        f'{len(rows)} hotels · Agoda is the main labeled verified source · Booking.com is the dated-rate source'
        '</caption>'
        '<thead><tr><th>City</th><th>Hotel</th><th>Agoda</th><th>Booking.com</th><th>Agoda page type</th></tr></thead>'
        f'<tbody>{body}</tbody></table>'
    )


def main():
    hotels = load(HOTELS)
    itinerary = load(ITINERARY)

    data = {
        'trip': hotels['trip'],
        'split': hotels['split'],
        'arrivalNight': hotels.get('arrivalNight', {}),
        'itinerary': itinerary,
        'hotels': hotels['hotels'],
        'findings': build_findings(hotels, itinerary),
        'meta': hotels.get('meta', {}),
    }
    data_json = json.dumps(data, ensure_ascii=False, separators=(',', ':'))

    with open(TEMPLATE, encoding='utf-8') as f:
        template = f.read()

    assert '__DATA__' in template, "placeholder __DATA__ missing in template"
    assert '__AGODA_DIRECTORY__' in template, "placeholder __AGODA_DIRECTORY__ missing in template"
    html = template.replace('__DATA__', data_json)
    html = html.replace('__AGODA_DIRECTORY__', agoda_directory_html(hotels['hotels']))

    with open(OUTPUT, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Built {OUTPUT} ({len(html)} bytes) from {HOTELS} + {ITINERARY}")


if __name__ == '__main__':
    main()
