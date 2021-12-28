# UART example for the BE32-01

## General

The alternative UART pins of the 4x2 pinheader are on `IO25` (TX) and `IO26`
(RX), selectable via the two solder jumpers on the non-component side of the
BE32-01 board.

### Default

In order to output the same content on the programmers USB port as on the 4x2
pinheader, simply place the solder jumpers on the non-component side of the
BE32-01 board to `RX` and `TX`.

### Alternative UART

In order to use the alternative pins `IO25` and `II26` for communcation
purposes on the 4x2 header while communicating with the componter via the
programmers USB port place the solder jumpers on the non-component side of the
BE32-01 board to `25` and `26`.

## Usage

This example shows how to print debug data via the programmer boards USB port
and other content on the 4x2 pinheader repeatedly every second.

### Arduino

Open the [UART sketch][ref-uart-sketch] in the Arduino IDE, compile and
upload it to the board as described in the [general README][ref-root-readme]

### Micropython

Copy the [`main.py`][ref-main-py] file to the BE32-01 board with the rshell as
described in the [micropython README][ref-micropython-readme]

To start the UART example running on the BE32-01 perform one of these steps:

 - press `CTRL-D` inside the rshell for a soft reboot
 - press the reset button on the programmer board
 - powercycle the board

<!-- links and other references -->
[ref-uart-sketch]: arduino/UART/UART.ino
[ref-main-py]: main.py
[ref-micropython-readme]: ../../README.md
