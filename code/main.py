from turtle import Turtle , Screen
import time
from day20_21_snake.score import Score
from snake import Snake
from food import Food
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

tim = Turtle()
food = Food()
snake = Snake()
score = Score()

speed_on_game=0.09


screen.listen()
screen.onkey(snake.up, key='Up' )
screen.onkey(snake.down, key='Down' )
screen.onkey(snake.right, key='Right' )
screen.onkey(snake.left, key='Left' )




game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(speed_on_game)
    snake.move()

    if snake.head.distance(food) < 15 :
        snake.extend()
        food.refresh()
        # food.big_food()
        score.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        #game_is_on = False
        score.reset_score()
        snake.reset()

    for segment in snake.segment[1:] :
        if snake.head.distance(segment) < 10:
            #game_is_on = False
            score.reset_score()
            snake.reset()

screen.exitonclick()