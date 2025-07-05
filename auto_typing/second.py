import pytesseract #type:ignore
from PIL import Image
import time
from Screenshot.recangledrawer import RectangleDrawerBackend
from Screenshot.fontend import FontendApp

"""This is the simple a method to load the ty. where the tr file is store so don't wor"""
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = 'cropped_image.png'

# Load an image
image = Image.open(img)

# Backend variable 
runner = FontendApp(RectangleDrawerBackend,image)
runner.run()
image = runner.crop_image_saver(img)



# Run OCR
start = time.time()
text = pytesseract.image_to_string(image)
print(text)
print(f"The time taken by this function is {time.time()- start}")


