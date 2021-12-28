#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Let the onboard LED blink in an endless loop

This main.py file corresponds to the "loop()" function in Arduino.
"""

from machine import Pin
import time

# initialize pin IO4 as an output
led_pin = Pin(4, Pin.OUT)

while True:
    # turn the LED on
    led_pin.value(0)
    # wait for a second
    time.sleep_ms(1000)
    # turn the LED off
    led_pin.value(1)
    # wait for a second
    time.sleep_ms(1000)
