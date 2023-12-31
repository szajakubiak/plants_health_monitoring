from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import DigitalOutputDevice, Servo


# Servo positions for visible light filter states
FILTER_ON_POS = -0.95
FILTER_OFF_POS = 0.8


factory = PiGPIOFactory()


class Filter_visible:
    def __init__(self, pin=17):
        self.pin = pin
        self.servo = Servo(self.pin, pin_factory=factory)

    def on(self):
        self.servo.value = FILTER_ON_POS

    def off(self):
        self.servo.value = FILTER_OFF_POS


class Filter_infrared:
    def __init__(self, pin=27):
        self.pin = pin
        self.output = DigitalOutputDevice(self.pin, pin_factory=factory)

    def on(self):
        self.output.off()

    def off(self):
        self.output.on()


if __name__ == "__main__":
    from time import sleep

    vis_fil = Filter_visible()
    ir_fil = Filter_infrared()
    vis_fil.off()
    ir_fil.off()
    while True:
        vis_fil.on()
        # print("Visible light filter on")
        sleep(2)
        vis_fil.off()
        # print("Visible light filter off")
        sleep(2)
        ir_fil.on()
        # print("Infrared light filter on")
        sleep(2)
        ir_fil.off()
        # print("Infrared light filter off")
        sleep(2)
