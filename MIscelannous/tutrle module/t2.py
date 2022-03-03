import turtle

scrn = turtle.Turtle()
direction = 'right'
scrn.penup()

print(screen.window_width())
for i in range(1,20):

    
    if direction == 'right':
        direction = 'left'
        scrn.left(90)
        scrn.forward(50)
        scrn.left(90)
        scrn.forward(300)

    else:
        direction = 'right'
        scrn.right(90)
        scrn.forward(50)
        scrn.right(90)
        scrn.forward(300)

         
