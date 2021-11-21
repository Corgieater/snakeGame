from turtle import Turtle
FONT = ("Ariel", 20, "bold")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(0, 260)
        self.score = 0
        self.writing_score()

    def plus_score(self):
        self.score += 1

    def writing_score(self):
        self.clear()
        self.write(f"Score: {self.score}", font=FONT, align=ALIGN)

    def game_over(self):
        self.setpos(0, 0)
        self.write(f"Game over :(", font=FONT, align=ALIGN)

