from Constants import *
from cmaeraTurtle import CameraTurtle


class Cell(CameraTurtle):
    def __init__(self, x, y, color, linked_to=None):
        super().__init__(x, y)
        self.x_cell = x
        self.y_cell = y
        self.color(color)
        self.penup()
        self.goto(x, y)
        self.shape("square")
        self.shapesize(stretch_wid=Cell_SCALE, stretch_len=Cell_SCALE)
        self.pencolor("light blue")
        self.cell_number = 0
        self.linked_to = linked_to
        self.is_snake_or_ladder = False
        if LOAD_TEXTURES:
            self.shape(PATH_TEXTURES + color + '.gif')

        self.convert_reverse = lambda position: (N_CELLS * M_CELLS) - position

    def write_number(self, number):
        self.clear()
        if self.is_snake_or_ladder:
            self.write(str(number) + f'\n{self.convert_reverse(self.linked_to)}', font=("Arial", 12, "bold"),
                       align="center")
        else:
            self.write(number, font=("Arial", 14, "bold"))

    def snake_shape(self):
        self.shape(PATH_TEXTURES + 'snake.gif')
        self.is_snake_or_ladder = True

    def ladder_shape(self):
        self.shape(PATH_TEXTURES + 'ladder.gif')
        self.is_snake_or_ladder = True
