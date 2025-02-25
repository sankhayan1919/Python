my_list=[10,20,30,40,50]
for index, value in enumerate(my_list,start=1):
    #if we remove "start=1" indexing will start from zero.
    print(index,"-",value)

print("////////////")
my_list=[10,20,30,40,50]
#incase of letters spaces are also counted at the time of indexing
for index in range(len(my_list)):
    value=my_list[index]
    print(index,value)
    
print(my_list[3])
print(my_list[0:3])

print("//////Find empty list /////////")
my_list=[]
print("List is empty") if not my_list else print("List is not empty")
#Another process
print("List is empty") if my_list==[] else print("List is not empty")
#Another process
print(len(my_list))
if(len(my_list)==0):
    print("List is empty")

print("///////////////")
#here unique values are obtained
l1=["a","q",1,2,22,5,14] 
l2=["a","b",8,9,15,1]
l12=list(set(l1+l2))
print(l12)
#Another process 
l1.extend(l2)
print(l1)

print("///////////////")
numbers=[6,7,8,4,2,-3]
squares=[]
for i in numbers:
  square=i**2
  squares.append(square)
  print("the list of square is: ",square)

print("////////List Comprehension///////")
my_list=[10,20,30,40]
new_list=[i*2 for i in my_list]
print(new_list)

print("///////////////")
my_list=["Sreeju","Sanu","Jini","Dipen","Argha","Uttu","Agnik"]
print(my_list[-7:-3])
print(my_list[1:5])
print(my_list[::])
print(my_list[:2])
print(my_list[5:],end=" ")
print(my_list[::3])
print(my_list[::-1])

