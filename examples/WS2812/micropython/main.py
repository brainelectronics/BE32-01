#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Let the WS2812 RGB LED light up in red, green and blue with one second delay

This main.py file corresponds to the "loop()" function in Arduino.
"""

from machine import Pin
import neopixel
import time

# initialize pin IO27 as an output
neopixel_pin = Pin(27, Pin.OUT)

# create a pixel instance on the configured neopixel pin
pixel = neopixel.NeoPixel(pin=neopixel_pin, n=1)

while True:
    # turn the RGB LED at index 0 red with 10/255 intensity
    pixel[0] = (10, 0, 0)
    pixel.write()

    # wait for a second
    time.sleep_ms(1000)

    # turn the RGB LED at index 0 green with 10/255 intensity
    pixel[0] = (0, 10, 0)
    pixel.write()

    # wait for a second
    time.sleep_ms(1000)

    # turn the RGB LED at index 0 blue with 10/255 intensity
    pixel[0] = (0, 0, 10)
    pixel.write()

    # wait for a second
    time.sleep_ms(1000)
