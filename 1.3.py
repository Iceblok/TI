from machine import Pin
import time

# gpio_pin = Pin(20, Pin.OUT)
#
# while True:
#     gpio_pin.value(1)
#     time.sleep(0.5)
#     gpio_pin.value(0)
#     time.sleep(0.5)
#
#
# gpio_pin = Pin(20, Pin.OUT)
#
# # 1.3 LED
# def pulse(pin, high_time, low_time):
#     pin.value(1)
#     time.sleep(high_time)
#     pin.value(0)
#     time.sleep(low_time)
#
#
#
# while True:
#     pulse(gpio_pin, 0.2, 0.2)
#     pulse(gpio_pin, 0.2, 0.2)
#     pulse(gpio_pin, 0.2, 0.2)
#     pulse(gpio_pin, 0.2, 3)


# gpio_pin = Pin(20, Pin.OUT)
#
#
# def pulse(pin, high_time, low_time):
#     pin.value(1)
#     time.sleep(high_time)
#     pin.value(0)
#     time.sleep(low_time)
#
#
# def morse(pin, delay, text):  # .--. --. --.. -.-
#     for i in text:
#         if i == '.':
#             pulse(pin, delay, delay)
#         elif i == '-':
#             pulse(pin, delay * 3, delay)
#         elif i == ' ':
#             time.sleep(delay * 7)
#
#
# morse(gpio_pin, 0.2, ".--. -.-- - .... --- -.")
#

# 1.3 vervolg
led_pin = Pin(20, Pin.OUT)
switch_pin = Pin(19, Pin.IN, pull=Pin.PULL_DOWN)
switch_pin1 = Pin(18, Pin.IN, pull=Pin.PULL_DOWN)


while True:
    if switch_pin.value():
        led_pin.value(1)
    if switch_pin1.value():
        led_pin.value(0)







