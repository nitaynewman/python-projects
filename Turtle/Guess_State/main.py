import turtle
import pandas

import csv

screen = turtle.Screen()
screen.title('Guess The State')
screen.setup(740, 500)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


guessed = []
data = pandas.read_csv("States.csv")
states = data.state.to_list()
while len(guessed) < 50:
    answer = screen.textinput(title=f'{len(guessed)}/50 State Correct', prompt='Whats another state').title()
    if answer == 'Exit':
        missing_states = []
        for i in states:
            if i not in guessed:
                missing_states.append(i)
        missing = pandas.DataFrame(missing_states)
        missing.to_csv('missing_states.csv')
        # print(missing)
        break
    if answer in states:
        guessed.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        data_state = data[data.state == answer]
        t.goto(int(data_state.x), int(data_state.y))
        t.write(answer)


# '''finding coordinates on map'''
# def get_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_coor)
# turtle.mainloop()
