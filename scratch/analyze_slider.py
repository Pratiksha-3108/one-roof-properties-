import cv2
import glob
import numpy as np

frames = sorted(glob.glob('scratch/slider_effect/f_*.jpg'))
print(f'Total frames extracted: {len(frames)}')

f_indices = [0, 4, 8, 12, 16, 19]
selected = [cv2.resize(cv2.imread(frames[i]), (480, 270)) for i in f_indices]

row1 = np.hstack(selected[:3])
row2 = np.hstack(selected[3:])
sheet = np.vstack([row1, row2])
cv2.imwrite('scratch/slider_effect/sheet.jpg', sheet)
print('Contact sheet saved: scratch/slider_effect/sheet.jpg')
