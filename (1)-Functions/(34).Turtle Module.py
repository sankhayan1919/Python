# import turtle
# def draw():
#     distance=int(input("Enter the distance: "))
#     angle=int(input("Enter the angle: "))
#     side=int(input("Enter the number of side: "))
#     turtle.speed(10)
#     for i in range(0,side+1):
#         turtle.forward(distance)
#         turtle.left(angle)
# draw()
# turtle.shape("turtle")
# print(turtle.shape())
# turtle.exitonclick()

print("////////////////////")
import turtle
for i in range(3,11):
    angle=360/i
    for _ in range(i):
        turtle.forward(100)
        turtle.left(angle)
turtle.exitonclick()
