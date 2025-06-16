import turtle
import math

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create shield turtle
shield = turtle.Turtle()
shield.speed(0)
shield.hideturtle()

# Function to draw filled circle
def draw_circle(radius, color):
    shield.penup()
    shield.goto(0, -radius)
    shield.color(color)
    shield.begin_fill()
    shield.circle(radius)
    shield.end_fill()

# Draw concentric circles
draw_circle(150, "red")     # Outer red
draw_circle(120, "white")   # White
draw_circle(90, "red")      # Inner red
draw_circle(60, "blue")     # Center blue

# --- Draw centered star ---
def draw_star(center_x, center_y, radius, color):
    star = turtle.Turtle()
    star.hideturtle()
    star.speed(0)
    star.color(color, color)

    # Calculate the 5 outer points of the star
    points = []
    for i in range(5):
        angle_deg = 90 + i * 72
        angle_rad = math.radians(angle_deg)
        x = center_x + radius * math.cos(angle_rad)
        y = center_y + radius * math.sin(angle_rad)
        points.append((x, y))

    # Draw the star by connecting every second point
    star.penup()
    star.goto(points[0])
    star.begin_fill()
    for i in [0, 2, 4, 1, 3, 0]:
        star.goto(points[i])
    star.end_fill()

# Draw the star with radius ~57 to touch circle edge
draw_star(center_x=0, center_y=0, radius=57, color="white")

# Label
shield.penup()
shield.goto(0, -190)
shield.color("white")
shield.write("CAPTAIN AMERICA", align="center", font=("Arial", 18, "bold"))

turtle.done()
