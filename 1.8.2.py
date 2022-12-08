import time

import machine
import neopixel

np = neopixel.NeoPixel(machine.Pin(13), 8)

while True:
    time.sleep(1)
    np[0] = [255, 0, 0]
    np.write()
    time.sleep(1)
    np[1] = [255, 0, 0]
    np.write()
    time.sleep(1)
    np[2] = [255, 0, 0]
    np.write()
    time.sleep(1)
    np[3] = [255, 0, 0]
    np.write()
    time.sleep(1)
    np[4] = [255, 0, 0]
    np.write()
    time.sleep(1)
    np[5] = [255, 0, 0]
    np.write()
    time.sleep(1)
    np[6] = [255, 0, 0]
    np.write()
    time.sleep(1)
    np[7] = [255, 0, 0]
    np.write()
    time.sleep(1)
    np[0] = [0, 255, 0]
    np[1] = [0, 255, 0]
    np[2] = [0, 255, 0]
    np[3] = [0, 255, 0]
    np[4] = [0, 255, 0]
    np[5] = [0, 255, 0]
    np[6] = [0, 255, 0]
    np[7] = [0, 255, 0]
    np.write()

    time.sleep(1)

