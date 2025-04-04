import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, messagebox


def create_file_organizer_app():
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
    style.configure("Custom.TButton", background="#3498db", foreground="black", font=("Arial", 12), padding=5)
    style.configure("TLabel", font=("Arial", 15), padding=10)


    def select_folder():
        global folder_path
        folder_path = filedialog.askdirectory(title="Select Folder")
        update_folder_label(folder_path)

    def update_folder_label(folder_path):
        folder_label.config(text=folder_path if folder_path else "No folder selected")
        if not folder_path:
            messagebox.showerror("Error", "No folder selected!")
        else:
            messagebox.showinfo("Success", "Folder selected successfully!")
            converter_button.pack(pady=10)  # Show the Converter button when a folder is selected

    # ___existing code 
    log_widget = tk.Text(window, height=10, wrap="word", font=("Arial", 10))
    log_widget.pack(pady=10)
    log_widget.tag_configure("success", foreground="green")
    log_widget.tag_configure("error", foreground="red")


    def open_converter():
        """Placeholder function for the Converter button."""
        from file_organizer import main
        error_count = main(folder_path, log_widget)
        
        if error_count == 0:
            messagebox.showinfo("Success", "Files organized successfully!")
        else:
            messagebox.showwarning("Completed with Errors", f"Files organized with {error_count} errors. Check the log.")
        

    # Use ttk.Button and ttk.Label
    folder_button = ttk.Button(window, text="Select Folder", command=select_folder,style="Custom.TButton")
    folder_button.pack(pady=10)

    folder_label = ttk.Label(window, text="No folder selected", anchor="center",style="TLabel")
    folder_label.pack(pady=10)

    # Add a new button for the Converter (initially hidden)
    converter_button = ttk.Button(window, text="Converter", command=open_converter, style="Custom.TButton")
    # Do not pack the button initially; it will be packed after folder selection

    return window


if __name__ == "__main__":
    app = create_file_organizer_app()
    app.mainloop()

