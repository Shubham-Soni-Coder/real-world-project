import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

class PDFMergeTool:
    def __init__(self, root,merge_function,width=900,height=600):
        # Adjustable height and width
        self.width = width
        self.height = height

        self.root = root
        self.root.title("PDF Merge Tool")
        self.root.geometry(f"{self.width}x{self.height}")  # Use variables for size
        self.root.resizable(False, False)

        # Style Configuration
        style = ttk.Style()
        style.theme_use("clam")

        # Merge PDFs Button (Moved to the top)
        self.merge_button = ttk.Button(root, text="Merge PDFs", command=self.merge_pdfs)
        self.merge_button.pack(pady=10)
        self.merge_button.configure(style="Merge.TButton")

        # Frame for Buttons
        self.button_frame = ttk.Frame(root, padding=10)
        self.button_frame.pack(fill=tk.X)

        # Add PDF Files Button
        self.add_button = ttk.Button(self.button_frame, text="Add PDF Files", command=self.add_files)
        self.add_button.grid(row=0, column=0, padx=5, pady=5)
        self.add_button.configure(style="Accent.TButton")

        # Remove Selected File Button
        self.remove_button = ttk.Button(self.button_frame, text="Remove Selected File", command=self.remove_selected)
        self.remove_button.grid(row=0, column=1, padx=5, pady=5)
        self.remove_button.configure(style="Accent.TButton")

        # Clear All Button
        self.clear_button = ttk.Button(self.button_frame, text="Clear All", command=self.clear_all)
        self.clear_button.grid(row=0, column=2, padx=5, pady=5)
        self.clear_button.configure(style="Accent.TButton")

        # Move Up Button
        self.move_up_button = ttk.Button(self.button_frame, text="Move Up", command=self.move_up)
        self.move_up_button.grid(row=0, column=3, padx=5, pady=5)
        self.move_up_button.configure(style="Accent.TButton")

        # Move Down Button
        self.move_down_button = ttk.Button(self.button_frame, text="Move Down", command=self.move_down)
        self.move_down_button.grid(row=0, column=4, padx=5, pady=5)
        self.move_down_button.configure(style="Accent.TButton")

        # Listbox with Scrollbar
        self.listbox_frame = ttk.Frame(root, padding=10)
        self.listbox_frame.pack(fill=tk.BOTH, expand=True)
        self.scrollbar = ttk.Scrollbar(self.listbox_frame, orient=tk.VERTICAL)
        self.listbox = tk.Listbox(self.listbox_frame, selectmode=tk.SINGLE, yscrollcommand=self.scrollbar.set, height=20)
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Output Location Section
        self.output_frame = ttk.Frame(root, padding=10)
        self.output_frame.pack(fill=tk.X)
        self.output_button = ttk.Button(self.output_frame, text="Select Output Location", command=self.select_output_location)
        self.output_button.pack(side=tk.LEFT, padx=5)
        self.output_button.configure(style="Accent.TButton")
        self.output_label = ttk.Label(self.output_frame, text="No output location selected", foreground="blue")
        self.output_label.pack(side=tk.LEFT, padx=5)

        # Status Label
        self.status_label = ttk.Label(root, text="", foreground="green")
        self.status_label.pack(pady=5)

        # Internal Variables
        self.pdf_files = []
        self.output_path = ""
        self.merge_function = merge_function  # Store the merge function

        # Custom Styles
        style.configure("Accent.TButton", background="#4CAF50", foreground="white", font=("Arial", 10, "bold"))
        style.map("Accent.TButton", background=[("active", "#45A049")])
        style.configure("Merge.TButton", background="#FF5722", foreground="white", font=("Arial", 12, "bold"))
        style.map("Merge.TButton", background=[("active", "#E64A19")])

    def add_files(self):
        files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
        for file in files:
            if file not in self.pdf_files:
                self.pdf_files.append(file)
                self.listbox.insert(tk.END, file)

    def remove_selected(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.pdf_files.pop(index)
            self.listbox.delete(index)

    def clear_all(self):
        self.pdf_files.clear()
        self.listbox.delete(0, tk.END)

    def move_up(self):
        selected = self.listbox.curselection()
        if selected and selected[0] > 0:
            index = selected[0]
            self.pdf_files[index - 1], self.pdf_files[index] = self.pdf_files[index], self.pdf_files[index - 1]
            self.listbox.delete(0, tk.END)
            for file in self.pdf_files:
                self.listbox.insert(tk.END, file)
            self.listbox.select_set(index - 1)

    def move_down(self):
        selected = self.listbox.curselection()
        if selected and selected[0] < len(self.pdf_files) - 1:
            index = selected[0]
            self.pdf_files[index + 1], self.pdf_files[index] = self.pdf_files[index], self.pdf_files[index + 1]
            self.listbox.delete(0, tk.END)
            for file in self.pdf_files:
                self.listbox.insert(tk.END, file)
            self.listbox.select_set(index + 1)

    def select_output_location(self):
        self.output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if self.output_path:
            self.output_label.config(text=self.output_path)

    def merge_pdfs(self):
        if len(self.pdf_files) < 2:
            messagebox.showerror("Error", "Please add at least 2 PDFs")
            return
        if not self.output_path:
            messagebox.showerror("Error", "Please select an output location")
            return
        try:
            self.merge_function(self.pdf_files, self.output_path)  # Call the merge function
            self.status_label.config(text="Files merged successfully", foreground="green")
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}", foreground="red")

if __name__ == "__main__":
    root = tk.Tk()
    # Example merge function
    def example_merge_function(pdf_files, output_path):
        print(f"Merging {pdf_files} into {output_path}")
    app = PDFMergeTool(root,example_merge_function)
    root.mainloop()