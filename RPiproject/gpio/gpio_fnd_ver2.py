# import RPi.GPIO as GPIO
# import time
from RPi.GPIO import *
from time import *

num = 0
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

def FND_setup():
    setmode(BOARD)
    setwarnings(False)

    setup(seg,OUT,initial=LOW)
    # for value in list_RGB:
    #     setup(value, OUT)


def main():
    FND_setup()
    i=0
    
    while True:
        output(seg,fnd[i])
        sleep(1)
        print(i)
        print(seg)
        print(fnd[i])
        
        if i < 9:
            i= i+1
        else:
            i=0
        

        # cleanup()

if __name__ == '__main__':
    main()

