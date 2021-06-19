import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('image.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.subplot(1, 3, 1)
plt.imshow(img)


def to_gray(img):
    avg = np.array(img[:, :, 0]) * .299 + np.array(img[:, :, 1]) * .587 + np.array(img[:, :, 2]) * .114
    ans = img.copy()
    for i in range(3):
        ans[:, :, i] = avg
    return ans


gray = to_gray(img)
plt.subplot(1, 3, 2)
plt.imshow(gray)

threshold = 80


def to_black_white(img):
    avg = np.array(img[:, :, 0] > threshold) * 255 / 3 + np.array(img[:, :, 1] > threshold) * 255 / 3 + np.array(
        img[:, :, 2] > threshold) * 255 / 3
    avg = np.where(avg < 200, 0, 255)
    print(avg)
    ans = img.copy()
    for i in range(3):
        ans[:, :, i] = avg
    return ans


black_white = to_black_white(img)
plt.subplot(1, 3, 3)
plt.imshow(black_white)

plt.show()
