import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class HistoryWindow:
    def __init__(self, root, history_file="history.txt", width=800, height=600):
        self.root = tk.Toplevel(root)
        self.root.title("Calculator History")
        self.root.geometry(f"{width}x{height}")
        self.root.configure(bg="#181818")
        self.root.resizable(False, False)
        self.history_file = history_file

        self._setup_styles()
        self._setup_widgets()
        self.load_history()

    def _setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("HistoryTitle.TLabel",
                        font=("Segoe UI", 20, "bold"),
                        foreground="#ffffff",
                        background="#181818",
                        padding=12)

        style.configure("History.TFrame",
                        background="#181818")

    def _setup_widgets(self):
        # Main vertical layout using pack (title > text > buttons)
        
        # Title
        title = ttk.Label(self.root, text="Calculation History", style="HistoryTitle.TLabel")
        title.pack(pady=(18, 8))

        # Frame for text and scrollbar
        text_frame = ttk.Frame(self.root, style="History.TFrame")
        text_frame.pack(padx=18, pady=8, fill="both", expand=True)

        scrollbar = ttk.Scrollbar(text_frame, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        self.text = tk.Text(
            text_frame,
            font=("Consolas", 13),
            bg="#232323",
            fg="#f5f5f5",
            insertbackground="#f5f5f5",
            wrap="word",
            borderwidth=0,
            relief="flat",
            yscrollcommand=scrollbar.set,
            highlightthickness=1,
            highlightbackground="#333333"
        )
        self.text.pack(side="left", fill="both", expand=True)
        self.text.config(state="disabled")
        scrollbar.config(command=self.text.yview)

        # Button frame (fixed height so it always shows)
        btn_frame = tk.Frame(self.root, bg="#181818", height=60)
        btn_frame.pack(pady=(0, 10), padx=20, fill="x")

        clear_btn = tk.Button(btn_frame, text="Clear History", font=("Segoe UI", 13, "bold"),
                              fg="#ffffff", bg="#232323", activebackground="#333333",
                              activeforeground="#ffffff", bd=0, padx=10, pady=6,
                              command=self.clear_history)
        clear_btn.grid(row=0, column=0, sticky="ew", padx=(0, 10), pady=6)

        save_btn = tk.Button(btn_frame, text="Save History", font=("Segoe UI", 13, "bold"),
                             fg="#ffffff", bg="#232323", activebackground="#333333",
                             activeforeground="#ffffff", bd=0, padx=10, pady=6,
                             command=self.save_history)
        save_btn.grid(row=0, column=1, sticky="ew", padx=10, pady=6)

        close_btn = tk.Button(btn_frame, text="Close", font=("Segoe UI", 13, "bold"),
                              fg="#ffffff", bg="#232323", activebackground="#333333",
                              activeforeground="#ffffff", bd=0, padx=10, pady=6,
                              command=self.root.destroy)
        close_btn.grid(row=0, column=2, sticky="ew", padx=(10, 0), pady=6)

        # Equal size buttons
        btn_frame.columnconfigure(0, weight=1)
        btn_frame.columnconfigure(1, weight=1)
        btn_frame.columnconfigure(2, weight=1)

    def load_history(self):
        self.text.config(state="normal")
        self.text.delete(1.0, tk.END)
        try:
            with open(self.history_file, "r") as file:
                content = file.read()
                self.text.insert(tk.END, content)
        except FileNotFoundError:
            self.text.insert(tk.END, "No history found.")
        self.text.config(state="disabled")

    def clear_history(self):
        if messagebox.askyesno("Clear History", "Are you sure you want to clear all history?"):
            with open(self.history_file, "w") as file:
                file.write("")
            self.load_history()

    def save_history(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")], title="Save History As")
        if file_path:
            try:
                with open(self.history_file, "r") as src, open(file_path, "w") as dst:
                    dst.write(src.read())
                messagebox.showinfo("Success", f"History saved to {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save history: {e}")

# Example usage:
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide root window
    HistoryWindow(root, width=800, height=600)  # You can adjust dimensions here
    root.mainloop()
