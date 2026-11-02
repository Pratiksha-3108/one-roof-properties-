import cv2
import numpy as np

frames = [cv2.imread(f'scratch/torch_anim/frame_{i:02d}.jpg') for i in range(16)]
small_frames = [cv2.resize(f, (320, 180)) for f in frames]

row1 = np.hstack(small_frames[0:4])
row2 = np.hstack(small_frames[4:8])
row3 = np.hstack(small_frames[8:12])
row4 = np.hstack(small_frames[12:16])
grid = np.vstack([row1, row2, row3, row4])

cv2.imwrite('scratch/torch_anim/full_grid.jpg', grid)
print('Grid saved: scratch/torch_anim/full_grid.jpg')
