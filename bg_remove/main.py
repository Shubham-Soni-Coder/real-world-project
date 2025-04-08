from rembg import remove, new_session

session = new_session()

def remove_background(input_image_path, output_image_path):
    try:
        with open(input_image_path, 'rb') as input_file:
            input_image = input_file.read()
    except FileNotFoundError:
        print("❌ Error: File not found.")
        return
    except Exception as e:
        print(f"❌ Error while reading file: {e}")
        return

    print("Working...")

    try:
        output_image = remove(input_image, session=session)
    except Exception as e:
        print(f"❌ Error during background removal: {e}")
        return

    try:
        with open(output_image_path, 'wb') as output_file:
            output_file.write(output_image)
        print("✅ Completed. Image saved.")
    except Exception as e:
        print(f"❌ Error while saving file: {e}")

if __name__ == "__main__":
    print("Welcome to Background Remover")

    input_path = input("Enter the path of the input image: ").strip()
    if not input_path:
        print("❌ No input path provided.")
    else:
        output_path = input("Enter the path to save the output image (e.g., output.png): ").strip()
        if not output_path:
            print("❌ No output path provided.")
        else:
            remove_background(input_path, output_path)
