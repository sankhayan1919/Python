num=int(input("Enter:"))
fact=1
if num==0:
    print("factorial is 1")
elif(num<0):
    print("Please enter positive number")
else:
    for i in range(1,num+1):
        fact=fact*i
    print(f"factorial is {fact}")

print("//////////////////")

def fact(num):
    if num==0:
        return 1
    elif(num<0):
        print("Please enter positive number")
    else:
        return (num*fact(num-1))
num=int(input("Enter:"))
result=fact(num)
print(f"factorial is {result}")