import RPi.GPIO as GPIO
import tplink_smartplug_py3 as plug

GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.IN)
GPIO.setup(21,GPIO.OUT)

while True:
    if GPIO.input(20)==GPIO.HIGH:
        GPIO.output(21,GPIO.HIGH)
        plug.control('172.41.195.22', 'on')
#        plug.control('172.41.195.22', 'off')
    else:
        GPIO.output(21,GPIO.LOW)
