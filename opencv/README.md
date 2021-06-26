# License Plate Detector

- Detects license plate and recognizes its characters

## Method

- Detect License Plate from image
- Detect characters in License Plate
- Crop License Plate and save
- Prediction of characters in License Plate using pytesseract

## Install pytesseract

1. Install tesseract using windows installer available at: https://github.com/UB-Mannheim/tesseract/wiki

2. Note the tesseract path from the installation. Default installation path at the time of this edit was: C:
   \Users\USER\AppData\Local\Tesseract-OCR. It may change so please check the installation path.

3. pip install pytesseract

4. Set the tesseract path in the script before calling image_to_string:

   pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'

## Setup

- Clone the repository :
  $ git clone https://github.com/Emu6901/Python_Sgroup.git
- pip install -r requirements.txt
- python main.py

## Screenshots

1. Original image

- ![img_2.png](img_2.png)

2. Detect License Plate from image

- ![img_3.png](img_3.png)

3. Detect characters in License Plate

- ![img_5.png](img_5.png)

4. Crop License Plate

- ![img_4.png](img_4.png)

5. Prediction of characters in License Plate using pytesseract

- ![img_6.png](img_6.png)