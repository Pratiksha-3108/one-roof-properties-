import cv2
import numpy as np

# In torch sensors video, what happens when user scrolls?
# Look at the center image:
# In f_60, f_80, f_100, f_120:
# Is the image card moving smoothly?
# Does the image inside have a smooth parallax or smooth scale / floating animation?
# Let's crop the center card in f_60, f_80, f_100 and compare:

im60 = cv2.imread('scratch/torch_anim/f_60.jpg')
im80 = cv2.imread('scratch/torch_anim/f_80.jpg')
im100 = cv2.imread('scratch/torch_anim/f_100.jpg')

# Let's find the cards on screen
print('Frames loaded successfully!')

