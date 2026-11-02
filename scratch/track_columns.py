import cv2
import numpy as np

# In Torch Sensors, let's track:
# 1. Left card: "Harsh weather survival" (white card)
# 2. Center card: "Torch sensor in rain" (image card)
# 3. Right card: "High accuracy" (white card) or "Easy installation" (white card)

# Let's find their Y position in frame 0, 16, 32, 48, 64, 80:
# Left card has text "Harsh weather survival" (orange/red text)
# Center card has gray background with dark sensor
# Right card has "High accuracy" or "Easy installation"

# Let's crop the 3 columns in frame 0 and frame 48:
f0 = cv2.imread('scratch/detailed_anim/frame_0000.jpg')
f48 = cv2.imread('scratch/detailed_anim/frame_0048.jpg')

# Find template match for the image card in center of f0 in f48:
center_card_f0 = f0[350:550, 480:680]
res_center = cv2.matchTemplate(f48, center_card_f0, cv2.TM_CCOEFF_NORMED)
_, _, _, max_loc_center = cv2.minMaxLoc(res_center)
dy_center = max_loc_center[1] - 350

# Find template match for left card of f0 in f48:
left_card_f0 = f0[350:550, 160:360]
res_left = cv2.matchTemplate(f48, left_card_f0, cv2.TM_CCOEFF_NORMED)
_, _, _, max_loc_left = cv2.minMaxLoc(res_left)
dy_left = max_loc_left[1] - 350

print(f'From Frame 0 to Frame 48:')
print(f'Center Image Card moved dy = {dy_center}')
print(f'Left Content Card moved dy = {dy_left}')

