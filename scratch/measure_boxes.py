import cv2
import numpy as np

im = cv2.imread(r'C:/Users/Admin/.gemini/antigravity/brain/6ea31858-5b2b-44bd-ac91-9f917ce239ee/.user_uploaded/media_1793617486484_c9b6a169.jpg')
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# Find width of left white card (around y=200):
row200 = im[200, :, :]
white_cols = np.where((row200[:, 0] > 245) & (row200[:, 1] > 245) & (row200[:, 2] > 245))[0]
print('Left box cols at y=200:', white_cols[0], 'to', white_cols[-1], 'width =', white_cols[-1] - white_cols[0])

# Right box is grey (starts around x=460):
# Find right box border:
# Sample along row 200 after x=450:
grey_cols = np.where((row200[450:, 0] < 225) & (row200[450:, 0] > 180))[0] + 450
print('Right box cols at y=200:', grey_cols[0], 'to', grey_cols[-1], 'width =', grey_cols[-1] - grey_cols[0])

