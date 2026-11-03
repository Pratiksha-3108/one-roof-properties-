with open('services.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

for i, m in enumerate(re.finditer(r'<i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>', text)):
    print(f'Match {i+1} at position {m.start()}')

