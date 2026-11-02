import cv2
import glob

f0 = cv2.imread('scratch/detailed_anim/frame_0000.jpg')
center_card_f0 = f0[350:550, 480:680]
left_card_f0 = f0[350:550, 160:360]

for idx in [0, 16, 32, 48, 64, 80, 96, 112, 128, 144, 160]:
    im = cv2.imread(f'scratch/detailed_anim/frame_{idx:04d}.jpg')
    res_center = cv2.matchTemplate(im, center_card_f0, cv2.TM_CCOEFF_NORMED)
    _, max_val_center, _, max_loc_center = cv2.minMaxLoc(res_center)
    
    res_left = cv2.matchTemplate(im, left_card_f0, cv2.TM_CCOEFF_NORMED)
    _, max_val_left, _, max_loc_left = cv2.minMaxLoc(res_left)
    
    print(f'Frame {idx:04d}: Center dy={max_loc_center[1]-350} (score={max_val_center:.2f}) | Left dy={max_loc_left[1]-350} (score={max_val_left:.2f})')

