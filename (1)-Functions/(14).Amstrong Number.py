def armstrong(num):
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum=sum+digit**3
        temp//=10
    if(sum==num):
        print("It s an armstrong number")
    else:
        print("It is not an armstrong number")
num=int(input("enter the number:"))
armstrong(num)