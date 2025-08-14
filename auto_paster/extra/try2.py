import psutil
import os
import time
import keyboard  #type:ignore
# Get the current process ID
process = psutil.Process(os.getpid())

def get_ram_usage():
    """
    Returns the memory usage of the current process in megabytes (MB).
    """
    # memory_info().rss returns the "resident set size" in bytes, 
    # which is the non-swapped physical memory used by the process.
    return process.memory_info().rss / (1024 * 1024)

def my_program_logic():
    """
    This function contains the code you want to execute when 'alt+shift+s' is pressed.
    """
    print("Executing main program logic...")
    start = time.time()
    # --- Simulate a task that uses more RAM ---
    large_list = [i for i in range(10_000_000)]
    print(f"RAM usage during task: {get_ram_usage():.2f} MB")
    print(f"The time taken by this tasks is {time.time() - start:.2f}")
    
    # Delete the large object to free up memory
    del large_list
    print("Task finished.")
    time.sleep(1) # Give Python time to potentially free memory


def exit_program():
    print("\n'Ctrl+shift+q' pressed. Exiting the program" )
    os._exit(0)

#Register the hotkey to exit the program
keyboard.add_hotkey('ctrl+shift+q',exit_program)


# The main loop to keep the program running
print(f"Script is in 'sleep mode' and ready. Initial RAM usage: {get_ram_usage():.2f} MB")
print("Press 'alt+shift+s' to activate.")
print("Press 'ctrl+shift+q' for exit the program")

while True:
    keyboard.wait("alt+shift+s")
    
    print("\n'alt+shift+s' key was pressed! Starting the program...")
    
    my_program_logic()
    
    print(f"\nReturning to 'sleep mode'. Current RAM usage: {get_ram_usage():.2f} MB")
    print("Press 'alt+shift+s' again to activate.") 


