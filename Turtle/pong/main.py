from turtle import Screen, Turtle
from player import Player
from ball import Ball
from Score import Score
import time

screen = Screen()
screen.title("pong game")
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

tim = Turtle()


r_paddle = Player((350, 0))
l_paddle = Player((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

score = Score()

game = True
while game:
  screen.update()
  ball.move()
  time.sleep(ball.Speed)

  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.baunce_y()

  if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
    ball.baunce_x()
  if ball.xcor() > 380: 
    ball.reset()
    ball.baunce_x()
    score.player_point()
    
  if ball.xcor() < -380:
    ball.reset()
    ball.baunce_x()
    score.computer_point()
  
  # if score.score_computer() == 1:
  #   game = False
  #   tim.write("computer wins")
  # if score.player_score() == 1:
  #   game = False
  #   tim.write("you win")
    

screen.exitonclick()