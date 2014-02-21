from ch.aplu.nxtsim import NxtRobot, Motor, MotorPort, Tools, TouchSensor, SensorPort, NxtContext

NxtContext.init()
NxtContext.showNavigationBar();
NxtContext.useObstacle("sprites/bar0.gif", 250, 200);
NxtContext.useObstacle("sprites/bar1.gif", 400, 250);
NxtContext.useObstacle("sprites/bar2.gif", 250, 400);
NxtContext.useObstacle("sprites/bar3.gif", 100, 250);

robot = NxtRobot()

motA = Motor(MotorPort.A)
motB = Motor(MotorPort.B)
sensor = TouchSensor(SensorPort.S3)

robot.addPart(motA)
robot.addPart(motB)
robot.addPart(sensor)

def start_forward():
    motA.stop()
    motB.stop()
    motA.forward()
    motB.forward()

def move_backward(delay):
    motA.stop()
    motB.stop()
    motA.backward()
    motB.backward()
    Tools.delay(delay)

def turn_right(delay):
    motA.stop()
    motB.stop()
    motA.backward()
    motB.forward()
    Tools.delay(delay)

start_forward()
while (True):
    if sensor.isPressed():
        move_backward(1200)
        turn_right(750)
        start_forward()

