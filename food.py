from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("gold")
        self.shapesize(0.7, 0.7)
        self.speed("fastest")
        self.penup()
        self.food_pos()

    def food_pos(self):
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        self.goto(x, y)

