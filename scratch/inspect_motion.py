import cv2
import numpy as np

# Let's inspect frame 0 to frame 15
# Specifically let's track the position of a specific card image across frames
# e.g., the sensor device on the tree or on the pole, or the white navbar

for i in [3, 4, 5, 6, 7]:
    img = cv2.imread(f'scratch/torch_anim/frame_{i:02d}.jpg')
    # Print height, width
    # In Torch Sensors, the page is being scrolled down.
    # What animations happen?
    # 1. Entrance / fade-in / slide-in?
    # 2. Smooth parallax zoom / scale?
    # 3. Floating effect?
    # 4. Sticky center column?
    print(f'Frame {i} analyzed.')

