from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Device, DigitalOutputDevice, Servo
from time import sleep

# Servo positions for visible light filter states
FILTER_ON_POS = -0.95
FILTER_OFF_POS = 0.8
SERVO_PIN = 17
IRCUT_PIN = 27
IRLED_PIN = 22


factory = PiGPIOFactory()


class Filter_visible:
    def __init__(self, pin):
        self.pin = pin
        self.servo = Servo(self.pin, pin_factory=factory)
    
    def on(self):
        self.servo.value = FILTER_ON_POS

    def off(self):
        self.servo.value = FILTER_OFF_POS


class Filter_infrared:
    def __init__(self, pin):
        self.pin = pin
        self.output = DigitalOutputDevice(self.pin, pin_factory=factory)
    
    def on(self):
        self.output.off()

    def off(self):
        self.output.on()


class Infrared_led:
    def __init__(self, pin):
        self.pin = pin
        self.output = DigitalOutputDevice(self.pin, pin_factory=factory)
    
    def on(self):
        self.output.on()

    def off(self):
        self.output.off()


if __name__ == "__main__":
    vis_fil = Filter_visible(SERVO_PIN)
    ir_fil = Filter_infrared(IRCUT_PIN)
    ir_led = Infrared_led(IRLED_PIN)
    vis_fil.off()
    ir_fil.off()
    ir_led.off()
    while True:
        vis_fil.on()
        #print("Visible light filter on")
        sleep(2)
        vis_fil.off()
        #print("Visible light filter off")
        sleep(2)
        ir_fil.on()
        #print("Infrared light filter on")
        sleep(2)
        ir_fil.off()
        #print("Infrared light filter off")
        sleep(2)
