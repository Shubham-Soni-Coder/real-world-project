# backend.py
from PIL import ImageTk

class RectangleDrawerBackend:
    def __init__(self, canvas, image):
        self.canvas = canvas
        self.image = image

        self.start_x = None
        self.start_y = None
        self.rect = None

        self.tk_image = None
        self.last_rect_coords = None

        self.all_rectangles = [] # store all the id of the rectangles

        self.croped_image = None
        self.save_path = "D:/coding/python/real-world-project/auto_typing/screenshots/image.jpg"
    


        self.load_image()
        self.bind_events()

    def load_image(self):
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.tk_image)

    def bind_events(self):
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(
            self.start_x, self.start_y, self.start_x, self.start_y,
            outline="red", width=2
        )
        self.all_rectangles.append(self.rect)

    def on_mouse_drag(self, event):
        if self.rect:
            self.canvas.coords(self.rect, self.start_x, self.start_y, event.x, event.y)

    def on_button_release(self, event):
        if self.rect:
            # Save the final rectangle coords
            self.last_rect_coords = (self.start_x, self.start_y, event.x, event.y)
        self.rect = None
    
    def crop_selected_area(self, save_path=None):
        """Crop the selected area and save it. Show a message box if saved."""
        import tkinter.messagebox as messagebox
        if save_path is None:
            save_path = self.save_path
        if self.last_rect_coords:
            x1, y1, x2, y2 = self.last_rect_coords
            # Ensure proper bounding box
            x1, x2 = sorted([x1, x2]) #type:ignore
            y1, y2 = sorted([y1, y2]) #type:ignore
            cropped = self.image.crop((x1, y1, x2, y2))
            cropped.save(save_path)
            self.crop_image = cropped
            msg = f"Cropped image saved to {save_path}"
            print(msg)
            messagebox.showinfo("Image Saved", msg)
            return self.croped_image 
        else:
            print("No rectangle selected to crop.")
            messagebox.showwarning("No Selection", "No rectangle selected to crop.")


    def clear_all_rectangles(self):
        """Delete all the rectangle from the canvas."""
        for rect_id in self.all_rectangles:
            self.canvas.delete(rect_id)
        self.all_rectangles.clear()
        self.last_rect_coords = None
        print("All rectangle is delete")