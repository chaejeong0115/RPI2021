import serial
import time

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
	while 1:
		ser.flushInput()
		cmd = input("Enter command or 'exit':")		
		if cmd == 'exit':
			ser.write(cmd.encode('UTF-8')+ b"\n")
			ser.close()
			exit()
		else:
			# ser.write(cmd.encode('UTF-8'))
			ser.write(cmd.encode('UTF-8')+ b"\n")
	

		time.sleep(0.5)
else:
	print ("Cannot open serial port.")
