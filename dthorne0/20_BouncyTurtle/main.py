import turtle
import random

print("Danny Thorne")
print("Bouncing Turtle Example")

wn = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

w = 0.95*wn.window_width()
h = 0.95*wn.window_height()

t.left(random.randrange(360))

for i in range(10000):
    t.forward(10)
    if t.xcor() >= w/2:
        theta = t.heading()
        print("Went off the right side heading", theta)
        t.right( theta)
        t.left( 180 - theta)
    if t.xcor() <= -w/2:
        theta = t.heading()
        print("Went off the left side heading", theta)
        t.right( theta)
        t.left( 180 - theta)
    if t.ycor() >= h/2:
        theta = t.heading()
        print("Went off the top side heading", theta)
        t.right(theta)
        t.left(-theta)
    if t.ycor() <= -h/2:
        theta = t.heading()
        print("Went off the bottom side heading", theta)
        t.right(theta)
        t.left(-theta)

wn.exitonclick()