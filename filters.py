from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Device, Servo
from time import sleep

# Servo positions for visible light filter states
FILTER_ON_POS = -0.95
FILTER_OFF_POS = 0.8
SERVO_PIN = 17

factory = PiGPIOFactory()


class Filter_visible:
    def __init__(self, pin):
        self.pin = pin
        self.servo = Servo(SERVO_PIN, pin_factory=factory)
    
    def on(self):
        self.servo.value = FILTER_ON_POS

    def off(self):
        self.servo.value = FILTER_OFF_POS


if __name__ == "__main__":
    vis_fil = Filter_visible(SERVO_PIN)
    while True:
        vis_fil.on()
        print("Visible light filter on")
        sleep(2)
        vis_fil.off()
        print("Visible light filter off")
        sleep(2)
