from pynput import mouse,keyboard

class clickTracker:
    def __init__(self) -> None:
        self.start_pos = None # store x1,x2 when left click is press
        self.end_pos = None # store x2,y2 when left click id released
        self.mouse_listener = mouse.Listener(on_click=self.on_click)
        self.keyboard_listener = keyboard.Listener(on_press=self.on_press) #type:ignore


    def on_click(self, x, y, button, pressed):
        """Handles mouse click events (press and release)."""
        if button == mouse.Button.left:
            if pressed:
                self.start_pos = (x, y)
                print(f"[Pressed] at x1: {x}, y1: {y}")
            else:
                self.end_pos = (x, y)
                print(f"[Released] at x2: {x}, y2: {y}")
                dx = self.end_pos[0] - self.start_pos[0] #type:ignore
                dy = self.end_pos[1] - self.start_pos[1] #type:ignore
                print(f"Mouse moved -> dx: {dx}, dy: {dy}")

    def on_press(self,key):
        """Handles keyboard press events. Press 'c' to exit the program."""
        if hasattr(key, 'char') and key.char == 'c':
            print("Key 'c' pressed. Exiting program.")
            self.stop_listeners()
            return False  # Stop keyboard listener


    def start_listeners(self):
        """Starts both mouse and keyboard listeners."""
        self.mouse_listener.start()
        self.keyboard_listener.start()
        self.mouse_listener.join()
        self.keyboard_listener.join()


    def stop_listeners(self):
        """Stops the mouse listener. Keyboard listener stops automatically with 'return False'."""
        print("[Stop] Stopping mouse listener...")
        self.mouse_listener.stop()


    # Add some porpertly to the class
    @property
    def x1(self):
        return self.start_pos[0] if self.start_pos else None
    
    @property
    def y1(self):
        return self.start_pos[1] if self.start_pos else None

    @property
    def x2(self):
        return self.end_pos[0] if self.end_pos else None

    @property
    def y2(self):
        return self.end_pos[0] if self.end_pos else None

def main():
    tracker = clickTracker()
    tracker.start_listeners()


if __name__=="__main__":
    main()
