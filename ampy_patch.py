from machine import Pin


class PatchedPin(Pin):
    def high(self):
        self.value(1)

    def low(self):
        self.value(0)
