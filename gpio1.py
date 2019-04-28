# This is a simple test of the Jetson.GPIO library
# To understand more about this library, read /opt/nvidia/jetson-gpio/doc/README.txt

import sys

sys.path.append('/opt/nvidia/jetson-gpio/lib/python')
sys.path.append('/opt/nvidia/jetson-gpio/lib/python/Jetson/GPIO')

import Jetson.GPIO as GPIO

mode = GPIO.getmode()
print(mode)
