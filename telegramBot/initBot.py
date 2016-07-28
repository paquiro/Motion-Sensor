# -*- coding: utf-8 -*-

import time
import sys
from commandsBot import *
import threading
import RPi.GPIO as GPIO

reload(sys)
sys.setdefaultencoding("utf-8")

def detect(run_event):
    isDetected = False
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.IN) # Set GPIO 11 pin as input
    GPIO.setup(12,GPIO.OUT)
    GPIO.setup(16,GPIO.OUT)


    while run_event.is_set():
        i=GPIO.input(11)
        if i==0:         # if don't detect signal
            #print "\033[95mNobody detected.\033[0m",i
            GPIO.output(12,GPIO.HIGH)
            GPIO.output(16,GPIO.LOW)
            isDetected = False
            time.sleep(0.1)
        if i==1 and isDetected == False:       # if detect signal
            print "\033[92mSomeone detected.\033[0m --> " + time.strftime("%H:%M:%S")
            bot.send_message(admin, "Someone detected -->   " + time.strftime("%H:%M:%S"))
            GPIO.output(16,GPIO.HIGH)
            GPIO.output(12,GPIO.LOW)
            isDetected = True
            time.sleep(0.1)
    GPIO.cleanup()




try:
    run_event = threading.Event()
    run_event.set()
    t = threading.Thread(target=detect, args = (run_event,))
    t.start()
    bot.polling(none_stop=True, interval=0, timeout=3) #Bot must continue if it fails
    while 1:
        time.sleep(0.1)
except KeyboardInterrupt:
    run_event.clear()
    t.join()
    bot.send_message(admin, "The bot is set to off -->   " + time.strftime("%H:%M:%S"))
