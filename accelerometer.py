"""
Show an acceleration on screen in binary.

Range seems to be -1024 to 1023.

Press A and B to cycle between X, Y and Z accelerations.
"""

from microbit import *

def show_binary(i):
    dig = 1
    img = Image(5, 5)
    for y in range(5):
        for x in range(5):
            if dig & i:
                val = 9
            else:
                val = 0
            img.set_pixel(x, y, val)
            dig <<= 1
    display.show(img)

mode = 0
mode_change = True
while True:

    # Update mode.
    if button_a.was_pressed():
        mode -= 1
        mode_change = True
    if button_b.was_pressed():
        mode += 1
        mode_change = True
    if mode_change:
        mode %= 3
        if mode == 0:
            val = 'x'
        elif mode == 1:
            val = 'y'
        else:
            val = 'z'
        display.show(val)
        sleep(1000)

    # Decide and show value.
    if mode == 0:
        val = accelerometer.get_x()
    elif mode == 1:
        val = accelerometer.get_y()
    else:
        val = accelerometer.get_z()
    show_binary(val)

    mode_change = False
