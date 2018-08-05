# LED panel client

## Introduction ##

This will be a MicroPython client for the
[MQTT server][ledpanel-server]. It’s going to run on
a [ESP8266 microcomputer using MicroPython][esp8266]. The LED panel will be
composed of daisy-chained [MAX7219 8 × 8 dot matrix LED arrays][max7219].

Currently it is just a playground to see, how to operate the LEDs. It displays a
Space Invader image. The image switches to another when the on-board `FLASH`
button.

## Requirements ##

First, you need a [ESP8266 microcomputer with a MicroPython firmware][esp8266]
and a working serial connection from your computer. See [documentation][esp8266]
for further instructions.

To simplify uploading the files onto the MicroPython board, you may want to use
[Adafruit Ampy][adafruit-ampy], a [Python][python] program to do just that:

* [Python 3][python] with [PIP][pip] – `brew install python`
* [Adafruit Ampy][adafruit-ampy] – install with `pip3 install adafruit-ampy`

The [Adafruit MAX7219 driver library][adafruit-max7219] to make the LED array
control simple is already included.

## Instructions ##

General remark: In all further commands replace `/dev/tty.wchusbserial1420` with
the actual path to your COM device.

### Installation ###

Connect the microcomputer to the macrocomputer.

Put all the necessary files onto the PyBoard:

```
ampy -p /dev/tty.wchusbserial1420 put max7219.py
ampy -p /dev/tty.wchusbserial1420 put main.py
```

### 8 × 8 matrix connection ###

Connect the [MAX7219 dot matrix][max7219] to the microcomputer. The pin pairs
are in the first two columns of the following table:

| MAX7219 | NodeMCU | Pin    | SPI          |
|:--------|:--------|:-------|:-------------|
| VCC     | 3V      |        |              |
| GND     | G       |        |              |
| DIN     | D7      | GPIO13 | HMOSI (mosi) |
| CS      | D8      | GPIO15 | GCS   (cs)   |
| CLK     | D5      | GPIO14 | HSCLK (sck)  |

### Run ###

Reset the microcomputer using the `RST` button on the board. This should load
the `main.py` script.

For debugging, `screen` to the PyBoard’s Python REPL:

```
screen /dev/tty.wchusbserial1420 115200
```

## Credit ##

* [Adafruit industries][adafruit] for the useful libraries
* [Nauč se Python!][naučse] for the MicroPython workshop

Space invaders image found
[somewhere](https://tineye.com/search/a1bb7cf24f90f375d0cb62080ace6b3ad2bed7a7/)
on the interwebz. 


[adafruit]: https://www.adafruit.com/
[adafruit-ampy]: https://github.com/adafruit/ampy
[adafruit-max7219]: https://github.com/adafruit/micropython-adafruit-max7219
[esp8266]: https://docs.micropython.org/en/latest/esp8266/index.html
[ledpanel-server]: https://github.com/Glutexo/ledpanel-server
[max7219]: https://datasheets.maximintegrated.com/en/ds/MAX7219-MAX7221.pdf
[naučse]: https://naucse.python.cz/
[pip]: https://pypi.org/project/pip/
[python]: https://www.python.org/
