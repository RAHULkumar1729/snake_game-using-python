import turtle
from turtle import Turtle

HEADS_POSITION = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.class_list = []
        self.create_snake()

    def create_snake(self):
        global HEADS_POSITION
        for position in HEADS_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.class_list.append(tim)

    def reset(self):
        for segments in self.class_list:
            segments.goto(1000, 1000)
        self.class_list.clear()
        self.create_snake()

    def extend(self):
        global HEADS_POSITION
        x = self.class_list[-1].xcor()
        y = self.class_list[-1].ycor()
        self.add_segment((x, y))

# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)

    def move(self):
        for i in range(len(self.class_list)-1, 0, -1):
            mx = self.class_list[i-1].xcor()
            my = self.class_list[i-1].ycor()
            self.class_list[i].goto(mx, my)
        self.class_list[0].forward(20)

    def up(self):
        if self.class_list[0].heading() != 270:
            self.class_list[0].setheading(90)

    def down(self):
        if self.class_list[0].heading() != 90:
            self.class_list[0].setheading(270)

    def right(self):
        if self.class_list[0].heading() != 0 and self.class_list[0].heading() != 180:
            self.class_list[0].setheading(0)

    def left(self):
        if self.class_list[0].heading() != 0 and self.class_list[0].heading() != 180:
            self.class_list[0].setheading(180)






