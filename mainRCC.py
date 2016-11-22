import RPi.GPIO as GPIO
import time

# starting the GPIO and setting warnings to false
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Sensors being set to GPIO
TRIG = 23  # sensor 1
ECHO = 24
DELTA = 17  # sensor 2
BRAVO = 27

# initializing/ setting up the sensors
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
print "Sensor 1 Online"
GPIO.setup(DELTA, GPIO.OUT)
GPIO.setup(BRAVO, GPIO.IN)
print "Sensor 2 Online"
print ""

# variables
sensorSleep = 0.15  # change this for faster or slower output.
sensorSleep2 = 0.0001  # largely ignore this
sleep3 = 5  # for button pausing
sOneArray = []  # array for sensor 1
sTwoArray = []  # array for sensor 2
counterOne = 0  # counter for loop in sensor 1
counterTwo = 0  # counter for loop in sensor 2
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
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    # defining distance
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    # distane = (distance - 0.5) --- Remove this later?

    # printing the distance of sensor 1
    if 2 < distance < 400:
        print '1:', distance
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
        pulse_startT = time.time()

    while GPIO.input(BRAVO) == 1:
        pulse_endT = time.time()

    # defining distance
    pulse_durationT = pulse_endT - pulse_startT
    distanceT = pulse_durationT * 17150
    distanceT = round(distanceT, 2)
    # distaneT = (distanceT - 0.5) --- Remove this later?

    # printing the distance of sensor 2
    if 2 < distanceT < 400:
        print "2:", distanceT
        print ' '
    else:
        print "Out of Range - 2"
        print ' '
