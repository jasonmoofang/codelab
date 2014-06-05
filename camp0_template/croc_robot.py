from ch.aplu.nxt import *

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
    
while True:
    move_forward(motor1, motor2, 500)
    turn(motor1, motor2, 500)
    move_backward(motor1, motor2, 500)
    snap_jaw(jaw, 3)