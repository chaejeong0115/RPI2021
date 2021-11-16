import I2C_driver as LCD
from time import *
import time

SW= 10
LED= 12

mylcd = LCD.lcd()
mylcd.lcd_display_string("Hello World",1)
mylcd.lcd_display_string("Raspberry Pi3 b+",2)
sleep(5)

mylcd.lcd_clear()
mylcd.lcd_display_string("LCD display",2)
