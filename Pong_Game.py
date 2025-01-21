# imorting the libraries
import turtle

# buliding screen
wind = turtle.Screen()  # inialize Screen
wind.title("Ping Pong")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)  # Stop the window from updating automatiaclly

# Create frist Madrab
madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.shapesize(stretch_len=1, stretch_wid=5)
madrab1.color("blue")
madrab1.penup()
madrab1.goto(-350, 0)

# Create Scend Madrab
madrab2 = turtle.Turtle()  # inialize the object shape
madrab2.speed(0)
madrab2.shape("square")
madrab2.shapesize(stretch_len=1, stretch_wid=5)
madrab2.color("red")
madrab2.penup()  # stop the object from creating lines
madrab2.goto(350, 0)

# Create The ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(stretch_len=1, stretch_wid=1)
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.25

# Create Score
score1=0
score2=0
score=turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player 1: 0   Player 2: 0 ", align="center",font=("Courier",24,"normal")) 





# Create the functions
# 1st Move the madrap1 to up
def madrab1_up():
    y = madrab1.ycor()  # get the y coordinate of madrab 1
    y += 20  # increse y by 20 to up
    madrab1.sety(y)  # Set the old y by new one increased by 20


# 1st Move the madrap1 to down
def madrab1_down():
    y = madrab1.ycor()
    y -= 20
    madrab1.sety(y)


# 1st Move the madrap2 to up
def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)


# 1st Move the madrap1 to down
def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)


# Keyboard bindings
wind.listen()
wind.onkeypress(madrab1_up, "w")
wind.onkeypress(madrab1_down, "s")
wind.onkeypress(madrab2_up, "Up")
wind.onkeypress(madrab2_down, "Down")


# Game Loop
while True:
    wind.update()  # update the screen everytime the loop run
    # Move the bool
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check the border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1+=1
        score.clear()
        score.write("Player 1: {}   Player 2: {}".format(score1,score2), align="center",font=("Courier",24,"normal")) 


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2+=1
        score.clear()
        score.write("Player 1: {}   Player 2: {}".format(score1,score2), align="center",font=("Courier",24,"normal")) 

    if madrab1.ycor()>290:
        madrab1.sety(290)

    if madrab1.ycor()<-290:
        madrab1.sety(-290)

    if madrab2.ycor()>290:
        madrab2.sety(290)
    if madrab2.ycor()<-290:
        madrab2.sety(-290)
    
    # Tasadom madrap + Ball 

    if (ball.xcor()>340 and ball.xcor()<350)and (ball.ycor()<madrab2.ycor()+40 and ball.ycor()>madrab2.ycor()-40 ):
        ball.setx(340)
        ball.dx*=-1
    if (ball.xcor()<-340 and ball.xcor()<-350)and (ball.ycor()<madrab1 .ycor()+40 and ball.ycor()>madrab1.ycor()-40 ):
        ball.setx(-340)
        ball.dx*=-1

