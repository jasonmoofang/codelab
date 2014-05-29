# Straightforward program. Robot moves forward until detecting something
# close on ultrasonic, backs away, turns, repeats

from ch.aplu.nxt import NxtRobot, Motor, MotorPort, TouchSensor, SensorPort, Tools

robot = NxtRobot()
motor1 = Motor(MotorPort.B)
motor2 = Motor(MotorPort.C)
us = UltrasonicSensor(SensorPort.S3)
robot.addPart(motor1)
robot.addPart(motor2)
robot.addPart(us)

def move_backward(m1, m2, t):
    m1.stop()
    m2.stop()
    m1.backward
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

def start_forward(m1, m2):
    m1.forward()
    m2.forward()

start_forward(motor1, motor2)
while true:
    if (us.getDistance() < 80):
        move_backward(motor1, motor2, 500)
        turn(motor1, motor2, 1000)
        start_forward(motor1, motor2)
    Tools.delay(20)
