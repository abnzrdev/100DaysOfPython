from turtle import Turtle, Screen

tur = Turtle()
scr = Screen()
scr.setup(width=600, height=600)
scr.title("Snake Game")
scr.bgcolor("black")

tur.begin_fill()
for i in range(4):
    tur.forward(15)
    tur.right(90)
tur.end_fill()




scr.exitonclick()