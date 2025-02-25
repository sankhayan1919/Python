def div(num1,num2,range):
    for i in range(range1,range2):
        if(i%num1==0 and i%num2==0):
            print("\nfizzbuzz")
        elif(i%num1==0):
            print("\nfizz")
        elif(i%num2==0):
            print("\nbuzz")
        else:
            print(i,end=",")
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
range1=int(input("Enter the upper range:"))
range2=int(input("Enter the lower range:"))
div(num1,num2,range)