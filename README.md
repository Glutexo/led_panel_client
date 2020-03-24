# LED panel client

## Introduction ##

This will be a [MicroPython][micropython] client for the [MQTT server][ledpanel-server]. It’s going to run on an
[ESP8266][esp8266] or [ESP32](esp32) microcomputer using MicroPython. The LED panel will be composed of daisy-chained
[MAX7219 8 × 8 dot matrix LED arrays][max7219].

Currently it is just a playground to see, how to operate the LEDs. It displays a Space Invader image. The image switches
to another when the on-board `FLASH` button.

## Requirements ##

First, you need an [ESP8266][esp8266] or [ESP32](esp32) microcomputer with a MicroPython firmware and a working serial
connection from your computer. See the documentation for further instructions.

(Where to get a working USB to Serial driver? Seriously, I don’t know. I found one when I needed it and forgot which one
was that. Sorry. 😞 Please let me know if you find and test one.)

Then, you need [Python 3][python] with [PIP][pip]. Install using `brew install python`.

To connect to the [MicroPython’s][micropython] REPL, you need [picocom]. Install using `brew install picocom`.

## Instructions ##

General remark: In all further commands replace `/dev/tty.wchusbserial1420` with the actual path to your COM device.

### Installation ###

Install this package and its dependencies using [setuptools]:

```
$ pip install --process-dependency-links --editable .
```

Connect the microcomputer to the macrocomputer.

Put all the necessary files onto the PyBoard using this package’s command:

```
$ led_panel_client_put /dev/tty.wchusbserial1420
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

| MAX7219 | ESP-WROOM-32 | Pin    | SPI          |
|:--------|:-------------|:-------|:-------------|
| VCC     | 3V3          |        |              |
| GND     | GND          |        |              |
| DIN     | D7           | GPIO13 | HMOSI (mosi) |
| CS      | D8           | GPIO15 | GCS   (cs)   |
| CLK     | D5           | GPIO14 | HSCLK (sck)  |

### Run ###

Reset the microcomputer using the `RST` button on the board. This should load the `main.py` script.

For debugging, use [picocom] to connect to the PyBoard’s [MicroPython][micropython] REPL:

```
picocom -b 115200 /dev/tty.wchusbserial1420 
```

## Credit ##

* [Adafruit industries][adafruit] for the useful libraries
* [Nauč se Python!][naučse] for the MicroPython workshop

Space invaders image found [somewhere](https://tineye.com/search/a1bb7cf24f90f375d0cb62080ace6b3ad2bed7a7/) on the
interwebz. 


[adafruit]: https://www.adafruit.com/
[adafruit-ampy]: https://github.com/adafruit/ampy
[adafruit-max7219]: https://github.com/adafruit/micropython-adafruit-max7219
[esp8266]: https://docs.micropython.org/en/latest/esp8266/quickref.html
[esp32]: https://docs.micropython.org/en/latest/esp32/quickref.html
[ledpanel-server]: https://github.com/Glutexo/ledpanel-server
[max7219]: https://datasheets.maximintegrated.com/en/ds/MAX7219-MAX7221.pdf
[micropython]: https://micropython.org/
[naučse]: https://naucse.python.cz/
[picocom]: https://github.com/npat-efault/picocom
[pip]: https://pypi.org/project/pip/
[python]: https://www.python.org/
[setuptools]: https://github.com/pypa/setuptools
