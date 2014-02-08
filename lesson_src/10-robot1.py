# Import the stuff we need:
from ch.aplu.nxtsim import NxtRobot, Motor, MotorPort, Tools

# Make a robot object!
robot = NxtRobot()

# Make motor objects!
motA = Motor(MotorPort.A)
motB = Motor(MotorPort.B)

# Add motoro to robot!
robot.addPart(motA)
robot.addPart(motB)

# move the robot forward!
motA.forward()
motB.forward()
Tools.delay(2000)

# pause!
motA.stop()
motB.stop()
Tools.delay(2000)

# turn the robot!
motA.backward()
motB.forward()
Tools.delay(2000)

# pause!
motA.stop()
motB.stop()
Tools.delay(2000)

# move the robot backward!
motA.backward()
motB.backward()
Tools.delay(2000)

# finish!
robot.exit()
