import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self, root,width ,height):
        self.root = root
        self.width = width
        self.height = height

        self.root.title("Calculator")
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.configure(bg="#2c3e50")
        self.root.resizable(False, False)
   


        self._setup_styles()
        self._setup_display()
        self._setup_buttons()
        self._setup_bindings()

    def _setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Calc.TButton",
                        font=("Segoe UI", 14, "bold"),
                        padding=10,
                        foreground="#ffffff",
                        background="#3498db",
                        borderwidth=0)
        style.map("Calc.TButton",
                  background=[("active", "#2980b9")])

    def _setup_display(self):
        self.display_var = tk.StringVar()
        self.display_label = tk.Label(self.root,
                                      textvariable=self.display_var,
                                      anchor="e",
                                      font=("Segoe UI", 24),
                                      bg="#ecf0f1",
                                      fg="#2c3e50",
                                      padx=10,
                                      pady=20)
        self.display_label.pack(fill="x", padx=10, pady=(20, 10))

    def _setup_buttons(self):
        self.button_frame = tk.Frame(self.root, bg="#2c3e50")
        self.button_frame.pack(padx=10, pady=10)

        buttons = [
            ['C', '±', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', 'Back']
        ]

        for r, row in enumerate(buttons):
            for c, char in enumerate(row):
                if char == '':
                    continue
                if char == 'C':
                    command = self.clear
                elif char == 'Back':
                    command = self.on_back
                elif char == '=':
                    command = self.equal
                else:
                    command = lambda ch=char: self.append(ch)

                btn = ttk.Button(self.button_frame,
                                 text=char,
                                 style="Calc.TButton",
                                 cursor="hand2",
                                 command=command)
                btn.grid(row=r, column=c, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

        # Adjust column and row weights for 4 columns now
        for i in range(4):
            self.button_frame.columnconfigure(i, weight=1)
        for i in range(len(buttons)):
            self.button_frame.rowconfigure(i, weight=1)

    def _setup_bindings(self):
        self.root.bind("<Key>", self.handle_key)

    def append(self, value):
        self.display_var.set(self.display_var.get() + value)

    def clear(self):
        self.display_var.set("")

    def equal(self):
        expression = self.display_var.get()
        try:
            # Evaluate the math expression safely
            result = eval(expression, {"__builtins__":None}, {})
            self.display_var.set(str(result))
            self.histroy_saver(expression,result)
        except Exception:
            self.display_var.set("Error")

    def on_back(self):
        # Placeholder function for Back button
        from main import CalculatorMainMenu
        self.display_label.destroy()
        self.button_frame.destroy()
        menu = CalculatorMainMenu(self.root)
        menu.run()

    def handle_key(self, event):
        key = event.keysym

        if key in "0123456789":
            self.append(key)
        elif key in ["plus", "KP_Add"]:
            self.append("+")
        elif key in ["minus", "KP_Subtract"]:
            self.append("-")
        elif key in ["asterisk", "KP_Multiply"]:
            self.append("*")
        elif key in ["slash", "KP_Divide"]:
            self.append("/")
        elif key == "period" or event.char == ".":
            self.append(".")
        elif key == "Return":
            self.equal()
        elif key == "BackSpace":
            current = self.display_var.get()
            self.display_var.set(current[:-1])
        elif key == "Escape":
            self.clear()
        elif key.lower() == "c":
            self.clear()

    def histroy_saver(self,expression,result):
        equation  = f"{expression}={result}"
        with open("histroy.txt",'a') as file:
            file.write(equation+"\n")
            print("Histroy is Saved")





if __name__ == "__main__":
    root = tk.Tk()
    width = 400
    height = 550
    app = CalculatorApp(root,width,height)
    root.mainloop()
