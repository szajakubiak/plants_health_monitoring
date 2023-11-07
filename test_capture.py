import argparse
from picamera2 import Picamera2, Preview
from time import sleep
from datetime import datetime


parser = argparse.ArgumentParser()
parser.add_argument("-l", "--lights", help="lights to use", type=str, default="")
parser.add_argument("-f", "--filters", help="filters to use", type=int, default="")


args = parser.parse_args()
lig = args.lights
fil = args.filters


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
filename = timestamp
if len(lig) > 0:
    filename += "_" + lig
if len(fil) > 0:
    filename += "_" + fil
picam2.capture_file(filename + ".jpg")
