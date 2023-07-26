#create a method in a class to calculate sum of two number given by user

class Sum:
    def __init__(self,a,b):
        self.a=a
        self.a=b
    def add(self):
        self.addition=self.a+self.b
        print("addition is ",self.addition)

a=int(input("enter first num :"))
b=int(input("enter second num :"))
ob=Sum(a,b)
ob.add()

