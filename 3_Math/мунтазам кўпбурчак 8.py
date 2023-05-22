import turtle
window = turtle.Screen()
t = turtle.Turtle()
t.color('black')
t.speed(0)

n = 4
sumangle = 180*(n-2)
angle = sumangle/n 
for j in range(n):
    t.forward(400)
    t.left(180-angle)


def bir_qator():
    def kv():
        n = 4
        sumangle = 180*(n-2)
        angle = sumangle/n 

        for j in range(n):
            t.forward(50)
            t.left(180-angle)
    for i in range(1, 9):
        kv()
        t.forward(50)
#-----------------------------------------
bir_qator()
t.left(90)
bir_qator()
t.left(90)
bir_qator()
t.left(90)
bir_qator()
#-----------------------------------------
for i in range(3):
    t.left(90)
    t.forward(100)
    t.left(90)
    bir_qator()
    t.right(90)
    t.forward(0)
    t.right(90)
    bir_qator()


#------------------------------------------

window.mainloop()
