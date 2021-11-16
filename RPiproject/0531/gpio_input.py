import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
import I2C_drivewr as LCD

Switch= 10
LED= 12

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

def main():
    # Set pin 10 to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
    GPIO.setup(LED, GPIO.OUT, initial= GPIO.LOW) 
    
    mclcd= LCD.lcd()
    
    while True: 
        # GPIO.input(Switch)와 GPIO.HIGH를 AND 연산으로 변경 가능
        if GPIO.input(Switch) == GPIO.HIGH:
            print("Button was pushed!")
            GPIO.output(LED, GPIO.HIGH)
            # LED ON dispaly
        else:
            print("Button was not pushed!")        
            GPIO.output(LED, GPIO.LOW)
            # LED OFF display
        time.sleep(1)
    
if __name__ == '__main__':
    main()
