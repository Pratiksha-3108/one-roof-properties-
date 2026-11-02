import cv2

# Let's inspect the images in scratch/torch_anim/frame_00.jpg, frame_04.jpg, frame_08.jpg, frame_12.jpg
# Specifically let's look at the center column:
# In Torch Sensors, the center column has:
# 1) Top card: The sensor on a post/bracket
# 2) Middle card: The sensor in the rain (water droplets falling / raining)
# 3) Bottom card: The sensor being mounted to a tree trunk with screws
# What is animating?
# Is it a looping video/canvas? Or as the user scrolls, does the card have:
# - Smooth zoom/parallax inside the image?
# - Or does the image scale up smoothly?
# - Or does the background/foreground animate?

im4 = cv2.imread('scratch/torch_anim/frame_04.jpg')
im5 = cv2.imread('scratch/torch_anim/frame_05.jpg')
# Let's crop the rain card (middle card) in frame 4 and 5
h, w, _ = im4.shape
rain4 = im4[int(h*0.3):int(h*0.7), int(w*0.38):int(w*0.62)]
rain5 = im5[int(h*0.3):int(h*0.7), int(w*0.38):int(w*0.62)]
cv2.imwrite('scratch/torch_anim/rain4.jpg', rain4)
cv2.imwrite('scratch/torch_anim/rain5.jpg', rain5)
print('Rain crops saved!')

