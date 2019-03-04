import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
import time


gpio.setup(04,gpio.OUT)


while 1:
	gpio.output(04,True)
	time.sleep(.4)
	gpio.output(04,False)
	time.sleep(0.4)
