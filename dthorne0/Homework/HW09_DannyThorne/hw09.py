import turtle

print("Danny Thorne")
print("HW09")

n = input("Enter number of squares to draw: ")
n = int(n)

wn = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

w = 0.95*wn.window_width()
s = w / (2*n)

t.penup()
t.backward(w/2)
t.pendown()

for i in range(n):
    t.forward(s)
    t.penup()
    t.forward(s)
    t.pendown()

t.penup()
t.backward(w)
t.pendown()

for i in range(n):
    t.left(90)
    t.forward(s)
    t.backward(s)
    t.right(90)
    t.penup()
    t.forward(2*s)
    t.pendown()

wn.getcanvas().postscript(file="hw09.eps",colormode="color")
wn.exitonclick()