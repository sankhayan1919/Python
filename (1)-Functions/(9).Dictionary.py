train_data={
    'Amritsar_mail_data':{
        "Train No.":13005,
        "Date":"23 Dec",
        "Station":"Lucknow charbagh",
        "Fare":"735 rupees",
        "Time":"7.15pm to 3.40pm"
    },
    'Lalkuan_express_data':{
        "Train No.":12354,
        "Date":"30 Dec",
        "Station":"Howrah",
        "Fare":"595 rupees",
        "Time":"7.20pm to 6.25pm"
        },
    'Kathgodam_express_data':{
        "Train No.":15043,
        "Date":"24 Dec",
        "Station":"Kathgodam",
        "Fare":"225 rupees",
        "Time":"11.25pm to 8.05am"
    }

}
train_data["Amritsar_mail_data"]["Destination"]="Amritsar"
print(train_data)

print("/////////////////")
dict1={"sankhayan":45,"sreejita":77,"sinjini":68,"dipen":89,"argha":91}
dict2={"sankhayan":54,"utsav":84,"agnik":91}
print({**dict1,**dict2})
dict3=dict2.copy()
dict3.update(dict1)
print(dict3)
for key,value in dict1.items():
    print(key,"-",value)
sorted_dict1=sorted(dict1.items(),key=lambda x:x[1])
print(sorted_dict1)
sorted_dict2=sorted(dict2.values())
print(sorted_dict2)
del dict1["sreejita"]
print(dict1)
pop_item=dict1.pop("argha")
print(dict1)

print("///////////////")
list_marks={
    "sankhayan":45,"sreejita":77,"sinjini":68,"dipen":89,"argha":91
}
list_grades={}
for student in list_marks:
  marks=list_marks[student]
  if marks>90:
    list_grades[student]='A'
  elif marks>80:
    list_grades[student]='B'
  elif marks>70:
    list_grades[student]='C'
  elif marks>60:
    list_grades[student]='D'
  elif marks>50:
    list_grades[student]='E'
  elif marks>40:
    list_grades[student]='F'
print(list_grades)

#print("///////Nested Dictionary//////////")
#from pathlib import Path
#Path("").mkdir(parents=True,exist_ok=True)