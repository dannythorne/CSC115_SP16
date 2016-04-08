import turtle

print("Danny Thorne")
print("Draw a House with Functions")

def drawSquare( t, x, y, n):
  moveTo(t,x,y)
  for i in range(4):
    t.forward(n)
    t.left(90)

def moveTo( t, x, y):
  t.penup()
  t.goto( x, y)
  t.pendown()

def drawTriangle( t, x, y, n):
  moveTo(t,x,y)
  for i in range(3):
    t.forward(n)
    t.left(120)

########################################

wn = turtle.Screen()
t = turtle.Turtle()
t.speed(5)

x0 = -200
y0 = -400

drawSquare( t, x0, y0, 400)
drawSquare( t, x0+50, y0+50, 67)
drawSquare( t, x0+400-50-67, t.ycor(), 67)
drawSquare( t, x0+200-50, y0, 100)
drawTriangle( t, x0-50, y0+400, 500)

wn.exitonclick()
