from turtle import Turtle
import paddle

class ScoreBoard(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.color('White')
        self.penup()
        self.score = 0
        self.goto(position)
        self.hideturtle()
        
        # self.update_scoreboard()
    
    def update_scoreboard(self):
        '''starting score of players'''
        self.write(f"Score:{self.score} ", False, align='center', font=("Ariel", 15, "normal"))
    
    def add_score(self):
        '''Adds the winning player's score by one(1)'''
        self.clear()
        self.score += 1
        self.update_scoreboard()
        

class CenterLine(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, - 300)
        self.hideturtle()
    
    def line(self):
        for dashes in range(65):
            self.setheading(90)
            self.pendown()
            self.forward(5)
            self.penup()
            self.forward(5)