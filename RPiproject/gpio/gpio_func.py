# import RPi.GPIO as GPIO
# import time
from RPi.GPIO import *
from time import *
import sys

Red= 8; Green=10; Blue= 12

list_RGB= [Red, Green, Blue]

def LED_setup():
    setmode(BOARD)
    setwarnings(False)

    for value in list_RGB:
        setup(value, OUT)

def main():
    LED_setup()
    while True:
        for value in list_RGB:
            output(value, HIGH)
            sleep(0.5)
            output(value, LOW)
            sleep(0.5)

if __name__ == '__main__':
    main()
