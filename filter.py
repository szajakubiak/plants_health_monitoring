from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Device, Servo
from time import sleep

factory = PiGPIOFactory()

servo_gpio=17

servo = Servo(servo_gpio, pin_factory=factory)

def on():
    servo.value = -0.95

def off():
    servo.value = 0.8

if __name__ == "__main__":
    while True:
        on()
        print("filter on")
        sleep(2)
        off()
        print("filter off")
        sleep(2)
