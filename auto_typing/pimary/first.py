import time
import pyautogui

file_path = "words.txt"

# def read_line(file_path):
#     start = time.time()
#     with open(file_path, 'r', encoding='utf-8') as file:
#                 for line in file:
#                     # Split the line into words.
#                     # .split() without argumesnts splits by any whitespace and handles multiple spaces.
#                     words = line.strip().split()
#                     for word in words:
#                         for letter in word:
#                             print(letter,end='')

#     end = time.time()
#     return f"Time taken to read and display all words: {end - start} seconds"


def read_file(file_path):
    start = time.time()



def type_letters(file_path):
    # Start timing
    start = time.time()

    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Optional pause before typing (so you can focus a window)
    print("Typing will start in 3 seconds. Switch to the input window...")
    time.sleep(3)

    # Type each letter using pyautogui
    for letter in content:
        if letter.isspace():
            pyautogui.press('space')  # handle spaces/tabs/newlines
        else:
            pyautogui.write(letter)

    # End timing
    end = time.time()
    return f"Time taken to read and type all letters: {end - start} seconds"


print(type_letters(file_path))