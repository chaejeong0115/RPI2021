#!/usr/bin/env python
import max7219.led as led
import max7219.canvas as canvas
import time
 
font5x3 = { # python data type dictionary for the pixelfont
    "0" : [0b01110, 0b10001, 0b01110], # "0"
    "1" : [0b10010, 0b11111, 0b10000], # "1"
    "2" : [0b11001, 0b10101, 0b10010], # "2"
    "3" : [0b10001, 0b10101, 0b01110], # "3"
    "4" : [0b01110, 0b01000, 0b11111], # "4"
    "5" : [0b10111, 0b10101, 0b01001], # "5"
    "6" : [0b01110, 0b10101, 0b01000], # "6"
    "7" : [0b10001, 0b01001, 0b00111], # "7"
    "8" : [0b01010, 0b10101, 0b01010], # "8"
    "9" : [0b00010, 0b10101, 0b01110], # "9"
    ":" : [0b01010], # ":"
    "-" : [0b00100, 0b00100, 0b00100], # "-"
    "|" : [      0], # one blank line
    " " : [      0,       0,       0] # space
    } # you can create additional letters
 
def creatematrix(text):
    text = str(text)
    matrix = []
    for i in range(len(text)): # write complete pixelmatrix in a buffer
        if text[i].upper() in font5x3: # check if dictionary entry exists
            matrix = matrix + font5x3[text language=""[i""][/text].upper()] # add letter; upper() for reduced font
        matrix = matrix + [0] # separator/space
    return matrix
 
def drawmatrix(matrix, up, left):
    for i in range(8): # fill the 8x8 matrix buffer
        if up &lt; 0:
            canvas.gfxbuf[i] = matrix[(i + left) % len(matrix)] &lt;&gt; abs(up)
     
led.init()
horz = 0
vert = -2
led.brightness(0) # 0, 3, 7, 15 seems to work
 
while True:
    t = [int(time.strftime("%H")), int(time.strftime("%M")), int(time.strftime("%S")), int((time.time()*1000) % 1000)]
    if (t[3] % 500) &lt; 250: # switch for the blinking colon
        m = creatematrix(str(t[0]) + &quot;:&quot; + str(t[1]).zfill(2) + &quot; &quot;)
    else:
        m = creatematrix(str(t[0]) + &quot;|&quot; + str(t[1]).zfill(2) + &quot; &quot;)
 
    drawmatrix(m, vert, horz)
    horz = (horz + 1) % len(m) # scroll left
    canvas.render()
    time.sleep(0.05)
