from turtle import Turtle
import time

class Score(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.color("white")
    self.penup()
    self.goto(0, 280)
    self.update()
    # self.pendown()
    
    self.hideturtle()

  def update(self):
    self.write(f"your score: {self.score}", align="center", font=("Courier", 12, "normal"))

  def game_over(self):
    self.clear()
    self.goto(0, 0)
    
    # for i in range(4):
    self.write("GAME-OVER \n", align="center", font=("Courier", 12, "normal"))
    # self.clear()
    # self.time.sleep(.5)
      
    self.write(f"FAINAL SCORE: {self.score}", align="center", font=("Courier", 12, "normal"))
  
  def increace(self):
    self.score += 1
    self.clear()
    self.update()
    