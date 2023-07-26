# wpp in python hto swap two solve quadratic equation
# where x=(-b+-sqrt(b**2-4ac))/(2a)
import cmath
a=float(input("enter a :"))
b=float(input("enter b :"))
c=float(input("enter c :"))

d=(cmath.sqrt(b**2-4*a*c)/(2*a))
#solution
pos=-b+d
neg=-b-d
print("positive value is",pos,"negative value is",neg)

