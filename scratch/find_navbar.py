import cv2
import numpy as np

# In frame_0000 to frame_0120:
# Let's inspect what happens to the image cards:
# 1. As the page scrolls down:
# Look at the top center card (sensor render):
# Does the image card stay sticky / fixed in the center while cards scroll?
# Look at the white navbar: in frame 0, where is the navbar?
# In frame 40, where is the navbar?
# Is the navbar fixed or scrolling?
# What about the image cards?

for idx in [0, 16, 32, 48, 64, 80, 96, 112]:
    im = cv2.imread(f'scratch/detailed_anim/frame_{idx:04d}.jpg')
    # Let's find the position of the white navbar in the frame
    # In Torch Sensors, there is a horizontal white navbar with "TORCH", "Product", "Pricing", etc.
    # Let's find its Y coordinate!
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # The navbar is a bright white horizontal band
    row_means = np.mean(gray, axis=1)
    # Find rows that are very white (>250)
    white_rows = np.where(row_means > 245)[0]
    print(f'Frame {idx:04d}: white navbar rows around:', white_rows[len(white_rows)//2] if len(white_rows)>0 else 'None')

