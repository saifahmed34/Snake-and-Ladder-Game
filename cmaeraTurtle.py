from Constants import *
from Constants import LOAD_TEXTURES
from turtle import Turtle


class CameraTurtle(Turtle):
    list_of_obj = []

    def __init__(self, x, y, follow_camera=True):
        super().__init__()
        CameraTurtle.list_of_obj.append(self)
        self.follow_camera = follow_camera
        self.x = x
        self.y = y

    def goto(self, x, y):
        self.x = x
        self.y = y
        super().goto(x, y)

    @classmethod
    def move_camera(cls, x, y):
        for obj in cls.list_of_obj:
            if not obj.follow_camera:
                continue
            obj.goto(obj.x - x, obj.y - y)
