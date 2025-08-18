
"""
main_code.py

Automated workflow for taking a screenshot, allowing the user to crop a region,
performing OCR (Optical Character Recognition) on the cropped image, and copying the recognized text to the clipboard.

Modules Used:
- PIL.ImageGrab: For capturing screenshots.
- Screenshot.fontend.FontendApp: Tkinter frontend for cropping images.
- Screenshot.recangledrawer.RectangleDrawerBackend: Backend for rectangle drawing/cropping.
- pytesseract: For OCR (requires Tesseract-OCR installed).
- pyperclip: For copying text to clipboard.

Workflow:
1. Take a screenshot.
2. Let the user crop a region interactively.
3. Run OCR on the cropped image.
4. Copy the recognized text to the clipboard.

Usage:
    python main.py
"""

from PIL import ImageGrab
import time
from Screenshot.fontend import FontendApp
from Screenshot.recangledrawer import RectangleDrawerBackend
import pytesseract #type:ignore
import pyperclip
from plyer import notification




# Update this path based on your system
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

if not pytesseract.pytesseract.tesseract_cmd:
    print("plz download the pytesseract from this offical website for use it.")



def take_screenshot():
    """
    Capture a screenshot of the entire screen.
    Returns:
        PIL Image object of the screenshot, or None if an error occurs.
    """
    try:
        screenshot = ImageGrab.grab()
        print("Screenshot is taken")
        return screenshot
    except Exception as e:
        print(f"An error occurred: {e}")
        return None



def detailer(img):
    """
    Launch the cropping UI for the user to select a region of the image.
    Args:
        img: PIL Image object to crop.
    Returns:
        Path to the saved cropped image.
    """
    # print("Detailer function is starting")
    runner = FontendApp(RectangleDrawerBackend, img)
    runner.run()
    # print(runner.last_cropped_image)
    # print(runner.image_path)
    # print("Detailer function is ended")
    return runner.image_path


def reader(image_path):
    """
    Run OCR on the given image file.
    Args:
        image_path: Path to the image file.
    Returns:
        Recognized text as a string.
    """
    # print("Reader function is starting")
    start = time.time()
    text = pytesseract.image_to_string(image_path)
    print("The time taken by this function : ",(time.time()-start))
    # print("Reader function is ended")
    return text


def paster(text):
    """
    Copy the given text to the clipboard.
    Args:
        text: String to copy.
    """
    pyperclip.copy(text)
    print("The Text is copy to clipboard")
    notification.notify(
        title="Copy sucessful",
        message="Your text is copy sucessful , you can use by 'ctrl+v' shortcut"
    ) # pyright: ignore[reportOptionalCall]


def main():
    """
    Main workflow: screenshot -> crop -> OCR -> clipboard.
    """
    img = take_screenshot()
    image_path = detailer(img)
    text = reader(image_path)
    paster(text)



if __name__=="__main__":
    main()


    