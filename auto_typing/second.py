import pytesseract #type:ignore
from PIL import Image
import time
from Screenshot.recangledrawer import RectangleDrawerBackend
from Screenshot.fontend import FontendApp
import pyperclip

"""This is the simple a method to load the ty. where the tr file is store so don't wor"""
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


image_path = "D:/coding/python/real-world-project/auto_typing/screenshots/s1.jpg"

# Load an image
image = Image.open(image_path)

# Backend variable 
runner = FontendApp(RectangleDrawerBackend,image)
runner.run()
print("This is the path where the immage is store ",runner.image_path)


# Run OCR
start = time.time()
text = pytesseract.image_to_string(runner.image_path)
print(text)


# Run paperclip
pyperclip.copy(text)
print("The Text is copy to clipboard")


print(f"The time taken by this function is {time.time()- start}")