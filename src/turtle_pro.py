import turtle
wn = turtle.Screen()
wn.bgcolor("gray")
tess = turtle.Turtle()
tess.color("yellow")
tess.shape("turtle")

dist = 5
tess.up()
for i in range(500):
    tess.stamp()
    tess.forward(dist)
    tess.right(90)
    dist = dist + 0.5

wn.exitonclick()