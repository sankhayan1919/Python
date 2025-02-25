class demo:
    def add(self,*args):
        total=self
        for i in args:
            total=total+i
        return total
print(demo.add(1,2))
print(demo.add(2,4,6))
print(demo.add(3,6,9,12))
