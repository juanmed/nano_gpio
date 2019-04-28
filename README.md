# Jetson Nanon GPIO

This repository contains several examples on using the GPIO pins and libraries (Jetson.GPIO) in the Jetson Nano.

It is assumed you already went throught the Jetson Nano quick setup process and have the Ubuntu image running.

To start off, the library that lets you use the GPIO in the Jetson Nano is namedJetson.GPIO. It is located in /opt/nvidia/jetson-gpio/lib/python. The Jetson.GPIO API instructions can be found in /opt/nvidia/jetson-gpio/doc/README.txt. I recommend you read through it and also check the examples.

Instructions to use the library, taken from here, are as follows.

a) 
b) In your python script, add the library directories to the path where python will search for libraries:

```python
import sys

sys.path.append('/opt/nvidia/jetson-gpio/lib/python')
sys.path.append('/opt/nvidia/jetson-gpio/lib/python/Jetson/GPIO')
```

c) Now proceed to import the library

```python
import Jetson.GPIO as GPIO
```

d) To check if the library is working correctly, try:

```python
mode = GPIO.getmode()
print(mode) 
```

which should output any of 4: GPIO.BOARD, GPIO.BCM, GPIO.CVM, GPIO.TEGRA_SOC or
None




