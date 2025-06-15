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
flag_height = 180
stripe_width = flag_width // 3
x_start = -180
y_start = -90

# Colors of the Italian flag (left to right)
colors = ["green", "white", "red"]

# Draw vertical stripes
for i in range(3):
    myPen.penup()
    myPen.goto(x_start + i * stripe_width, y_start)
    myPen.color(colors[i])
    myPen.fillcolor(colors[i])
    myPen.pendown()
    myPen.begin_fill()
    myPen.goto(x_start + (i + 1) * stripe_width, y_start)
    myPen.goto(x_start + (i + 1) * stripe_width, y_start + flag_height)
    myPen.goto(x_start + i * stripe_width, y_start + flag_height)
    myPen.goto(x_start + i * stripe_width, y_start)
    myPen.end_fill()

# Add country name
myPen.penup()
myPen.goto(0, -140)
myPen.color("black")
myPen.write("ITALY", align="center", font=("Arial", 24, "bold"))

turtle.done()
