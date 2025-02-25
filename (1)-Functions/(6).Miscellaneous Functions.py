# sum=0
# for i in range(0,101,2):
#   sum=sum+i
# print(sum)
# print(round(667,-3))
# print(round(667,-1))
# print(round(-1.5))
# print(round(8/3))

# print("//////Lambda Function//////")
# a=lambda b:b**2
# print(a(4))

# print("//////Zip Function/////")
# names=["Sreeju","Sanu","Jini","Dipen","Argha","Uttu","Agnik"]
# marks=[90,89,92,86,85,84,90]
# for name,mark in zip(names,marks):
#   print(name,"scored",mark,"marks")

# print("/////Unpacking//////")
# a,b,*c,d=(1,2,3,4,5)
# print(a)
# print(b)
# print(c)
# print(d)

# print("///////Generator///////")
# def my_gen():
#   yield 1
#   yield 2
#   yield 3

# x=my_gen()
# print(x)
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

# print("///////Map///////")
# def cube(x):
#     return x*x*x
# mylist=[1,2,3,4]
# newlist=list(map(cube, mylist))
# print(newlist)

# print("///////Filter///////")
# def filter_func(x):
#     return x != 2
# mylist=[1,2,3,4]
# newlist=list(filter(filter_func, mylist))
# print(newlist)

# print("///////Reduce///////")
# from functools import reduce
# def sum_func(x,y):
#     return x + y
# mylist=[1,2,3,4]
# res=reduce(sum_func, mylist)
# print(res)

# print("///////Walrus Operator///////")
# numbers=list()
# while(number := input("Enter number: ")) !="quit":numbers.append(number)
# print(numbers)
