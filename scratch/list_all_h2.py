with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find any other sections with project or properties
headings = re.findall(r'<h2[^>]*>(.*?)</h2>', text, re.IGNORECASE)
for h in headings:
    print('H2:', h.strip())

