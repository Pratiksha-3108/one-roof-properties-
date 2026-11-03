with open('about.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find vision and mission in about.html
vm_matches = re.findall(r'(.{0,100}(?:vision|mission).{0,150})', text, re.IGNORECASE)
for m in vm_matches[:10]:
    print(m.strip())
    print('-'*40)

