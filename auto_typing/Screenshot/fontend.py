# frontend.py
import tkinter as tk


class FontendApp:
    def __init__(self,RectangleDrawerBackend, image=None):
        self.root = tk.Tk()
        self.root.title("Image Rectangle Drawer")
        self.last_cropped_image = None
        self.image_path = None
        if image is None:
            from PIL import Image
            image = Image.new("RGB", (600, 400), color="white")

        self.canvas = tk.Canvas(self.root, width=image.width, height=image.height)
        self.canvas.pack()

        # Pass canvas and image to backend
        self.app = RectangleDrawerBackend(self.canvas, image)
        self.image_path = self.app.save_path

        # Bind Enter key to crop
        self.root.bind("<Return>", lambda event: self.crop_image_saver())
        # Bind Backspace to clear all rectangles
        self.root.bind("<BackSpace>", lambda event: self.app.clear_all_rectangles())

    def crop_image_saver(self, save_path=None):
        self.last_cropped_image = self.app.crop_selected_area(save_path)
        self.root.destroy()
        return self.last_cropped_image

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    from recangledrawer import RectangleDrawerBackend
    image_path = "D:/coding/python/real-world-project/auto_typing/screenshots"
    
    app = FontendApp(RectangleDrawerBackend)
    app.run()
    print(app.image_path)