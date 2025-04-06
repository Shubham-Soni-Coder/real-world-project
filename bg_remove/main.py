from rembg import new_session,remove
import PIL 
import time
import sys
session = new_session()
def remove_background(input_image_path,output_image_path):
    
    # Open the input image
    with open(input_image_path, 'rb') as input_file:
        input_image = input_file.read()   
    # Remove background
    output_image = remove(input_image,session=session)
    
    # Save the output image
    with open(output_image_path, 'wb') as output_file:
        output_file.write(output_image)

if __name__ == "__main__":
    # Input and output image file paths
    try:
        input_path = PIL.Image.open('test.jpg')
    except FileNotFoundError:
        print(f"Error: Ths specified file was not found.")
        sys.exit(1)
    except PIL.UnidentifiedImageError:
        print("Error: The specified file is not a valid image.")
        sys.exit(1)
                    
    output_path = 'test.webp'
    # Remove background
    start = time.time()
    remove_background(input_path,output_path)
    end = time.time()
    print(f'Time taken to remove background: {end - start} seconds')
    print(f'Background removed and saved to {output_path}')