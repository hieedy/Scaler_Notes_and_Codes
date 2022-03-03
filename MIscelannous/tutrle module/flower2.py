import turtle

t = turtle.Turtle()
t.color('orange', 'black')
t.speed('fastest')
t.begin_fill()
for i in range(100):
    t.forward(500)
    t.left(155)
t.end_fill()

t.right(180)
t.forward(200)
t.begin_fill()
for i in range(100):
    t.forward(500)
    t.left(155)
t.end_fill()
