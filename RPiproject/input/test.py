import RPi.GPIO as GPIO
import time

num = 0
#      A   B   C   D   E   F   G   DP
# seg = [11, 13, 15, 10, 18, 19, 21, 23]
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

def number():
    global num
    if num == 10:
        num = 0
    GPIO.output(seg,fnd[num])
    time.sleep(0.2)
    num += 1
    print(num-1)

def button_callback(channel):
    number()
    print("Button was pushed!")


Switch = 16

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(seg,GPIO.OUT,initial=GPIO.LOW)

for i in range(10):
        GPIO.output(seg,fnd[i])
        time.sleep(0.2)

GPIO.setup(Switch,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(Switch,GPIO.RISING,callback=button_callback,bouncetime=300)

message = input("Press enter to quit\n\n")

GPIO.cleanup()
