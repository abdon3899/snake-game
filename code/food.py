from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.pu()
        self.shapesize(0.5, 0.5)
        self.color('red')
        self.speed("fastest")
        self.refresh()


    # def big_food(self):
    #     super().__init__()
    #     if random.randint(0,10) == 5:
    #         self.shape('circle')
    #         self.pu()
    #         self.shapesize(1, 1)
    #         self.color('green')
    #         self.speed("fastest")
    #         self.refresh()

    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y )
