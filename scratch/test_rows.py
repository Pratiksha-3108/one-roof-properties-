with open('services.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
rows = re.findall(r'<div class="stagger-row[^"]*" id="service-row-\d+">.*?</div>\s*</div>', text, re.DOTALL)
print('Total rows found:', len(rows))

