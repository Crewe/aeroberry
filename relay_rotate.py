import RPi.GPIO as GPIO
import time

iobyte = [18, 23, 24, 25]

def setup_ports():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(18, GPIO.OUT)
	GPIO.setup(23, GPIO.OUT)
	GPIO.setup(24, GPIO.OUT)
	GPIO.setup(25, GPIO.OUT)

while (1):
	# Turn off relays one at a time
	for port in iobyte:
		GPIO.output(port, GPIO.HIGH)
		time.sleep(1)

	# Turn on relays one at a time
	for port in iobyte:
		GPIO.output(port, GPIO.LOW)
		time.sleep(1)

def porta(val):
	if (val(0) == 1):
		GPIO.output(18, GPIO.HIGH)
	else:
		GPIO.output(18, GPIO.LOW)

	if (val(1) == 1):
		GPIO.output(23, GPIO.HIGH)
	else:
		GPIO.output(23, GPIO.LOW)

	if (val(2) == 1):
		GPIO.output(24, GPIO.HIGH)
	else:
		GPIO.output(24, GPIO.LOW)

	if (val(3) == 1):
		GPIO.output(25, GPIO.HIGH)
	else:
		GPIO.output(25, GPIO.LOW)
