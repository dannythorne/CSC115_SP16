import turtle # required to use turtle graphics

wn = turtle.Screen() # required for the turtle to draw on
ted = turtle.Turtle() # the turtle itself

ted.shape("turtle") # optional
ted.speed(1) # optional: 1 to 10 for slow to fast (0 for no animation)

ted.forward(100)
ted.right(30)
ted.forward(100)
ted.left(120)
ted.forward(100)


wn.exitonclick() # make the window wait for click before closing
