import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox


def create_file_organizer_app():
    global folder_path
    """Creates and returns the File Organizer application window."""
    width = 600
    height = 500

    window = tk.Tk()
    window.title("File Organizer")
    window.geometry(f"{width}x{height}")
    window.resizable(False, False)
    window.iconbitmap("icon.ico")  # Set the icon for the window


    # Apply ttk styles
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 12), padding=10)
    style.configure("TLabel", font=("Arial", 12), padding=10)

    folder_path = ""  # Initialize folder_path to avoid undefined variable error

    def select_folder():
        folder_path = filedialog.askdirectory(title="Select Folder")
        update_folder_label(folder_path)

    def update_folder_label(folder_path):
        folder_label.config(text=folder_path if folder_path else "No folder selected")
        if not folder_path:
            messagebox.showerror("Error", "No folder selected!")
        else:
            messagebox.showinfo("Success", "Folder selected successfully!")

    # Use ttk.Button and ttk.Label
    folder_button = ttk.Button(window, text="Select Folder", command=select_folder)
    folder_button.pack(pady=10)

    folder_label = ttk.Label(window, text="No folder selected", anchor="center")
    folder_label.pack(pady=10)

    return window


if __name__ == "__main__":
    app = create_file_organizer_app()
    app.mainloop()

