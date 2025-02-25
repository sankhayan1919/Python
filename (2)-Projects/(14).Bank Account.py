class bankaccount:
    def __init__(self,name,balance=0):
        self.account_holder=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"Deposited {amount} to your account")
    def withdraw(self,amount):
        if(amount>self.balance):
            print("Not enough balance")
        else:
            self.balance-=amount
            print("Successfully withdrew")
    def __str__(self):
        return f"AccountHolder Name: {self.account_holder}\nBalance: {self.balance}"
obj=bankaccount("Sanu",3800)
print(obj)
obj.withdraw(500)
print(obj)
obj.deposit(150)
print(obj)