import cv2
import numpy as np

# Let's inspect the crops
for i in [3, 4, 5, 6, 7, 8, 9, 10]:
    im = cv2.imread(f'scratch/torch_anim/crop_center_{i:02d}.jpg')
    print(f'Crop {i} shape: {im.shape}')

# Let's check if the video has torchsensors.html in scratch from earlier
import os
if os.path.exists('scratch/torchsensors.html'):
    print('Found scratch/torchsensors.html!')
    html = open('scratch/torchsensors.html', 'r', encoding='utf-8').read()
    print('Length of torchsensors.html:', len(html))
    # Look for interactions, webflow animations, GSAP, lottie, etc.
    for kw in ['data-w-id', 'ix2', 'gsap', 'scrollTrigger', 'transform', 'scale', 'parallax', 'swiper']:
        print(f'Keyword "{kw}" count:', html.count(kw))
else:
    print('torchsensors.html not found in scratch')

