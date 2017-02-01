import RPi.GPIO as GPIO
import time

# starting the GPIO and setting warnings to false
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Sensors being set to GPIO
TRIG = 23   # sensor 1 output - connected to trig pin
ECHO = 24   # sensor 1 input  - connected to echo pin
DELTA = 17  # sensor 2 output - connected to trig pin
BRAVO = 27  # sensor 2 input  - connected to echo pin

# initializing/ setting up the sensors 
GPIO.setup(TRIG, GPIO.OUT)      
GPIO.setup(ECHO, GPIO.IN)
print "Sensor 1 Online"
GPIO.setup(DELTA, GPIO.OUT)
GPIO.setup(BRAVO, GPIO.IN)
print "Sensor 2 Online"
print ""

# don't edit anything above this comment

# defining variables
sensorSleep = 0.2       # change this for faster or slower output.
sensorSleep2 = 0.0001   # necessary buffer time - don't change this
arrayOne = []           # array for sensor 1
arrayTwo = []           # array for sensor 2
counterOne = 0          # counter for loop in sensor 1
counterTwo = 0          # counter for loop in sensor 2

# the actual program
print "Starting the While Loop"
print " "
while True:  # infinite loop

    # kills the loop after 100 iterations (change this later for testing purposes at the moment)
    if counterTwo == 100:
        break
    
    # ==============================================================================
    # Sensor 1
    # ==============================================================================
    
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

    # printing the distance of sensor 1
    if 1 < distanceOne < 10000:
        counterOne = counterOne + 1
        print '1)', distanceOne
        arrayOne.append(distanceOne) # adding each iteration to arrayOne
    else:
        print "Out of Range - 1"

    # =============================================================================
    # Sensor 2
    # =============================================================================
    
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

    # printing the distance of sensor 2
    if 1 < distanceTwo < 10000:
        counterTwo = counterTwo + 1
        print "2)", distanceTwo
        print ' '
        arrayTwo.append(distanceTwo) # adding each iteration to arrayTwo
    else:
        print "Out of Range - 2"
        print ' '

sumOne = sum(arrayOne)
averageOne = sumOne/100
print 'Sensor One Average:'
print averageOne

sumTwo = sum(arrayTwo)
averageTwo = sumTwo/100
print 'Sensor Two Average:'
print averageTwo
