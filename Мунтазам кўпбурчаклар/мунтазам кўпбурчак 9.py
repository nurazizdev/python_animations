import turtle
window = turtle.Screen()
t = turtle.Turtle()
t.color('black')
t.speed(0)

def kv(n,dlina):
    sumangle = 180*(n-2)
    if sumangle%n == 0:
        angle = sumangle/n 
        for j in range(n):
            t.forward(dlina)
            t.left(180-angle)
for j in range(3,12):
    kv(j,50)
window.mainloop()
