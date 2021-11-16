import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library


def button_callback(channel):
    print("Button was pushed!")

Switch= 40

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

# Set pin Switch to be an input pin and set initial value to be pulled low (off)
GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


# Setup event on pin Switch rising edge. button_callback는 함수
GPIO.add_event_detect(Switch,GPIO.RISING,callback=button_callback)

message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up