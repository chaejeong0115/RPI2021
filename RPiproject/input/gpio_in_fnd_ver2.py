import RPi.GPIO as GPIO
import time
# from RPi.GPIO import *
# from time import *
import sys

num = 0
switch= 16
#        A   B   C   D   E   F   G   DP
# seg = [11, 13, 15, 16, 18, 19, 21, 23]
seg = [8, 10, 12, 13, 19, 21, 23, 24]

#       A B C D E F G DP
fnd = [(1,1,1,1,1,1,0,0),#0
       (0,1,1,0,0,0,0,0),#1
       (1,1,0,1,1,0,1,0),#2
       (1,1,1,1,0,0,1,0),#3
       (0,1,1,0,0,1,1,0),#4
       (1,0,1,1,0,1,1,0),#5
       (1,0,1,1,1,1,1,0),#6
       (1,1,1,0,0,0,0,0),#7
       (1,1,1,1,1,1,1,0),#8
       (1,1,1,1,0,1,1,0)]#9

def button_callback(channel):
    ISP_Swtich()
    print("Button was pushed!")

def ISP_Swtich():
    global num
    if num == 10:
        num = 0
    GPIO.output(seg,fnd[num])
    time.sleep(0.2)
    num += 1
    print(num-1)

def FND_setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    GPIO.setup(seg,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(switch,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    
    

def main():
    FND_setup()
    GPIO.add_event_detect(switch,GPIO.RISING, callback=button_callback,bouncetime=300)
    
    for i in range(10):
        GPIO.output(seg,fnd[i])
        time.sleep(0.2)
    
    # message = sys.stdin.readline()
    message = input("Press enter to quit\n\n")

# 
        # cleanup()

if __name__ == '__main__':
    main()

