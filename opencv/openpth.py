import cv2
from PIL import Image
import pytesseract
import numpy as np
# import main
import easyocr

crop_img = cv2.imread('cropped.jpg', cv2.IMREAD_COLOR)
if crop_img.shape[1] / crop_img.shape[0] > 3:
    crop_img = cv2.resize(crop_img, (600, 200))
else:
    crop_img = cv2.resize(crop_img, (400, 200))
crop_gray = cv2.cvtColor(crop_img.copy(), cv2.COLOR_BGR2GRAY)
kernel = np.ones((1, 1), np.uint8)
crop_gray = cv2.dilate(crop_gray, kernel, iterations=1)
crop_gray = cv2.erode(crop_gray, kernel, iterations=1)
crop_gray = cv2.bilateralFilter(crop_gray, 13, 15, 15)
crop_blur = cv2.GaussianBlur(crop_gray, (5, 5), 1)
crop_edged = cv2.threshold(crop_gray, 0, 80, cv2.THRESH_OTSU)[1]
cv2.imshow("cropped", crop_edged)

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
text = pytesseract.image_to_string(crop_edged, config='--oem 3 --psm 6')  # converts image characters to string

reader = easyocr.Reader(['en'])
result = reader.readtext('cropped.jpg')
print(result)

ans = ''
for i in text:
    if 'A'<=i <='Z' or '0'<=i<='9' or i=='\n' or i=='-':
        ans+=i
print(ans)
cv2.waitKey(0) == ord('q')
