with open('services.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
imgs = re.findall(r'<div class="stagger-photo-card">\s*<img src="([^"]+)"', text)
print('Images used in stagger-photo-card:', imgs)

from PIL import Image
for im_path in imgs:
    try:
        im = Image.open(im_path)
        print(im_path, im.size)
    except Exception as e:
        print(im_path, 'Error:', e)

