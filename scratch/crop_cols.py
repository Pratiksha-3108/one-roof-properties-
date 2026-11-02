import cv2

edges = cv2.imread('scratch/slider_effect/edges.jpg', cv2.IMREAD_GRAYSCALE)
# In Torch Sensors:
# Column 1 (Left card): x = 207 to 533 (width = 326)
# Column 2 (Center card): x = 553 to 879 (width = 326)
# Column 3 (Right card): x = 899 to 1225 (width = 326)
# Let's verify these column coordinates:
im = cv2.imread('scratch/slider_effect/f_0000.jpg')
h, w, _ = im.shape
print(f'Frame width: {w}, height: {h}')

# Let's crop column 1, 2, 3:
col1 = im[100:650, 207:533]
col2 = im[100:650, 553:879]
col3 = im[100:650, 899:1225]

cv2.imwrite('scratch/slider_effect/col1.jpg', col1)
cv2.imwrite('scratch/slider_effect/col2.jpg', col2)
cv2.imwrite('scratch/slider_effect/col3.jpg', col3)
print('Columns cropped successfully!')

