import cv2
import numpy as np

im = cv2.imread('scratch/slider_effect/f_0000.jpg')
# Let's find horizontal boundaries of Right card:
# Column 1050 is white [255, 255, 255].
# Let's scan horizontally across row 200:
row200 = im[200, :, :]
# Find where it is pure white [255, 255, 255]
white_cols = np.where((row200[:, 0] > 250) & (row200[:, 1] > 250) & (row200[:, 2] > 250))[0]
print('Right card horizontal span at row 200:', white_cols[0], 'to', white_cols[-1], 'width =', white_cols[-1] - white_cols[0])

# Let's scan vertically across column 1050:
col1050 = im[:, 1050, :]
white_rows = np.where((col1050[:, 0] > 250) & (col1050[:, 1] > 250) & (col1050[:, 2] > 250))[0]
print('Right card vertical span at col 1050:', white_rows[0], 'to', white_rows[-1], 'height =', white_rows[-1] - white_rows[0])

# Now let's find the boundaries of the Center card (around col 680, row 400):
# Center card has background around [210, 215, 220] or similar.
# Let's look at the center card crop:
crop_center = cv2.imread('scratch/slider_effect/crop_center_box.jpg')
# Save edge detection:
edges = cv2.Canny(im, 50, 150)
cv2.imwrite('scratch/slider_effect/edges.jpg', edges)
print('Edges saved!')

