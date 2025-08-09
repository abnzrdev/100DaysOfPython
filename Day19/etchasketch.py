from turtle import *

while True:
    tur = Turtle()
    scr = Screen()
    scr.listen()
    tur.hideturtle()
    tur.pensize(5)

    def moveforward():
        x_cor = tur.xcor()
        tur.setx(x_cor + 10)

    def moveback():
        x_cor = tur.xcor()
        tur.setx(x_cor - 10)

    def moveup():
        y_cor = tur.ycor()
        tur.sety(y_cor + 10)

    def movedown():
        y_cor = tur.ycor()
        tur.sety(y_cor - 10)

    def upper_right_curve():
        tur.pendown()
        tur.circle(30,20)

    def upper_left_curve():
        tur.pendown()
        tur.circle(-30,20)

    def clear():
        tur.clear()
        tur.penup()
        tur.home()
        tur.pendown()

    scr.onkeypress(fun=moveforward, key="Right")
    scr.onkeypress(fun=moveback, key="Left")
    scr.onkeypress(fun=moveup, key="Up")
    scr.onkeypress(fun=movedown, key="Down")
    scr.onkey(fun=clear, key="c")
    scr.onkey(fun=upper_right_curve, key="d")
    scr.onkey(fun=upper_left_curve, key="h")

    scr.exitonclick()



