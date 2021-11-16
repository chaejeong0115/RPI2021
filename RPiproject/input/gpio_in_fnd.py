# import RPi.GPIO as GPIO
# import time
from RPi.GPIO import *
from time import *

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
    output(seg,fnd[num])
    sleep(0.2)
    num += 1
    print(num-1)

def FND_setup():
    setmode(BOARD)
    setwarnings(False)

    setup(seg,OUT,initial=LOW)
    setup(switch,IN,pull_up_down=PUD_DOWN)
    
    

def main():
    FND_setup()
    add_event_detect(switch,RISING, callback=button_callback,bouncetime=300)
    
    for i in range(10):
        output(seg,fnd[i])
        sleep(0.2)
    
    message = input("Press enter to quit\n\n")

# 
        # cleanup()

if __name__ == '__main__':
    main()

