"""
Let's see if display image uses some more efficient hardware built-in than looping.

Same speed it seems.
"""
from microbit import *
imax = pow(2, 25)
i = 0
while i < imax:
    dig = 1
    img = Image()
    for x in range(5):
        for y in range(5):
            if dig & i:
                val = 9
            else:
                val = 0
            img.set_pixel(x, y, val)
            dig <<= 1
    display.show(img)
    i += 1
