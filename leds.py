from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import DigitalOutputDevice
import board
import neopixel


IRLED_PIN = 22
NEOPIXEL_PIN = board.D18
NEOPIXEL_COUNT = 8


factory = PiGPIOFactory()


class Infrared_led:
    def __init__(self, pin):
        self.pin = pin
        self.output = DigitalOutputDevice(self.pin, pin_factory=factory)

    def on(self):
        self.output.on()

    def off(self):
        self.output.off()


class Rgb_led:
    def __init__(self, pin, length):
        self.strip = neopixel.NeoPixel(pin, length)
        self.length = length
        self.red = 0
        self.green = 0
        self.blue = 0
    
    def set(self):
        for led in range(self.length):
            self.strip[led] = (self.red, self.green, self.blue)

    def on(self):
        self.red = 255
        self.green = 255
        self.blue = 255
        self.set()

    def off(self):
        self.red = 0
        self.green = 0
        self.blue = 0
        self.set()
    
    def red_on(self):
        self.red = 255
        self.set()

    def red_off(self):
        self.red = 0
        self.set()
    
    def green_on(self):
        self.green = 255
        self.set()

    def green_off(self):
        self.green = 0
        self.set()
    
    def blue_on(self):
        self.blue = 255
        self.set()

    def blue_off(self):
        self.blue = 0
        self.set()


if __name__ == "__main__":
    ir_led = Infrared_led(IRLED_PIN)
    rgb_led = Rgb_led(NEOPIXEL_PIN, NEOPIXEL_COUNT)
    ir_led.off()
    rgb_led.off()
    while True:
        ir_led.on()
        # print("Infrared LED on")
        sleep(2)
        ir_led.off()
        # print("Infrared LED off")
        sleep(2)
        rgb_led.on()
        # print("RGB LED on")
        sleep(2)
        rgb_led.off()
        # print("RGB LED off")
        sleep(2)
