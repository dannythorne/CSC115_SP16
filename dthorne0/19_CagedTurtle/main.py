import turtle
import random

print("Danny Thorne")
print("Caged Turtle Example")

wn = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

w = wn.window_width()
h = wn.window_height()

for i in range(2000):
    t.forward(10)
    if t.xcor() >= wn.window_width()/2:
        t.goto( random.randrange( w) - w/2
              , random.randrange( h) - h/2 )
        t.left( random.randrange(360))
    if t.xcor() <= -wn.window_width()/2:
        t.goto( random.randrange( w) - w/2
              , random.randrange( h) - h/2 )
        t.left( random.randrange(360))
    if t.ycor() >= wn.window_height()/2:
        t.goto( random.randrange( w) - w/2
              , random.randrange( h) - h/2 )
        t.left( random.randrange(360))
    if t.ycor() <= -wn.window_height()/2:
        t.goto( random.randrange( w) - w/2
              , random.randrange( h) - h/2 )
        t.left( random.randrange(360))



wn.exitonclick()