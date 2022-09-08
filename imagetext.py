from PIL import Image
from pytesseract import pytesseract
import os

class image_text():
    def __init__(self):
        # path to tesseract
        self.tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        # path to image folder
        self.image_path = 'images/'

        # point tesseract.cmd to tesseract.exe

        pytesseract.tesseract_cmd = self.tesseract_path

    def get_text(self):
        for root, dirs, file_names in os.walk(self.image_path):
            for file_name in file_names:
                # open image in PIL by concatenating the path w/ the file name
                img = Image.open(self.image_path + file_name)

                # extract text from image
                text = pytesseract.image_to_string(img)

                # creates a file and appends text from each image to the text file
                with open('sample.txt', 'a') as f:
                    f.writelines(text)
