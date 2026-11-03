with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find project section in index.html
proj_sections = re.findall(r'(<section[^>]*id=["\'][^"\']*(?:project|residen|prop)[^"\']*["\'][^>]*>.*?</section>)', text, re.DOTALL | re.IGNORECASE)
print(f'Total project sections found: {len(proj_sections)}')
for p in proj_sections:
    # Print the opening tag and first 200 chars
    print(p[:300].strip())
    print('='*40)

