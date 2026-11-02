import cv2
import glob
import numpy as np

crops = sorted(glob.glob('scratch/detailed_anim/crops/crop_*.jpg'))

# Let's inspect what changes between crop_00, crop_01, crop_02, etc.
# In Torch Sensors:
# In frame 0: What is visible?
# In frame 5: What is visible?
# In frame 10: What is visible?
# Let's check text or object in each crop
for idx, c_path in enumerate(crops):
    c = cv2.imread(c_path)
    # Check if there is a white box, gray box, or what
    # Let's compute average intensity and color
    mean_val = np.mean(c)
    print(f'Crop {idx:02d} ({c_path}): mean intensity = {mean_val:.1f}, shape={c.shape}')

