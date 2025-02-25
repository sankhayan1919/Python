class complex:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i
    def __add__(self,other):
        return f"{self.real+other.real} + {self.imaginary+other.imaginary}i"
        #return str(self.real+other.real) + "+" + str(self.imaginary+other.imaginary) + "i"
c1=complex(1,2)
c2=complex(2,3)
print(c1+c2)

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __gt__(self,other):
        if self.age>other.age:
            return True
        else:
            return False
p1=person("Sanu",19)
p2=person("Jini",20)
if p1>p2:
    print(f"{p1.name} is elder")
else:
    print(f"{p2.name} is elder")