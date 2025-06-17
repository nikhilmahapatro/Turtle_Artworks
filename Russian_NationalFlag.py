import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")  # Black background

# Create turtle
pen = turtle.Turtle()
pen.speed(0)
pen.penup()

# Flag dimensions
flag_width = 300
flag_height = 180
stripe_height = flag_height // 3

# Function to draw a stripe
def draw_stripe(x, y, width, height, color):
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

# Draw top white stripe
draw_stripe(-flag_width//2, flag_height//2, flag_width, stripe_height, "white")

# Draw middle blue stripe
draw_stripe(-flag_width//2, flag_height//2 - stripe_height, flag_width, stripe_height, "blue")

# Draw bottom red stripe
draw_stripe(-flag_width//2, flag_height//2 - 2 * stripe_height, flag_width, stripe_height, "red")

# Write country name in block letters
pen.goto(0, -flag_height//2 - 40)
pen.color("white")
pen.write("RUSSIA", align="center", font=("Arial Black", 28, "bold"))

# Finish
pen.hideturtle()
turtle.done()
