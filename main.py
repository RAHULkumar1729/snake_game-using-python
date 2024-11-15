from turtle import Screen
import time
from snake import HEADS_POSITION
from snake import Snake
from food import Food
from score import Score
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake game")
screen.tracer(0)
snake = Snake()
food = Food()
sore = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


#  if collision from the food
    if snake.class_list[0].distance(food) < 15:
        food.refresh()
        sore.increase_score()
        snake.extend()


#   if collision from the wall
    if snake.class_list[0].xcor() > 290 or snake.class_list[0].xcor() < -290 or snake.class_list[0].ycor() > 300 \
            or snake.class_list[0].ycor() < -290:
        snake.reset()
        sore.reset()

#   if collision of snake head with any of the tail
    for segments in snake.class_list[1:]:
        if snake.class_list[0].distance(segments) < 10:
            snake.reset()
            sore.reset()


screen.exitonclick()
