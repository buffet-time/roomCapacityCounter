import RPi.GPIO as GPIO
import time

sensorSleep = 0.15       #change this for faster or slower output.
sensorSleep2 = 0

#starting the GPIO and setting warnings to false
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Sensors being set to GPIO
TRIG = 23      #sensor 1
ECHO = 24
DELTA = 17     #sensor 2
BRAVO = 27

#intializing/ setting up the sensors
print("Sensor 1 Online")
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
time.sleep(0.1) # failsafe
print("Sensor 2 Online")
GPIO.setup(DELTA,GPIO.OUT)
GPIO.setup(BRAVO,GPIO.IN)


#the actual program
time.sleep(1) #this is for readabilities sake... Remove later on.
while True: #while True means infinite loop (unless you set a False.

    #Sensor 1
    GPIO.output(TRIG, False)
    time.sleep(sensorSleep)
    GPIO.output(TRIG,True)
    time.sleep(sensorSleep2)
    GPIO.output(TRIG,False)

    while GPIO.input(ECHO)==0:
        pulse_start=time.time()

    while GPIO.input(ECHO)==1:
        pulse_end=time.time()

    #defining distance
    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17150
    distance=round(distance,2)
    distane=(distance-0.5)
    
    #printing the distance of sensor 1
    if distance>2 and distance<400:
        print ('1:',distance)
    else:
        print ("Error 1")

    #Sensor 2
    GPIO.output(DELTA, False)
    time.sleep(sensorSleep)
    GPIO.output(DELTA,True)
    time.sleep(sensorSleep2)
    GPIO.output(DELTA,False)

    while GPIO.input(BRAVO)==0:
        pulse_startT=time.time()

    while GPIO.input(BRAVO)==1:
        pulse_endT=time.time()
    

    #defining distance
    pulse_durationT=pulse_endT-pulse_startT
    distanceT=pulse_durationT*17150
    distanceT=round(distanceT,2)
    distaneT=(distanceT-0.5)
    
    #printing the distance of sensor 2
    if distanceT>2 and distanceT<400:
        print("2:",distanceT)
        print(' ')
    else:
        print("Error 2")
        print(' ')
