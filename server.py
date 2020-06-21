import cv2
import pytesseract
import os
from pathlib import Path
pytesseract.pytesseract.tesseract_cmd = "/usr/local/Cellar/tesseract/4.1.1/bin/tesseract"

img = cv2.imread("Import/image.jpg")
text = pytesseract.image_to_string(img)
f = open("output.py", "w+")
f.write(text)
#os.system(programm)
f.close()
os.rmdir("Import")
os.mkdir("Import")