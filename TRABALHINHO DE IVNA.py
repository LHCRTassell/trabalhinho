import Rpi.GPIO as GPIO
import time
contador=0
GPIO.setmode(GPIO.BOARD)
variavel1 = 11
variavel2 = 12
variavel3 = 13

GPIO.setup(variavel1,GPIO.OUT)
GPIO.setup(variavel2,GPIO.OUT) 
GPIO.setup(variavel3,GPIO.OUT) 

GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.output(variavel1,1) 
GPIO.output(variavel2,1) 
GPIO.output(variavel3,1) 
try:
	while(1):
		if GPIO.input(18)==GPIO.LOW:
			contador=contador+1
			time.sleep(0.5)
		if contador==1:
			GPIO.output(variavel1,0)
			GPIO.output(variavel2,1)
			GPIO.output(variavel3,1)
		elif contador==2:
			GPIO.output(variavel1,1)
			GPIO.output(variavel2,0)
			GPIO.output(variavel3,1)
		elif contador==3:
			GPIO.output(variavel1,1)
			GPIO.output(variavel2,1)
			GPIO.output(variavel3,0)
		elif contador>=4:
			GPIO.output(variavel1,1)
			GPIO.output(variavel2,1)
			GPIO.output(variavel3,1)
		if contador==4:
			contador=0
		time.sleep(0.1)
