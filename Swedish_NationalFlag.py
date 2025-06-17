import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")  # Black background

# Create turtle
pen = turtle.Turtle()
pen.speed(0)
pen.penup()

# Flag dimensions (Swedish flag: 16x10 ratio)
flag_width = 320
flag_height = 200
cross_thickness = flag_height // 5
vertical_bar_x = flag_width * 5 // 16  # vertical bar is at 5/16 of the flag width

# Function to draw filled rectangle
def draw_rectangle(x, y, width, height, color):
    pen.goto(x, y)
    pen.color(color)
    pen.begin_fill()
    pen.pendown()
    for _ in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)
    pen.end_fill()
    pen.penup()

# Draw blue background
draw_rectangle(-flag_width//2, flag_height//2, flag_width, flag_height, "blue")

# Draw yellow horizontal cross
draw_rectangle(-flag_width//2, cross_thickness//2, flag_width, cross_thickness, "yellow")

# Draw yellow vertical cross
draw_rectangle(-flag_width//2 + vertical_bar_x, flag_height//2, cross_thickness, flag_height, "yellow")

# Write country name below the flag
pen.goto(0, -flag_height//2 - 40)
pen.color("white")
pen.write("SWEDEN", align="center", font=("Arial Black", 28, "bold"))

# Finish
pen.hideturtle()
turtle.done()
