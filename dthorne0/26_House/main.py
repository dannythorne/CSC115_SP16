import turtle
print("Danny Thorne")
print("Draw a house using custom functions.")

def drawSquare(t,n):
    for i in range(4):
        t.forward(n)
        t.left(90)

def moveTo(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def drawTriangle(t,n):
    for i in range(3):
        t.forward(n)
        t.left(120)

########################################

wn = turtle.Screen()
t = turtle.Turtle()
t.speed(5)

x0 = -200
y0 = -400

moveTo(t,x0,y0)
drawSquare(t,400)

moveTo( t, x0+50, y0+50 )
drawSquare( t, 67)

moveTo( t, x0+400-50-67, t.ycor())
drawSquare( t, 67)

moveTo( t, x0+200-50, y0)
drawSquare( t, 100)

moveTo( t, x0-50, y0+400)
drawTriangle( t, 500)

wn.exitonclick()
