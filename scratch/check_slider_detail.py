import cv2
import glob
import numpy as np

frames = sorted(glob.glob('scratch/slider_effect/f_*.jpg'))
for i in range(len(frames)-1):
    f1 = cv2.imread(frames[i])
    f2 = cv2.imread(frames[i+1])
    diff = cv2.absdiff(f1, f2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    print(f'Frame {i} -> {i+1}: changed pixels = {np.count_nonzero(gray > 25)}')
