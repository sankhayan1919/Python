print("//////////Random Lines//////////")
import turtle
import random
turtle.colormode(255)
turtle.width(10)
turtle.speed(10)
turtle.shape("turtle")
for _ in range(50):
    r=random.randrange(0,255)
    g=random.randrange(0,255)
    b=random.randrange(0,255)
    turtle.setheading(random.randrange(0,360,90))
    turtle.pencolor((r,g,b))
    turtle.forward(20)
turtle.exitonclick()

print("//////////Star//////////")
import turtle
turtle.speed(10)
turtle.color("red","yellow")
turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170)
    if turtle.heading()==0:
        break
turtle.end_fill()
turtle.exitonclick()

print("//////////Circle//////////")
import turtle
import random
turtle.speed("fastest")
turtle.colormode(255)
while True:
    r=random.randrange(0,255)
    g=random.randrange(0,255)
    b=random.randrange(0,255)
    turtle.pencolor((r,g,b))
    turtle.circle(50)
    turtle.left(5)
    if turtle.heading()==0:
        break
turtle.exitonclick()

print("//////////Random Dots//////////")
import turtle
from turtle import Screen
import random
s=Screen()
print(s.screensize())
turtle.speed("fastest")
turtle.colormode(255)
turtle.penup()
for _ in range(100):
  r=random.randrange(0,255)
  g=random.randrange(0,255)
  b=random.randrange(0,255)
  turtle.pencolor((r,g,b))
  turtle.goto(random.randint(-100,100),random.randint(-100,100))
  turtle.dot(20)
turtle.exitonclick()
