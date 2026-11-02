import cv2

col1 = cv2.imread('scratch/slider_effect/col1.jpg')
# Check vertical line in col1 (x = 163):
line1 = col1[:, 163, :]
for y in range(0, col1.shape[0], 25):
    print(f'Col1 Y={y}: BGR={line1[y]}')

