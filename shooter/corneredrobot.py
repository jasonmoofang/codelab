# A cautious robot that stays still until approached from front
# backs away each time it is approached from front 5 times
# if it senses it is backed against the wall it starts shooting briefly
# after backing away a full 5 times goes berserk and shoots all ammo left

from ch.aplu.nxt import NxtRobot, Motor, MotorPort, UltrasonicSensor, TouchSensor, SensorPort, Tools, LightSensor

robot = NxtRobot()
gunmotor = Motor(MotorPort.A)
motor1 = Motor(MotorPort.B)
motor2 = Motor(MotorPort.C)
ts1 = TouchSensor(SensorPort.S2)
ts2 = TouchSensor(SensorPort.S3)
us = UltrasonicSensor(SensorPort.S4)
robot.addPart(gunmotor)
robot.addPart(motor1)
robot.addPart(motor2)
robot.addPart(ts1)
robot.addPart(ts2)
robot.addPart(us)

def back_away(m1, m2, t):
    m1.stop()
    m2.stop()
    m1.backward
    m2.backward()
    Tools.delay(t)
    m1.stop()
    m2.stop()

def shoot(m, t):
    m.forward()
    Tools.delay(t)
    m.stop()

for i in range(5):
    # wait until something approaches
    while(us.getDistance() > 80):
        Tools.delay(20)
    # back away when it does
    back_away(m1, m2, 1000)
    if ts1.isPressed() or ts2.isPressed():
        # shoot if backed against wall!
        shoot(gunmotor, 1000)

# after we're forced back 5 times
# we just open fire!
shoot(gunmotor, 10000)
robot.exit()