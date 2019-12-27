import turtle
import sys
import os


#Screen
wn = turtle.Screen()
wn.title("pong1")
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)


#Score
score_a = 0
score_b = 0




#reset button
reset_button = turtle.Turtle()
reset_button.speed(0)
reset_button.color('grey')
reset_button.penup()
reset_button.goto(0, -280)
reset_button.write('Press spacebar to reset score', align="center", font=("Courier", 12))
reset_button.hideturtle()



#Resetting the score:




#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 240)
pen.write("Player A: 0   Player B: 0" , align="center", font=("Courier", 24))







#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.color('white')
paddle_a.shape('square')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)



#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.color('white')
paddle_b.shape('square')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.color('white')
ball.shape('circle')
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2


#paddle movement
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

def reset_score():
    pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24))






#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")




#the while loop

while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #stop at the border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        score_b += 1
        pen.write("Player A:{}  Player B:{}".format(score_a, score_b), align="center", font=("Courier", 24))

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        score_a += 1
        pen.write("Player A:{}  Player B:{}".format(score_a, score_b), align="center", font=("Courier", 24))


    def score_clear():
        pen.clear()
        pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24))


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if paddle_a.ycor() > 260:
        paddle_a.goto(-350,250)

    if paddle_a.ycor() < -260:
        paddle_a.goto(-350,-250)

    if paddle_b.ycor() > 260:
        paddle_b.goto(350, 250)

    if paddle_b.ycor() < - 240:
        paddle_b.goto(350,-240)


    #ball hits the paddle:
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1





