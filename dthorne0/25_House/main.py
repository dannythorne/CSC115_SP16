import turtle

print("Danny Thorne")
print("Picture of a House")

wn = turtle.Screen()
t = turtle.Turtle()

x0 = -200
y0 = -300

t.penup()
t.goto(x0,y0) # coords of bottom left corner of house
t.pendown()

for i in range(4):
    t.forward(400)
    t.left(90)

t.penup()
t.goto(x0+50,y0+50)
t.pendown()

for i in range(4):
    t.forward(67)
    t.left(90)

t.penup()
t.goto(x0+400-50-67,t.ycor())
t.pendown()

for i in range(4):
    t.forward(67)
    t.left(90)

t.penup()
t.goto(x0+200-50,y0)
t.pendown()

for i in range(4):
    t.forward(100)
    t.left(90)

wn.exitonclick()