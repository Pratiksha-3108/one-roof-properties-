import cv2
import numpy as np

# In torch sensors video:
# What is moving when the user scrolls?
# Look at the cards:
# 1. As the page scrolls, does the center column of image cards scroll with a parallax speed,
#    OR does the center card stay sticky while the content cards scroll past?
#    OR do the image cards have a smooth zoom/scale on scroll?
#    OR do the cards have a floating/smooth parallax effect?

for sec in range(1, 12):
    s1 = cv2.imread(f'scratch/torch_anim/sec_{sec:02d}.jpg')
    s2 = cv2.imread(f'scratch/torch_anim/sec_{sec+1:02d}.jpg')
    # Let's see the scroll delta:
    # Match template of a patch from s1 in s2
    patch = s1[300:400, 450:550]
    res = cv2.matchTemplate(s2, patch, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    dy = max_loc[1] - 300
    dx = max_loc[0] - 450
    print(f'Sec {sec} -> {sec+1}: center patch moved dy={dy}, dx={dx}, score={max_val:.2f}')

