import turtle

wn = turtle.Screen()
wn.bgcolor("lavenderblush") # https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm
t = turtle.Turtle()

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

t.color("blue")
t.pensize(3)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

t.penup()
t.forward(150)
t.pendown()
t.color("red")
t.forward(64)

wn.exitonclick()