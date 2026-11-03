with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

for m in re.finditer(r'trainRes', text):
    p = m.start()
    if p > 100000: # inside script
        print(text[p-200:p+800])
        print('='*50)

