from turtle import Screen

from Constants import *
from Constants import PATH_TEXTURES


class ScreenManger:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.tracer(0)
        self.screen.title("BlockKing")
        self.screen.bgcolor("black")
        self.load_textures()

    def load_textures(self):
        self.screen.addshape(PATH_TEXTURES + 'red.gif')
        self.screen.addshape(PATH_TEXTURES + 'red40.gif')
        self.screen.addshape(PATH_TEXTURES + 'green.gif')
        self.screen.addshape(PATH_TEXTURES + 'green40.gif')
        self.screen.addshape(PATH_TEXTURES + 'gray.gif')
        self.screen.addshape(PATH_TEXTURES + 'ladder.gif')
        self.screen.addshape(PATH_TEXTURES + 'snake.gif')
        self.screen.bgpic(PATH_TEXTURES + 'bg.png')
