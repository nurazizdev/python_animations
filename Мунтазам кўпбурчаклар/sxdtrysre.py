from turtle import Turtle, Screen

kv = 8
kv_size = 20

def main():
    uzunlik = 50

    screen = Screen()
    screen.bgcolor("WHITE")

    turtle = Turtle('square', visible = False)
    turtle.shapesize(kv * uzunlik / kv_size)
    turtle.speed('fastest')
    turtle.stamp()

    turtle.shapesize(uzunlik / kv_size)
    turtle.fillcolor("white")
    turtle.penup()

    edge = (1 - kv) / 2 * uzunlik
    turtle.goto(edge, edge)

    for qator in range(kv):
        for ustun in range(kv):
            if (qator + ustun) % 2 == 0:
                turtle.stamp()

            turtle.forward(uzunlik)

        turtle.goto(edge, edge + (qator + 1) * uzunlik)

    screen.exitonclick()

main()
