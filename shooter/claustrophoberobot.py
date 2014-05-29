# Robot basically spins around while scanning with the ultrasonic sensor, looks for the
# direction with the least obstacles, and moves there

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
    
def move_forward(m1, m2, t):
    m1.stop()
    m2.stop()
    m1.forward()
    m2.forward()
    Tools.delay(t)

# start turning
start_turn(motor1, motor2)
# find largest us value
largest_us_value = 0
for i in range(20):
    us_value = us.getDistance()
    if (us_value > largest_us_value):
        largest_us_value = us_value
    Tools.delay(20)
# spin until facing direction of largest us value
while (us.getDistance() < largest_us_value):
    continue
# move in the discovered direction like a boss
move_forward(5000)