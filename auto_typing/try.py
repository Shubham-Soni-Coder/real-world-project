# from extra.mouseinfo import clickTracker
# import numpy as np
# import cv2
# import threading

# # object of this cladd
# mouseinfo = clickTracker()
# runner = False

# """This is the function that update the x1,x2,y1,y2 value """
# def updater_mouse():
#     global runner
#     runner = True
#     mouseinfo.start_listeners()
#     runner = False


# def make_rectangle(img,x1,x2,y1,y2):
#     rect_img = img.copy()
#     cv2.rectangle(rect_img, (x1, y1), (x2, y2), (0, 255, 0), 2)
#     return rect_img

# threading.Thread(target=updater_mouse,daemon=True).start()


# """black or no rgb picture"""
# black_img = np.zeros((768,1366,3),dtype=np.uint8)

# # starting point 
# x1 = 0
# y1 = 0
# x2 = 0
# y2 = 0 

# dx , dy = 0 , 0 

# while runner:
#     rect_img = make_rectangle(black_img, x1,x2, y1, y2)
#     cv2.imshow('Rectangle Image', rect_img)
#     cv2.waitKey(100)
#     if mouseinfo.start_pos and mouseinfo.end_pos:
#         x1 = mouseinfo.start_pos[0]
#         y1 = mouseinfo.end_pos[0]
#         x2 = x1+mouseinfo.dx
#         y2 = y1+mouseinfo.dy

# cv2.destroyAllWindows()
