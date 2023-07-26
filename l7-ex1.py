# ex-1 wpp to create menu of arithmetic operations using function

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y
def menu():
    print("menu")
    print("1.add")
    print("2.minus")
    print("3.multiply")
    print("4.division")
menu()
choice=int(input("plz enter your choice :"))
a=int(input("enter num 1:"))
b=int(input("enter num 2:"))
if choice==1:
    s=add(a,b)
elif choice==2:
    s=sub(a,b)
elif choice==3:
    s=mul(a,b)
elif choice==4:
    s=div(a,b)
else:
    print("plz input valud entry")
    
print("your ans is :",s)
