import argparse
from picamera2 import Picamera2
from time import sleep
from datetime import datetime
import leds
import filters
from time import sleep


parser = argparse.ArgumentParser()
parser.add_argument("-l", "--lights", help="lights to use", type=str, default="")
parser.add_argument("-f", "--filters", help="filters to use", type=str, default="")
parser.add_argument("-e", "--extension", help="output file extension", type=str, default="jpg")
args = parser.parse_args()
lig = args.lights
fil = args.filters
ext = args.extension


def get_timestamp():
    """Return the current timestamp as a string."""
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%dT%H-%M-%S")
    return timestamp


# Create LED objects
led_rgb = leds.Rgbw_led()
led_ir = leds.Infrared_led()


# Create filter objects
fil_ir = filters.Filter_infrared()
fil_vis = filters.Filter_visible()


# Set LEDs according to passed parameters
led_rgb.off()
led_ir.off()
if "r" in lig:
    led_rgb.red_on()
if "g" in lig:
    led_rgb.green_on()
if "b" in lig:
    led_rgb.blue_on()
if "w" in lig:
    led_rgb.white_on()
if "i" in lig:
    led_ir.on()


# Set filters according to passed parameters
fil_ir.off()
fil_vis.off()
if "i" in fil:
    fil_ir.on()
if "v" in fil:
    fil_vis.on()


sleep(1)


# Create the name of the output file
timestamp = get_timestamp()
filename = timestamp
if len(lig) > 0:
    filename += "_" + lig
if len(fil) > 0:
    filename += "_" + fil


# Capture image
picam2 = Picamera2()
capture_config = picam2.create_still_configuration()
picam2.start(show_preview=False)
sleep(1)
picam2.switch_mode_and_capture_file(capture_config, filename + "." + ext)


# Set camera to normal mode
sleep(1)
led_rgb.off()
led_ir.off()
fil_ir.on()
fil_vis.off()
