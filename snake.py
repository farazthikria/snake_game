from turtle import Turtle ,Screen

snake_direction = [(0,0),(-20,0),(-40,0)]
class Snake:
   def __init__(self):
    self.squares = []
    self.create_snake()
    self.head = self.squares[0]

   def create_snake(self):   
      for position in snake_direction:
        self.add_segment(position)
         
   def add_segment(self,position):
      new = Turtle()
      new.penup()
      new.color('white')
      new.shape('square')
      new.goto(position)
      self.squares.append(new)




   def extend(self):   
     self.add_segment(self.squares[-1].position())  

   def move(self):
    for seg_num in range(len(self.squares)-1,0,-1):
        new_x = self.squares[seg_num-1].xcor()
        new_y = self.squares[seg_num-1].ycor()
        self.squares[seg_num].goto(new_x,new_y)
    self.head.forward(10)

   def up(self):
     if self.head.heading() != 270:
      self.head.setheading(90)

   def right(self):
     if self.head.heading() != 180:
      self.head.setheading(0)

   def left(self):
     if self.head.heading() != 0:
       self.head.setheading(180)
  
   def down(self):
     if self.head.heading() != 90:
      self.head.setheading(270)    
