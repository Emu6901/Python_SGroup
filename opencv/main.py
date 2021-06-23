import os

import cv2
import imutils as imutils
import numpy as np
import pytesseract
from PIL import ImageFilter, Image

img = cv2.imread('img.jpg', cv2.IMREAD_COLOR)
# img = cv2.imread('Cars14.png', cv2.IMREAD_COLOR)
# img = cv2.imread('Cars0.png', cv2.IMREAD_COLOR)
# img = cv2.imread('img1.jpg', cv2.IMREAD_COLOR)
img = cv2.resize(img, (600, 300))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 13, 15, 15)
blur = cv2.GaussianBlur(gray, (5, 5), 1)
edged = cv2.Canny(blur, 10, 50)
cv2.imshow("edged", edged)

contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv2.contourArea, reverse=True)
screenCnt = None

for cnt in contours:
    epsilon = 0.05 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    print(len(approx), cv2.contourArea(cnt))
    if len(approx) == 4 and cv2.contourArea(cnt) > 200:
        screenCnt = approx
        break

if screenCnt is not None:
    print(screenCnt)
    cv2.drawContours(img, [screenCnt], -1, (0, 0, 255), 1)
    cv2.imshow('img', img)
    x, y, w, h = cv2.boundingRect(cnt)

    crop_img = img.copy()
    crop_img = crop_img[y:y + h, x:x + w]
    crop_img = cv2.resize(crop_img, (300, 100))

    os.remove('cropped.jpg')
    cv2.imwrite('cropped.jpg', crop_img)
    cv2.imshow("cropped", crop_img)

    crop_gray = cv2.cvtColor(crop_img.copy(), cv2.COLOR_BGR2GRAY)
    crop_gray = cv2.bilateralFilter(crop_gray, 13, 15, 15)
    crop_blur = cv2.GaussianBlur(crop_gray, (5, 5), 1)
    crop_edged = cv2.threshold(crop_gray, 0, 80, cv2.THRESH_OTSU)[1]

    crop_contours = cv2.findContours(crop_edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    crop_contours = imutils.grab_contours(crop_contours)
    crop_contours = sorted_ctrs = sorted(crop_contours,
                                         key=lambda ctr: cv2.boundingRect(ctr)[0] + cv2.boundingRect(ctr)[1] * 10)

    image = cv2.imread('cropped.jpg')
    ROI_number = 0
    for cnt in crop_contours:
        area = cv2.contourArea(cnt)
        print(area)
        if 200 < area < 2000:
            x, y, w, h = cv2.boundingRect(cnt)
            ROI = 255 - crop_edged[y:y + h, x:x + w]
            cv2.drawContours(image, [cnt], -1, (0, 255, 255), -1)
            cv2.imwrite(r'ROI\ROI\ROI_{}.jpg'.format(ROI_number), ROI)
            ROI_number += 1
            cv2.imshow("image", image)
            cv2.waitKey(200)

    cv2.imshow("image", image)

cv2.waitKey(0) == ord('q')
