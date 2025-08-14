import time
import os
import keyboard  #type:ignore
from main_code import main  

def my_program_logic():
    """
    This function contains the code you want to execute when 'alt+shift+s' is pressed.
    """
    print("Executing main program logic...")
    main()
    time.sleep(1) # Give Python time to potentially free memory



def exit_program():
    print("\n'Ctrl+shift+q' pressed. Exiting the program")
    os._exit(0)


#Register the hotkey to exit the program
keyboard.add_hotkey('ctrl+shift+q',exit_program)


# The main loop to keep the program running
print("Press 'alt+shift+s' to activate.")
print("Press 'ctrl+shift+q' for exit the program")


while True:
    keyboard.wait("alt+shift+s")
    
    print("\n'alt+shift+s' key was pressed! Starting the program...")
    
    my_program_logic()
    print("Press 'alt+shift+s' again to activate.") 
    print("\n'Ctrl+shift+q' press for Exit the program")


    