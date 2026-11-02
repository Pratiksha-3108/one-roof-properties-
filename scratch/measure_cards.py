import cv2
import numpy as np

img = cv2.imread(r'C:/Users/Admin/.gemini/antigravity/brain/6ea31858-5b2b-44bd-ac91-9f917ce239ee/.user_uploaded/media_1793612334171_2275bbda.jpg')
h, w, _ = img.shape

# Let's inspect the gap between the left card and right card
# Left card is white, right card has image
# Background between them is around x=420 to 460
gap_strip = img[200:300, 400:460]
print("Gap strip mean color:", gap_strip.mean(axis=(0,1)))

# Let's find the exact x boundary of left card (where white stops)
# and right card (where image starts)
mid_y = 250
row = img[mid_y, :, :]
# Find where white card is:
white_xs = np.where(row.mean(axis=1) > 245)[0]
if len(white_xs) > 0:
    print(f"White card x bounds: {white_xs.min()} to {white_xs.max()} (width={white_xs.max() - white_xs.min()})")

# Where does right card start?
# Right card pixels are not background
bg = img[mid_y, white_xs.max() + 10, :]
print(f"Background at gap: {bg}")

# Height of the cards:
# Check column in white card around x=200
col = img[:, 200, :]
white_ys = np.where(col.mean(axis=1) > 245)[0]
if len(white_ys) > 0:
    print(f"White card y bounds: {white_ys.min()} to {white_ys.max()} (height={white_ys.max() - white_ys.min()})")

# Let's print aspect ratio
width = white_xs.max() - white_xs.min()
height = white_ys.max() - white_ys.min()
print(f"Aspect ratio (width / height): {width / height:.2f}")

