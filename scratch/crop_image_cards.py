import cv2
import numpy as np

# In frame_0000.jpg, frame_0040.jpg, frame_0080.jpg, frame_0120.jpg
# Let's find the exact bounds of the image card in each frame and save high-res crops!
for idx in [0, 24, 48, 72, 96, 120, 144, 168]:
    im = cv2.imread(f'scratch/detailed_anim/frame_{idx:04d}.jpg')
    if im is None: continue
    # Save a crop of the image card (which is in the middle column or where it appears)
    # The image card has grey rounded corners and a 3D product render
    cv2.imwrite(f'scratch/detailed_anim/image_card_{idx}.jpg', im[150:700, 350:800])

print('Saved image card crops!')

