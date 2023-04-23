from turtle import *

s = Screen()

s.bgcolor("black")

t = Turtle()

t.speed("fastest")

# Start of crescent code

t.goto(0, -200)

t.color("white")

t.begin_fill()

t.circle(200)

t.end_fill()

t.up()

t.goto(50, -200)

t.color("black")

t.begin_fill()

t.circle(200)

t.end_fill()

# End of crescent code

# Start of star code

t.up()

t.goto(50, 0)

t.color("white")

t.begin_fill()

for i in range(5):
    t.forward(40)
    t.right(144)

t.end_fill()

# End of star code

pen = Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Eid Mubarak!", align="center", font=("Arial", 48, "normal"))

while True:

    s.update()