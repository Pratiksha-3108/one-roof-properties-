import cv2

# Let's save smaller previews of frames 0, 48, 96, 144, 192, 240
for idx in [0, 40, 80, 120, 160, 200, 240]:
    f_path = f'scratch/detailed_anim/frame_{idx:04d}.jpg'
    im = cv2.imread(f_path)
    if im is not None:
        small = cv2.resize(im, (640, 360))
        cv2.imwrite(f'scratch/detailed_anim/preview_{idx}.jpg', small)

print('Saved previews!')

