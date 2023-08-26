import turtle

wn = turtle.Screen()
wn.title("Pong!")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#blocks
block1 = turtle.Turtle()
block1.speed(0)
block1.shape("square")
block1.color("white")
block1.shapesize(stretch_wid=10,stretch_len=1)
block1.penup()
block1.hideturtle()
block1.sety(400)
block1.dy = -0.1


# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = -0.3
ball.dy = 0.3

# paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)



# Scoring system
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("PlayerA: 0   PlayerB: 0", align="center",font=("Courier", 20,"normal"))

#score
score_a = 0
score_b = 0


# function
def paddle_a_up():
    y = paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y-=20
    paddle_b.sety(y)
    
#move block
def fxn_block1():
    block1.showturtle()
    block1.sety(block1.ycor()+block1.dy)
#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#main game loop
while True:
    wn.update()
    # move the ball
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)

    # Border Checking
    if ball.ycor() >290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("PlayerA: {}   PlayerB: {}".format(score_a,score_b), align="center",font=("Courier", 20,"normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("PlayerA: {}   PlayerB: {}".format(score_a,score_b), align="center",font=("Courier", 20,"normal"))

    # Collision
    if (ball.xcor() > 340 and (ball.xcor()<350) and ball.ycor() < paddle_b.ycor()+40 and ball.ycor()> paddle_b.ycor()  -40):
       ball.setx(340)
       ball.dx *= -1.05

    if (ball.xcor() < -340 and ball.xcor()> -350) and (ball.ycor() < paddle_a.ycor()+40 and ball.ycor()> paddle_a.ycor() -40):
       ball.setx(-340)
       ball.dx *= -1.05

    #paddle lock
    if paddle_a.ycor()>255:
        paddle_a.sety(255)
    if paddle_a.ycor()<-255:
        paddle_a.sety(-255)

    if paddle_b.ycor()>255:
        paddle_b.sety(255)
    if paddle_b.ycor()<-255:
        paddle_b.sety(-255)

    #Blocks border checking
    if (ball.xcor() < block1.xcor()+10 and ball.xcor()> block1.xcor()) and (ball.ycor() < block1.ycor()+100 and ball.ycor()> block1.ycor() -100):
       ball.setx(block1.xcor()+10)
       ball.dx *= -2
    if (ball.xcor() > block1.xcor()-5 and ball.xcor()< block1.xcor()) and (ball.ycor() < block1.ycor()+100 and ball.ycor()> block1.ycor() -100):
       ball.setx(block1.xcor()-5)
       ball.dx *= -2
    

    if score_a==1 or score_b == 1:
        fxn_block1()


