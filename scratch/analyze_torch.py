import cv2
import glob

# Let's see what is happening to the image cards in the frames
# In Torch Sensors, is there parallax, 3D tilt, or scroll-tied movement?
# Let's inspect the positions of cards or the contents of the image card across frames.

for idx in [2, 4, 6, 8, 10, 12]:
    img = cv2.imread(f'scratch/torch_anim/frame_{idx:02d}.jpg')
    # Save a thumbnail
    thumb = cv2.resize(img, (480, 270))
    cv2.imwrite(f'scratch/torch_anim/thumb_{idx:02d}.jpg', thumb)

print('Thumbnails saved!')

