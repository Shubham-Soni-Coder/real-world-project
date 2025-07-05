from PIL import ImageGrab
import time
from Screenshot.fontend import FontendApp
from Screenshot.recangledrawer import RectangleDrawerBackend
import pytesseract #type:ignore
import pyperclip


"""This is the simple a method to load the ty. where the tr file is store so don't wor"""
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'





def take_screenshot():
    try:
        screenshot = ImageGrab.grab()
        
        print("Screenshot is taken")
        return screenshot

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def detailer(img):
    print("Detailer function is starting")
    runner = FontendApp(RectangleDrawerBackend,img)
    runner.run()
    # if runner.last_cropped_image:
    print(runner.last_cropped_image)
    print(runner.image_path)
    print("Detailer function is ended")
    return runner.image_path

def reader(image_path):
    # Run OCR
    print("Reader function is starting")
    text = pytesseract.image_to_string(image_path)
    print("Reader function is ended")
    return text

def paster(text):
    # Run paperclip
    pyperclip.copy(text)
    print("The Text is copy to clipboard")

def main():
    img = take_screenshot()
    image_path = detailer(img)
    text = reader(image_path)
    paster(text)


if __name__=="__main__":
    save_path = "D:/coding/python/real-world-project/auto_typing/screenshots/image.jpg"
    start = time.time()
    main()
    print("The time taken by this function : ",(time.time()-start))