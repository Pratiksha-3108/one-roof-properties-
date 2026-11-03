with open('services.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
titles = re.findall(r'(\.[a-zA-Z0-9_-]*(?:title|headline|subtitle|subtext|desc)[a-zA-Z0-9_-]*\s*\{[^}]+\})', text)
for t in titles:
    print(t)
    print('-'*40)

