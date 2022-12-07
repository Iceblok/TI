from machine import ADC, PWM, Pin
import time

# led = PWM(Pin(20))
# led.freq(1000)
#
# adc = ADC(Pin(26))
#
#
# def led_brightness(value):
#     """
#         Zet de led intensiteit.
#         Waarde tussen de 0 en 65535
#     """
#
#     led.duty_u16(65535-value)
#
#
# while True:
#     adc_value = adc.read_u16()
#     led_brightness(adc_value)
#     time.sleep(0.01)


from machine import ADC, PWM, Pin
import time

led = PWM(Pin(20))
led.freq(1000)

adc = ADC(Pin(26))

gpio_pin = Pin(20, Pin.OUT)


def pulse(pin, high_time, low_time):
    pin.value(1)
    time.sleep(high_time)
    pin.value(0)
    time.sleep(low_time)


while True:
    adc_value = adc.read_u16()
    pulse(gpio_pin, adc_value / 65535, adc_value / 65535)




