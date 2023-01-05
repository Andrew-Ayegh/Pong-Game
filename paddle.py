from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position, name):
        super().__init__()
        self.name = name
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(position)
        

    def up(self):
        y_axis = self.ycor() + 20
        self.goto(self.xcor(), y_axis)

    def down(self):
        y_axis = self.ycor() - 20
        self.goto(self.xcor(), y_axis)
