import turtle

print("Danny Thorne")
print("Turtle Coordinates Example")

wn = turtle.Screen()
t = turtle.Turtle()

print( t.xcor(), t.ycor())

for i in range(20):
    t.forward(10)
    t.left(20)
    print( t.xcor(), t.ycor())

wn.exitonclick()