import Rpi.GPIO as GPIO
import time
contador=0
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.output(11,1)
GPIO.output(12,1)
GPIO.output(13,1)
try:
	while(1):
		if GPIO.input(18)==GPIO.LOW:
			contador=contador+1
			time.sleep(0.5)
		if contador==1:
			GPIO.output(11,0)
			GPIO.output(12.1)
			GPIO.output(13,1)
		elif contador==2:
			GPIO.output(11,1)
			GPIO.output(12.0)
			GPIO.output(13,1)
		elif contador==3:
			GPIO.output(11,1)
			GPIO.output(12,1)
			GPIO.output(13,0)
		elif contador>=4:
			GPIO.output(11,1)
			GPIO.output(12,1)
			GPIO.output(13,1)
		if contador==4:
			contador=0
		time.sleep(0.1)
