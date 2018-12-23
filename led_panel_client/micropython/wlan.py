from config import WLAN_ESSID, WLAN_PASSWORD
from network import STA_IF, WLAN
from time import sleep


__all__ = ["connect"]

_wlan = WLAN(STA_IF)


def connect():
    _wlan.active(True)
    if _wlan.isconnected():
        return  # Already connected.

    _wlan.connect(WLAN_ESSID, WLAN_PASSWORD)
    while not _wlan.isconnected():
        sleep(0.1)

    # Connected.
