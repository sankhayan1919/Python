from turtle import Turtle,Screen
s=Screen()
t=Turtle()
t.speed(10)
def forward():
    t.forward(20)
def backward():
    t.forward(20)    
def left():
    new_heading=t.heading()+20
    t.setheading(new_heading)
    t.forward(20)
def right():
    new_heading=t.heading()-20
    t.setheading(new_heading)
    t.forward(20)
def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()
s.listen()
s.onkey(fun=forward,key="f")
s.onkey(fun=backward,key="b")
s.onkey(fun=left,key="l")
s.onkey(fun=right,key="r")
s.onkey(fun=clear_screen,key="c")
s.exitonclick()