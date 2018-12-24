from ampy_patch import PatchedPin
from config import DISPLAY_BRIGHTNESS
from machine import Pin, SPI
from max7219 import Matrix8x8
from time import sleep


__all__ = ["init", "draw_image", "draw_progress"]

_IMAGE_MAP = {"0": False, "1": True}
_DISPLAY_WIDTH = 8
_DISPLAY_HEIGHT = 8


def init():
    spi = SPI(-1, 10000000, miso=Pin(12), mosi=Pin(13), sck=Pin(14))
    display = Matrix8x8(spi, PatchedPin(15))
    display.brightness(DISPLAY_BRIGHTNESS)
    return display


def draw_fill(display, color):
    display.fill(color)
    display.show()


def draw_image(display, image):
    display.fill(False)

    x = 0
    y = 0
    for char in image:
        if char == "\n":
            x = 0
            y += 1
            continue

        display.pixel(x, y, _IMAGE_MAP[char])
        x += 1

    display.show()


def draw_progress(display, generator):
    draw_fill(display, False)

    x = 0
    y = 0
    for _ in generator:
        display.pixel(x, y, True)
        display.show()
        if x + 1 == _DISPLAY_WIDTH:
            x = 0
            if y + 1 == _DISPLAY_HEIGHT:
                y = 0
                draw_fill(display, False)
            else:
                y += 1
        else:
            x += 1


def flash(display, on_duration=0.1, off_duration=0.1):
    display.fill(True)
    display.show()
    sleep(on_duration)
    display.fill(False)
    display.show()
    sleep(off_duration)
