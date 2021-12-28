# WS2812 example for the BE32-01

## General

The WS2812 LED is available on pin `IO27` at the BE32-01 board.

## Usage

This example shows how to light up the WS2812 RGB LED in red, green and blue
with one second delay between a color change.

### Arduino

For interaction with the WS2812, the
[Adafruit NeoPixel library][ref-adafruit-lib] is used.

Install this library with the Library Manager in the Arduino IDE. From the
`Sketch` menu select `Include Library` and choose `Manage Libraries...`.
Search for `NeoPixel` and install the `Adafruit NeoPixel by Adafruit` library
with the `Install` button.

Open the [WS2812 sketch][ref-ws2812-sketch] in the Arduino IDE, compile and
upload it to the board as described in the [general README][ref-root-readme]

### Micropython

Copy the [`main.py`][ref-main-py] file to the BE32-01 board with the rshell as
described in the [micropython README][ref-micropython-readme]

To start the WS2812 example running on the BE32-01 perform one of these steps:

 - press `CTRL-D` inside the rshell for a soft reboot
 - press the reset button on the programmer board
 - powercycle the board

For a more advanced usage with e.g. fading, read more on
[brainelectronics micropython modules][ref-brainelectronics-micopython-modules]

<!-- links and other references -->
[ref-adafruit-lib]: https://learn.adafruit.com/adafruit-neopixel-uberguide/arduino-library-installation
[ref-ws2812-sketch]: arduino/WS2812/WS2812.ino
[ref-main-py]: micropython/main.py
[ref-micropython-readme]: ../../README.md
[ref-brainelectronics-micopython-modules]: https://github.com/brainelectronics/micropython-modules
