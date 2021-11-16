import RPi.GPIO as GPIO
import serial
import time

# global variable
# LED = 3
RGB= [3, 5, 7]

ser = serial.Serial(
	port= '/dev/ttyS0',
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
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(RGB, GPIO.OUT)

	while 1:
		ser.flushOutput()
		ser_bytes = ser.readline()
		decoded_bytes = (ser_bytes.decode("utf-8"))
		
		if len(decoded_bytes):		
			print('Receiving')
			print(type(decoded_bytes))
			print('Rx Data: '+ decoded_bytes)

			# print(decoded_bytes)
			# print(type(decoded_bytes))
			# print(len(decoded_bytes))

			ledNum= decoded_bytes.strip()
			print(ledNum)
			if ledNum == '1':
				print('LED ON')
				GPIO.output(RGB, GPIO.HIGH)
			elif ledNum == '2':
				print('LED OFF')
				GPIO.output(RGB, GPIO.LOW)    
			else:
				print('error')

		time.sleep(0.5)

	    # programming..
else:
	print ("Cannot open serial port.")
