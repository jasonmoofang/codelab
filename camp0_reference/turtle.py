from ch.aplu.turtle import *

ann = Turtle()
ann.setPenColor("red")

#square
ann.forward(100)
ann.right(90)
ann.forward(100)
ann.right(90)
ann.forward(100)
ann.right(90)
ann.forward(100)

#triangle
ann.setPenColor("blue")
ann.forward(100)
ann.right(120)
ann.forward(100)
ann.right(120)
ann.forward(100)

#hexagon
ann.setPenColor("green")
for i in range(6):
    ann.forward(100)
    ann.right(60)    

#star
for i in range(5):
    ann.forward(100)
    ann.right(144)

#spiralling star
for i in range(20):
    ann.forward(i * 10)
    ann.right(144)
    
#intricate star
for i in range(50):
    ann.forward(100)
    ann.right(123)