from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.setpos(0, 270)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}", align='center', font=('Courier', 15, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=('Courier', 15, 'normal'))
