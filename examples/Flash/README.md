# External flash example for the BE32-01

## General

The external flash is connected through the VSPI bus at the BE32-01 board.

| Pin name | Pin on ESP32 | Comment |
|----------|--------------|---------|
| SCK      | IO18         | fixed   |
| MOSI     | IO23         | fixed   |
| MISO     | IO19         | fixed   |
| CS       | IO5          | free, fixed on BE32-01 to IO5 |

As the `W25Qxxx` chips in SOIC8 format do not offer a reset pin, a software
reset sequence is used.

## Usage

This example shows how to mount the external flash, place a file on the
chip, unmount the external flash, re-mount it again and print the content of
the previously saved file on the external flash.

### Arduino

Open the [Flash sketch][ref-flash-sketch] in the Arduino IDE, compile and
upload it to the board as described in the
[example folder README][ref-example-readme]

### Micropython

Copy the [`main.py`][ref-main-py] as well as the [`winbond.py`][ref-winbond-py]
files to the BE32-01 board with the rshell as described in the
[example folder README][ref-example-readme]

To start the flash example running on the BE32-01 perform one of these steps:

 - press `CTRL-D` inside the rshell for a soft reboot
 - press the reset button on the programmer board
 - powercycle the board

May find more advanced usage on
[brainelectronics micropython modules][ref-brainelectronics-micopython-modules]

<!-- links and other references -->
[ref-flash-sketch]: arduino/Flash/Flash.ino
[ref-main-py]: micropython/main.py
[ref-winbond-py]: micropython/winbond.py
[ref-example-readme]: ../README.md
[ref-brainelectronics-micopython-modules]: https://github.com/brainelectronics/micropython-modules

