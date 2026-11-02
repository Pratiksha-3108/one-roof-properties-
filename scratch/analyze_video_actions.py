import cv2
import numpy as np

# Let's inspect where changes occur in the video
# In media_1793615017444_de31b7fa.mp4:
# Is the user scrolling the Torch website?
# Let's see what happens to the image cards in the Torch website:
# 1. Look at the cards:
# Are the cards arranged in columns that move with parallax?
# In frame 0: What cards are on the screen?
# In frame 80: What cards are on the screen?
# In frame 160: What cards are on the screen?

for f_idx in [0, 40, 80, 120, 160, 200, 240]:
    im = cv2.imread(f'scratch/detailed_anim/preview_{f_idx}.jpg')
    # Let's see how much gray vs white background there is
    # Torch site background is #e5e5e5 or light gray
    print(f'Frame {f_idx}: shape={im.shape}')

