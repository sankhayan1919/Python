class Student:
    def __init__(self,name,rollno,age):
        self.name=name
        self._rollno=rollno
        self.__age=age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age>35:
           print("invalid age given")
        else:
            self.__age=age 
    def __display(self):
        print(f"Hi myself {self.name} {self.__age} years old with rollno {self._rollno} from student class")
    def displayPrivateData(self):
        self.__display()
class Branch(Student):
    def show(self):
        print(f"My rollno is {self._rollno}")
#b1=Branch("Sanu",78,19)
#b1.show()
#def showData():
    #b1=Branch("Sanu",19)
    #print(b1.name)
#showData()
s1=Student("Sankhayan",181,19)
#print(s1._Student__age)
#s1._Student__display()
#s1.displayPrivateData()
print(s1.get_age())
s1.set_age(20)
print(s1.get_age())