from picamera2 import Picamera2, Preview
from time import sleep
from datetime import datetime


def get_timestamp():
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%dT%H-%M-%S")
    return timestamp


timestamp = get_timestamp()
picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start_preview(Preview.DRM)
picam2.start()
sleep(2)
picam2.capture_file(timestamp + ".jpg")
