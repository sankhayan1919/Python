num=int(input("Enter the number:"))
count=0
for i in range(1,num+1):
    if(num%i==0):
        count+=1
        print(i,end=",")
    else:
        continue
if(count==0):
    print("no factors are present")
else:
    print(f"\ncount={count}")