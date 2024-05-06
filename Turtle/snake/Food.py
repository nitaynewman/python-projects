from turtle import Turtle
import random

class food(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.penup()
    self.shapesize(0.5, 0.5)
    self.color("blue")
    self.speed(20)

    self.refresh()

  def refresh(self):
    X = random.randint(-280, 280)
    Y = random.randint(-280, 280)
    self.goto(X, Y)