import cv2
import numpy as np

# Let's inspect image_card_0, image_card_48, image_card_96
for idx in [0, 24, 48, 72, 96, 120, 144]:
    im = cv2.imread(f'scratch/detailed_anim/image_card_{idx}.jpg')
    print(f'image_card_{idx}: mean={np.mean(im):.2f}, std={np.std(im):.2f}')

