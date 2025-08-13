from turtle import Screen, Turtle
from bar import Bar
from ball import Ball
from score import Score

# TODO : Make a function based on the game state (start , gameloop , outside) of the screen
# Defining the screen boundaries as tuples
HORIZONTAL_LIMIT = (-300, 300)  # (left, right)
VERTICAL_LIMIT = (-300, 300)    # (bottom, top)

# Creating the screen of game
scr = Screen()
scr.listen()
scr.bgcolor("black")
scr.setup((HORIZONTAL_LIMIT[1] - HORIZONTAL_LIMIT[0]), (VERTICAL_LIMIT[1] - VERTICAL_LIMIT[0]))

# ---- First game state ---- run as soon the program run

# Draw dashed center line
dash = Turtle()
dash.speed("fastest")
dash.hideturtle()
for y in range(-280, 300, 40):
    dash.penup()
    dash.goto(0, y)
    dash.pendown()
    dash.pencolor("white")
    dash.setheading(270)
    dash.forward(20)
    dash.penup()

# Positioning the player
player = Bar()
computer = Bar()
player.goto(HORIZONTAL_LIMIT[0] + 20, 0)
computer.goto(HORIZONTAL_LIMIT[1] - 20, 0)

# Positioning the ball
playing_ball = Ball()

# Positioning the score
player_score = Score()
computer_score = Score(x_cor=30, y_cor=230)


# Game Loop -- Middle part -----
def game_loop():

    while True:

        def is_collision(ball, bar):
            ball_x, ball_y = ball.xcor(), ball.ycor()
            bar_x, bar_y = bar.xcor(), bar.ycor()
            bar_width = 20  # adjusted width of the bar
            bar_height = 60 # adjusted height of the bar
            ball_radius = 10  # default ball's radius

            return (bar_x - bar_width/2 - ball_radius < ball_x < bar_x + bar_width/2 + ball_radius and
            bar_y - bar_height/2 - ball_radius < ball_y < bar_y + bar_height/2 + ball_radius)

     # Colliding with the bar
        print(f"Before {is_collision(playing_ball, player)}")
        if is_collision(playing_ball, player):
            print(is_collision(playing_ball, player))
            playing_ball.collide()
            print("collide")
        if is_collision(playing_ball, computer):
            playing_ball.collide()
            print("collide")

        # Colliding with the upper and lower limits of the screen
        if not (VERTICAL_LIMIT[0] + 10 < playing_ball.ycor() < VERTICAL_LIMIT[1] - 10):
            playing_ball.collide()

        # Score Increment
        if playing_ball.xcor() > HORIZONTAL_LIMIT[1]:
            player_score.increase_score()
        if playing_ball.xcor() < HORIZONTAL_LIMIT[0]:
            computer_score.increase_score()

        # Making the bar to be fixed in the screen
        scr.onkeypress(fun=lambda: player.move_bar_up() if player.ycor() < VERTICAL_LIMIT[1] - 40 else None, key="Up")
        scr.onkeypress(fun=lambda: player.move_bar_down() if player.ycor() > VERTICAL_LIMIT[0] + 40 else None, key="Down")
        scr.onkeypress(fun=lambda: computer.move_bar_up() if computer.ycor() < VERTICAL_LIMIT[1] - 40 else None, key="w")
        scr.onkeypress(fun=lambda: computer.move_bar_down() if computer.ycor() > VERTICAL_LIMIT[0] + 40 else None, key="s")

        playing_ball.goto(0, 300)
        print("moving")

if __name__ == "__main__": # do not run when imported it will run when executed
    game_loop()

scr.exitonclick()

