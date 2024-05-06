import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

color = ["blue", "lime", "dark violet", "dark orange", "firebrick", "slate blue", "spring green", "yellow",
         "cornflower blue", "dark orange", "white", "teal", "cyan", "red", "ghost white", "magenta", "dark blue",
         "black", "powder blue"]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# create 7 shapes
def calc(num, total_angle):
    return 180 - (total_angle / num)


def shape(num, angle):
    for i in range(num):
        tim.forward(100)
        tim.right(angle)


num = 3
total_angle = 180

for i in range(7):
    tim.color(random.choice(color))
    angle = calc(num, total_angle)
    shape(num, angle)
    num += 1
    total_angle += 180

# randomly walk anywere

angle = [90, 180, 270, 360]
tim.speed(5)
tim.pensize(15)
game = True
while game:
    tim.color(random.choice(color))
    tim.forward(30)
    tim.right(random.choice(angle))

# spielgragh

for i in range(72):
    # option 1
    tim.color(random_color())
    # option 2
    '''tim.color(random.choice(color))'''
    tim.circle(50)
    tim.right(5)

# draeing random dot pic
y = -150
tim.penup()
tim.hideturtle()
for i in range(10):

    tim.goto(-150, y)
    y += 30
    for i in range(10):
        tim.dot(10, random_color())
        tim.forward(30)

# keyboad listenr drawing
from turtle import Turtle, Screen

# import random

tim = Turtle()
screen = Screen()


def forward():
    tim.forward(10)


def backward():
    tim.backward(10)


def clockwise():
    tim.right(10)


def counter_coclockwise():
    tim.left(10)


def clear():
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=counter_coclockwise)
screen.onkey(key="c", fun=clear)

# turtle race

from turtle import Turtle, Screen
import random

game = False
screen = Screen()
screen.setup(550, 550)
bet = screen.textinput(title="make your bet", prompt="which turtle will win the race? (enter a color) ")

'''finsh line drawing'''
fl = Turtle()
fl.hideturtle()
fl.penup()
fl.goto(250, 250)
fl.pendown()
fl.right(90)
fl.forward(500)

colors = ["red", "orange", "yellow", "green", "blue"]
turtle = ["red", "orange", "yellow", "green", "blue"]
y = 160
# print(colors[0])
for i in range(5):
    turtle[i] = Turtle(shape="turtle")
    turtle[i].color(colors[i])
    turtle[i].penup()
    turtle[i].goto(-250, y)
    y -= 80

if bet:
    game = True

while game:
    for i in turtle:
        if i.xcor() > 225:
            if i.pencolor() == bet:
                print(f"u win. {i.pencolor()} is the one who won")
            else:
                print(f"u loose. {i.pencolor()} won the game")

            game = False
        distance = random.randint(0, 10)
        i.forward(distance)

# turtle race game

game = False
screen = Screen()
screen.setup(550, 550)
bet = screen.textinput(title="make your bet", prompt="which turtle will win the race? (enter a color) ")

'''finsh line drawing'''
fl = Turtle()
fl.hideturtle()
fl.penup()
fl.goto(250, 250)
fl.pendown()
fl.right(90)
fl.forward(500)

colors = ["red", "orange", "yellow", "green", "blue"]
turtle = ["red", "orange", "yellow", "green", "blue"]
y = 160
# print(colors[0])
for i in range(5):
    turtle[i] = Turtle(shape="turtle")
    turtle[i].color(colors[i])
    turtle[i].penup()
    turtle[i].goto(-250, y)
    y -= 80

if bet:
    game = True

while game:
    for i in turtle:
        if i.xcor() > 225:
            if i.pencolor() == bet:
                print(f"u win. {i.pencolor()} is the one who won")
            else:
                print(f"u loose. {i.pencolor()} won the game")

            game = False
        distance = random.randint(0, 10)
        i.forward(distance)

screen.exitonclick()