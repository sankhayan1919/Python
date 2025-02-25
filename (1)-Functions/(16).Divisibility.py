def div(num1,num2):
    count=0
    my_list=[]
    for i in range(num1,num2+1):
        if(i%num1==0):
            count+=1
            print(i,end=",")
        else:
           continue
    if(count==0):
        print("no number is divisible by {num1}")
    else:
        print(f"\ncount={count}")
num1=int(input("Enter the number:"))
num2=int(input("Enter the range:"))
div(num1,num2)