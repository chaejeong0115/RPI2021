import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import I2C_driver as LCD

#LCD display
mylcd= LCD.lcd()


# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)

# Create differential input between channel 0 and 1
# chan = AnalogIn(ads, ADS.P0, ADS.P1)

print("{:>5}\t{:>5}".format("raw", "v"))

mylcd.lcd_display_string("LCD display", 1)
mylcd.lcd_display_string("ADC value", 2)
#print("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
time.sleep(2)

while True:
    mylcd.lcd_clear()
    mylcd.lcd_display_string("One bus. I2C", 1)
    adc_str= "ADC value:"+ str(chan.voltage)
    mylcd.lcd_display_string(adc_str, 2)

    print("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
    time.sleep(1)


