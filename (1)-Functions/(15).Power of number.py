def power(num1,num2):
    for i in range(0,num2+1):
        result=(num1)**i
        print(f"{num1} raised to the power {i} is {result}")
num1=int(input("Enter the number:"))
num2=int(input("Enter the number till which you want:"))
power(num1,num2)