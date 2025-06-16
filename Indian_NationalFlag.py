import turtle
import math

# Setup screen
screen = turtle.Screen()
screen.bgcolor("#DDDDDD")

# Main turtle
flag = turtle.Turtle()
flag.speed(5)
flag.hideturtle()

# Flag size
flag_width = 360
flag_height = 180
stripe_height = flag_height / 3
x_start = -180
y_start = 90

# Colors
colors = ["#FF9933", "white", "#138808"]  # Saffron, White, Green

# Draw horizontal tricolor
for i in range(3):
    flag.penup()
    flag.goto(x_start, y_start - i * stripe_height)
    flag.color("black", colors[i])
    flag.pendown()
    flag.begin_fill()
    for _ in range(2):
        flag.forward(flag_width)
        flag.right(90)
        flag.forward(stripe_height)
        flag.right(90)
    flag.end_fill()

# ---- Draw Ashoka Chakra ----
chakra = turtle.Turtle()
chakra.hideturtle()
chakra.speed(0)
chakra.color("navy")
chakra.pensize(1)

# Center of white stripe
chakra_radius = 20
center_x = 0
center_y = y_start - stripe_height - (stripe_height / 2)  # Middle of white stripe

# Draw outer circle
chakra.penup()
chakra.goto(center_x, center_y - chakra_radius)
chakra.setheading(0)
chakra.pendown()
chakra.circle(chakra_radius)

# Draw 24 spokes
for i in range(24):
    angle = i * (360 / 24)
    chakra.penup()
    chakra.goto(center_x, center_y)
    chakra.setheading(angle)
    chakra.forward(0)
    chakra.pendown()
    chakra.forward(chakra_radius)

# Add label
flag.penup()
flag.goto(0, -120)
flag.color("black")
flag.write("INDIA", align="center", font=("Arial", 24, "bold"))

turtle.done()
