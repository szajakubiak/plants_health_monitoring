from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Device, Servo
from time import sleep

# Servo positions for visible light filter states
FILTER_ON_POS = -0.95
FILTER_OFF_POS = 0.8

factory = PiGPIOFactory()

servo_gpio=17

servo = Servo(servo_gpio, pin_factory=factory)

def on():
    servo.value = FILTER_ON_POS

def off():
    servo.value = FILTER_OFF_POS

if __name__ == "__main__":
    while True:
        on()
        print("filter on")
        sleep(2)
        off()
        print("filter off")
        sleep(2)
