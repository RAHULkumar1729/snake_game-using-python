from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        file = open("New_score.txt")
        self.highscore = int(file.read())
        file.close()
        self.goto(0, 270)
        self.write(arg=f"Score= {self.score} HighScore= {self.highscore}", move=False, align="center", font=("Arial", 16, "italic"))

    def update_score(self):
        self.clear()
        self.write(arg=f"Score= {self.score}  HighScore= {self.highscore}", move=False, align="center", font=("Arial", 16, "italic"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score

        with open("New_score.txt", mode="w") as file:
            file.write(str(self.highscore))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", move=False, align="center", font=("Bold", 16, "italic"))

    def increase_score(self):
        self.score += 1
        self.color("white")
        self.goto(0, 270)
        self.update_score()



