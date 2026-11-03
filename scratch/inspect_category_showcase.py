with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

pos = text.find('categoryShowcaseSection')
print("Position:", pos)
print(text[pos:pos+1500])

