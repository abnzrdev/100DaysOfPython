# ===============================================
# WRITTEN BY: ABENEZER
# US STATES GUESSING GAME
# ===============================================

# Import libraries: turtle for graphics/map display, pandas for CSV data handling
import turtle
import pandas as pd

# ===============================================
# GAME SETUP AND SCREEN CONFIGURATION
# ===============================================

# Setup game window with title and US map background (without state names)
screen = turtle.Screen()
screen.title("State Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.bgpic(image)

# ===============================================
# USER INPUT HANDLING FUNCTION
# ===============================================

# Creates popup window for player to enter state name guesses
def get_user_guess():
    """Function to get user input for state name"""
    answer = screen.textinput(title="Guess the State",
                             prompt="What's another state's name?")
    return answer

# ===============================================
# DATA LOADING AND PREPARATION
# ===============================================

# Read CSV file with state names and coordinates, convert to searchable list
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

# ===============================================
# STATE PLACEMENT FUNCTION
# ===============================================

# Finds state coordinates from data and writes state name on map at correct position
def place_state_on_map(state_name):
    """Place the state name at its x,y coordinates on the map"""
    state_data = data[data.state == state_name]
    if not state_data.empty:
        x = int(state_data.x.iloc[0])
        y = int(state_data.y.iloc[0])
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_turtle.goto(x, y)
        state_turtle.write(state_name)


# ===============================================
# MAIN GAME LOGIC AND LOOP
# ===============================================

# Game loop: runs until all states guessed or player types 'exit', tracks score and correct guesses
game_is_on = True
guessed_states = []

while game_is_on:
    screen.title(f"{len(guessed_states)}/50 States Correct")
    user_answer = get_user_guess()

    if user_answer is None or user_answer.lower() == 'exit':
        game_is_on = False
        break

    user_answer = user_answer.title()  # The data is titled Alabama , Texas

    if user_answer in all_states and user_answer not in guessed_states:
        guessed_states.append(user_answer)
        place_state_on_map(user_answer)

    if len(guessed_states) == 50:
        game_is_on = False
        screen.title("Congratulations! You got all 50 states!")

# ===============================================
# GAME ENDING AND FINAL SCORE DISPLAY
# ===============================================

# Display final score message and wait for click to close
game_over_turtle = turtle.Turtle()
game_over_turtle.hideturtle()
game_over_turtle.penup()
game_over_turtle.goto(0, 0)
game_over_turtle.write(f"Game over! You guessed {len(guessed_states)} out of 50 states correctly.",
                       align="center", font=("Arial", 16, "bold"))


screen.exitonclick()

