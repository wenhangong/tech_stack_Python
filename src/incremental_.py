import turtle
import math
wn = turtle.Screen()
bob = turtle.Turtle()
bob.right(90)
bob.forward(40)
bob.left(90)
bob.forward(40)
bob.left(90)
bob.forward(40)
bob.left(90)
bob.forward(40)

dist = math.sqrt(40**2 / 2)
bob.right(135)
bob.forward(dist)
bob.right(90)
bob.forward(dist)

wn.exitonclick()