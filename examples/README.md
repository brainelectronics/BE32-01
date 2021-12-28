# BE32-01 examples

Simple Arduino and Micropython examples for the BE32-01 peripherals
---------------

## Contents
- [Installation](#installation)
	- [Arduino](#install-required-package)
	- [Micropython](#install-required-tools)
- [Firmware](#firmware)
	- [Arduino compilation](#compile-arduino-sketch)
	- [Flash Micropython firmware](#flash-micropython-firmware)
- [Upload Code](#upload-code)
	- [Arduino](#upload-code)
	- [Micropython](#upload-code)
		- [Connect to device](#connect-to-device)
		- [Copy files](#copy-files)
		- [REPL](#repl)
- [Further documentation](#further-documentation)

## Installation

These steps guide you through to a fully usable BE32-01 board.

### Arduino
#### Install required package

Arduino IDE must be installed on your system. Further instructions on how to
install the Arduino IDE can be found at
[Getting Started with Arduino][ref-getting-started-arduino]

As the ESP32 package is not part of the Arduino IDE by default, add the
following URL to the additional packages menu inside the settings.

	https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json

Multiple packages can be separated with commas.

Open `Boards Manager` from the `Tools` menu, select `Board menu` and install
the freshly added `esp32` platform.

### Micropython
#### Install required tools

Python3 must be installed on your system. Further instructions on how to
install Python3 can be found at
[Getting Started with Python][ref-getting-started-python]

Start by checking the currently installed Python version with the following
command from a console/cmd

```bash
python --version
python3 --version
```

Depending on which command `Python 3.x.y` (with x.y as some numbers) is
returned, use that command to proceed. In the onwards used example `python3`
is used.

Create a [virtual environment][ref-virtual-env] to avoid side effects with the
installed packages and other python installations on your computer

```bash
python3 -m venv .venv

# on Linux or Apple systems
source .venv/bin/activate

# on Windows systems
.venv\Scripts\activate.bat

python3 -m pip install -r requirements.txt
```

## Firmware
### Compile Arduino sketch

Select the following options from the `Tools` menu in order to compile the
code for the BE32-01

| Option Name      | Option Value              |
|------------------|---------------------------|
| Board            | `ESP32 Pico Kit`          |
| Upload Speed     | `921600`                  |
| Partition Scheme | `Standard`                |
| Code Debug Level | `None`                    |
| Port             | `/dev/tty.SLAB_USBtoUART` |

Depending on your system the port might be `COMx` on Windows or
`/dev/tty.SLAB_USBtoUART` on Linux or Apple machines.

Continue reading on the [`simple LED`][ref-led-example] example.

### Flash Micropython firmware

Depending on the available RAM of the BE32-01 board either the
[firmware *without* external RAM][ref-firmware-without-ram] or the
[firmware *with* external RAM][ref-firmware-without-ram] can be used. Boards
with additional external RAM can use the firmware for boards without additional
RAM but not vice versa.

To flash the mentioned [micropython firmware][ref-micropython-download]
as described on the micropython firmware download page, use the `esptool.py`
to erase the flash before flashing the firmware.

Depending on your system the port might be `COMx` on Windows or
`/dev/tty.SLAB_USBtoUART` on Linux or Apple machines.

May you also need to adjust the name of the downloaded micropython firmware.

```bash
esptool.py --chip esp32 --port /dev/tty.SLAB_USBtoUART erase_flash
esptool.py --chip esp32 --port /dev/tty.SLAB_USBtoUART --baud 921600 write_flash -z 0x1000 esp32-20210623-v1.16.bin
```

## Upload Code
### Arduino

Click the upload button or select from `Sketch` menu `Upload`

### Micropython
#### Connect to device

Open a [micropython remote shell][ref-rshell] with the following command.

*Remember: Depending on your system the port might be `COMx` on Windows or
`/dev/tty.SLAB_USBtoUART` on Linux or Apple machines.*

```bash
rshell --port /dev/tty.SLAB_USBtoUART
```

#### Copy files

This step is optional. Micropython is also usable via the `REPL`, see next
section.

The BE32-01 file directory is available as `/pyboard`. To copy e.g. a `main.py`
file use the following command inside the currently open rshell

```bash
cp LED/micropython/main.py /pyboard/main.py
```

Continue reading on the [`simple LED`][ref-led-example] example.

#### REPL

The REPL (Read Evaluate Print Loop) can be opened after connecting to the
device and calling this command inside the rshell

```bash
repl
```

To print a simple `Hello World` paste this to the REPL in the same way as it
is done in a Python terminal.

```python
print('Hello World')
```

## Further documentation

As the BE32-01 is based on a ESP32, the
[official Arduino quick reference][ref-arduino-quickref] or
[official micropython quick reference][ref-micropython-quickref] can be used
for further testing and usage.

 <!-- links and other references -->
[ref-getting-started-arduino]: https://www.arduino.cc/en/Guide
[ref-getting-started-python]: https://www.python.org/about/gettingstarted/
[ref-virtual-env]: https://docs.python.org/3/tutorial/venv.html
[ref-led-example]: LED/README.md
[ref-firmware-without-ram]: https://micropython.org/download/esp32/
[ref-firmware-with-ext-ram]: https://micropython.org/download/esp32spiram/
[ref-micropython-download]: https://micropython.org/download/
[ref-rshell]: https://github.com/dhylands/rshell
[ref-arduino-quickref]: https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html
[ref-micropython-quickref]: https://docs.micropython.org/en/latest/esp32/quickref.html
