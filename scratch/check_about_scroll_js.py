with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(\/\* [^*]*ABOUT SCROLL[^*]*\*\/.*?(?=\/\*|$))', text, re.DOTALL)
if matches:
    print(matches[0][:800])
else:
    # search for aboutExpandSection in script
    for m in re.finditer(r'aboutExpandSection', text):
        pos = m.start()
        print(text[pos-100:pos+500])
        print('='*50)

