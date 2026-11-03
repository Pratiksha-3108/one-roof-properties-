with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Look for titles, subtitles, headings in index.html CSS
headings = re.findall(r'(\.[a-zA-Z0-9_-]*(?:title|subtitle|subtext|headline|heading|h2|h3)[a-zA-Z0-9_-]*\s*\{[^}]+\})', text)
for h in headings[:15]:
    print(h)
    print('-'*40)

