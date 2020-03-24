#!/usr/bin/env python

from functools import partial
from os import listdir
from os.path import join
from re import match
from subprocess import run
from sys import argv


DEV_PATH = "/dev"
DEVICE_FILE_PATTERN = r"^tty\.(usbserial-|wchusbserial)\d{4}$"
PICOCOM_COMMAND = ("picocom", "-b", "115200")


def _get_device_from_args(args):
    if len(args) < 1:
        raise ValueError
    return argv[0]


def _get_device_from_dev(files):
    for file in files:
        if match(DEVICE_FILE_PATTERN, file):
            return file

def _device_path(file):
    return join(DEV_PATH, file)


def _command(device_path):
    return PICOCOM_COMMAND + (device_path,)


def _main(args):
    device = None

    from_args = partial(_get_device_from_args, args)
    from_dev = partial(_get_device_from_dev, listdir(DEV_PATH))
    for get_func in (from_args, from_dev):
        try:
            device = get_func()
        except ValueError:
            continue

    if not device:
        print("No device found.")
        return 1

    device_path = _device_path(device)
    command = _command(device_path)

    command_str = " ".join(command)
    print(f"Running `{command_str}`…")

    run(command)
    return 0


if __name__ == "__main__":
    code = _main(argv)
    exit(code)

