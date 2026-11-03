with open('services.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

rows = re.findall(r'<div class="stagger-row ([^"]+)" id="([^"]+)">(.*?)</div>\s*</div>\s*(?:<!--|<div|</section>)', text, re.DOTALL)
print('Total rows found:', len(rows))
for r_type, r_id, content in rows:
    has_spacer = 'stagger-empty-spacer' in content
    photo = re.findall(r'<div class="stagger-photo-card">\s*<img src="([^"]+)"', content)
    title = re.findall(r'<h3 class="card-service-title">([^<]+)</h3>', content)
    print(f"Row {r_id} ({r_type}):")
    print(f"  Title: {title[0] if title else 'NONE'}")
    print(f"  Photo: {photo[0] if photo else 'NONE'}")
    print(f"  Has spacer: {has_spacer}")

assert len(rows) == 6
assert 'applyTransform' not in text
print("All checks passed!")

