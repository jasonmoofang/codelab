# Robot basically spins around while scanning with the ultrasonic sensor, pausing to shoot
# at anything it "sees"

from ch.aplu.nxt import NxtRobot, Motor, MotorPort, UltrasonicSensor, SensorPort, Tools

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

def stop(m1, m2, t):
    m1.stop()
    m2.stop()
    Tools.delay(t)

start_turn(motor1, motor2)
while true:
    if (us.getDistance() < 80):
        stop(motor1, motor2, 500)
        gunmotor.forward()
        Tools.delay(1000)
        gunmotor.stop()
        start_turn(motor1, motor2)
        Tools.delay(400) # don't shoot again for awhile
    Tools.delay(20)
