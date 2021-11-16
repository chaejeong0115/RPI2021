import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LED = 3

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
while 1:
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(1)