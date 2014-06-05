from ch.aplu.nxt import *

robot = NxtRobot()
gunmotor = Motor(MotorPort.A)
motor1 = Motor(MotorPort.B)
motor2 = Motor(MotorPort.C)
us = UltrasonicSensor(SensorPort.S4)
robot.addPart(gunmotor)
robot.addPart(motor1)
robot.addPart(motor2)
robot.addPart(us)

def start_turn(m1, m2):
    m1.stop()
    m2.stop()
    m1.backward()
    m2.forward()

start_turn(motor1, motor2)
while True:
    gunmotor.forward()
    Tools.delay(900)
    gunmotor.forward()
    Tools.delay(1000)
