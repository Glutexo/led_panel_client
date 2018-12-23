from ampy.pyboard import Pyboard
from ampy.files import Files
from .files import led_panel_client, max7219
from os.path import basename
from sys import argv


def put():
    """
    Uploads all necessary files to the pyboard.
    """
    if len(argv) < 2:
        print(
            "Pyboard COM port not specified. Usage: led_panel_client_put /dev/tty.wchusbserial1410"
        )
        exit(1)

    pyboard_pyboard = Pyboard(argv[1])
    pyboard_files = Files(pyboard_pyboard)

    files_to_put = led_panel_client() | max7219()
    for file_path in files_to_put:
        name = basename(file_path)
        with open(file_path) as file_object:
            data = file_object.read()
        pyboard_files.put(name, data)
