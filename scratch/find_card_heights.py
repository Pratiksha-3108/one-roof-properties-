import cv2
import numpy as np

# In col1.jpg, col2.jpg, col3.jpg:
col1 = cv2.imread('scratch/slider_effect/col1.jpg')
col2 = cv2.imread('scratch/slider_effect/col2.jpg')
col3 = cv2.imread('scratch/slider_effect/col3.jpg')

# Let's see the height of the card in col1 vs col2 vs col3:
# In col2 (center column):
# Top edge and bottom edge of the card:
# Find rows in col2 where the rounded card starts and ends:
# Look along the middle of col2 (x = 163):
line = col2[:, 163, :]
# In Torch Sensors, the card is distinct from the page background.
# Page background is light gray/cream.
# Let's print out pixel values along the vertical line of col2:
for y in range(0, col2.shape[0], 25):
    print(f'Y={y}: BGR={line[y]}')

