import turtle
import math

smith = turtle.Turtle()
smith.speed('fastest')
smith.penup()
smith.forward(50)
for i in range(50):
    smith.forward(3)
    smith.left(1)

a,b = smith.pos()

smith.pendown()
while True:
    smith.forward(3)
    smith.left(1)
    x,y = smith.pos()
    if x>-a and y<b:
        break

a2,b2 = smith.pos()
d = math.sqrt((a2-a)**2 + (b2-b)**2)


smith.setheading(0)    
smith.forward(d)


#inner head

smith.left(180)
smith.forward(d-(d-50))
smith.left(180)
a,b = smith.pos()
while True:
    smith.forward(5)
    smith.left(2)
   
