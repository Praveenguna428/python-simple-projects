import turtle
screen = turtle.Screen()
screen.bgcolor("black")
heart = turtle.Turtle()
heart.color("red")
heart.fillcolor("red")
heart.pensize(3)
heart.speed(5)
heart.begin_fill()
heart.left(140)
heart.forward(180)
heart.circle(-90, 200)
heart.setheading(60)
heart.circle(-90, 200)
heart.forward(180)
heart.end_fill()
heart.hideturtle()
turtle.done()