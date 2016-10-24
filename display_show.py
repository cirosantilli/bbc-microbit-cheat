"""
Print string to display on character at a time.

Calls block until the next one comes.
"""
from microbit import *
while True:
    display.show('ab')
    display.show('cd')
