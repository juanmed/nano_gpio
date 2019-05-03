# This is a simple test of the Jetson.GPIO library
# To understand more about this library, read /opt/nvidia/jetson-gpio/doc/README.txt

import sys

sys.path.append('/opt/nvidia/jetson-gpio/lib/python')
sys.path.append('/opt/nvidia/jetson-gpio/lib/python/Jetson/GPIO')
sys.path.append('/home/nvidia/repositories/nano_gpio/gpio_env/lib/python2.7/site-packages/periphery/')

import Jetson.GPIO as GPIO
from periphery import PWM
import time

# set GPIO mode to BOARD
GPIO.setmode(GPIO.BOARD)
mode = GPIO.getmode()
print(mode)


# Open PWM channel 0, pin 32
pins = range(0,41)
"""
for pin in pins:
	try:
		pwm = PWM(0, pin)
		print("** Channel 0 pin {} works!".format(pin))
	except:
		print("Pin {} does not work".format(pin))
"""

pwm = PWM(0,2)

#Channel 0 pin 2

# Set frequency to 1 kHz
pwm.frequency = 1e3
# Set duty cycle to 75%
pwm.duty_cycle = 0.5

pwm.enable()

# Change duty cycle to 50%
pwm.duty_cycle = 0.50

time.sleep(5*60)

pwm.close()
