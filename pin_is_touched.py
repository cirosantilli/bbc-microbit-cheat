"""
Check which electric connector pins are touched.

You must also touch the GND pin at the same time to see anything.
"""
from microbit import *
while True:
    val = 0
    if pin0.is_touched():
        val += 1
    if pin1.is_touched():
        val += 2
    if pin2.is_touched():
        val += 4
    display.show(str(val))
