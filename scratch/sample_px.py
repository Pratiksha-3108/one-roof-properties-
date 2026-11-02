import cv2
import numpy as np

im = cv2.imread('scratch/slider_effect/f_0000.jpg')
# Let's inspect where the card borders are:
# In f_0000.jpg, the background outside the cards is #FAF8EE or light cream/grey #ebebeb?
# Let's sample pixels at various positions:
print('Background at (100, 100):', im[100, 100])
print('Background at (50, 400):', im[400, 50])
print('Card 1 center (400, 300):', im[400, 300]) # Left card
print('Center card center (400, 680):', im[400, 680]) # Center card
print('Right card center (200, 1050):', im[200, 1050]) # Right card

