import cv2
import pytesseract
import os
from pathlib import Path
from shutil import rmtree
pytesseract.pytesseract.tesseract_cmd = "/usr/local/Cellar/tesseract/4.1.1/bin/tesseract"



def scanner():
    obj = os.scandir("Import")
    for item in obj:
        return item.name


img = cv2.imread("Import/{}".format(scanner()))
text = pytesseract.image_to_string(img)
f = open("output.py", "w+")
f.write(text)
f.close()
rmtree("Import")
os.mkdir("Import")