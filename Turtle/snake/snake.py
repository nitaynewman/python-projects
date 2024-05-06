from turtle import Turtle

START = [(00, 00), (-20,00), (-40,00)]
DISTANCE = 20

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
  def __init__(self):
    self.position = []
    self.create_snake()
    self.head = self.position[0]

  def create_snake(self):
    for i in START:
      self.add_seg(i)

  def add_seg(self, i):
      new_segment = Turtle("square")
      new_segment.color("white")
      new_segment.penup()
      new_segment.goto(i)
      self.position.append(new_segment)
    
  def extend(self):
    self.add_seg(self.position[-1].position())
    
  def move(self):
    for a in range(len(self.position) - 1, 0, -1):
      X = self.position[a - 1].xcor()
      Y = self.position[a - 1].ycor()
      self.position[a].goto(X, Y)
      
    self.head.forward(DISTANCE)

  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)
    
  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)
    
  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)
    
  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)
