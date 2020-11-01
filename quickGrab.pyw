import ImageGrab
import os
import time

#Globals
#------------
x_pad = 279
y_pad = 225

def screenGrab():
    box = (x_pad+1, y_pad+1, x_pad+1023, y_pad+599)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')
 
def main():
    screenGrab()
 
if __name__ == '__main__':
    main()