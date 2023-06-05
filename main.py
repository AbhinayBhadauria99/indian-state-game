import turtle
import pandas

screen = turtle.Screen()
screen.title("INDIA States Game")
image = "india.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.State_Name.str.lower().to_list()
guessed_states = []

answer_state = screen.textinput(title="Guess the State", prompt="What is another state's name?")
print(answer_state)

while len(guessed_states) < 32:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What is the name of another state?")

    if answer_state is None or answer_state.lower() == "exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    answer_state = answer_state.lower()  # Convert to lowercase here

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.State_Name.str.lower() == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

turtle.mainloop()
