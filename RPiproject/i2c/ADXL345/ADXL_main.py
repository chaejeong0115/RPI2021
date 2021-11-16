# smbus library
import ADXL345_driver as ADXL

# time library
import time

x_adr= 0x32
y_adr= 0x34
z_adr= 0x36



def main():
    ADXL.init_ADXL345()

    while 1:
        x_acc = ADXL.measure_acc(x_adr)
        y_acc = ADXL.measure_acc(y_adr)
        z_acc = ADXL.measure_acc(z_adr)

        print ('X = %2.2f' % x_acc, '[g], Y = %2.2f' % y_acc, '[g], Z = %2.2f' % z_acc, '[g]')

        time.sleep(1)
        
if __name__ == '__main__':
    main()



