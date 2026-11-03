with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find about section in index.html
about_matches = re.finditer(r'<section[^>]*id=["\'][^"\']*about[^"\']*["\'][^>]*>|<div[^>]*class=["\'][^"\']*about[^"\']*["\'][^>]*>', text, re.I)
for m in about_matches:
    start = m.start()
    print("Match at", start)
    print(text[start:start+500])
    print('='*50)

# Also search for img inside about section
about_imgs = re.findall(r'<div class="about-image-expand-box"[^>]*>.*?</div>', text, re.DOTALL)
for ai in about_imgs:
    print("about-image-expand-box:", ai)

