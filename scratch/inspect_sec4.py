import cv2

# Let's inspect the cards in sec_04.jpg:
im = cv2.imread('scratch/torch_anim/sec_04.jpg')
# Where are the cards?
# The screen has a white top bar (or floating navbar)
# Card 1: Top Right "High accuracy"
# Card 2: Center "Torch sensor 3D"
# Card 3: Left "Harsh weather survival"
# Card 4: Center "Torch sensor in rain"
# Card 5: Right "Easy installation"
# Card 6: Center "Torch sensor on tree"

print('Image size:', im.shape)

