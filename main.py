from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard, CenterLine
import time


# Constant coordinated for the left and right paddle 
LEFT_POSITION = (-380, 0)
RIGHT_POSITION = (380, 0)
LEFT_SCORE_POSITION = (-200, 280)
RIGHT_SCORE_POSITION = (200, 280)

# screen creation
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PONG')
screen.tracer(0)

# storing name of both players
first_player = screen.textinput("Player 1 name", "what is your paddle name? ")
second_player = screen.textinput("Player 2 name", "what is your paddle name? ")

# Setting winning point to end game
bet = screen.numinput('Bet Score', "What sore would you like to determine the winner? ")

# Paddle initialization
r_paddle = Paddle(RIGHT_POSITION, first_player)
l_paddle = Paddle(LEFT_POSITION, second_player)

# Ball Initialization
ball = Ball()

# Score board for both players
l_score = ScoreBoard(LEFT_SCORE_POSITION)
r_score = ScoreBoard(RIGHT_SCORE_POSITION)

# bringing both score boards to display
l_score.update_scoreboard()
r_score.update_scoreboard()

#initializing the center partition of the game screen
center = CenterLine()
center.line()


screen.listen()

# Command for right paddle movement
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")

# Command for left paddle movement
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")


# BODY OF THE GAME
game_is_on = True
while game_is_on:
    time.sleep(ball.sleep_time)
    screen.update()
    ball.move()
    
    # detect collision with wall 
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()
    
    # detect collision with right and left paddle
    if (ball.distance(r_paddle) < 50 and  ball.xcor()>=360) or (ball.distance(l_paddle) <50 and ball.xcor() <=-360):
        ball.bounce_x()
        ball.sleep_time
    # detect right paddle miss
    if ball.xcor() > 370:
        ball.reset_position()
        l_score.add_score()
    
    # detect left paddle miss
    if ball.xcor() < -370:
        ball.reset_position()
        r_score.add_score()
        # game_is_on =  False
    
    if l_score.score == bet or r_score.score == bet:
        game_is_on = False
        if l_score.score > r_score.score:
            print(f"{l_paddle.name} won the Match!")
        else:
            print(f"{r_paddle.name} won the match")

screen.exitonclick()