import RPi.GPIO as GPIO 
import serial
import time

Switch= [38, 40]
global sw_status
sw_status=0 

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

def red_button(channel):
	global sw_status
	sw_status = 1

def green_button(channel):
	global sw_status
	sw_status = 2

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
	GPIO.add_event_detect(Switch[0],GPIO.RISING,callback=red_button)
	GPIO.add_event_detect(Switch[1],GPIO.RISING,callback=green_button)
	
	    
	while True:
		if sw_status== 1:	        
			sw_status= 0
			print("Sw1(red) Button was pushed!")
			cmd= 'r'
			ser.write(cmd.encode('UTF-8')+b"\n") 
		elif sw_status== 2:	        
			sw_status= 0
			print("Sw2(green) Button was pushed!")
			cmd= 'g'
			ser.write(cmd.encode('UTF-8')+b"\n") 

		time.sleep(1)
else:
	print ("Cannot open serial port.")
