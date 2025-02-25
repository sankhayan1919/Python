import random
alphabets=['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S',
           's','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','^','&','*']
password_alphabets=int(input('how many alphabets you want- '))
password_numbers=int(input('how many numbers you want- '))
password_symbols=int(input('how many symbols you want- '))
password=[]
for i in range(1,password_alphabets+1):
  char=random.choice(alphabets)
  password+=char
for i in range(1,password_numbers+1):
  char=random.choice(numbers)
  password+=char
for i in range(1,password_symbols+1):
  char=random.choice(symbols)
  password+=char
random.shuffle(password)
print(password)
key=''
for char in password:
  key+=char
print(key)

print("//////Hide the password//////")
from getpass import getpass
name=input("Enter username: ")
password=getpass("Enter password: ")
print(password)