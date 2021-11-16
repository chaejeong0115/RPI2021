import RPi.GPIO as GPIO 
import serial
import time

Switch= 40

ser = serial.Serial(
	# port= '/dev/ttyS0',
	port= '/dev/ttyUSB0',
	baudrate = 115200,	    	
	parity= serial.PARITY_NONE,
	stopbits= serial.STOPBITS_ONE,
	bytesize= serial.EIGHTBITS,
	timeout=1,
	xonxoff = False, 
	rtscts = False,     
	dsrdtr = False,    
	writeTimeout = 0
)
print ("Starting Up Serial Monitor")

try:
    ser.open()
except Exception as e:
    print ("Exception: Opening serial port: " + str(e))
#finally:
#    ser.close()

if ser.isOpen():
	GPIO.setwarnings(False) # Ignore warning for now
	GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
	GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	
	while 1:
		cmd= '0'    		
		ser.flushInput()
		if GPIO.input(Switch) == GPIO.HIGH:
			cmd= '1'
			print('Button was pushed!')
			ser.write(cmd.encode('UTF-8')+ b"\n")			
		else:
			cmd= '2'
			print('Button was not pushed!')
			ser.write(cmd.encode('UTF-8')+ b"\n") 
		
	

		time.sleep(0.5)
else:
	print ("Cannot open serial port.")
