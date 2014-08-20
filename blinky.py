import time
import RPi.GPIO as GPIO

LED = 22

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

while True:
	GPIO.output(LED, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(LED, GPIO.LOW)
	time.sleep(0.5)