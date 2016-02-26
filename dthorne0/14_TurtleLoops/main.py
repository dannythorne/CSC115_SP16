import turtle

print("Danny Thorne")
print("Turtle Loops Example")

wn = turtle.Screen()
t = turtle.Turtle()

for i in range(4):
    t.pensize(i+1)
    t.forward(100)
    t.left(90)

wn.exitonclick()