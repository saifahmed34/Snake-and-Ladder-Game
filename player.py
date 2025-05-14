from Constants import *
from cmaeraTurtle import CameraTurtle


class Player(CameraTurtle):
    def __init__(self, x, y, cell_idx, color):
        super().__init__(x, y)
        self.shape("square")
        self.penup()
        self.showturtle()
        self.goto(x, y)
        self.color(color)
        self.player_color = color
        self.shapesize(stretch_wid=PLAYER_SCALE, stretch_len=PLAYER_SCALE)
        self.cell_idx = cell_idx
        if LOAD_TEXTURES:
            self.shape(PATH_TEXTURES + color + '.gif')
