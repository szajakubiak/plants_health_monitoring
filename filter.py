from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Device, Servo
from time import sleep

factory = PiGPIOFactory()

pwm_gpio=17

servo = Servo(pwm_gpio, pin_factory=factory)

def on():
    servo.min()

def off():
    servo.max()

if __name__ == "__main__":
    while True:
        on()
        print("filter on")
        sleep(2)
        off()
        print("filter off")
        sleep(2)
