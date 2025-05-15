from machine import Pin, PWM
from neopixel import NeoPixel
from time import sleep
import random

led_button_pin = Pin(17, Pin.OUT)

led_button_pin.value(1023)

led_pin = Pin(5)
led_amount = 35
leds = NeoPixel(led_pin, led_amount)

button_pin = Pin(11, Pin.IN, Pin.PULL_UP)
reed_pin = Pin(13, Pin.IN, Pin.PULL_DOWN)

buzzer_pin = Pin(4)
buzzer_pwm = PWM(buzzer_pin)
buzzer_pwm.freq(1000)
buzzer_pwm.duty(0)

#leiddi hjól velur númer og hvaða ljós á að kveikja
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
        leds[i] = (150, 0, 0)

    leds.write()


while True:
    if button_pin.value() == 0:
        for i in range(20):
            leds.fill((0, 0, 0))
            r = random.randint(0, 34)
            leds[r] = (0, 150, 0)
            leds.write()
            sleep(0.05)
            


        result = random.randint(1, 6)
        show_number(result)
        sleep(0.5)
        print(result)
#hljóðmerki virkjar þegar reyrinn virkjar
    if reed_pin.value() == 1:
        buzzer_pwm.duty(1000)
        sleep(1)
        buzzer_pwm.duty(0)
        sleep(1)
        buzzer_pwm.duty(1000)
        sleep(1)
        buzzer_pwm.duty(0)
        sleep(1)
        print("active")
