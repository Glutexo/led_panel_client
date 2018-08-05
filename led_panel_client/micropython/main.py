from ampy_patch import PatchedPin
from machine import Pin, SPI
from max7219 import Matrix8x8

FLASH = Pin(0, Pin.IN)

IMAGES = [
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

MAP = { '0': False, '1': True }

spi = SPI(-1, 10000000, miso=Pin(12), mosi=Pin(13), sck=Pin(14))
# display = Matrix8x8(spi, Pin(2))
display = Matrix8x8(spi, PatchedPin(15))
display.brightness(15)

def pressed(pin):
    value = pin.value()
    if value == 1:
        return False
    elif value == 0:
        return True
    else:
        raise ValueError('Unknown pin value')

def draw_image(image):
    display.fill(False)

    x = 0
    y = 0
    for char in image:
        if char == '\n':
            x = 0
            y += 1
            continue

        display.pixel(x, y, MAP[char])
        x += 1

    display.show()

last_flash_pressed = None
current_image = 0
draw_image(IMAGES[current_image])
while True:
    current_flash_pressed = pressed(FLASH)
    if current_flash_pressed == last_flash_pressed:
        continue

    if current_flash_pressed:
        next_image = current_image + 1
        current_image = next_image if next_image < len(IMAGES) else 0
        draw_image(IMAGES[current_image])

    last_flash_pressed = current_flash_pressed
