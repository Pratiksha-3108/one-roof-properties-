with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'about-building', text)]
print('Occurrences of about-building in index.html:', len(matches), matches)
for m in matches:
    print(text[m-50:m+100])
    print('-'*40)

