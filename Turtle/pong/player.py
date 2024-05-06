from turtle import Turtle

class Player(Turtle):
  
  def __init__(self, positin):
    super().__init__()
    self.shape("square")
    self.color("white")
    self.shapesize(stretch_wid=4, stretch_len=1)
    self.penup()
    self.goto(positin)

  def go_up(self):
    new_y = self.ycor() + 20
    self.goto(self.xcor(), new_y)

  def go_down(self):
    new_y = self.ycor() - 20
    self.goto(self.xcor(), new_y)

    