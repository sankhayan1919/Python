punc='''!@#$%^&*()/||*<>?':;",.'''
string=input("Enter: ")
result=""
for i in string:
    if i not in punc:
        result+=i
print(result)