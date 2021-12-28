#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Print debug data via the programmer boards USB port and other content on the
4x2 pinheader repeatedly every second.

This main.py file corresponds to the "loop()" function in Arduino.
"""

from machine import UART
import time

print('Setting up the alternative UART on D25 (TX) and D26 (RX)')
uart1 = UART(1, baudrate=115200, tx=25, rx=26)

while True:
    # print current timestamp via programmer board on USB C
    print('Debug message on programmer USB at {}'.format(time.ticks_ms()))

    # print "Hello World" on the 4x2 pinheader TX pin
    uart1.write('Hello World from 4x2 pinheader at {}'.format(time.ticks_ms()))

    # wait for a second
    time.sleep_ms(1000)
