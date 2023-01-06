from turtle import Turtle
import sys


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        with open("high_score.txt") as high_score_file:
            content = high_score_file.readline()
            if content:
                print("YAS")
                print(content)
                self.high_score = int(content)

            else:
                self.high_score = 0
        self.setpos(0, 270)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align='center', font=('Courier', 15, 'normal'))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align='center', font=('Courier', 15, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as high_score_file:
                    high_score_file.write(f"{self.high_score}")
        self.score = 0
        self.update()
