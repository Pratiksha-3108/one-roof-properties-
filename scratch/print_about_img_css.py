with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(\.about-image-expand-box[^{]*\{[^}]+\})', text)
for m in matches:
    print(m)
    print('-'*40)
matches_img = re.findall(r'(\.about-image-expand-box\s+img\s*\{[^}]+\})', text)
for m in matches_img:
    print(m)
    print('-'*40)

