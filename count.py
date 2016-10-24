"""
Count in binary with the LEDs.

Takes a very long time to complete.

So speed must be LED limited: CPU is 16MHz,
and we are cycling 2^25 = 32M values,
let's say at 100 operations per cycle.

CPU chip becomes worryingly, put your hand on it to feel.
"""
from microbit import *
imax = pow(2, 25)
i = 0
while i < imax:
    dig = 1
    for x in range(5):
        for y in range(5):
            if dig & i:
                val = 9
            else:
                val = 0
            display.set_pixel(x, y, val)
            dig <<= 1
    i += 1
