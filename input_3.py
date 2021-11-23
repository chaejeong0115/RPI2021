import RPi.GPIO as GPIO
import time
from time import sleep, strftime
from datetime import datetime

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT

import I2C_driver as LCD
from time import *


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

def main():
    LED = 10
    Touch = 11
    Flame = 13
    Light = 15
    GPIO.setup(LED, GPIO.OUT)
    GPIO.setup(Touch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Flame, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Light, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    mylcd = LCD.lcd()

    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, width=8, height=8, block_orientation=0)
    print(device)
    device.contrast(100)
    virtual = viewport(device, width=8, height=8)

    #show_message(device, 'Raspberry Pi MAX7219', fill="white", font=proportional(LCD_FONT), scroll_delay=0.08)

    while True:
        if (GPIO.input(Touch) == GPIO.HIGH):
            print("Touch on")
            GPIO.output(LED, GPIO.LOW)
            with canvas(virtual) as draw:
                text(draw, (0, 1), 'T', fill="white", font=proportional(CP437_FONT))
            mylcd.lcd_clear()
            sleep(1)


        elif (GPIO.input(Flame) == GPIO.HIGH):
            print("Flame On")
            with canvas(virtual) as draw:
                text(draw, (0, 1), 'F', fill="white", font=proportional(CP437_FONT))
            mylcd.lcd_clear()
            for i in range(50):
                GPIO.output(LED, GPIO.HIGH)
                sleep(0.1)
                GPIO.output(LED, GPIO.LOW)
                sleep(0.1)
            sleep(1)


        elif (GPIO.input(Light) == GPIO.HIGH):
            print("Light On")
            GPIO.output(LED, GPIO.LOW)
            mylcd.lcd_display_string("Room Light On", 1)
            with canvas(virtual) as draw:
                text(draw, (0, 1), 'L', fill="white", font=proportional(CP437_FONT))
            sleep(1)


        elif (GPIO.input(Touch) == GPIO.LOW and GPIO.input(Flame) == GPIO.LOW and GPIO.input(Light) == GPIO.LOW):
            print("OFF")
            with canvas(virtual) as draw:
                text(draw, (0, 1), '', fill="white", font=proportional(CP437_FONT))
            mylcd.lcd_clear()
            GPIO.output(LED, GPIO.LOW)
            sleep(1)


'''
        for _ in range(1):
            for intensity in range(16):
                device.contrast(intensity*16)
                sleep(0.1)
'''

if __name__ == '__main__':
    main()
