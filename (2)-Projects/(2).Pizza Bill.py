size=str(input('please order:'))
bill=0
if(size=='small'):
 bill+=100
elif(size=='medium'):
 bill+=200
else:
 bill+=300
pepperoni=(input('wanna try pepperoni? '))
if(pepperoni=='yes'):
 if(size=='small'):
  bill+=30
 else:
  bill+=50
cheese=str(input("wanna try cheese? "))
if(cheese=='yes'):
  bill+=20
print(f'Your bill is: {bill}')