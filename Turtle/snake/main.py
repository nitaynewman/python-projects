from turtle import Screen
from snake import Snake
# import random
import time
from Food import food
from score import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

food = food()
score = Score()

game = True
while game:
  screen.update()
  time.sleep(0.1)
  snake.move()
  if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    score.increace()

  if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor(
  ) > 290 or snake.head.ycor() < -290:
    game = False
    score.game_over()

  for i in snake.position[1:]:
    if snake.head.distance(i) < 10:
      game = False
      score.game_over()

screen.exitonclick()