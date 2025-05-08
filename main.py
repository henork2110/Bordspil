from machine import Pin, PWM
from neopixel import NeoPixel
from time import sleep
import random

led_pin = Pin(5)
led_amount = 35
leds = NeoPixel(led_pin, led_amount)

button_pin = Pin(11, Pin.IN, Pin.PULL_UP)
reed_pin = Pin(13, Pin.IN, Pin.PULL_DOWN)

buzzer_pin = Pin(4)
buzzer_pwm = PWM(buzzer_pin)
buzzer_pwm.freq(10)
buzzer_pwm.duty(0)

def show_number(n):
    leds.fill((0, 0, 0))

    if n == 1:
        leds_range = range(0, 6)
    elif n == 2:
        leds_range = range(6, 12)
    elif n == 3:
        leds_range = range(12, 18)
    elif n == 4:
        leds_range = range(18, 24)
    elif n == 5:
        leds_range = range(24, 30)
    elif n == 6:
        leds_range = range(30, 35)
    else:
        leds_range = []

    for i in leds_range:
        leds[i] = (255, 0, 0)

    leds.write()


while True:
    if button_pin.value() == 0:
        for i in range(20):
            leds.fill((0, 0, 0))
            r = random.randint(0, 34)
            leds[r] = (0, 255, 0)
            leds.write()
            sleep(0.05)

        result = random.randint(1, 6)
        show_number(result)
        sleep(0.5)

    if reed_pin.value() == 1:
        buzzer_pwm.duty(1000)
        sleep(0.1)
        buzzer_pwm.duty(0)
        sleep(1)
