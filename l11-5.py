#how to declare variable insight a class using constructor.
class Myclass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
obj=Myclass("harsh",19)
print("name is:",obj.name,"age is :",obj.age)
