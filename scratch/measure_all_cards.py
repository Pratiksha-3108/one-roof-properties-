import cv2
import numpy as np

img = cv2.imread(r'C:/Users/Admin/.gemini/antigravity/brain/6ea31858-5b2b-44bd-ac91-9f917ce239ee/.user_uploaded/media_1793611889410_27880e79.png')
# The image is 1024 wide by 793 high.
# Let's find:
# 1. Left card: "Harsh weather survival" (white card)
# 2. Top-center card: Torch sensor (grey card)
# 3. Top-right card: "High accuracy" (white card)
# 4. Middle-center card: Torch sensor in rain (grey card)
# 5. Bottom-right card: "Easy installation" (white card)
# 6. Bottom-center card: Torch sensor on tree (grey card)

# Let's locate the white cards and grey cards:
# White card mask: RGB > 240
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
white_mask = (gray > 245).astype(np.uint8) * 255

# Grey card mask: 180 < gray < 235
grey_mask = ((gray >= 180) & (gray <= 235)).astype(np.uint8) * 255

# Let's find contours of white cards
contours, _ = cv2.findContours(white_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print('White card contours found:')
for c in contours:
    x, y, w, h = cv2.boundingRect(c)
    if w > 100 and h > 100:
        print(f'White card at ({x}, {y}): width={w}, height={h}, aspect={w/h:.2f}')

# Let's find contours of grey cards
contours_grey, _ = cv2.findContours(grey_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print('\nGrey card contours found:')
for c in contours_grey:
    x, y, w, h = cv2.boundingRect(c)
    if w > 100 and h > 100:
        print(f'Grey card at ({x}, {y}): width={w}, height={h}, aspect={w/h:.2f}')

