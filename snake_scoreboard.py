from turtle import Turtle

#
class ScoreBoard(Turtle):
  def __init__(self):
    
    super().__init__()

    self.score = 0
    self.goto(-20,250)
    self.color('white')
    self.hideturtle()
    self.writer()

  def writer(self):
    self.write(f"score : {self.score} ",font=('Arial',17,'bold'))

  def gameover(self):
    self.goto(-30,0)
    self.write(f"gameOver",font=('Arial',17,'bold'))



  def increase_score(self):
    self.score+=1
    self.clear()
    self.writer()

  


  
