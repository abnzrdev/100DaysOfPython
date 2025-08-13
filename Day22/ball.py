from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 12
        self.y_move = 2
        self.shape("circle")
        self.speed("slowest")
        self.color("white")
        self.penup()

    def collide(self):
        current_x = self.xcor()
        current_y = self.ycor()
        self.goto(current_y, current_x)






