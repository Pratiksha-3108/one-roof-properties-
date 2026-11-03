with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find CSS for sr-
css_block = re.findall(r'/\* =+ \*/\s*/\* CATEGORY SHOWCASE SECTION.*?\*/(.*?)(?=/\* =+ \*/|\Z)', text, re.DOTALL)
if css_block:
    print(css_block[0][:2500])
else:
    # search for sr-node
    pos = text.find('.sr-node-name')
    print(text[pos-400:pos+800])

