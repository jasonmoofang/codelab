# "Lazy robot" that stays still until you bump a touch sensor
# bumping the right touch sensor gets the right wheel to spin for a time
# bumping the left gets the left wheel to do likewise. Logic is
# relatively complex because we need to keep time for both wheels
# simultaneously, not sure if we want to use this.

from ch.aplu.nxt import NxtRobot, Motor, MotorPort, TouchSensor, SensorPort, Tools

robot = NxtRobot()
motor1 = Motor(MotorPort.B)
motor2 = Motor(MotorPort.C)
ts1 = TouchSensor(SensorPort.S1)
ts2 = TouchSensor(SensorPort.S2)
robot.addPart(motor1)
robot.addPart(motor2)
robot.addPart(ts1)
robot.addPart(ts2)

m1counter = 0
m2counter = 1
while true:
    if (ts1.isPressed()):
        if (m1counter == 0):
            motor1.forward()
        m1counter = 5
    if (ts2.isPressed()):
        if (m2counter == 0):
            motor2.forward()
        m2counter = 5
    if (m1counter == 0):
        motor1.stop()
    else:
        m1counter = m1counter - 1
    if (m2counter == 0):
        motor2.stop()
    else:
        m2counter = m2counter - 1
    Tools.delay(500)