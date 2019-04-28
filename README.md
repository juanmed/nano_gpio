# Jetson Nano GPIO

This repository contains several examples on using the GPIO pins and libraries (Jetson.GPIO) in the Jetson Nano.

It is assumed you already went throught the Jetson Nano quick setup process and have the Ubuntu image running.

To start off, the library that lets you use the GPIO in the Jetson Nano is namedJetson.GPIO. It is located in /opt/nvidia/jetson-gpio/lib/python. The Jetson.GPIO API instructions can be found in /opt/nvidia/jetson-gpio/doc/README.txt. I recommend you read through it and also check the examples.

Instructions to use the library, taken in part from [here](https://github.com/NVIDIA-AI-IOT/jetbot/issues/18), are as follows.

a) Execute the following from a terminal on your Jetson

```bash
sudo groupadd -f -r gpio
sudo usermod -a -G gpio $USER
sudo cp /opt/nvidia/jetson-gpio/etc/99-gpio.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules && sudo udevadm trigger
```
Then, reboot the Jetson

```bash
sudo reboot now
```

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



## Other resources

On instaling Tensorflow, Pytorch, Keras and the PCA9685 PWM driver click [here](https://medium.com/@feicheung2016/getting-started-with-jetson-nano-and-autonomous-donkey-car-d4f25bbd1c83).
To see hardware PWM devices [available](https://devtalk.nvidia.com/default/topic/1049655/jetson-nano/how-do-i-use-pwm-on-jetson-nano-/post/5328800/#5328800)


