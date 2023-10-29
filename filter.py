from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Device, Servo
from time import sleep

# Servo positions for visible light filter states
FILTER_ON_POS = -0.95
FILTER_OFF_POS = 0.8
SERVO_PIN = 17

factory = PiGPIOFactory()

servo = Servo(SERVO_PIN, pin_factory=factory)

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
