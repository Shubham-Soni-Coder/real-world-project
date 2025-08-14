
"""
RectangleDrawerBackend: A Tkinter backend class for drawing, cropping, and managing rectangles on a canvas.

Features:
- Draw rectangles interactively with mouse events on a Tkinter canvas.
- Crop the selected area of an image and save it to disk.
- Show message boxes for crop/save actions.
- Support for callback on crop event.
- Clear all drawn rectangles.

Usage:
    backend = RectangleDrawerBackend(canvas, image, on_crop=callback)
    # canvas: Tkinter Canvas widget
    # image: PIL Image object
    # on_crop: Optional callback function called with cropped image after crop
"""

from PIL import ImageTk
import os
class RectangleDrawerBackend:
    """
    Backend for rectangle drawing and cropping on a Tkinter canvas.
    Handles mouse events, cropping, and rectangle management.
    """
    def __init__(self, canvas, image, on_crop=None):
        """
        Initialize the backend.
        Args:
            canvas: Tkinter Canvas widget to draw on.
            image: PIL Image object to display and crop.
            on_crop: Optional callback function called with cropped image after crop.
        """
        self.canvas = canvas
        self.image = image
        self.on_crop = on_crop  # Callback function for crop event

        self.start_x = None
        self.start_y = None
        self.rect = None

        self.tk_image = None
        self.last_rect_coords = None

        self.all_rectangles = [] # store all the id of the rectangles

        self.croped_image = None
        self.save_path = "screenshots"

        if not os.path.exists(self.save_path):  
            os.mkdir(self.save_path)

        self.load_image()
        self.bind_events()

    def load_image(self):
        """
        Load the image onto the canvas as a background.
        """
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.tk_image)

    def bind_events(self):
        """
        Bind mouse events to the canvas for rectangle drawing:
            - ButtonPress-1: Start drawing rectangle
            - B1-Motion: Drag to resize rectangle
            - ButtonRelease-1: Finish rectangle
        """
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

    def on_button_press(self, event):
        """
        Mouse button pressed: Start a new rectangle at the cursor position.
        """
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(
            self.start_x, self.start_y, self.start_x, self.start_y,
            outline="red", width=2
        )
        self.all_rectangles.append(self.rect)

    def on_mouse_drag(self, event):
        """
        Mouse is dragged: Update the rectangle's bottom-right corner to the current cursor position.
        """
        if self.rect:
            self.canvas.coords(self.rect, self.start_x, self.start_y, event.x, event.y)

    def on_button_release(self, event):
        """
        Mouse button released: Finalize the rectangle and store its coordinates.
        """
        if self.rect:
            self.last_rect_coords = (self.start_x, self.start_y, event.x, event.y)
        self.rect = None
    
    def crop_selected_area(self, save_path=None):
        """
        Crop the selected rectangle area from the image and save it.
        Shows a message box if saved, and calls the on_crop callback if set.
        Args:
            save_path: Optional path to save the cropped image. Defaults to self.save_path.
        Returns:
            The cropped PIL Image object, or None if no rectangle is selected.
        """
        import tkinter.messagebox as messagebox # for messsage show that crop image is saved
        if save_path is None: # check that any another save_path is not used
            save_path = f"{self.save_path}/image.jpg"
        if self.last_rect_coords:
            x1, y1, x2, y2 = self.last_rect_coords
            # Ensure proper bounding box
            x1, x2 = sorted([x1, x2]) #type:ignore
            y1, y2 = sorted([y1, y2]) #type:ignore
            cropped = self.image.crop((x1, y1, x2, y2))
            cropped.save(save_path)
            self.crop_image = cropped
            msg = f"Cropped image saved to {save_path}"
            messagebox.showinfo("Image Saved", msg) #show msg
            if self.on_crop: #check for on_crop
                self.on_crop(self.crop_image)
            return self.crop_image 
        else:
            print("No rectangle selected to crop.")
            messagebox.showwarning("No Selection", "No rectangle selected to crop.")


    def clear_all_rectangles(self):
        """
        Delete all rectangles from the canvas and reset state.
        """
        for rect_id in self.all_rectangles:
            self.canvas.delete(rect_id)
        self.all_rectangles.clear()
        self.last_rect_coords = None
        print("All rectangle is delete") #this is also for testing