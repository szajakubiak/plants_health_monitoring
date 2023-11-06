from leds import Infrared_led, Rgb_led


IRLED_PIN = 22
NEOPIXEL_PIN = board.D18
NEOPIXEL_COUNT = 8


ir_led = Infrared_led(IRLED_PIN)
rgb_led = Rgb_led(NEOPIXEL_PIN, NEOPIXEL_COUNT)


ir_led.off()
rgb_led.off()
