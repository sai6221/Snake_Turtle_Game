from turtle import Turtle
import random
ALIGN = "center"
FONT_FAMILY = "Arial"
FONT_SIZE =24
FONT_TYPE="normal"

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()
    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGN, font = (FONT_FAMILY,FONT_SIZE,FONT_TYPE))
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align=ALIGN, font = (FONT_FAMILY,FONT_SIZE,FONT_TYPE))
    def increase(self):
        self.score+=1
        self.clear()
        self.update_score()
        