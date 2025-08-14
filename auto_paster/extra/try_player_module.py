from plyer import notification
import time

if callable(getattr(notification, "notify", None)):
    notification.notify(
        title='Testing',
        message='This is a final test notification.',
        timeout=5
    )
else:
    print("Notification feature is not available on this system.")

# Add a small delay to keep the script running
time.sleep(6)