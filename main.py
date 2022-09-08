from PIL import Image
from pytesseract import pytesseract
import os


#path to tesseract
tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image_path = 'images/'

#point tesseract.cmd to tesseract.exe

pytesseract.tesseract_cmd = tesseract_path

for root, dirs, file_names in os.walk(image_path):
    for file_name in file_names:
        #open image in PIL by concatenating the path w/ the file name
        img = Image.open(image_path + file_name)

        #extract text from image
        text = pytesseract.image_to_string(img)

        with open ('mouret.txt', 'a') as f:
            f.writelines(text)

