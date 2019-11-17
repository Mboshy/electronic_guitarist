import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('samples\moonlight.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
# template = cv2.imread('samples/notes/quarter/1.png', 0)
template = cv2.imread('samples/notes/half/1.png', 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)

plt.imshow(img_rgb)
plt.show()


imga = cv2.imread('D:\Studia\inz\obrazki/raspi4.jpg')
img_gray = cv2.cvtColor(imga, cv2.COLOR_BGR2GRAY)
thresholded = cv2.Canny(img_gray, 50, 200)
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(img_gray, cmap='gray')
ax1.set_title('Skala szarości')
ax1.axis('off')
ax2.imshow(thresholded, cmap='gray')
ax2.set_title('Progowanie')
ax2.axis('off')
plt.show()
