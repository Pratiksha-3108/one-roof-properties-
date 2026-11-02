with open('services.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
items = re.findall(r'<h3 class="card-service-title">([^<]+)</h3>\s*<div class="card-service-headline">([^<]+)</div>\s*<p class="card-service-desc">([^<]+)</p>', text)
print(f"Total service cards: {len(items)}")
for title, head, desc in items:
    print('TITLE:', title.strip())
    print('HEAD:', head.strip())
    print('DESC words:', len(desc.strip().split()), 'chars:', len(desc.strip()))
    print('---')

