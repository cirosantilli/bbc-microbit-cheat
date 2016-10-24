"""
Compare all 10 possible intensities.
"""
from microbit import *
for x in range(5):
    for y in range(5):
        display.set_pixel(x, y, (5 * x + y) % 10)
