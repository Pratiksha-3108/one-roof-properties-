with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Search for card styles in index.html
card_titles = re.findall(r'(\.[a-zA-Z0-9_-]*(?:card-title|card-heading|card-name|card-sub|card-desc|card-header)[a-zA-Z0-9_-]*\s*\{[^}]+\})', text)
for c in card_titles[:15]:
    print(c)
    print('='*40)

