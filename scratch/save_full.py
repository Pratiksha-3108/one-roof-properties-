import cv2

# Let's inspect the entire viewport of frame 0, 40, 80, 120, 160
for f_idx in [0, 40, 80, 120, 160]:
    im = cv2.imread(f'scratch/detailed_anim/frame_{f_idx:04d}.jpg')
    # Save top half and bottom half
    h, w, _ = im.shape
    cv2.imwrite(f'scratch/detailed_anim/full_f_{f_idx}.jpg', cv2.resize(im, (800, 450)))

print('Full frame previews saved!')

