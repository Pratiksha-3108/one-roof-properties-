import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'<section[^>]*id=["\']([^"\']+)["\']', text):
    print(m.group(1))

