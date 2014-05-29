# Simple but fun idea. Press both touch sensors together to unleash balls

from ch.aplu.nxt import NxtRobot, Motor, MotorPort, TouchSensor, SensorPort, Tools

robot = NxtRobot()
gunmotor = Motor(MotorPort.A)
ts1 = TouchSensor(SensorPort.S1)
ts2 = TouchSensor(SensorPort.S2)
robot.addPart(gunmotor)
robot.addPart(ts1)
robot.addPart(ts2)

while true:
    if ts1.isPressed() and ts2.isPressed():
        gunmotor.forward()
    else:
        gunmotor.stop()