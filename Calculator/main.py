import tkinter as tk
from tkinter import ttk

class CalculatorMainMenu:
    def __init__(self,root, width = 400 , height = 550):
        # Define screen dimensions
        self.width = width
        self.height = height
        self.root = root

        # Create main window
        self.root.title("Calculator Main Menu")
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.configure(bg="#2c3e50")

        # Styling
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Custom.TButton",
                        font=("Segoe UI", 14, "bold"),
                        padding=12,
                        foreground="#ffffff",
                        background="#3498db",
                        borderwidth=0)
        style.map("Custom.TButton",
                  background=[("active", "#2980b9")])

        # Title label
        self.title = tk.Label(self.root,
                         text="Welcome to Calculator",
                         font=("Segoe UI", 20, "bold"),
                         fg="#ecf0f1",
                         bg="#2c3e50")
        self.title.pack(pady=(self.height * 0.125, 30))

        # Frame for buttons
        self.button_frame = tk.Frame(self.root, bg="#2c3e50")
        self.button_frame.pack(pady=10)

        # Create buttons with hand cursor
        start_button = ttk.Button(self.button_frame, text="Start", command=self.on_start, style="Custom.TButton", cursor="hand2")
        start_button.pack(pady=10, ipadx=40)

        history_button = ttk.Button(self.button_frame, text="History", command=self.on_history, style="Custom.TButton", cursor="hand2")
        history_button.pack(pady=10, ipadx=40)

        exit_button = ttk.Button(self.button_frame, text="Exit", command=self.on_exit, style="Custom.TButton", cursor="hand2")
        exit_button.pack(pady=10, ipadx=40)

    def on_start(self):
        from start.forentent import CalculatorApp
        self.button_frame.destroy()
        self.title.destroy()
        app = CalculatorApp(self.root,self.width,self.height)

    def on_history(self):
        pass

    def on_exit(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    menu = CalculatorMainMenu(root)
    menu.run()
