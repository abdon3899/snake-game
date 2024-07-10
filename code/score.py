from turtle import Turtle


ALIGN="center"
FONT=("Arial", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high.txt") as data:
           self.high_score = int(data.read())
        self.color('white')
        self.penup()
        self.goto(0 , 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"score is {self.score} , high score {self.high_score}",align= ALIGN,font= FONT)


    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color('blue')
    #     self.write('GAME OVER',align= ALIGN,font= FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()