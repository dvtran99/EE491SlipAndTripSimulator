import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM

#Initialize dual PWM signals that share the same signal bus so operate as single PWM Signal over 2 pins
myPWM = "P8_13"
myPWM2 = "P8_19"

#Initialize digital output pins that dictate the direction the motors will spin
dir1 = "P8_10"
GPIO.setup(dir1, GPIO.OUT)
dir2 = "P8_12"
GPIO.setup(dir2, GPIO.OUT)
dir3 = "P8_14"
GPIO.setup(dir3, GPIO.OUT)
dir4 = "P8_16"
GPIO.setup(dir4, GPIO.OUT)

#Start a "Run simulation" loop
loop = 1
while loop == 1:
	#Enter in data needed for simulation
	requiredSpeed = float(input("Required Speed (cm/s) = "))
	requiredDistance = float(input("Required Distance (cm) = "))

	#Check to make sure the distance doesnt exceed our 15 cm maximum
	while requiredDistance > 15:
		print("Distance too High!")
		requiredDistance = float(input("Required Distance (cm) = "))

	#Choose direction of simulation
	print("Enter 1 for Forward, 2 for Backward, 3 for Right, 4 for Left")
	direction = float(input("Required Direction = "))

	#Radius of wheel (meters)
	#Our wheels have R = 50mm or 0.05m
	R = 0.05

	#Use to get appropiate duty cycle to achieve required speed
	#Can change this number to fine tune, right now its low due to no load
	maxRPM = 200
	maxSpeed = (2*3.14*R)/(maxRPM/60)

	#Get the run time of the simulation based off speed distance and circumference of wheel
	simTime = (requiredDistance/requiredSpeed)/(2*3.14*R)

	#Gets duty cycle and makes sure it doesnt go over 100%
	#The setting to 100% might be unnecessry, but added just to be safe
	dutyCycle = (requiredSpeed/(maxSpeed*100))*100
	if dutyCycle > 100:
		dutyCycle = 100
	
	#Calculates Return to Center Position Simulation Time with a 10% Duty Cycle
	simTime2 = simTime*dutyCycle/10

	#Gets sleep command from BBB to allow pauses
	from time import sleep

	#Based off the direction the user chose, set which of the 4 motors needs to be reversed and start the simulation
	#After simulation runs, waits 5 seconds, then returns to the original position at a slow speed (10% duty cycle)
	if direction == 1:
		GPIO.output(dir1, GPIO.HIGH)
		GPIO.output(dir3, GPIO.HIGH)
		PWM.start(myPWM, dutyCycle, 1000)
		PWM.start(myPWM2, dutyCycle, 1000)
		sleep(simTime)
		PWM.stop(myPWM)
		PWM.stop(myPWM2)
		GPIO.output(dir1, GPIO.LOW)
		GPIO.output(dir3, GPIO.LOW)
		sleep(5)
		GPIO.output(dir2, GPIO.HIGH)
		GPIO.output(dir4, GPIO.HIGH)
		PWM.start(myPWM, 10, 1000)
		PWM.start(myPWM2, 10, 1000)
		sleep(simTime2)
		PWM.stop(myPWM)
		PWM.stop(myPWM2)
		GPIO.output(dir2, GPIO.LOW)
		GPIO.output(dir4, GPIO.LOW)
	elif direction == 2:
		GPIO.output(dir2, GPIO.HIGH)
		GPIO.output(dir4, GPIO.HIGH)
		PWM.start(myPWM, dutyCycle, 1000)
		PWM.start(myPWM2, dutyCycle, 1000)
		sleep(simTime)
		PWM.stop(myPWM)
		PWM.stop(myPWM2)
		GPIO.output(dir2, GPIO.LOW)
		GPIO.output(dir4, GPIO.LOW)
		sleep(5)
		GPIO.output(dir1, GPIO.HIGH)
		GPIO.output(dir3, GPIO.HIGH)
		PWM.start(myPWM, 10, 1000)
		PWM.start(myPWM2, 10, 1000)
		sleep(simTime2)
		PWM.stop(myPWM)
		PWM.stop(myPWM2)
		GPIO.output(dir1, GPIO.LOW)
		GPIO.output3dir4, GPIO.LOW)
	elif direction == 3:
		GPIO.output(dir1, GPIO.HIGH)
		GPIO.output(dir2, GPIO.HIGH)
		PWM.start(myPWM, dutyCycle, 1000)
		PWM.start(myPWM2, dutyCycle, 1000)
		sleep(simTime)
		PWM.stop(myPWM)
		PWM.stop(myPWM2)
		GPIO.output(dir1, GPIO.LOW)
		GPIO.output(dir2, GPIO.LOW)
		sleep(5)
		GPIO.output(dir3, GPIO.HIGH)
		GPIO.output(dir4, GPIO.HIGH)
		PWM.start(myPWM, 10, 1000)
		PWM.start(myPWM2, 10, 1000)
		sleep(simTime2)
		PWM.stop(myPWM)
		PWM.stop(myPWM2)
		GPIO.output(dir3, GPIO.LOW)
		GPIO.output3dir4, GPIO.LOW)
	elif direction == 4:
		GPIO.output(dir3, GPIO.HIGH)
		GPIO.output(dir4, GPIO.HIGH)
		PWM.start(myPWM, dutyCycle, 1000)
		PWM.start(myPWM2, dutyCycle, 1000)
		sleep(simTime)
		PWM.stop(myPWM)
		PWM.stop(myPWM2)
		GPIO.output(dir3, GPIO.LOW)
		GPIO.output(dir4, GPIO.LOW)
		sleep(5)
		GPIO.output(dir1, GPIO.HIGH)
		GPIO.output(dir2, GPIO.HIGH)
		PWM.start(myPWM, 10, 1000)
		PWM.start(myPWM2, 10, 1000)
		sleep(simTime2)
		PWM.stop(myPWM)
		PWM.stop(myPWM2)
		GPIO.output(dir1, GPIO.LOW)
		GPIO.output3dir2, GPIO.LOW)
	
	#.cleanup() resets the PWM and GPIO pins so its a clean pin for the next simulation
	PWM.cleanup()
	GPIO.cleanup()

	#Asks if you want to run another simulation
	#This is just for convienence fo before GUI implementation
	loop = float(input("Another Simulation? (Yes = 1, No = 0)"))
	while loop != 0 or loop != 1:
		print("Please enter a 1 for Yes or 0 for No.")
		loop = float(input("Another Simulation? (Yes = 1, No = 0)"))
		