import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
LED = 10
LED1= 12

def main():
    GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(LED1, GPIO.OUT)
    while 1:
        GPIO.output(LED, GPIO.HIGH)
        GPIO.output(LED1, GPIO.LOW)
        time.sleep(1)
        GPIO.output(LED, GPIO.LOW)
        GPIO.output(LED1, GPIO.HIGH)
        time.sleep(1)

if __name__=='__main__':
    main()

