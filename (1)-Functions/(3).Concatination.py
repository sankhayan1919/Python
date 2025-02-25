var_1 = "123"
var_2= "123"
print(var_1)
print(var_2)
print(type(var_1))
print(var_1+var_2)

print("////////////")
my_list=["Welcome","to","Vscode"]
new_list=" ".join(my_list)
print(new_list)

X="Python"
Y="VsCode"
print("Welcome to "+X+" using "+Y)
print("Welcome to %s using %s" %("Python", Y))
print("Welcome to {} using {}".format(X,Y))
print("Welcome to {1} using {0}".format(X,Y))
print("Welcome to {classname} using {platform}".format(classname=X,platform=Y))