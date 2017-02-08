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

# defining variables
sensorSleep = 0.1       # change this for faster or slower output.
sensorSleep2 = 0.0001   # necessary buffer time - don't change this
arrayOne = []           # array for sensor 1
arrayTwo = []           # array for sensor 2
counterOne = 0          # counter for loop in sensor 1
counterTwo = 0          # counter for loop in sensor 2
arraySize = 10          # the number of items to be averaged

# ====================================
#       loop to calculate average
# ====================================

print "Starting the loop to calculate average"
print " "
while True:  

    # breaks the while loop after it reaches the integer in variable arraySize
    if counterTwo == arraySize:
        break
    
    # ==============================================================================
    #           Sensor 1
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

    # calculating distance for sensor 1
    if True:
        counterOne += 1
        arrayOne.append(distanceOne) # adding each iteration to arrayOne

    # =============================================================================
    #           Sensor 2
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

    # calculating distance for sensor 2
    if True:
        counterTwo += 1
        arrayTwo.append(distanceTwo) # adding each iteration to arrayTwo

# =========================================
#       end of loop to compute average
# =========================================

sumOne = sum(arrayOne)
averageOne = sumOne/arraySize

sumTwo = sum(arrayTwo)
averageTwo = sumTwo/arraySize

percentageAverageOne = averageOne / 10 * 4      # 40% of the average
percentageAverageTwo = averageTwo / 10 * 4      # 40% of the average

print str(percentageAverageOne)
print str(percentageAverageTwo)
print ''


# ===================
#    True loop  
# ===================

while True:
    
    # ==============================================================================
    #           Sensor 1
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

    if True:
        counterOne += 1
        print '1)', distanceOne

    # =============================================================================
    #           Sensor 2
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
    if True:
        counterTwo += 1
        print '2)', distanceTwo
        print ''
