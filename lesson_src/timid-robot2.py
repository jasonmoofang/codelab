# Import the stuff we need:
from ch.aplu.nxtsim import NxtRobot, Motor, MotorPort, Tools, LightSensor, SensorPort, NxtContext

NxtContext.useBackground("sprites/road.gif")

# Make a robot object!
robot = NxtRobot()

motA = Motor(MotorPort.A)
motB = Motor(MotorPort.B)
sensor = LightSensor(SensorPort.S3)

robot.addPart(motA)
robot.addPart(motB)
robot.addPart(sensor)

def step_forward():
    motA.setSpeed(50)
    motB.setSpeed(50)
    motA.forward()
    motB.forward()
    Tools.delay(1000)
    motA.stop()
    motB.stop()
    Tools.delay(300)

def run_backward():
    motA.setSpeed(100)
    motB.setSpeed(100)
    motA.backward()
    motB.backward()
    Tools.delay(1000)
    motA.stop()
    motB.stop()
    Tools.delay(300)

# sense for light, if it's bright step back three times! else move forward
while (True):
    if (sensor.getValue() < 800):
        step_forward()
    else:
        run_backward()
