import cv2
import numpy as np

im = cv2.imread('scratch/slider_effect/f_0000.jpg')
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# White card mask (white is > 250)
white_thresh = (gray > 250).astype(np.uint8) * 255
cnts, _ = cv2.findContours(white_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print('=== WHITE CARDS IN VIDEO FRAME 0 ===')
for c in cnts:
    x, y, w, h = cv2.boundingRect(c)
    if w > 150 and h > 150:
        print(f'White card: x={x}, y={y}, width={w}, height={h}, aspect={w/h:.2f}')

# Grey card in the center:
# In f_0000.jpg, the center card has sensor in the rain.
# Its background is around (210, 215, 218)
# Let's find its bounding box:
# Look between x=500 and x=850
crop_center = im[100:650, 520:860]
cv2.imwrite('scratch/slider_effect/crop_center_box.jpg', crop_center)
print('Center crop saved!')

