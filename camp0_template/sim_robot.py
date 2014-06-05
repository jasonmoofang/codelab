from ch.aplu.nxtsim import *
from java.awt import Point, Color

NxtContext.init()
mesh_hbar = [Point(200, 10), Point(-200, 10), 
             Point(-200, -10), Point(200, -10)]
mesh_vbar = [Point(10, 200), Point(-10, 200),
             Point(-10, -200), Point(10, -200)]
NxtContext.useTarget("sprites/bar0.gif", 
                     mesh_hbar, 250, 100)
NxtContext.useTarget("sprites/bar0.gif", 
                     mesh_hbar, 250, 400)
NxtContext.useTarget("sprites/bar1.gif", 
                     mesh_vbar, 100, 250)
NxtContext.useTarget("sprites/bar1.gif", 
                     mesh_vbar, 400, 250)

robot = NxtRobot()
motor1 = Motor(MotorPort.A)
motor2 = Motor(MotorPort.B)
robot.addPart(motor1)
robot.addPart(motor2)
us = UltrasonicSensor(SensorPort.S1)
robot.addPart(us)

def start_forward(m1, m2):
    m1.stop()
    m2.stop()
    m1.forward()
    m2.forward()
    
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

start_forward(motor1, motor2)
while True: 
    continue
