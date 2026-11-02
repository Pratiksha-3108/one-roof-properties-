import cv2
import numpy as np

# In torchsensors.webflow.io, what is happening to the image cards?
# Let's crop the center column (where the product image is) across frames 3 to 10
# to see if the image inside rotates, scales, moves with parallax, or changes!

for i in [3, 4, 5, 6, 7, 8, 9, 10]:
    im = cv2.imread(f'scratch/torch_anim/frame_{i:02d}.jpg')
    h, w, _ = im.shape
    # Center column is between w*0.35 and w*0.65
    center_crop = im[int(h*0.2):int(h*0.8), int(w*0.35):int(w*0.65)]
    cv2.imwrite(f'scratch/torch_anim/crop_center_{i:02d}.jpg', center_crop)

print('Cropped center column across frames')

