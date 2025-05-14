from random import randint, seed

from Constants import *
from cmaeraTurtle import CameraTurtle


class Dot(CameraTurtle):
    def __init__(self, x, y, divide_by):
        super().__init__(x, y, follow_camera=False)
        self.color("black")
        self.shape("circle")
        self.shapesize(stretch_wid=(DIE_SCALE / (2 * divide_by)), stretch_len=(DIE_SCALE / (2 * divide_by)))
        self.goto(x, y)
        if SEED != -1:
            seed(SEED)


class DieRoller(CameraTurtle):

    def __init__(self):
        super().__init__(DIE_X, DIE_Y, follow_camera=False)
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=DIE_SCALE, stretch_len=DIE_SCALE)
        self.goto(DIE_X, DIE_Y)
        self.number = []

    def draw_number(self, number):
        for num in self.number:
            num.hideturtle()

        self.number.clear()

        if number == 1:
            self.number.append(Dot(self.xcor(), self.ycor(), 1))
        elif number == 2:
            self.number.append(Dot(self.xcor() - 20, self.ycor() - 20, 2))
            self.number.append(Dot(self.xcor() + 20, self.ycor() + 20, 2))
        elif number == 3:
            self.number.append(Dot(self.xcor() - 20, self.ycor() - 20, 2))
            self.number.append(Dot(self.xcor(), self.ycor(), 3))
            self.number.append(Dot(self.xcor() + 20, self.ycor() + 20, 2))

        elif number >= 4:
            self.number.append(Dot(self.xcor() - 20, self.ycor() - 20, 2))
            self.number.append(Dot(self.xcor() + 20, self.ycor() + 20, 2))
            self.number.append(Dot(self.xcor() - 20, self.ycor() + 20, 2))
            self.number.append(Dot(self.xcor() + 20, self.ycor() - 20, 2))

        if number == 5:
            self.number.append(Dot(self.xcor(), self.ycor(), 2))
        elif number == 6:
            self.number.append(Dot(self.xcor() - 20, self.ycor() - 20 + 20, 2))
            self.number.append(Dot(self.xcor() + 20, self.ycor() + 20 - 20, 2))

    def roll(self):
        rnd = randint(1, 6)
        self.draw_number(rnd)
        return rnd

    def rotate_dice_right(self):
        self.right(5)

    def rotate_dice_left(self):
        self.left(5)
