import turtle

t = turtle.Turtle()

t.color('#F26327', '#9BD7D1')
t.speed('fastest')

for i in range(3):
    t.begin_fill()

    for i in range(1,50):
        t.forward(200)
        t.left(145)


    t.end_fill()

    t.right(145)    
    t.forward(100)


