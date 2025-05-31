# gui.py
import tkinter as tk
from tkinter import ttk
import threading
from backend.backend import TranslatorBackend # type: ignore

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 Language Translator")
        self.root.geometry("400x220")
        self.root.configure(bg="#f4f4f8")
        self.root.resizable(False, False)
        self.root.attributes("-alpha", 0.0)  # Start transparent

        self.backend = TranslatorBackend()
        self.name_to_code = self.backend.name_to_code
        self.language_names = self.backend.language_names

        self.selected_language = tk.StringVar(value="Hindi")

        self.style_ui()
        self.build_gui()

        self.fade_in()

    def style_ui(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TLabel', font=("Segoe UI", 11), background="#f4f4f8")
        style.configure('TEntry', font=("Segoe UI", 11))
        style.configure('TCombobox', font=("Segoe UI", 11))
        style.configure('TFrame', background="#f4f4f8")
        style.configure('TButton', font=("Segoe UI", 10), padding=5)
        self.root.option_add("*Font", ("Segoe UI", 11))

    def build_gui(self):
        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.pack(fill='both', expand=True)

        ttk.Label(self.frame, text="Enter text:").grid(row=0, column=0, sticky='w')
        self.entry1 = ttk.Entry(self.frame, width=30)
        self.entry1.grid(row=0, column=1, pady=5)
        self.entry1.bind('<KeyRelease>', self.update_second_box)

        ttk.Label(self.frame, text="Select language:").grid(row=1, column=0, sticky='w')
        self.language_combo = ttk.Combobox(
            self.frame, values=self.language_names,
            textvariable=self.selected_language,
            width=28, state='readonly'
        )
        self.language_combo.grid(row=1, column=1, pady=5)
        self.language_combo.bind('<<ComboboxSelected>>', self.on_language_change)
        self.language_combo.set("Hindi")

        ttk.Label(self.frame, text="Translation:").grid(row=2, column=0, sticky='w')
        self.entry2 = ttk.Entry(self.frame, width=30)
        self.entry2.grid(row=2, column=1, pady=5)

    def update_second_box(self, *args):
        text = self.entry1.get()
        language = self.selected_language.get()
        threading.Thread(target=self.perform_translation, args=(text, language)).start()

    def perform_translation(self, text, language):
        result = self.backend.translate_text(text, language)
        self.entry2.after(0, lambda: self.update_entry2(result))

    def update_entry2(self, result):
        self.entry2.delete(0, tk.END)
        self.entry2.insert(0, result)

    def on_language_change(self, event=None):
        self.update_second_box()

    def fade_in(self, alpha=0.0):
        if alpha < 1.0:
            alpha += 0.05
            self.root.attributes("-alpha", alpha)
            self.root.after(30, lambda: self.fade_in(alpha))
        else:
            self.root.attributes("-alpha", 1.0)

def run():
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    run()
