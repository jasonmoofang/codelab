# simulator maze traversal

from ch.aplu.nxtsim import NxtContext, NxtRobot, TouchSensor, SensorPort, Tools, LightSensor

NxtContext.setLocation(10, 10)
NxtContext.setStartDirection(5)
NxtContext.setStartPosition(100, 240)
NxtContext.useObstacle(NxtContext.channel)
NxtContext.useBackground("sprites/channel.jpg")

robot = NxtRobot()
motor1 = Motor(MotorPort.A)
motor2 = Motor(MotorPort.B)
robot.addPart(gear)
ts1 = TouchSensor(SensorPort.S1) # right sensor
ts2 = TouchSensor(SensorPort.S2) # left sensor
robot.addPart(ts1)
robot.addPart(ts2)

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
while True:
    t1 = ts1.isPressed()
    t2 = ts2.isPressed()
    if (t1 and t2):
        move_backward(motor1, motor2, 500)
        turn(motor1, motor2, 400)
        start_forward(motor1, motor2)
    else:
        if t1:
            move_backward(motor1, motor2, 1000)
            turn(motor2, motor1, 800)
            start_forward(motor1, motor2)
        elif t2:
            move_backward(motor1, motor2, 1000)
            turn(motor1, motor2, 800)
            start_forward(motor1, motor2)

    Tools.delay(20)
 