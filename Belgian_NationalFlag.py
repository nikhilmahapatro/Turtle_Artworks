import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("white")  # Changed from black to white

# Turtle setup
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()

# Flag dimensions
flag_width = 300
flag_height = 180
stripe_width = flag_width // 3

# Function to draw vertical stripe
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

# Draw black stripe (left)
draw_stripe(-flag_width//2, flag_height//2, stripe_width, flag_height, "black")

# Draw yellow stripe (middle)
draw_stripe(-flag_width//2 + stripe_width, flag_height//2, stripe_width, flag_height, "yellow")

# Draw red stripe (right)
draw_stripe(-flag_width//2 + 2 * stripe_width, flag_height//2, stripe_width, flag_height, "red")

# Write "BELGIUM" in block letters below the flag
pen.goto(0, -flag_height//2 - 40)
pen.color("black")  # Better contrast on white background
pen.write("BELGIUM", align="center", font=("Arial Black", 28, "bold"))

# Finish
turtle.done()
