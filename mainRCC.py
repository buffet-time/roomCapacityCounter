import RPi.GPIO as GPIO
import time

# starting the GPIO and setting warnings to false
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Sensors being set to GPIO
TRIG = 23   # sensor 1 output - connected to trig pin - don't change this
ECHO = 24   # sensor 1 input  - connected to echo pin - don't change this
DELTA = 17  # sensor 2 output - connected to trig pin - don't change this
BRAVO = 27  # sensor 2 input  - connected to echo pin - don't change this

# initializing/ setting up the sensors 
GPIO.setup(TRIG, GPIO.OUT)      
GPIO.setup(ECHO, GPIO.IN)
print "Sensor 1 Online"
GPIO.setup(DELTA, GPIO.OUT)
GPIO.setup(BRAVO, GPIO.IN)
print "Sensor 2 Online"
print ""

# defining variables
sensorSleep = 0.05      # change this for faster or slower output.
sensorSleep2 = 0.001    # necessary buffer time - don't change this
arrayOne = []           # array for sensor 1 - don't change this
arrayTwo = []           # array for sensor 2- don't change this
counter = 0             # counter for loop 1
arraySize = 100         # the number of items to be averaged - the larger the more accurate.

# ====================================
#       loop to calculate average
# ====================================

print "Starting the loop to calculate average"
print " "
while True:  

    # breaks the while loop after it reaches the integer in variable arraySize
    if counter == arraySize:
        break
    
    # ==========================
    #          Sensor 1
    # ==========================
    
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

    # calculating distance for sensor 1
    if True:
        arrayOne.append(distanceOne) # adding each iteration to arrayOne

    # =============================
    #           Sensor 2
    # =============================
    
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

    # calculating distance for sensor 2
    if True:
        arrayTwo.append(distanceTwo) # adding each iteration to arrayTwo
        counter += 1

# =========================================
#       end of loop to compute average
# =========================================

# averageOne is distance to the floor for sensor 1
sumOne = sum(arrayOne)
averageOne = sumOne/arraySize       

# averageTwo is distance to the floor for sensor 2
sumTwo = sum(arrayTwo)
averageTwo = sumTwo/arraySize

percentageAverageOne = round((averageOne / 10) * 6, 2)      # 60% of the average rounded to two decimals
percentageAverageTwo = round((averageTwo / 10) * 6, 2)      # 60% of the average rounded to two decimals

print str(percentageAverageOne)
print str(percentageAverageTwo)
print ''

# ======================================================
#                       main loop
# ======================================================

time.sleep(2) # for readability purposes

while True:

    if distanceOne < percentageAverageOne:      # for sensor 1: if the distance is smaller than the average
        print 'distance 1 is smaller'

    if distanceTwo < percentageAverageTwo:      # for sensor 2: if the distance is smaller than the average
        print 'distance 2 is smaller' 

    # ==============================
    #           Sensor 1
    # ==============================
    
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

    pulseDurationOne = pulseEndOne - pulseStartOne
    distanceOne = pulseDurationOne * 17150
    distanceOne = round(distanceOne, 2)

    if True:
        print '1)', distanceOne

    # =============================
    #           Sensor 2
    # =============================
    
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

    pulseDurationTwo = pulseEndTwo - pulseStartTwo
    distanceTwo = pulseDurationTwo * 17150
    distanceTwo = round(distanceTwo, 2)

    if True:
        print '2)', distanceTwo
        print ''
