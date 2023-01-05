# from turtle import Turtle
from segment import Segment
STARTING_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.new_snake()
        self.head = self.segments[0]

    def new_snake(self):
        for coordinate in STARTING_COORDINATES:
            new_segment = Segment()
            new_segment.goto(coordinate)
            self.segments.append(new_segment)
        self.segments[0].is_head = True

    def add_to_tail(self):
        new_segment = Segment()
        new_segment.setpos(self.segments[-1].pos())
        self.segments.append(new_segment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].pos())
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
