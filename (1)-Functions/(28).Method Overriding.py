class mother:
    def sleep(self):
        print("sleeps from 12.00pm to 3am")
class son(mother):
    def sleep(self):
        print("sleeps from 1.00am to 8am")
        super().sleep()
Sanu=son()
Sanu.sleep()