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
stripe_height = flag_height // 3
x_start = -180
y_start = 90

# Colors of the German flag
colors = ["black", "red", "gold"]

# Draw horizontal stripes
for i in range(3):
    myPen.penup()
    myPen.goto(x_start, y_start - i * stripe_height)
    myPen.color(colors[i])
    myPen.fillcolor(colors[i])
    myPen.pendown()
    myPen.begin_fill()
    myPen.goto(x_start + flag_width, y_start - i * stripe_height)
    myPen.goto(x_start + flag_width, y_start - (i + 1) * stripe_height)
    myPen.goto(x_start, y_start - (i + 1) * stripe_height)
    myPen.goto(x_start, y_start - i * stripe_height)
    myPen.end_fill()

# Add country name
myPen.penup()
myPen.goto(0, -120)
myPen.color("black")
myPen.write("GERMANY", align="center", font=("Arial", 24, "bold"))

turtle.done()
