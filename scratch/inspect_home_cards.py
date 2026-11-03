with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find cards in index.html
cards = re.findall(r'(<div class="[^"]*card[^"]*"[^>]*>.*?</div>\s*</div>)', text, re.DOTALL)
print(f'Total cards found: {len(cards)}')
for c in cards[:5]:
    # print first 300 chars of each
    print(c[:300].strip())
    print('='*40)

