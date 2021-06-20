#Gabriel Gafencu
#Raspberry Pi Remote Gate Control with Stepper Motor

import RPi.GPIO as GPIO
import time
import sys

# signifies the delay between each command to the motor
# acts as frequency / duty_cycle
delay = 0.001

# sensor bool
detected = False

# argument passed in command line, if 1 => open gate, if 0 => close gate
if sys.argv[1] == '1':
    open = True
else:
    open = False

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# pins on the BOARD layout for the raspberry pi zero
outA_1_pin = 13
outA_2_pin = 11
outB_1_pin = 15
outB_2_pin = 12
sensor = 37

GPIO.setup(outA_1_pin, GPIO.OUT)
GPIO.setup(outA_2_pin, GPIO.OUT)
GPIO.setup(outB_1_pin, GPIO.OUT)
GPIO.setup(outB_2_pin, GPIO.OUT)
GPIO.setup(sensor, GPIO.IN)

def setStep(w1, w2, w3, w4):
  GPIO.output(outA_1_pin, w1)
  GPIO.output(outA_2_pin, w2)
  GPIO.output(outB_1_pin, w3)
  GPIO.output(outB_2_pin, w4)

# run motor as long as sensor hasn't yet detected metal
while not detected:
    if open:
    	setStep(1,0,1,0)
    	time.sleep(delay)
    	setStep(0,1,1,0)
    	time.sleep(delay)
    	setStep(0,1,0,1)
    	time.sleep(delay)
    	setStep(1,0,0,1)
    	time.sleep(delay)
    else:
       	setStep(1,0,0,1)
	time.sleep(delay)
	setStep(0,1,0,1)
	time.sleep(delay)
	setStep(0,1,1,0)
	time.sleep(delay)
	setStep(1,0,1,0)
	time.sleep(delay)
    if GPIO.input(sensor) == 1:
	detected = True

#at the end, move gate back a few steps, in order to ensure the metal marker
#doesn't get stuck in the sensor
for i in range(0, 150):
    if open:
	setStep(1,0,0,1)
    	time.sleep(delay)
    	setStep(0,1,0,1)
    	time.sleep(delay)
    	setStep(0,1,1,0)
    	time.sleep(delay)
    	setStep(1,0,1,0)
    	time.sleep(delay)
    else:
	setStep(1,0,1,0)
    	time.sleep(delay)
    	setStep(0,1,1,0)
    	time.sleep(delay)
    	setStep(0,1,0,1)
    	time.sleep(delay)
    	setStep(1,0,0,1)
    	time.sleep(delay)

#clean up pins used
GPIO.cleanup()
