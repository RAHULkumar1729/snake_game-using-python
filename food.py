from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("Blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-290, 290), random.randint(-290, 290))
