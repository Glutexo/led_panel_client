from importlib.util import find_spec
from os import scandir
from os.path import dirname


LED_PANEL_CLIENT_FILES = [
    "ampy_patch.py",
    "config.py",
    "graphics.py",
    "images.py",
    "main.py",
    "wlan.py",
]


def led_panel_client():
    """
    Populates this package’s micropython file paths.
    """

    def included(dir_entry):
        return dir_entry.name in LED_PANEL_CLIENT_FILES

    def dir_entry_path(dir_entry):
        return dir_entry.path

    spec = find_spec("led_panel_client.micropython")
    folder = dirname(spec.origin)
    included_dir_entries = filter(included, scandir(folder))
    return set(map(dir_entry_path, included_dir_entries))


def max7219():
    """
    Populates file path of the Adafruit MAX7219 driver.
    """
    spec = find_spec("max7219")
    return {spec.origin}
