"""
lcd1602.py

This file is generated and adapted from ChatGPT, a language model created by OpenAI.

"""

from machine import Pin
from time import sleep_ms

class LCD1602:
    def __init__(self, rs, en, d4, d5, d6, d7, cols, rows):
        self.rs = rs
        self.en = en
        self.d4 = d4
        self.d5 = d5
        self.d6 = d6
        self.d7 = d7
        self.cols = cols
        self.rows = rows
        self.rs.init(Pin.OUT)
        self.en.init(Pin.OUT)
        self.d4.init(Pin.OUT)
        self.d5.init(Pin.OUT)
        self.d6.init(Pin.OUT)
        self.d7.init(Pin.OUT)
        self.init_lcd()

    def pulse_enable(self):
        self.en.value(0)
        sleep_ms(1)
        self.en.value(1)
        sleep_ms(1)
        self.en.value(0)
        sleep_ms(1)

    def send(self, data, mode):
        self.rs.value(mode)
        self.d4.value((data >> 4) & 0x01)
        self.d5.value((data >> 5) & 0x01)
        self.d6.value((data >> 6) & 0x01)
        self.d7.value((data >> 7) & 0x01)
        self.pulse_enable()
        self.d4.value(data & 0x01)
        self.d5.value((data >> 1) & 0x01)
        self.d6.value((data >> 2) & 0x01)
        self.d7.value((data >> 3) & 0x01)
        self.pulse_enable()

    def command(self, cmd):
        self.send(cmd, 0)

    def write(self, value):
        if isinstance(value, int):
            self.send(value, 1)
        elif isinstance(value, str):
            self.send(ord(value), 1)
        else:
            raise TypeError("Value must be an integer or a single character string")

    def clear(self):
        self.command(0x01)  # Clear display
        sleep_ms(2)

    def set_cursor(self, col, row):
        row_offsets = [0x00, 0x40]
        if row >= self.rows:
            row = self.rows - 1
        self.command(0x80 | (col + row_offsets[row]))

    def print(self, message):
        for char in message:
            self.write(char)

    def create_char(self, location, charmap):
        location &= 0x7  # we only have 8 locations 0-7
        self.command(0x40 | (location << 3))
        for i in range(8):
            self.write(charmap[i])

    def init_lcd(self):
        self.send(0x33, 0)
        self.send(0x32, 0)
        self.send(0x28, 0)
        self.send(0x0C, 0)
        self.send(0x06, 0)
        self.clear()