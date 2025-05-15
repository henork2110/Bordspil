# ---------------------------------------------
# Rafrænt borðspil með ESP32 og MicroPython
# Leikmaður ýtir á takka til að kasta teningi.
# LED hringur sýnir niðurstöðu (1-6).
# Ef leikmaður lendir á sérstökum reit með segli
# skynjar reed switch það og spilar hljóð.
# ---------------------------------------------

from machine import Pin, PWM
from neopixel import NeoPixel
from time import sleep
import random

# LED hringur (35 LED)
led_pin = Pin(5)
led_amount = 24
leds = NeoPixel(led_pin, led_amount)

# Teningakast takki
button_pin = Pin(11, Pin.IN, Pin.PULL_UP)

# Reed switch til að skynja sérstakan reit
reed_pin = Pin(13, Pin.IN, Pin.PULL_DOWN)

# Buzzer/hátalari
buzzer_pin = Pin(4)
buzzer_pwm = PWM(buzzer_pin)
buzzer_pwm.freq(10)
buzzer_pwm.duty(0)

# Birta teningatölu með rauðum ljósum á hringnum
def show_number(n):
    leds.fill((0, 0, 0))

    if n == 1:
        leds_range = range(0, 4)
    elif n == 2:
        leds_range = range(4, 8)
    elif n == 3:
        leds_range = range(8, 12)
    elif n == 4:
        leds_range = range(12, 16)
    elif n == 5:
        leds_range = range(16, 20)
    elif n == 6:
        leds_range = range(20, 24)
    else:
        leds_range = []

    for i in leds_range:
        leds[i] = (255, 0, 0)

    leds.write()

# Aðal lykkja
while True:
    # Teningakast með takka
    if button_pin.value() == 0:
        for i in range(20):
            leds.fill((0, 0, 0))
            r = random.randint(0, 23)
            leds[r] = (0, 255, 0)
            leds.write()
            sleep(0.05)

        result = random.randint(1, 6)
        show_number(result)
        sleep(0.5)

    # Ef reed switch virkjast, spila hljóð
    if reed_pin.value() == 1:
        buzzer_pwm.duty(1000)
        sleep(0.1)
        buzzer_pwm.duty(0)
        sleep(1)
