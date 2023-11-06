import leds


ir_led = leds.Infrared_led(leds.IRLED_PIN)
rgb_led = leds.Rgb_led(leds.NEOPIXEL_PIN, leds.NEOPIXEL_COUNT)


ir_led.off()
rgb_led.off()
