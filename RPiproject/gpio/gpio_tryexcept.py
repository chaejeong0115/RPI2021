# import RPi.GPIO as GPIO
# import time
from RPi.GPIO import *
from time import *
import sys

setmode(BOARD)
setwarnings(False)

LED = 8

setup(LED, OUT, initial=LOW)

try:
    while True:
        output(LED, HIGH)
        sleep(1)
        output(LED, LOW)
        sleep(1)
except KeyboardInterrupt:
    # pass
    sys.exit(0)

finally:
    cleanup()
