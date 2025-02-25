heights=input('Enter list of heights(using space):')
heights_list=heights.split()
count=0
for height in heights_list:
  count=count+1
for i in range(count):
  heights_list[i]=int(heights_list[i])
max_height=heights_list[0]
for height in heights_list:
  if height>max_height:
    max_height=height
print(f'maximum height is :{max_height}')
total =0
for height in heights_list:
    total=total+height
    avg=total/count
print(f'average is : {round(avg)}')