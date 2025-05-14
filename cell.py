from Constants import *
from cmaeraTurtle import CameraTurtle


class Cell(CameraTurtle):
    def __init__(self, x, y, color):
        super().__init__(x, y)
        self.x_cell = x
        self.y_cell = y
        self.color(color)
        self.penup()
        self.goto(x, y)
        self.shape("square")
        self.shapesize(stretch_wid=Cell_SCALE, stretch_len=Cell_SCALE)
        self.pencolor("black")
        self.cell_number = 0

        if LOAD_TEXTURES:
            self.shape(PATH_TEXTURES + color + '.gif')

    def write_number(self, number):
        self.clear()
        self.write(number, font=("Arial", 14, "bold"))
