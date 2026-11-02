import cv2
import numpy as np

cap = cv2.VideoCapture(r'C:/Users/Admin/.gemini/antigravity/brain/6ea31858-5b2b-44bd-ac91-9f917ce239ee/.user_uploaded/media_1793613964169_b8f99ab8.mp4')
# Let's inspect frames 50, 60, 70, 80, 90, 100, 110, 120
for f_idx in [40, 60, 80, 100, 120, 140, 160, 180, 200]:
    cap.set(cv2.CAP_PROP_POS_FRAMES, f_idx)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(f'scratch/torch_anim/f_{f_idx}.jpg', frame)
cap.release()
print('Sampled frames saved!')

