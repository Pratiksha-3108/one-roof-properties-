import cv2

# Let's crop the top center sensor image across sec 2, 3, 4
s2 = cv2.imread('scratch/torch_anim/sec_02.jpg')
s3 = cv2.imread('scratch/torch_anim/sec_03.jpg')
s4 = cv2.imread('scratch/torch_anim/sec_04.jpg')

# Let's see what is inside the top card
cv2.imwrite('scratch/torch_anim/s2_crop.jpg', s2[100:400, 350:650])
cv2.imwrite('scratch/torch_anim/s3_crop.jpg', s3[100:400, 350:650])
print('Saved s2_crop, s3_crop')

