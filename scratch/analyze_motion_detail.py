import cv2
import numpy as np

# In frame 32:
# What is in the center column?
# The image card with Torch sensor in rain.
# In frame 64:
# The user scrolled down.
# Where is the image card with Torch sensor in rain?
# In frame 64, it moved UP!
# And what card came in from below?
# The image card with Torch sensor attached to a tree!
# And what about the content cards?
# "Harsh weather survival" was on the left.
# "Easy installation" came in on the right!

# NOW: Look at the image card:
# What animation is on the image card?
# 1. Look at the corners and scale:
# Does the image card scale or expand?
# Does the image inside have a parallax zoom?
# Look at the user's prompt:
# "see animation for image card clearly"

im32 = cv2.imread('scratch/detailed_anim/frame_0032.jpg')
im64 = cv2.imread('scratch/detailed_anim/frame_0064.jpg')

# Let's inspect the tree card in frame 64 vs 96:
print('Inspected!')

