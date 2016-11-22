import RPi.GPIO as GPIO
import time

# starting the GPIO and setting warnings to false
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Sensors being set to GPIO
TRIG = 23   # sensor 1 output
ECHO = 24   # sensor 1 input
DELTA = 17  # sensor 2 output
BRAVO = 27  # sensor 2 input

# initializing/ setting up the sensors
GPIO.setup(TRIG, GPIO.OUT)      
GPIO.setup(ECHO, GPIO.IN)
print "Sensor 1 Online"
GPIO.setup(DELTA, GPIO.OUT)
GPIO.setup(BRAVO, GPIO.IN)
print "Sensor 2 Online"
print ""

# defining variables
sensorSleep = 0.15      # change this for faster or slower output.
sensorSleep2 = 0.0001   # largely ignore this
sleep3 = 5              # for button pausing
arrayOne = []           # array for sensor 1
arrayTwo = []           # array for sensor 2
counterOne = 0          # counter for loop in sensor 1
counterTwo = 0          # counter for loop in sensor 2
#  ++counterOne     <--  correct formatting

# the actual program
print "Starting the While Loop"
print " "
while True:  # infinite loop

    #    if
    # time.sleep(sleep3)

    # Sensor 1
    time.sleep(sensorSleep)
    GPIO.output(TRIG, False)
    time.sleep(sensorSleep2)
    GPIO.output(TRIG, True)
    time.sleep(sensorSleep2)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulseStartOne = time.time()

    while GPIO.input(ECHO) == 1:
        pulseEndOne = time.time()

    # defining distance
    pulseDurationOne = pulseEndOne - pulseStartOne
    distanceOne = pulseDurationOne * 17150
    distanceOne = round(distanceOne, 2)
    # distane = (distance - 0.5) --- Remove this later?

    # printing the distance of sensor 1
    if 2 < distanceOne < 400:
        print '1:', distanceOne
    else:
        print "Out of Range - 1"

    # Sensor 2
    time.sleep(sensorSleep)
    GPIO.output(DELTA, False)
    time.sleep(sensorSleep2)
    GPIO.output(DELTA, True)
    time.sleep(sensorSleep2)
    GPIO.output(DELTA, False)

    while GPIO.input(BRAVO) == 0:
        pulseStartTwo = time.time()

    while GPIO.input(BRAVO) == 1:
        pulseEndTwo = time.time()

    # defining distance
    pulseDurationTwo = pulseEndTwo - pulseStartTwo
    distanceTwo = pulseDurationTwo * 17150
    distanceTwo = round(distanceTwo, 2)
    # distaneT = (distanceT - 0.5) --- Remove this later?

    # printing the distance of sensor 2
    if 2 < distanceTwo < 400:
        print "2:", distanceTwo
        print ' '
    else:
        print "Out of Range - 2"
        print ' '
