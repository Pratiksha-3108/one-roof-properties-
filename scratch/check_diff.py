import cv2
import numpy as np

im0 = cv2.imread('scratch/detailed_anim/image_card_0.jpg')
im24 = cv2.imread('scratch/detailed_anim/image_card_24.jpg')
diff = cv2.absdiff(im0, im24)
print('Diff sum between 0 and 24:', np.sum(diff))
cv2.imwrite('scratch/detailed_anim/diff_0_24.jpg', diff)

