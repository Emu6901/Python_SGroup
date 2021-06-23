import os

import cv2
import imutils as imutils
import numpy as np
import pytesseract
from PIL import ImageFilter, Image
from PIL.ImageEnhance import Color

# crop_img = cv2.imread('img.jpg', cv2.IMREAD_COLOR)
# crop_img = cv2.imread('Cars14.png', cv2.IMREAD_COLOR)
# crop_img = cv2.imread('Cars0.png', cv2.IMREAD_COLOR)
crop_img = cv2.imread('img1.jpg', cv2.IMREAD_COLOR)
crop_img = cv2.resize(crop_img, (620, 400))
crop_gray = cv2.cvtColor(crop_img.copy(), cv2.COLOR_BGR2GRAY)
crop_gray = cv2.bilateralFilter(crop_gray, 13, 15, 15)
crop_edged = edged = cv2.Canny(crop_gray, 30, 200)
cv2.imshow("crop_edged", crop_edged)
crop_contours = cv2.findContours(crop_edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
crop_contours = imutils.grab_contours(crop_contours)
crop_contours = sorted(crop_contours, key=cv2.contourArea, reverse=True)[:10]

image = crop_img.copy()
image = cv2.resize(image, (600, 400))
for cnt in crop_contours:
    area = cv2.contourArea(cnt)
    epsilon = 0.05 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    print(area)
    if len(approx) == 4 and cv2.contourArea(cnt)>200:
        x, y, w, h = cv2.boundingRect(cnt)
        ROI = 255 - crop_edged[y:y + h, x:x + w]
        cv2.drawContours(image, [cnt], -1, (0, 255, 0), -1)
        # cv2.imwrite('ROI_{}.png'.format(ROI_number), ROI)
        cv2.imshow("image", image)
        cv2.waitKey(1000)== ord('q')

cv2.waitKey(0) == ord('q')