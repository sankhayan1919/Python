class Duck:
    def swim(self):
        print("It can swim")
    def speak(self):
        print("Quack")
class Dog:
    def swim(self):
        print("It can swim")
    def speak(self):
        print("Bark")
class Human:
    def swim(self):
        print("only those who know swimming")
    def speak(self):
        print("different language")
class Demo:
    def display(self,object):
       object.swim()
       object.speak()
d=Duck()
do=Dog()
h=Human()
demo=Demo()
demo.display(h)
demo.display(d)
demo.display(do)