# A simple maze-traversing two-wheeled robot
# that does the additional aggressive thing of
# open firing on anything that appears before it
# suddenly!

from ch.aplu.nxt import NxtContext, NxtRobot, Gear, TouchSensor, SensorPort, Tools, LightSensor

robot = NxtRobot()
gunmotor = Motor(MotorPort.A)
motor1 = Motor(MotorPort.B)
motor2 = Motor(MotorPort.C)
ts1 = TouchSensor(SensorPort.S1)
ts2 = TouchSensor(SensorPort.S2)
us = UltrasonicSensor(SensorPort.S3)
robot.addPart(gunmotor)
robot.addPart(motor1)
robot.addPart(motor2)
robot.addPart(ts1)
robot.addPart(ts2)
robot.addPart(ls1)


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
  
def stopfor(m1, m2, t):
    m1.stop(t)
    m2.stop(t)

start_forward(m1, m2)
last_us_distance = -1
while true:
    t1 = ts1.isPressed()
    t2 = ts2.isPressed()
    if (t1 and t2):
        move_backward(motor1, motor2, 500)
        turn(motor1, motor2, 400)
        start_forward(motor1, motor2)
    else:
        if t1:
            move_backward(motor1, motor2, 500)
            turn(motor1, motor2, 400)
            start_forward(motor1, motor2)
        elif t2:
            move_backward(motor1, motor2, 500)
            turn(motor2, motor1, 400)
            start_forward(motor1, motor2)

    # if something appears close to sensor suddenly
    if (last_us_distance != -1 && last_us_distance - us.getDistance() > 50):
        stopfor(motor1, motor2, 1000)
        # shoot it!
        gunmotor.forward()
        Tools.delay(500)
    last_us_distance = us.getDistance();
    Tools.delay(20)
  
