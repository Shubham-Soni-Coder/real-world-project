from plyer import notification
import time
from datetime import datetime


notification_title = "Water Reminder"
notification_icon = "E:/plyer_module/water.ico"
notification_timeout = 60





def current_timing():
    return datetime.now().strftime("%H:%M:%S")  

for i in range(10):
    print(current_timing())
    notification_message = f"This is the current timing in this time {current_timing()}"
    notification.notify(
        title=notification_title,
        message=notification_message
    ) # pyright: ignore[reportOptionalCall]
    time.sleep(1)
