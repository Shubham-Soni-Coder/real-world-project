from PIL import ImageGrab
import time
from Screenshot.fontend import FontendApp
from Screenshot.recangledrawer import RectangleDrawerBackend


def take_screenshot():
    try:
        
        screenshot = ImageGrab.grab()
        
        print("Screenshot is taken")
        return screenshot

    except Exception as e:
        print(f"An error occurred: {e}")
        return None



def open_image(img,save_path=None):
    runner = FontendApp(RectangleDrawerBackend,img)
    runner.run()
    if save_path:
        runner.crop_image_saver(save_path)



if __name__=="__main__":
    img = take_screenshot()
    save_path = "D:/coding/python/real-world-project/auto_typing/screenshots/image.jpg"
    open_image(img)