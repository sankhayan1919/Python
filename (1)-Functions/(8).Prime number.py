def prime(n,count):
  count=0
  for i in range(1,n+1):
    if(n%i==0):
      count+=1
  if(count==2):
    print('prime')
  else:
    print('not prime')
num=int(input("enter:"))
prime(count=0,n=num)