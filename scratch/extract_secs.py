import cv2
import numpy as np

cap = cv2.VideoCapture(r'C:/Users/Admin/.gemini/antigravity/brain/6ea31858-5b2b-44bd-ac91-9f917ce239ee/.user_uploaded/media_1793613964169_b8f99ab8.mp4')

# Let's read frames at 1-second intervals: 1s, 2s, 3s, 4s, 5s...
fps = cap.get(cv2.CAP_PROP_FPS)
for sec in range(1, 13):
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(sec * fps))
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(f'scratch/torch_anim/sec_{sec:02d}.jpg', frame)

cap.release()
print('Extracted 1-second interval frames!')

