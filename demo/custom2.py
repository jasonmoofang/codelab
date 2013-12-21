# SimEx06.py
# Two touch sensors, complex track

import time
from ch.aplu.nxtsim import NxtContext, NxtRobot, Gear, TouchSensor, SensorPort, Tools, LightSensor

NxtContext.setLocation(10, 10)
NxtContext.setStartDirection(5)
NxtContext.setStartPosition(100, 240)
NxtContext.useObstacle(NxtContext.channel)
NxtContext.useBackground("sprites/channel.jpg")

robot = NxtRobot()
gear = Gear()
robot.addPart(gear)
ts1 = TouchSensor(SensorPort.S1) # right sensor
ts2 = TouchSensor(SensorPort.S2) # left sensor
ls1 = LightSensor(SensorPort.S3)
robot.addPart(ts1)
robot.addPart(ts2)
robot.addPart(ls1)
gear.forward()
lightsensor_timeout = False
while not robot.getGameGrid().isDisposed():
  if lightsensor_timeout != False and time.clock() > lightsensor_timeout:
      lightsensor_timeout = False
  t1 = ts1.isPressed()
  t2 = ts2.isPressed()
  if (t1 and t2):
    gear.backward(500)
    gear.left(400)
    gear.forward()
  else:
    if t1:
      gear.backward(500)
      gear.left(400)
      gear.forward()
    else:
      if t2:
        gear.backward(500)
        gear.right(100)
        gear.forward()
  if (ls1.getValue() < 990 and lightsensor_timeout == False):
    gear.left(4700)
    gear.forward(200)
    gear.forward()
    lightsensor_timeout = time.clock() + 2
  Tools.delay(20)
 
