
"""
FontendApp: A Tkinter-based frontend for drawing rectangles and cropping images interactively.

Features:
- Allows users to draw rectangles on an image using mouse events.
- Crops the selected area and saves it to disk when Enter is pressed.
- Clears all rectangles with Backspace.
- Destroys the window after cropping and exposes the cropped image and path.

Usage:
    app = FontendApp(RectangleDrawerBackend, image)
    app.run()
    print(app.image_path)  # Path to the saved cropped image
    print(app.last_cropped_image)  # PIL Image object of the cropped area
"""

import tkinter as tk


class FontendApp:
    """
    Tkinter frontend for interactive rectangle drawing and cropping.
    """
    def __init__(self, RectangleDrawerBackend, image=None):
        """
        Initialize the frontend window and canvas, and set up event bindings.
        Args:
            RectangleDrawerBackend: The backend class for rectangle/crop logic.
            image: Optional PIL Image to display. If None, creates a blank image.
        """
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
        """
        Crop the selected area, save it, destroy the window, and store the result.
        Args:
            save_path: Optional path to save the cropped image.
        Returns:
            The cropped PIL Image object.
        """
        self.last_cropped_image = self.app.crop_selected_area(save_path)
        self.root.destroy()
        return self.last_cropped_image

    def run(self):
        """
        Start the Tkinter main event loop.
        """
        self.root.mainloop()

if __name__ == "__main__":
    from recangledrawer import RectangleDrawerBackend
    image_path = "D:/coding/python/real-world-project/auto_typing/screenshots"
    app = FontendApp(RectangleDrawerBackend)
    app.run()
    print(app.image_path)