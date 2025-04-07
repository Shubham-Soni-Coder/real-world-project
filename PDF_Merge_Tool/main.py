from pypdf import PdfWriter, PdfReader  # type: ignore
from gui.gui import PDFMergeTool  # Import the GUI module
import tkinter as tk

pdf = PdfWriter()

def merget_pdf(file_path, output_path):
    for file in file_path:
        pdf_reader = PdfReader(file)
        for page in pdf_reader.pages:
            pdf.add_page(page)

    with open(output_path, "wb") as f:
        pdf.write(f)

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergeTool(root, merge_function=merget_pdf)  # Pass the merge function to the GUI
    root.mainloop()


