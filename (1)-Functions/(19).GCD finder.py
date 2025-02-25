def gcd(num1,num2):
    if(num1>num2):
        smaller=num2
    elif(num1==num2):
        print(f"GCD of them is {num1}")
    else:
        smaller=num1
    for i in range(2,smaller+1):
        if(num1%i==0 and num2%i==0):
            gcd=i
        else:
            continue
    print(f"GCD of them is {gcd}")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
gcd(num1,num2)