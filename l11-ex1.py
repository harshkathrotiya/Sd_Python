#11 ex1 using create a program to do all arithmatic operation using menu
# self is recommanded but not compulsory
class Arithmetic:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
print("menu")
print("1.sum")
print("2.minus")
print("3.multiplication")

print("4.division")
ch=int(input("which operaition you like to perform :"))
a=float(input("enter num 1: "))
b=float(input("enter num 2: "))
ob=Arithmetic(a,b)
if ch==1:
    print(ob.add())
elif ch==2:
    print(ob.sub())
elif ch==3:
    print(ob.mul())
elif ch==4:
    print(ob.div())
else:
    print("enter valid value ")
