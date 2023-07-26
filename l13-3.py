"""name number basic salary

"""
class Person:
    def __init__(self,name,number,bas_sal):
        self.name=name
        self.number=number
        self.sal=bas_sal
    def display(self):
        print("name of person is :",self.name)
        print("number of person :",self.number)
    
class Employee(Person):
    def __init__(self,name,num,bas_sal):
        Person.__init__(self,name,num,bas_sal)
    def cal_sal(self):
        self.s=self.sal+(self.sal*0.5)-(self.sal*0.3)
        print("total salary is ",self.s)

obj=Employee("harsh",1234565432,100000)
obj.display()
obj.cal_sal()
obj2=Employee("sahil",433,20000000)