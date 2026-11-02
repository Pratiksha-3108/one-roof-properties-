import cv2
import numpy as np

img = cv2.imread(r'C:/Users/Admin/.gemini/antigravity/brain/6ea31858-5b2b-44bd-ac91-9f917ce239ee/.user_uploaded/media_1793611889410_27880e79.png')
# In media_1793611889410_27880e79.png:
# Top center card: x from around 405 to 648
# Let's crop the top center card:
top_center = img[26:269, 405:648]
cv2.imwrite('scratch/slider_effect/top_center.jpg', top_center)
print('Top center card crop size:', top_center.shape)

# Middle center card:
mid_center = img[278:521, 405:648]
cv2.imwrite('scratch/slider_effect/mid_center.jpg', mid_center)
print('Mid center card crop size:', mid_center.shape)

# Bottom center card:
bot_center = img[531:774, 405:648]
cv2.imwrite('scratch/slider_effect/bot_center.jpg', bot_center)
print('Bot center card crop size:', bot_center.shape)

