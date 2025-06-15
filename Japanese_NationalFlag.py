import turtle

# Setup turtle
myPen = turtle.Turtle()
myPen.speed(10)
myPen.hideturtle()

# Setup screen
window = turtle.Screen()
window.bgcolor("#DDDDDD")

# Flag dimensions
flag_width = 360
flag_height = 240
x_start = -180
y_start = -120

# Draw white rectangular flag background
myPen.penup()
myPen.goto(x_start, y_start)
myPen.color("white")
myPen.fillcolor("white")
myPen.pendown()
myPen.begin_fill()
for _ in range(2):
    myPen.forward(flag_width)
    myPen.left(90)
    myPen.forward(flag_height)
    myPen.left(90)
myPen.end_fill()

# Draw the red circle (sun)
myPen.penup()
myPen.goto(0, -60)  # Circle centered; radius = 60
myPen.color("red")
myPen.fillcolor("red")
myPen.setheading(0)
myPen.pendown()
myPen.begin_fill()
myPen.circle(60)
myPen.end_fill()

# Add label below
myPen.penup()
myPen.goto(0, -160)
myPen.color("black")
myPen.write("JAPAN", align="center", font=("Arial", 24, "bold"))

turtle.done()
