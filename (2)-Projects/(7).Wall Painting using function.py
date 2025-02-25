import math
def paint(height,width,coverage):
  area=height*width
  requirement=math.ceil(area/coverage)
  print(f"requirement is {requirement}")
height=float(input('enter the height:'))
width=float(input('enter the width:'))
coverage=float(input('enter covering area:'))
paint(height,width,coverage)