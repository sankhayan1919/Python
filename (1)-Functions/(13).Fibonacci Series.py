def fibonacci(num):
    print("Fibonacci Series is:")
    a=0
    b=1
    sum=0
    print(a)
    if(num==0):
        print(f"sum of the series is: {num}")
        return
    else:
        print(b)
        for i in range(1,num-1):
            c=a+b
            a=b
            b=c
            print(c)
            sum+=i
    print(f"sum of the series is: {sum+1}")
num=int(input("enter the range:"))
fibonacci(num)