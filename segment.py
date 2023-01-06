from turtle import Turtle
COLOR = "white"
SHAPE = "square"


class Segment(Turtle):
    def __init__(self):
        super().__init__(SHAPE)
        self.color(COLOR)
        self.penup()
        # self.is_head = False
