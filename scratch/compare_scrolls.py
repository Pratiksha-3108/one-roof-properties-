import cv2
import numpy as np

im32 = cv2.imread('scratch/detailed_anim/frame_0032.jpg')
im64 = cv2.imread('scratch/detailed_anim/frame_0064.jpg')

# Let's save both full frames side-by-side:
h, w, _ = im32.shape
combined = np.hstack([cv2.resize(im32, (640, 360)), cv2.resize(im64, (640, 360))])
cv2.imwrite('scratch/detailed_anim/scroll_compare_32_64.jpg', combined)

# Let's also do between 64 and 96
im96 = cv2.imread('scratch/detailed_anim/frame_0096.jpg')
combined2 = np.hstack([cv2.resize(im64, (640, 360)), cv2.resize(im96, (640, 360))])
cv2.imwrite('scratch/detailed_anim/scroll_compare_64_96.jpg', combined2)

print('Comparisons saved!')

