from turtle import Turtle
import time

class Score(Turtle):
  def __init__(self):
    super().__init__()
    self.score_player = 0
    self.score_computer = 0
    self.penup()
    self.hideturtle()
    self.color("white")
    
    self.update()

  def update(self):
    self.clear()
    self.goto(50, 200)
    self.write(self.score_player, align="center", font=("Courier", 50, "normal"))
    self.goto(-50, 200)
    self.write(self.score_computer, align="center", font=("Courier", 50, "normal"))
    # self.pendown()

  def player_point(self):
    self.score_player += 1
    self.update()

  def computer_point(self):
    self.score_computer += 1
    self.update()
    
    

  

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

  # def end_game(self):
    