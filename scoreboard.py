from turtle import Turtle
ALIGNMENT ="center"
FONT = ('Courier', 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as file:
            self.high_score = int(file.read())
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()
    def update_score(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score: {self.score}  High score: {self.high_score}", move=True, align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.goto(0, 260)
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.home()
    #     self.write(f"Score: {self.score}  High score: {self.high_score}", move=True, align=ALIGNMENT, font=FONT)



