def sum(num):
  sum=0
  if(num<0):
    print("Enter positive number")
  elif(num==0):
    print("Sum is 0") 
  else:
    for i in range(1,num+1):
      sum+=i
  print(f"sum is: {sum}")
num=int(input('enter the limit:'))
sum(num)

print("////////////////")
num1=10_00_000
num2=23_000
sum=(num1+num2)
print(f"{sum:,}")