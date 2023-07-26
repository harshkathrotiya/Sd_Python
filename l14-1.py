#14-1 demo multilevel inheritance
class Student:
    def __init__(self,cname):
        self.cname=cname
class Ugstudent(Student):
    def __init__(self,name,year):
        self.name=name
        self.year=year
        Student.__init__(self,"abcd")
    def display(self):
        print(self.cname)

class Pgstudent(Student):
    def __init__(self,marks):
        self.marks=marks
        Student.__init__(self,"harsh")
    def display(self):
        print(self.marks)
        print(self.cname)

obj1=Ugstudent("harsh",2023)
obj2=Pgstudent(34)
obj2.display()
obj1.display()




