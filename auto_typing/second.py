from PIL import ImageGrab
import numpy as np
import cv2
import pytesseract #type:ignore
import time
import cv2


"""This is the simple a method to load the ty. where the tr file is store so don't wor"""
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'








def read_screen(bbox=None):
    try:
        if bbox:
            screenshot = ImageGrab.grab(bbox=bbox)
        else:
            screenshot = ImageGrab.grab()

        img = np.array(screenshot)

        # this is optical this only save the screenshot that is capture by the Imagegrab
        # cv2.imwrite("filename.jpg",img)

        return img 

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def extract_test(image_array):
    

    gray_image = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)


    _, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # # You can display these processed images to see what Tesseract is "seeing"
    # cv2.imshow("Grayscale Image", gray_image)
    # cv2.imshow("Binary Image", binary_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    try:
        print("This work is start , an the time is start")
        start = time.time()
        text = pytesseract.image_to_string(binary_image) # Use the preprocessed image here

    except pytesseract.TesseractNotFoundError:
        return "Error: Tesseract OCR engine not found. Please ensure it's installed and the path is correctly set."
    except Exception as e:
        return f"An error occurred: {e}"
    end = time.time()
    return end-start,text


def main(text):

    file_path = "result.txt"
    with open(file_path,'w') as file:
        file.write(text) # this write the text in the result.txt file 
        
        # this is also optional 
        print("text save in the file")


# text = extract_test(img)
# main(text)
print("Your time is start plz shift the window")
time.sleep(5)
img =  read_screen()
time_taken,text = extract_test(img)

print("For do this task time taken is :",time_taken)
# print(text)

print(main(text))