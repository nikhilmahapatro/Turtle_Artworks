import turtle

# Set the turtle's speed to the fastest
turtle.speed(0)

# Define the colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Draw a spiral
for i in range(360):
    # Set the color
    turtle.color(colors[i % len(colors)])
    # Draw a small line
    turtle.forward(i * 2)
    # Turn left
    turtle.left(130)

# Keep the window open until it's closed manually
turtle.done()