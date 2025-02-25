print("Using third variable")
a,b=input("enter the numbers: ").split(",")   #split is used in case of strings only
print("a= "+a)
print("b= "+b)
temp=a
a=b
b=temp
print("a= "+a)
print("b= "+b)

print("Without using third variable")
a,b=input("enter the numbers: ").split(",")
print("a= ",a)
print("b= ",b)
a,b=b,a
print("a= ",a)
print("b= ",b)