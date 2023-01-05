from  turtle import Turtle, Screen
import random 
DEGREE = 90
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.sleep_time = 0.1
    
    def move(self):
        x_axis = self.xcor() + self.x_move
        y_axis = self.ycor() + self.y_move
        self.goto(x_axis, y_axis)
        
    
    def bounce_y(self):
        self.y_move *= -1
        
        self.move()
        # print(self.pos())
    
    def bounce_x(self):
        self.x_move *= -1
        self.sleep_time *= 0.9
        self.move()
        # print(self.pos())
    
    def reset_position(self):
        self.goto(0,0)
        self.sleep_time = 0.1
        self.bounce_x()
    
