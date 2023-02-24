import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
GPIO.setup(5,GPIO.IN)
GPIO.setup(6,GPIO.IN)

#initialise a previous input variable to 0 (Assume no pressure applied)
#prev_input = 0
try:
    time1 = -1
    time2 = -1
    time3 = -1
    while True:
        #update time
        if (GPIO.input(4)):
            time1 = time()
        if (GPIO.input(5)):
            time2 = time()
        if (GPIO.input(6)):
            time3 = time()
        if (time1 > -1 and time1 < time2 and time2 < time3):
            print("Wag tail")
            time1 = time2 = time3 = -1
        if (time3 > -1 and time1 > time2 and time2 > time3):
            print("Bark")
            time1 = time2 = time3 = -1
        #if the last reading was low and this one high, alert us
        #if ((not prev_input) and input):
        #    print("Under Pressure")
        #update previous input
       # prev_input = input
        #slight pause
        time.sleep(0.05)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()