# Onboard LED example for the BE32-01

## General

The onboard LED is available on pin `IO4` at the BE32-01 board.

## Usage

This example shows how to let the onboard LED blink in an endless loop.

### Arduino

Open the [onboard LED sketch][ref-onboard-led-sketch] in the Arduino IDE,
compile and upload it to the board as described in the
[example folder README][ref-example-readme]

### Micropython

Copy the [`main.py`][ref-main-py] file to the BE32-01 board with the rshell as
described in the [example folder README][ref-example-readme]

To start the blink example running on the BE32-01 perform one of these steps:

 - press `CTRL-D` inside the rshell for a soft reboot
 - press the reset button on the programmer board
 - powercycle the board

For a more advanced usage with e.g. non blocking blinking, read more on
[brainelectronics micropython modules][ref-brainelectronics-micopython-modules]

<!-- links and other references -->
[ref-onboard-led-sketch]: arduino/Onboard-LED/Onboard-LED.ino
[ref-example-readme]: ../README.md
[ref-main-py]: micropython/main.py
[ref-brainelectronics-micopython-modules]: https://github.com/brainelectronics/micropython-modules
