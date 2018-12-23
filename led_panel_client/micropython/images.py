from machine import Pin
from graphics import draw_image


__all__ = ["cycle"]


_FLASH_BUTTON = Pin(0, Pin.IN)
_IMAGES = [
    '''\
00011000
00111100
01111110
11011011
11111111
00111100
01111110
10100101\
''',
    '''\
01000010
01100110
00100100
00011000
00111100
01011010
11111111
01100110\
'''
]


def _pressed(pin):
    value = pin.value()
    if value == 1:
        return False
    elif value == 0:
        return True
    else:
        raise ValueError('Unknown pin value')


def cycle(display):
    last_flash_pressed = None
    current_image = 0
    draw_image(display, _IMAGES[current_image])
    while True:
        current_flash_pressed = _pressed(_FLASH_BUTTON)
        if current_flash_pressed == last_flash_pressed:
            continue

        if current_flash_pressed:
            if current_image + 1 == len(_IMAGES):
                current_image = 0
            else:
                current_image += 1

            draw_image(display, _IMAGES[current_image])

        last_flash_pressed = current_flash_pressed
