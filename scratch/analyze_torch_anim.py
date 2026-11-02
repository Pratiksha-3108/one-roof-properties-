import cv2
import numpy as np

# Let's inspect full_f_0.jpg:
im0 = cv2.imread('scratch/detailed_anim/full_f_0.jpg')
im40 = cv2.imread('scratch/detailed_anim/full_f_40.jpg')
im80 = cv2.imread('scratch/detailed_anim/full_f_80.jpg')

# Let's find:
# 1. Is there an animation INSIDE the image card?
# In Torch Sensors, the center column has 3D renders or video clips:
# - One shows rain droplets hitting the sensor
# - One shows the sensor rotating
# - One shows the mounting bracket
# 2. What about the layout and motion of the cards?
# When scrolling:
# As you scroll, the cards glide smoothly into view.
# When the card enters view:
# Does the image have a zoom / reveal transition?
# Does the card have smooth parallax?

print('Images loaded successfully')

