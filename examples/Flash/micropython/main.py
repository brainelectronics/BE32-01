#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Interact with the external flash

Format the external flash and create a directory "external" on it.
Show all files in the device root directory and save a file named
"some-file.txt" to the external flash.
Unmount the external flash and show again all files in the device root dir.
Mount the external flash again, show all files in the mounted directory and
print the content of the previously saved file

This main.py file corresponds to the "loop()" function in Arduino.
"""

import machine
import os
import winbond

# set this to false to not format the flash on the next reboot
FIRST_TIME_USAGE = True

# see README.md file of this directory for further description
flash = winbond.W25QFlash(spi=machine.SPI(2),
                          cs=machine.Pin(5),
                          baud=2000000,
                          software_reset=True)

# !!! only required on the very first start (will remove everything)
if FIRST_TIME_USAGE:
    # takes some seconds/minutes!
    flash.format()

    # !!! only required on first setup and after formatting
    os.VfsFat.mkfs(flash)

# mount the external flash as a folder named "external" at the root directory
os.mount(flash, '/external')

# show all files and folders on the boards root directory
os.listdir('/')

# save a file to the external flash
with open('/external/some-file.txt', 'w') as f:
    f.write('Hello World')

# unmount flash
os.umount('/external')

# show all files and folders on the boards root directory
os.listdir('/')
# the "external" folder is no longer available

# mount the external flash again
os.mount(flash, '/external')

# show all files and folders on the external flash
os.listdir('/external')

# save a file to the external flash
with open('/external/some-file.txt', 'r') as f:
    print(f.read())
