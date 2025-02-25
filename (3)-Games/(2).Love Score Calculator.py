name1=(input("enter your name: "))
name2=(input("enter your partner's name: "))
name= name1+ name2
lower_case=name.lower()
t=lower_case.count('t')
r=lower_case.count('r')
u=lower_case.count('u')
e=lower_case.count('e')
true=t+r+u+e
l=lower_case.count('l')
o=lower_case.count('o')
v=lower_case.count('v')
e=lower_case.count('e')
love=l+o+v+e
score=str(true) + str(love)
print(f'your love score is {score}')
if(score>='40' and score<'70'):
    print("Average romantic life")
elif(score>='70'):
    print("Perfect Couple")
else:
    print("Think again about your relationship")