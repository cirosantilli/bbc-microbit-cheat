"""
Check if either button is pressed.

Shows:

- 0 if no button is pressed
- 1 if A is pressed
- 2 if B is pressed
- 3 if A and B are pressed
"""
from microbit import *
while True:
    val = 0
    if button_a.is_pressed():
        val += 1
    if button_b.is_pressed():
        val += 2
    display.show(str(val))
