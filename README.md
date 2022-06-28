## I2C and the PCA9685 PWM chip

Install [PCA9685-driver](https://github.com/voidpp/PCA9685-driver):

```bash 
sudo apt-get install build-essential libi2c-dev i2c-tools python-dev libffi-dev
pip install PCA9685-driver
```

Connect PCA9685 to I2C Bus 1, pin header J41:

PCA9685 SDA <---> SDA1 pin 3 (Jetson Nano)
PCA9685 SCL <---> SCL1 pin 5 (Jetson Nano)

Check I2C devices:

```bash
nvidia@nvidia-desktop: sudo i2cdetect -y -r 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: 40 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: 70 -- -- -- -- -- -- --                         
```
The 40 represents 0x40, which is the default address of PCA9685 chip.

Add yourself to i2c group and reboot:

```bash
sudo usermod -a -G i2c username
sudo reboot
```

Check your group settings. Note i2c appears:

```bash
vidia@nvidia-desktop:~/repositories/nano_gpio$ groups
nvidia adm cdrom sudo audio dip video plugdev i2c lpadmin gdm sambashare gpio
```

Finally run pca9685_tests.py 

```bash
python pca9685_tests.py
```

## Jetson Nano GPIO

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

## VRPN Client ROS on Jetson Nano

If you are trying to connect an Optitrack Motion Tracker system using Motiv, the [ROS VRPN CLient](https://github.com/ros-drivers/vrpn_client_ros.git) will come useful. To install it on Jetson Nano follow:

1) Install ROS Melodic follwoing [this tutorial](https://www.stereolabs.com/blog/ros-and-nvidia-jetson-nano/).

2) Create a catkin workspace, and clone vrpn_client_ros inside the source folder and caktin_make:

```bash
cd ~/catkin_ws/src
git clone -b kinetic-devel https://github.com/ros-drivers/vrpn_client_ros.git
cd ..
catkin_make
source devel/setup.bash
```

(this was found in [this tutorial](https://answers.ros.org/question/297054/vrpn_client_ros-unable-to-locate-package/).

3) if it fails (probably will fail) find dependencies using rosdep :
Enter the catkin_ws folder and:

```bash
cd catkin_ws
rosdep install --from-paths .
```

retry again step 2). catkin_make command should work and vrpn be installed.

(this was found here https://answers.ros.org/question/227267/catkin_make-error-when-using-vrpn_client_ros/)

4) tests vrpn:

```bash
roslaunch vrpn_client_ros sample.launch server:=<ip address>
```

Where <ip address> is the IP address of the computer running Motive with which you should be on the same network.

## Other resources

On instaling Tensorflow, Pytorch, Keras and the PCA9685 PWM driver click [here](https://medium.com/@feicheung2016/getting-started-with-jetson-nano-and-autonomous-donkey-car-d4f25bbd1c83).
To see hardware PWM devices [available](https://devtalk.nvidia.com/default/topic/1049655/jetson-nano/how-do-i-use-pwm-on-jetson-nano-/post/5328800/#5328800)
Interesting links:
- [Save ~1GB Memory on Jetson Nano](https://www.zaferarican.com/post/how-to-save-1gb-memory-on-jetson-nano-by-installing-lubuntu-desktop)
- [Docker related](https://blog.hypriot.com/post/nvidia-jetson-nano-intro/)


