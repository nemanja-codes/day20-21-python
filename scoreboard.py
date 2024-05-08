from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.goto(0, 270)
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)
