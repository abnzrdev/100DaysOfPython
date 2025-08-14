from turtle import Turtle, Screen

# Creating the turtle screen and the object
scr = Screen()
scr.setup(width=600, height=600)
scr.title("Snake Game")
scr.bgcolor("black")
scr.listen()

# define the movement
def move():
    head.forward(10)

# Defining what will happen when the key presses
scr.onkeypress(fun=move, key="Right")

# Creating the segments(head, middle, tail)
segments = []
for i in range(3):
    segment = Turtle()
    segment.shape("square")
    segment.color("white")
    segment.penup()
    segment.goto(x=-20 * i, y=0)
    segments.append(segment)

head = segments[0]  # the first segment to be controlled by the player

while True:
    scr.update()
    for i in range(3,2,-1):
        segments[i].goto(segments[i - 1].xcor(), segments[i - 1].ycor())



scr.exitonclick()