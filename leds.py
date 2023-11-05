from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import DigitalOutputDevice


IRLED_PIN = 22


factory = PiGPIOFactory()


class Infrared_led:
    def __init__(self, pin):
        self.pin = pin
        self.output = DigitalOutputDevice(self.pin, pin_factory=factory)

    def on(self):
        self.output.on()

    def off(self):
        self.output.off()


if __name__ == "__main__":
    ir_led = Infrared_led(IRLED_PIN)
    ir_led.off()
    while True:
        ir_led.on()
        # print("Infrared LED on")
        sleep(2)
        ir_led.off()
        # print("Infrared LED off")
        sleep(2)
