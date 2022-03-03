import turtle

smith = turtle.Turtle()
ang = 3
while True:
    smith.forward(5)
    smith.left(ang)
  

    if(ang<=0):
        ang = ang+0.05

    if ang>=3:
        ang = ang-0.05 
