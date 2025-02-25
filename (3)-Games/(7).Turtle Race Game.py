from turtle import Turtle,Screen
import random
width,height=600,600
color_list=["magenta","black","red","blue","green","yellow","lime","pink","orange","aquamarine"]
count=10
print("~"*30)
print("Welcome to my Turtle Race Game")
print("~"*30)
print(color_list)
guess=input("Which turtle will win the race:\n")
s=Screen()
x_spacing=width//11
turtle_list=[]
for i in range(1,11):
    new_turtle=Turtle()
    new_turtle.shape("turtle")
    new_turtle.left(90)
    new_turtle.color(color_list[i-1])
    new_turtle.penup()
    new_turtle.goto(-width/2+(i *x_spacing),-height//2+10)
    turtle_list.append(new_turtle)

def race():
    race_on=True
    while race_on:
       for turtle in turtle_list:
          distance=random.randrange(1,20)
          turtle.forward(distance)
          x,y=turtle.pos()
          if y>=height//2:
              winner=turtle.pencolor()
              print(f"The winner is {turtle.pencolor()} turtle")
              if winner==guess:
                  print("Congratulations!Your turtle won the race.")
              else:
                  print("Oops you lose.")
              race_on=False
race()

s.exitonclick()
   