import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.penup()
t.goto(0, -200)
t.pendown()

for i in range(8):
    t.forward(100)
    t.right(45)

t.penup()
t.goto(0, -200)
t.pendown()
t.right(90)
t.forward(300)
t.shape("circle")
t.color("brown")
t.stamp()

t.color("darkgreen")
t.penup()
t.goto(-100, -100)
t.pendown()
t.begin_fill()
t.circle(50)
t.end_fill()

t.penup()
t.goto(100, -100)
t.pendown()
t.begin_fill()
t.circle(50)
t.end_fill()

turtle.done()