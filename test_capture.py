import argparse
from picamera2 import Picamera2, Preview
from time import sleep
from datetime import datetime
import leds
import filters
from time import sleep


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


led_rgb = leds.Rgb_led(leds.NEOPIXEL_PIN, leds.NEOPIXEL_COUNT)
led_ir = leds.Infrared_led(leds.IRLED_PIN)


fil_ir = filters.Filter_infrared(filters.IRCUT_PIN)
fil_vis = filters.Filter_visible(filters.SERVO_PIN)


led_rgb.off()
led_ir.off()
if "r" in lig:
    led_rgb.red_on()
if "g" in lig:
    led_rgb.green_on()
if "b" in lig:
    led_rgb.blue_on()
if "i" in lig:
    led_ir.on()


fil_ir.off()
fil_vis.off()
if "i" in fil:
    fil_ir.on()
if "v" in fil:
    fil_vis.on()


sleep(1)


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
