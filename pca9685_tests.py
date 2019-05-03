# This is a simple program to tests the PCA9685_driver found in 
#                 https://github.com/voidpp/PCA9685-driver
# 
# To run this code use:
# Install pca9685_driver library
#    https://github.com/voidpp/PCA9685-driver
# add your user to i2c group and reboot:
#    https://medium.com/@feicheung2016/getting-started-with-jetson-nano-and-autonomous-donkey-car-d4f25bbd1c83
# 

import sys

sys.path.append('/opt/nvidia/jetson-gpio/lib/python')
sys.path.append('/opt/nvidia/jetson-gpio/lib/python/Jetson/GPIO')
sys.path.append('/home/nvidia/repositories/nano_gpio/gpio_env/lib/python2.7/site-packages/periphery/')

import Jetson.GPIO as GPIO
from pca9685_driver import Device

def set_duty_cycle(pwmdev, channel, dt):
    """
    @pwmdev a Device class object already configured
    @channel Channel or PIN number in PCA9685 to configure 0-15
    @dt desired duty cycle
    """
    val = (dt*4095)//100
    pwmdev.set_pwm(channel,val)



# SET GPIO mode to BOARD
GPIO.setmode(GPIO.BOARD)
mode = GPIO.getmode()
print(mode)

# discover I2C devices
i2c_devs = Device.get_i2c_bus_numbers()
print("The following /dev/i2c-* devices were found:\n{}".format(i2c_devs))

# Create I2C device
working_devs = list()
print("Looking out which /dev/i2c-* devices is connected to PCA9685")
for dev in i2c_devs:
    try:
        pca9685 = Device(0x40,dev)
        # Set duty cycle
        pca9685.set_pwm(5, 2047)

        # set pwm freq
        pca9685.set_pwm_frequency(1000)
        print("Device {} works!".format(dev))
        working_devs.append(dev)
    except:
        print("Device {} does not work.".format(dev))

# Select any working device, for example, the first one
print("Configuring PCA9685 connected to /dev/i2c-{} device.".format(working_devs[0]))
pca9685 = Device(0x40, working_devs[0])



# Set duty cycle
pca9685.set_pwm(0, 2047)

# set pwm freq
pca9685.set_pwm_frequency(1000)

# set by duty cycle: pin 0, 5% duty cycle 
set_duty_cycle(pca9685,1,5)

# set pins 5 - 14 in increasing duty cycle from 10% to 60%
pins = [5,6,7,8,9,10,11,12,13,14,15]
dt_range = [0,10,20,30,40,50,60,70,80,90,100]

for pin, dt in zip(pins, dt_range):
    set_duty_cycle(pca9685,pin,dt)

print("Configured! Bye!")
