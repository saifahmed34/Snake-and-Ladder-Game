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

    # def color(self, color_shape, no_texture=False):
    #     if no_texture or not LOAD_TEXTURES:
    #         super().color(color_shape)
    #         return
    #
    #     if LOAD_TEXTURES:
    #         color_shape += '.gif'
    #
    #     color_shape = PATH_TEXTURES + color_shape
    #
    #     if color_shape.endswith(".gif"):
    #         self.shape(color_shape)
    #         self.stamp()

    # def color(self, color_shape, no_texture=False):
    #     if no_texture or not LOAD_TEXTURES:
    #         super().color(color_shape)
    #         return
    #     if color_s
    #     hape == "red":
    #         self.shape(PATH_TEXTURES + 'red.gif')
    #         self.stamp()
    #     elif color_shape == "green":
    #         self.shape(PATH_TEXTURES + 'green.gif')
    #         self.stamp()
    #     elif color_shape == 'gray':
    #         self.shape(PATH_TEXTURES + 'gray.gif')
    #         self.stamp()
    #     else:
    #         super().color(color_shape)
    #         return

    @classmethod
    def move_camera(cls, x, y):
        for obj in cls.list_of_obj:
            if not obj.follow_camera:
                continue
            obj.goto(obj.x - x, obj.y - y)
