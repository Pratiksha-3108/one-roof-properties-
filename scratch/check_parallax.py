import cv2
import numpy as np

s2 = cv2.imread('scratch/torch_anim/sec_02.jpg')
s4 = cv2.imread('scratch/torch_anim/sec_04.jpg')

# Let's track:
# Left column patch (around x=200)
# Center column patch (around x=500)
# Right column patch (around x=800)

for name, x in [('Left Column', 200), ('Center Column', 500), ('Right Column', 800)]:
    patch = s2[300:380, x:x+80]
    res = cv2.matchTemplate(s4, patch, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    dy = max_loc[1] - 300
    print(f'{name}: dy={dy}, score={max_val:.2f}')

