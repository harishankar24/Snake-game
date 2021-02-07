from turtle import Turtle

FONT = ("Courier",12,"bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.speed("fastest")
        self.goto(-20,280)
        self.color("red")
        self.write(f"Score: {self.score}",False,"center",FONT)
        self.hideturtle()

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}",False,"center",FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",False,"center",FONT)