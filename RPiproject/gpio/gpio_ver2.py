# import RPi.GPIO as GPIO
# import time
from RPi.GPIO import *
from time import *

setmode(BOARD)
setwarnings(False)

LED = 8

setup(LED, OUT, initial=LOW)

while True:
    output(LED, HIGH)
    sleep(1)
    output(LED, LOW)
    sleep(1)
