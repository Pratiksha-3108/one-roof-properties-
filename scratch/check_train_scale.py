with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

pos = text.find('function updateTrainPositions')
if pos != -1:
    print(text[pos:pos+1200])

