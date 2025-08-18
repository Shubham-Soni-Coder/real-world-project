import time
import os
import keyboard  #type:ignore
from main_code import main  
from plyer import notification

def notificatio_show(notification_title,notification_message):
    notification.notify(
    title=notification_title,
    message=notification_message
) # pyright: ignore[reportOptionalCall]
    print("This function can as i wish")

def my_program_logic():
    """
    This function contains the code you want to execute when 'alt+shift+s' is pressed.
    """
    print("Executing main program logic...") 
    main()
    time.sleep(1) # Give Python time to potentially free memory



def exit_program():
    # global notificatio_runner 
    notificatio_show("Thanks..","Thanks for useing this program")
    print("\n'Ctrl+shift+q' pressed. Exiting the program")
    time.sleep(5)
    os._exit(0)


# notificatio_runner = None


#Register the hotkey to exit the program
keyboard.add_hotkey('ctrl+shift+q',exit_program)


# The main loop to keep the program running
notificatio_show("Running in background","Your auto screenshot are running in background , You can use by 'alt+shift+s'")
print("Press 'alt+shift+s' to activate.")
print("Press 'ctrl+shift+q' for exit the program")


while True:
    keyboard.wait("alt+shift+s")
    
    print("\n'alt+shift+s' key was pressed! Starting the program...")
    
    my_program_logic()
    print("Press 'alt+shift+s' again to activate.") 
    print("\n'Ctrl+shift+q' press for Exit the program")


    