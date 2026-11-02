import cv2
import glob
import os

frames = sorted(glob.glob('scratch/detailed_anim/frame_*.jpg'))
print(f'Total frames: {len(frames)}')

# Let's see what happens to the image cards across the entire video.
# In Torch Sensors:
# 1. Look at the center image card!
# Does the image card stay sticky / fixed in the center while cards scroll?
# OR does the 3D model inside the card ROTATE as you scroll?
# OR does the image card expand / change?
# Let's crop the center of every 3rd frame and save to scratch/detailed_anim/crops/

os.makedirs('scratch/detailed_anim/crops', exist_ok=True)
for i, f_path in enumerate(frames[::2]):
    im = cv2.imread(f_path)
    h, w, _ = im.shape
    # Center crop
    center = im[int(h*0.2):int(h*0.8), int(w*0.35):int(w*0.65)]
    cv2.imwrite(f'scratch/detailed_anim/crops/crop_{i:02d}.jpg', center)

print('Saved crops to scratch/detailed_anim/crops')

