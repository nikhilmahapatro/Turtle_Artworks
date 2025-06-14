import turtle

myPen = turtle.Turtle()
myPen.shape("arrow")
myPen.speed(10)

window = turtle.Screen()
window.bgcolor("#DDDDDD")

# Draw the French flag (blue, white, red)
stripe_width = 360 // 3
x_start = -180
colors = ["blue", "white", "red"]

for i in range(3):
    myPen.penup()
    myPen.goto(x_start + i * stripe_width, -120)
    myPen.color(colors[i])
    myPen.fillcolor(colors[i])
    myPen.pendown()
    myPen.begin_fill()
    myPen.goto(x_start + (i + 1) * stripe_width, -120)
    myPen.goto(x_start + (i + 1) * stripe_width, 120)
    myPen.goto(x_start + i * stripe_width, 120)
    myPen.goto(x_start + i * stripe_width, -120)
    myPen.end_fill()

# Add label below flag
myPen.penup()
myPen.goto(0, -160)
myPen.color("black")
myPen.write("FRANCE", align="center", font=("Arial", 24, "bold"))

myPen.hideturtle()
turtle.done()
