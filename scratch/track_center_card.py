import cv2
import numpy as np

# In frame 0:
f0 = cv2.imread('scratch/detailed_anim/frame_0000.jpg')
# Where is the image card?
# In frame 0, we have the Torch Sensors hero / services section:
# Look at the cards visible:
# Top middle: Card with Torch sensor 3D render (silver and black capsule).
# Top right: Card with "High accuracy".
# Below it on left: Card with "Harsh weather survival".
# Center: Card with Torch sensor in rain.
# Bottom right: Card with "Easy installation".
# Bottom center: Card with Torch sensor on tree trunk.

# As the page is scrolled:
# Look at the image card:
# Does the image inside ZOOM IN or SCALE as it reaches the center?
# Or does the card have a floating / parallax animation?
# Let's inspect the bounding box of the center image card across frames:
for idx in [0, 20, 40, 60, 80, 100, 120, 140, 160, 180]:
    im = cv2.imread(f'scratch/detailed_anim/frame_{idx:04d}.jpg')
    if im is None: continue
    # Save a crop of the center card
    crop = im[100:600, 400:850]
    cv2.imwrite(f'scratch/detailed_anim/center_card_{idx}.jpg', crop)

print('Saved center card crops!')

