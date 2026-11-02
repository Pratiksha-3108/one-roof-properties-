import cv2
import numpy as np

# In torch sensors video, let's track the image cards:
# 1. As the page is scrolled, how do the cards move?
# Does the image have an internal smooth zoom / scale or parallax on scroll?
# Does the card have a floating hover effect?
# Does the image slightly tilt or move with cursor?
# Or does the image scale up smoothly when the card enters viewport / on hover?

# Let's inspect frame 3, 4, 5:
# Let's find the exact bounding box of the top center image card in frame 3 vs frame 4
f3 = cv2.imread('scratch/torch_anim/frame_03.jpg')
f4 = cv2.imread('scratch/torch_anim/frame_04.jpg')
f5 = cv2.imread('scratch/torch_anim/frame_05.jpg')

# Let's compute difference between f3 and f4
diff = cv2.absdiff(f3, f4)
cv2.imwrite('scratch/torch_anim/diff_3_4.jpg', diff)
print('diff_3_4 saved')

