import sys
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN) # Set GPIO 11 pin as input
try:
    while True:
       i=GPIO.input(11)
       if i==0:         # if don't detect signal
           print "\033[95mNobody detected.\033[0m",i
           time.sleep(0.1)
       elif i==1:       # if detect signal
           print "\033[92mSomeone detected.\033[0m",i
           time.sleep(0.1)
except KeyboardInterrupt:
    # for example, Ctrl + C
    GPIO.cleanup()
    sys.exit(0)
except:
    GPIO.cleanup()
    print "Unexpected error:", sys.exc_info()[0]
    sys.exit(0)



