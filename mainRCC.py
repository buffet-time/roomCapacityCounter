import RPi.GPIO as GPIO
import time

#setting up gpio and etc.
''' useless printing '''
print("Sensor 1 Booting up")
time.sleep(.25)
print("Sensor 2 Booting up")
time.sleep(.25)
print(".")
time.sleep(.25)
print("..")
time.sleep(.25)
print("...")
''' end of useless printing '''


#starting the GPIO and setting warnings to false
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Sensor 1 Hookup
TRIG = 23
ECHO = 24

#Sensor 2 Hookup
DELTA = 17
BRAVO = 27

#intializing/ setting up the sensors
print("Sensor 1 Online")
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
time.sleep(.25) #useless time inbetween
print("Sensor 2 Online")
GPIO.setup(DELTA,GPIO.OUT)
GPIO.setup(BRAVO,GPIO.IN)


#the actual program
while True: #while True means infinite loop (unless you set a False.

    #Sensor 1
    GPIO.output(TRIG, False)
    time.sleep(0.2) #change this and the time.sleep(###) in sensor 1 for slower output

    GPIO.output(TRIG,True)
    time.sleep(0.00001)
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
        print ("1: ",distance)
    else:
        print ("Error 1")

    #Sensor 2
    GPIO.output(DELTA, False)
    ''' waiting to settle and length is 19 characters with spaces '''
    time.sleep(0.2) #change this and the time.sleep(###) in sensor 1 for slower output

    GPIO.output(DELTA,True)
    time.sleep(0.00001)
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
        print("2: ",distanceT)
        print(' ')
    else:
        print("error 2")
        print(' ')
