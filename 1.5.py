# Wat is het decimale getal dat door de
# volgende binaire waarde wordt
# weergegeven: 0b10101011

# 1*1 = 1
# 1*2 = 2
# 0*4 = 0
# 1*8 = 8
# 0*16 = 0
# 1*32 = 32
# 0*64 = 0
# 1*128 = 128

# 128 + 32 + 8 + 2 + 1 = 171

from machine import Pin
import time

led_pins = [
    Pin(0, Pin.OUT),
    Pin(1, Pin.OUT),
    Pin(2, Pin.OUT),
    Pin(3, Pin.OUT),
    Pin(4, Pin.OUT)
]


def leds(value, delay):
    for led in led_pins:
        if value % 2 == 1:
            led.value(1)
        else:
            led.value(0)
        value = value // 2
    time.sleep(delay)


delay = 0.2
while True:
    leds(1, delay)
    leds(2, delay)
    leds(4, delay)
    leds(8, delay)
    leds(16, delay)
    leds(16, delay)
    leds(8, delay)
    leds(4, delay)
    leds(2, delay)
    leds(1, delay)
