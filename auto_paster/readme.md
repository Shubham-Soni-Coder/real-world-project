
# Auto Paster

Auto Paster is a Python tool that automates the process of taking a screenshot, letting the user crop a region, performing OCR (Optical Character Recognition) on the cropped image, and copying the recognized text to the clipboard. It also includes hotkey support for quick activation and exit.

## Features

- Take a screenshot of your screen
- Interactive cropping UI (Tkinter-based)
- OCR on the cropped image using Tesseract
- Copy recognized text to clipboard
- Hotkey support for activation (`Alt+Shift+S`) and exit (`Ctrl+Shift+Q`)

## Folder Structure

```
main_code.py           # Main workflow for screenshot, crop, OCR, clipboard
main.py                # Hotkey-based runner for the main workflow
requirements.txt       # Python dependencies
extra/
 try_player_module.py # Example: desktop notification
 try2.py              # Example: RAM usage and hotkey logic
Screenshot/
 fontend.py           # Tkinter frontend for cropping
 recangledrawer.py    # Backend for rectangle drawing/cropping
 __init__.py          # (empty)
screenshots/
 image.jpg            # Example screenshot
```

## How It Works

1. **Run `main.py`**

- Starts a loop waiting for hotkeys.
- Press `Alt+Shift+S` to activate the screenshot-to-clipboard workflow.
- Press `Ctrl+Shift+Q` to exit the program.

2. **Workflow**

- Takes a screenshot of your screen.
- Opens a Tkinter window to let you crop a region.
- Runs OCR on the cropped image (requires Tesseract-OCR installed).
- Copies the recognized text to your clipboard.

### Requirements

- Python 3.x
- [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract) (must be installed and path set in `main_code.py`)
- Python packages (see `requirements.txt`):
 	- Pillow
 	- pytesseract
 	- pyperclip
 	- keyboard
 	- psutil

Install dependencies:

```sh
pip install -r requirements.txt
```

### Usage

1. **Install Tesseract-OCR**
  - Download and install from [here](https://github.com/tesseract-ocr/tesseract).
  - Update the path in `main_code.py` if needed:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```

2. **Run the program**
  ```sh
  python main.py
  ```

3. **Follow on-screen instructions**
  - Press `Alt+Shift+S` to start the screenshot-to-clipboard process.
  - Press `Ctrl+Shift+Q` to exit.

### Extra Scripts

- `extra/try_player_module.py`: Shows a desktop notification (uses `plyer`)
- `extra/try2.py`: Example of RAM usage tracking and hotkey logic

### Notes

- The `Screenshot` folder contains the Tkinter UI and backend for cropping.
- The `screenshots` folder may contain example images.
- Make sure Tesseract-OCR is installed and the path is correct.

---
**Author:** Shubham Soni
**License:** MIT (or specify your license)
