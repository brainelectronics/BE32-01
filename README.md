# BE32-01

An ESP32 Pico D4 based replacement for the ESP01 (ESP8266) with a bunch of
improvements
---------------

## General

The BE32-01 is a ESP32 D4 Pico board in the well known ESP01 (ESP8266) form
factor.

The main improvements can be shortly summarized as

 - additional external 4MB RAM
 - [additional external 16MB Flash](#external-flash)
 - [WS2812 RGB LED](#ws2812)
 - ceramic antenna and u.FL connector
 - onboard break-away programmer with USB C port
 - [JTAG debug connector](#jtag-debug)
 - [selectable UART pins](#uart)

## Peripherals

### GPIO pins

As long as no JTAG debugger is used and the programmer board is not broken of,
the GPIO pins `IO12`, `IO13`, `IO14`, `IO15` can be freely used for any
purpose by the user.

### Onboard LED

The BE32-01 is equipped with a blue LED on pin `IO4` in the same way as the
ESP01 (ESP8266).

The LED is connected from 3.3V to `IO4`, which requires to set the pin `LOW`
in order to turn the LED on and `HIGH` to turn the LED off.

For further details check the [onboard led example][ref-onboard-led-example].

### UART

The BE32-01 can use the default UART on the 4x2 pinheader for communication
and programming purposes in the same way the ESP01 (ESP8266) does.

Additionally the pins `IO25` and `IO26` can be used as alternative RX and TX
pins. This is especially usefull as long as the programming board is not
broken off. The communication with the programmer can be kept as default UART
while additional communication can be done with another device on a second
UART.

For further details check the [UART example][ref-uart-example].

### WS2812

For improved user feedback a WS2812 RGB LED is available on pin `IO27` at the
BE32-01 board.

For further details check the [WS2812 example][ref-ws2812-example].

### External Flash

The additional external flash (if equipped) can be used to store further data,
but not executable application code.

For further details check the
[external flash example][ref-external-flash-example].

## JTAG Debug

The BE32-01 is equipped with a 1x9 pinheader row on the programmer break-away
board. This header contains JTAG debug pins among others which can be used in
the same way as the black DC3 connectors.

### Connections

Connect the JTAG debugger as shown below with the 1x9 pinheader or use the two
DC3 connectors.

As the USB C port points to you, the pinout of the 1x9 pinheader from left to
right is as follows

	IO0:  RST/EN, JTAG Reset
	IO14: JTAG TMS
	IO12: JTAG TDI
	IO13: JTAG TCK
	IO15: JTAG TDO
	GND:  Ground
	RX:   RX pin of ESP32
	TX:   TX pin of ESP32
	3V3:  3.3V, JTAG VTref

Some JTAG debuggers use a 2x10 connector with the pinout shown below.

                 _____
    VTref 3.3V  |     | NC
    nTRST EN    |     | GND
    TDI   IO12  |     | NC
    TMS   IO14  |     | NC
    TCK   IO13 ||     | NC
    NC         ||     | NC
    TDO   IO15  |     | NC
    RESET NC    |     | NC
    NC          |     | NC
    5V          |     | NC
                 ------

As marked on the back of the programmer PCB, the 2x5 DC3 connector is the JTAG,
the 2x3 DC3 connector the Programmer connector which can be used with e.g. the
[ESP Prog Board][ref-esp-prog-board].

### Usage

In order to debug an Arduino sketch ...

<!-- links and other references -->
[ref-onboard-led-example]: examples/LED/README.md
[ref-uart-example]: examples/UART/README.md
[ref-ws2812-example]: examples/WS2812/README.md
[ref-external-flash-example]: examples/Flash/README.md

[ref-esp-prog-board]: https://docs.espressif.com/projects/espressif-esp-iot-solution/en/latest/hw-reference/ESP-Prog_guide.html
