import turtle
window = turtle.Screen()
t = turtle.Turtle()
t.color('yellow')
window.bgcolor('blue')
t.pensize(3)
t.speed(10)

def kvadr():
    for i in range(4):
        t.forward(50)
        t.left(90)
for j in range(4):
    kvadr()
    t.left(90)

def kvadr1():
    for i in range(4):
        t.forward(100)
        t.left(90)
for j in range(12):
    kvadr1()
    t.left(90)

t.screen.mainloop()
