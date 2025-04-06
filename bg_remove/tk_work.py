import tkinter as tk
from tkinter.ttk import Button, Label, Entry, Style,Frame
from tkinter import filedialog, messagebox
from PIL import Image,UnidentifiedImageError
window = tk.Tk()
window.title("Background Removal")
window.geometry("500x400")
window.resizable(False, False)


style = Style()
style.configure("TButton", font=("Arial", 12))
style.map("TButton", foreground=[("active", "blue")])
style.lookup("TButton", "padding")


def select_input_image():
    # Open a file dialog to select an input image
    input_image_path = filedialog.askopenfilename(
        title="Select Input Image",
        filetypes=(("Image Files", "*.jpg;*.jpeg;*.png"), ("All Files", "*.*")),
    )
    if not input_image_path:
        messagebox.showerror("Error", "No file selected.")
        return
    try:    
        # Open the input image to check if it's valid
        image = Image.open(input_image_path)
        image.verify()  # Verify that the image is valid
    except UnidentifiedImageError:
        messagebox.showerror("Error", "The selected file is not a valid image.")
        return
    return input_image_path

def select_output_image():
    # Open a file dialog to select an output image
    output_image_path = filedialog.asksaveasfilename(
        title="Select Output Image",
        defaultextension=".png",
        filetypes=(("PNG Files", "*.png"), ("JPEG Files", "*.jpg;*.jpeg"), ("All Files", "*.*")),
    )
    if not output_image_path:
        messagebox.showerror("Error", "No file selected.")
        return
    return output_image_path

def show_selected_image_path(path):
    # Update the label to show the selected image path
    input_image_label.config(text=f"Selected Input Image Path: {path}")



# Create a label to display the title
title_label = Label(window, text="Background Removal Tool",)
title_label.pack(pady=10)

# button frame
button_frmame = Frame(window,relief="raised",borderwidth=2,style="TButton")
button_frmame.pack()

# label frame
label_frame = Frame(window,relief="raised",borderwidth=2,style="TButton")
label_frame.pack(pady=10)



# Create a button for selecting the input image
select_button = Button(button_frmame, text="Select Input Image", command=select_input_image,cursor="hand2")
select_button.pack()


# Create a label for show the selected input image path
input_image_label = Label(label_frame, text="Selected Input Image Path:")
input_image_label.pack(pady=5)
 
# close tk window
window.mainloop()