import time 
import threading
from multiprocessing import Process



def first_function():
    start = time.time()
    for i in range(10):
        print("I am calling from the first function and my index is : ",i)
        time.sleep(0.5)
    end = time.time()
    print(f"The time required for running this function is {end - start}")


def second_function():
    start = time.time()
    for i in range(10):
        print("I am calling from the second function and my index is : ",i)
        time.sleep(0.5)
    end = time.time()
    print(f"The time required for running this function is {end - start}")

# # make the thrust 
thread1  = threading.Thread(target=first_function)
thread2  = threading.Thread(target=second_function)

# start both thread
thread1.start()
thread2.start()

# join both of than 
thread1.join()
thread2.join()




"""This time is taken by threding."""
# The time required for running this function is 5.015497446060181
# The time required for running this function is 5.017431020736694


"""This time is taken by Process of the multiprocessing class."""
# The time required for running this function is 5.051809549331665
# The time required for running this function is 5.03596568107605