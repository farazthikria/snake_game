from turtle import Turtle , Screen
import time
from snake import Snake
from snake_food import *
from snake_scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("snake game")
screen.tracer(0)

snake = Snake()
food = Food()

scorry = ScoreBoard()

screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)







game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scorry.increase_score()

    #detech collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor()< -280 or snake.head.ycor() >280 or snake.head.ycor() < -280:
        game_is_on = False
        scorry.gameover()

    #gameover
    for segments in snake.squares[1:]:
        
        
        if snake.head.distance(segments) < 10 :
            game_is_on = False
            scorry.gameover()




        

       
        

screen.exitonclick()    
