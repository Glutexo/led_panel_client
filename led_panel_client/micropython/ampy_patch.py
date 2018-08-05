from machine import Pin


class PatchedPin(Pin):
    """
    Translates Adafruit’s way to set a pin value to vanilla Micropython code.
    """

    def high(self):
        """
        Translates Adafruit’s way to set a high value to vanilla Micropython code.
        """
        self.value(1)

    def low(self):
        """
        Translates Adafruit’s way to set a low value to vanilla Micropython code.
        """
        self.value(0)
