from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.write(arg=f"Level: {self.level}", font=FONT)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER!", align="center", font=FONT)
