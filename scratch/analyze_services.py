with open('services.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
heroes = [m.start() for m in re.finditer(r'<section class=.services-hero', text)]
print('Hero sections count:', len(heroes), heroes)

services = [m.start() for m in re.finditer(r'<section class=.services-staggered-section', text)]
print('Services sections count:', len(services), services)

headers = [m.start() for m in re.finditer(r'<header class=.header', text)]
print('Header count:', len(headers), headers)

