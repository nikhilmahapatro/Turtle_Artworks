import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("#DDDDDD")

# Create turtle
flag = turtle.Turtle()
flag.speed(5)
flag.pensize(2)
flag.hideturtle()

# Flag dimensions
flag_size = 240
cross_arm_length = flag_size * 0.6
cross_arm_width = flag_size * 0.2

# Draw red square background
flag.penup()
flag.goto(-flag_size/2, -flag_size/2)
flag.color("red")
flag.begin_fill()
for _ in range(4):
    flag.forward(flag_size)
    flag.left(90)
flag.end_fill()

# Draw vertical part of white cross
flag.penup()
flag.goto(-cross_arm_width/2, -cross_arm_length/2)
flag.color("white")
flag.begin_fill()
for _ in range(2):
    flag.forward(cross_arm_width)
    flag.left(90)
    flag.forward(cross_arm_length)
    flag.left(90)
flag.end_fill()

# Draw horizontal part of white cross
flag.penup()
flag.goto(-cross_arm_length/2, -cross_arm_width/2)
flag.begin_fill()
for _ in range(2):
    flag.forward(cross_arm_length)
    flag.left(90)
    flag.forward(cross_arm_width)
    flag.left(90)
flag.end_fill()

# Add label
flag.penup()
flag.goto(0, -flag_size / 2 - 30)
flag.color("black")
flag.write("SWITZERLAND", align="center", font=("Arial", 20, "bold"))

turtle.done()
