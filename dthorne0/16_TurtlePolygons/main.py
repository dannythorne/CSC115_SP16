import turtle

print("Danny Thorne")
print("Turtle Polygons Example")

wn = turtle.Screen()
t = turtle.Turtle()

n = 100
angle = 360/n
r = 200
sideLength = 2*3.14159*r/n

t.penup()
t.right(90)
t.forward(r)
t.left(90)
t.pendown()

for i in range(n):
    t.forward(sideLength)
    t.left(angle)

wn.exitonclick()
