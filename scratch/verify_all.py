with open('services.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
titles = re.findall(r'<h3 class="card-service-title">([^<]+)</h3>', text)
print('Titles count:', len(titles))
for i, t in enumerate(titles):
    print(f'  {i+1}. {t}')

imgs = re.findall(r'<div class="stagger-photo-card">\s*<img src="([^"]+)"', text)
print('Images count:', len(imgs))
for i, im in enumerate(imgs):
    print(f'  {i+1}. {im}')

assert len(titles) == 6, f'Expected 6 titles, got {len(titles)}'
assert len(imgs) == 6, f'Expected 6 images, got {len(imgs)}'
assert 'stagger-empty-spacer' not in text, 'stagger-empty-spacer should be removed'
assert 'applyTransform' not in text, 'applyTransform should be removed'
assert 'hero-metrics' not in text, 'hero-metrics should be removed'
print('All checks successfully verified!')

