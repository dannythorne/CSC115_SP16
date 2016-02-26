import turtle

print("Danny Thorne")
print("Polygons Example")

n = 7
angle = 360/n
sideLength = 100

wn = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

for i in range(n):
    t.forward(sideLength)
    t.left(angle)

wn.exitonclick()