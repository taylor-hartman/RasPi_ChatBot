import adafruit_character_lcd.character_lcd as characterlcd
import digitalio
import board
import random
import time

##This Script is for LCD Control
##Only for Raspberry Pi

##Define LCD Screen Connections
lcd_rs = digitalio.DigitalInOut(board.D26)
lcd_en = digitalio.DigitalInOut(board.D19)
lcd_d7 = digitalio.DigitalInOut(board.D27)
lcd_d6 = digitalio.DigitalInOut(board.D22)
lcd_d5 = digitalio.DigitalInOut(board.D24)
lcd_d4 = digitalio.DigitalInOut(board.D25)
lcd_columns = 16
lcd_rows = 2
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

##Define Custom LCD Chars
leftSmile = bytes([0x00,0x0C,0x13,0x08,0x04,0x03,0x00,0x00])
lcd.create_char(0, leftSmile)

midSmile = bytes([0x00,0x00,0x1F,0x00,0x00,0x1F,0x00,0x00])
lcd.create_char(1, midSmile)

rightSmile = bytes([0x00,0x06,0x19,0x02,0x04,0x18,0x00,0x00])
lcd.create_char(2, rightSmile)

closedMouth = bytes([0x00,0x00,0x00,0x1F,0x1F,0x00,0x00,0x00])
lcd.create_char(3, closedMouth)

topZ = bytes([0x0F,0x02,0x04,0x0F,0x00,0x00,0x00,0x00])
lcd.create_char(4, topZ)

bottomZ = bytes([0x00,0x00,0x00,0x00,0x1E,0x04,0x08,0x1E])
lcd.create_char(5, bottomZ)

###Fucntions that make different faces
def makeAFace():
    """Makes a random face"""
    choice = random.randint(0,2)
    if(choice == 0):
        owoFace()
    elif(choice == 1):
        x_xFace()
    else:
        moneyFace()

def displaySmile():
    """Displays a smile until cleared"""
    lcd.clear()
    lcd.message = "      o o\n      \x00\x01\x02"

def sleeping():
    """Runs through a sleeping animation"""
    lcd.clear()
    lcd.message = "      - -\n       o\x04"
    time.sleep(1)
    lcd.clear()
    lcd.message = "      - -\x05\n       -"
    time.sleep(1)
    lcd.clear()
    lcd.message =  "      - -\n       -"
    time.sleep(1)

def wakeUp():
    """Runs through custom animation on boot up"""
    sleeping()
    sleeping()
    lcd.message = "      o o\n       -"
    time.sleep(1)
    lcd.clear()
    lcd.message = "      O O\n       o"
    time.sleep(1)
    lcd.clear()
    displaySmile()

def listeningFace():
    """Displays a listening face until cleared"""
    lcd.clear()
    lcd.message = "      o o\n       -"

def oooFace():
    """Displays an 'ooo' face until cleared"""
    lcd.clear()
    lcd.message = "      o o\n       o"

def owoFace():
    """Displays an 'owo' face until cleared"""
    lcd.clear()
    lcd.message = "      owo"

def x_xFace():
    """Displays an 'x_x' face until cleared"""
    lcd.clear()
    lcd.message = "      x_x"

def moneyFace():
    """Displays an money face until cleared"""
    lcd.clear()
    lcd.message = "      $ $\n       o"