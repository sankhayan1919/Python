class circle:
  pi=3.14
  def __init__ (self,radius):
    self.radius=radius
    self.area=circle.pi*radius*radius
  def circumference(self):
    return 2*circle.pi*self.radius
circle_1=circle(5)
print(circle_1.circumference())
circle_2=circle(4)
print(circle_2.area)

class rectangle:
  def __init__(self,length,breadth):
    self.length=length
    self.breadth=breadth
  def area(self):
    return self.length*self.breadth
rectangle_1=rectangle(4,5)
print(rectangle_1.area())

class square:
  def __init__(self,length):
    self.length=length
    self.area=4*self.length
square_1=square(4)
print(square_1.area)
