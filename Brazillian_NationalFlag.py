import turtle
import math

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")

# Turtle setup
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()

# Flag dimensions
flag_width = 360
flag_height = 240
circle_radius = 50

# Helper to draw filled rectangle
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

# Draw green background
draw_rectangle(-flag_width//2, flag_height//2, flag_width, flag_height, "green")

# Draw yellow diamond
pen.goto(0, 120)
pen.color("yellow")
pen.begin_fill()
pen.pendown()
pen.goto(180, 0)
pen.goto(0, -120)
pen.goto(-180, 0)
pen.goto(0, 120)
pen.end_fill()
pen.penup()

# Draw blue circle (centered)
pen.goto(0, -circle_radius)
pen.color("blue")
pen.begin_fill()
pen.pendown()
pen.circle(circle_radius)
pen.end_fill()
pen.penup()

# Draw white band (diagonal arc through circle)
def draw_diagonal_band():
    pen.color("white")
    pen.width(8)
    pen.penup()

    # Parameters for arc path
    steps = 100
    for i in range(steps):
        angle = math.radians(180 * i / steps)
        x = 50 * math.cos(angle)
        y = 20 * math.sin(angle)
        # Rotate the arc to tilt diagonally
        rotated_x = x * math.cos(math.radians(30)) - y * math.sin(math.radians(30))
        rotated_y = x * math.sin(math.radians(30)) + y * math.cos(math.radians(30))
        pen.goto(rotated_x, rotated_y)
        if i == 0:
            pen.pendown()
    pen.penup()
    pen.width(1)

draw_diagonal_band()

# Write BRAZIL below the flag
pen.goto(0, -flag_height//2 - 50)
pen.color("white")
pen.write("BRAZIL", align="center", font=("Arial Black", 28, "bold"))

turtle.done()
