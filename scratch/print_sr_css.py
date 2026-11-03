with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(\.sr-[a-zA-Z0-9_-]+\s*\{[^}]+\})', text)
for m in matches:
    if any(k in m for k in ['node', 'portal', 'project', 'viewport', 'train']):
        print(m)
        print('-'*40)

