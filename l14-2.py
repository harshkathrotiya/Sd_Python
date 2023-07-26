#14-2

class Student:
    def takedetail(self):
        self.name=input("enter your name :")
        self.fname=input("enter your father name :")
        self.sub1=int(input("enter marks 1 :"))
        self.sub2=int(input("enter marks 2 :"))
class Ugstudent(Student):
    def __init__(self,yearofg):
        self.yearofg=yearofg
    def display(self):
        print("name is ",self.name)
        print("father name is",self.fname)
        print("year of graduation is :",self.yearofg)
        if self.sub1+self.sub2<=70:
            print("grade is  c")
        elif self.sub1+self.sub2<80:
            print("grade is  b")
        elif self.sub1+self.sub2>=80:
            print("grade is a")
class Pgstudent(Student):
        def __init__(self):
            self.takedetail()
        def displays(self):
            print("name is ",self.name)
            print("father name is",self.fname)
            print("total marks is ",self.sub1+self.sub2)

ob=Ugstudent(2023)
ob.takedetail()
ob.display()
obj=Pgstudent()
obj.displays()

