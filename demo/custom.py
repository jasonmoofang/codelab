# SimEx08.py
# One light sensor, event driven

from ch.aplu.nxt import NxtRobot, Gear, UltrasonicSensor, SensorPort, NxtContext, TouchSensor, Motor, MotorPort, Tools
from random import randint

robot = NxtRobot()
jaw = Motor(MotorPort.A)
us = UltrasonicSensor(SensorPort.S4)
motor1 = Motor(MotorPort.B)
motor2 = Motor(MotorPort.C)
ts1 = TouchSensor(SensorPort.S1)
ts2 = TouchSensor(SensorPort.S2)
robot.addPart(jaw)
robot.addPart(us)
robot.addPart(ts1)
robot.addPart(ts2)
robot.addPart(motor1)
robot.addPart(motor2)

def motor_forward(motor, t):
	motor.stop()
	motor.forward()
	Tools.delay(t)
	motor.stop()

def motor_backward(motor, t):
	motor.stop()
	motor.backward()
	Tools.delay(t)
	motor.stop()
	
def move_forward(m1, m2, t):
	m1.stop()
	m2.stop()
	m1.forward()
	m2.forward()
	Tools.delay(t)
	m1.stop()
	m2.stop()
	
def move_backward(m1, m2, t):
	m1.stop()
	m2.stop()
	m1.backward()
	m2.backward()
	Tools.delay(t)
	m1.stop()
	m2.stop()
	
def turn(m1, m2, t):
	m1.stop()
	m2.stop()
	m1.backward()
	m2.forward()
	Tools.delay(t)
	m1.stop()
	m2.stop()
	
def snap_jaw(jaw, i):
	for j in range(0, i):
		jaw.setSpeed(50)
		jaw.forward()
		Tools.delay(130)
		jaw.stop()
		Tools.delay(100)
		jaw.backward()
		Tools.delay(130)
		jaw.stop()
		Tools.delay(100)
	# sync the jaw back to closed
	jaw.backward()
	Tools.delay(500) #close jaw
	jaw.stop()
	Tools.delay(100)
	jaw.forward()
	Tools.delay(100) #open it slightly
	jaw.stop()
	Tools.delay(100)
	
def sync_legs(l1, l2, s1, s2, desync_offset):
	l1.backward() # forward
	l2.backward()
	s1pressed = False
	s2pressed = False
	while not (s1pressed and s2pressed):
		if (s1.isPressed()):
			s1pressed = True
			l1.stop()
		if (s2.isPressed()):
			s2pressed = True
			l2.stop()
	motor_forward(l1, desync_offset) # add desired desync

sync_legs(motor1, motor2, ts1, ts2, 400) # 400 desync makes it non-butterfly
while True:
	if (us.getDistance() < 40):
		motor1.stop()
		motor2.stop()
		Tools.delay(1500)
		move_forward(motor1, motor2, 3000) # due to motor setup, forward is actually backward
		sync_legs(motor1, motor2, ts1, ts2, 0) # make it stand up
		snap_jaw(jaw, 3)
		if (randint(0,1) == 0):
			turn(motor1, motor2, 4000)
			sync_legs(motor1, motor2, ts1, ts2, 0)
			Tools.delay(1500)
			sync_legs(motor1, motor2, ts1, ts2, 400) # make it non butterfly
		else:
			turn(motor2, motor1, 4000)
			sync_legs(motor1, motor2, ts1, ts2, 0)
			Tools.delay(1500)
			sync_legs(motor1, motor2, ts1, ts2, 400) # make it non butterfly
	motor1.backward() # actually forward
	motor2.backward()
