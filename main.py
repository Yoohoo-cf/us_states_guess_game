import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")

states_guessed = []

while len(states_guessed) < 50:
    answer_state = screen.textinput(title=f"{len(states_guessed)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break
    if answer_state in data["state"].to_list():
        states_guessed.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data["x"].item()), int(state_data["y"].item()))
        t.write(state_data["state"].item())


# states_to_learn.csv

states_to_learn = data[~data["state"].isin(states_guessed)]

states_to_learn.to_csv("states_to_learn.csv")

