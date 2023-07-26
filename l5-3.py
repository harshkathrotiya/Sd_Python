#wpp to find maximum of theree numbers
a=int(input("ener the num  :"))
b=int(input("ener the num  :"))
c=int(input("ener the num  :"))
max=a if a>b and a>c else b if b>c else c
print("maximum num is ",max)
