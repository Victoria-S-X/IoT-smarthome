from machine import Pin
import lcd1602
import time

def initializeLcd():
    # Initialize pins for the LCD
    rs = Pin(12, Pin.OUT)
    en = Pin(11, Pin.OUT)
    d4 = Pin(10, Pin.OUT)
    d5 = Pin(9, Pin.OUT)
    d6 = Pin(8, Pin.OUT)
    d7 = Pin(7, Pin.OUT)

    # Create an instance of the LCD
    lcd = lcd1602.LCD1602(rs, en, d4, d5, d6, d7, 16, 2)
    return lcd

def createCustomChars(lcd):
    heart_char = [
        0b00000,
        0b01010,
        0b11111,
        0b11111,
        0b11111,
        0b01110,
        0b00100,
        0b00000
    ]

    open_lock_char = [
        0b01110,
        0b10001,
        0b10000,
        0b10000,
        0b11111,
        0b10001,
        0b11111,
        0b00000
    ]

    bell_char = [
        0b00100,
        0b01110,
        0b01110,
        0b01110,
        0b11111,
        0b00100,
        0b00000,
        0b00000
    ]

    closed_lock_char = [
        0b01110,
        0b10001,
        0b10001,
        0b11111,
        0b11111,
        0b10001,
        0b11111,
        0b00000
    ]

    lcd.create_char(0, heart_char)
    lcd.create_char(1, open_lock_char)
    lcd.create_char(2, bell_char)
    lcd.create_char(3, closed_lock_char)

def displayMainScreen(lcd):
    lcd.clear()  # Clear the LCD before printing the new key
    lcd.print("Sweet home ")  # Print the pressed key on the LCD
    lcd.write(0)
    lcd.print(" ")  # Print the pressed key on the LCD
    lcd.write(1)
    time.sleep(1)

def displaySecurityOn(lcd):
    lcd.clear()
    lcd.print("Alarm on... ")
    lcd.write(2)
    lcd.print(" ")  # Print the pressed key on the LCD
    lcd.write(3)
    time.sleep(0.5)

def displayMotionDetected(lcd):
    lcd.clear()
    lcd.print("Motion Detected!")
    time.sleep(0.5)