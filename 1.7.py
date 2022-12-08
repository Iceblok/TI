import machine
from machine import Pin
import time

led_pins = [
    Pin(0, Pin.OUT),
    Pin(1, Pin.OUT),
    Pin(2, Pin.OUT),
    Pin(3, Pin.OUT),
    Pin(4, Pin.OUT)
]

echo_us = 500 * 2 * 30
trigger_pin = Pin(14, Pin.OUT)
echo_pin = Pin(15, Pin.IN)


def measure_distance():
    trigger_pin.value(0)
    time.sleep_us(5)
    trigger_pin.value(1)
    time.sleep_us(10)
    trigger_pin.value(0)

    tijd = machine.time_pulse_us(echo_pin, 1, echo_us)

    dist = (tijd / 2) / 29.1
    return dist


def display_distance(distance):
    if distance < 10:
        led_pins[0].value(1)
    elif distance < 15:
        led_pins[1].value(1)
    elif distance < 20:
        led_pins[2].value(1)
    elif distance < 25:
        led_pins[3].value(1)
    elif distance <= 30:
        led_pins[4].value(1)
    elif distance > 30:
        for led in led_pins:
            led.value(0)
    time.sleep(0.5)


while True:
    distance = measure_distance()
    display_distance(distance)
    time.sleep_ms(100)

