import cv2
import numpy as np

# In media_1793616090077_8d043173.mp4:
# Let's inspect frame 0 to frame 269:
# What happens in the center card?
# In frame 0: Top card is sensor 3D.
# In frame 80: Center card is sensor in rain.
# In frame 160: Center card is sensor on tree.
# In frame 240: What card is there?
# Each card slides up smoothly into place as you scroll!
# It is literally a vertical sliding showcase where the center column has taller cards sliding into place!

cap = cv2.VideoCapture(r'C:/Users/Admin/.gemini/antigravity/brain/6ea31858-5b2b-44bd-ac91-9f917ce239ee/.user_uploaded/media_1793616090077_8d043173.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)

# Let's extract frame at 2s, 4s, 6s, 8s, 10s:
for sec in [2, 4, 6, 8, 10]:
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(sec * fps))
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(f'scratch/slider_effect/time_{sec}s.jpg', cv2.resize(frame, (640, 360)))

cap.release()
print('Time frames saved!')

