import argparse
from picamera2 import Picamera2, Preview
from time import sleep
from datetime import datetime
import leds
import filters
from time import sleep


parser = argparse.ArgumentParser()
parser.add_argument("-l", "--lights", help="lights to use", type=str, default="")
parser.add_argument("-f", "--filters", help="filters to use", type=str, default="")
args = parser.parse_args()
lig = args.lights
fil = args.filters


def get_timestamp():
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%dT%H-%M-%S")
    return timestamp


led_rgb = leds.Rgbw_led(leds.NEOPIXEL_PIN, leds.NEOPIXEL_COUNT)
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
if "w" in lig:
    led_rgb.white_on()
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
filename = timestamp
if len(lig) > 0:
    filename += "_" + lig
if len(fil) > 0:
    filename += "_" + fil


picam2 = Picamera2()
capture_config = picam2.create_still_configuration()
picam2 = picam2.configure(capture_config)
picam2.start(show_preview=False)
sleep(1)
picam2.capture_file(filename + ".jpg")


sleep(1)
led_rgb.off()
led_ir.off()
fil_ir.on()
fil_vis.off()
