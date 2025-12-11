import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('C:/Users/Admin/buildclub_tech_subpanel_25/assets/vijay.png')

rgbimage = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

blurred = cv2.medianBlur(rgbimage, 5)

n_levels = 5

levels = 256 // n_levels

lut = np.zeros(256, dtype=np.uint8)
for i in range(256):
    lut[i] = np.round(i/levels) * levels

cartoonised = np.zeros_like(blurred)
for i in range(3):
    cartoonised[:,:,i] = cv2.LUT(blurred[:,:,i], lut)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(rgbimage)
plt.title('VIJAY')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cartoonised)
plt.title('ANIME VIJAY')
plt.axis('off')

plt.tight_layout()
plt.show()

cv2.imwrite('cartonizedimage.jpg', cv2.cvtColor(cartoonised, cv2.COLOR_RGB2BGR))