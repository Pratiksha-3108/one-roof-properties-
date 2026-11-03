with open('about.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

for img in ['realestate23', 'realestate24']:
    matches = [m.start() for m in re.finditer(img, text)]
    print(f'{img} found {len(matches)} times at {matches}')

