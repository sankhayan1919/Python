class Human:
  def __init__(self,num_heart):
    print("calling from Human class")
    self.eyes=2
    self.heart=num_heart
  def eat(self):
    print("i eat rice")
  def work(self):
    print("i work as a programmer")
class Male(Human):
  def __init__(self,name):
    print("calling from Male class")
    self.name=name
  def sleep(self):
    print("i sleep 7 hours a day")
class Boy(Male):
  def __init__(self,heart,name,dance):
    Human.__init__(self,heart)
    Male.__init__(self,name)
    self.know_dancing=dance
  def work(self):
    #Human.work(self)
    super().work()
    print("I can code")
boy_1=Boy(1,"Sanu",True)
print(boy_1.name)
print(boy_1.know_dancing)
print(Boy.mro())