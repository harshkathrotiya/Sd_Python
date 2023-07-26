# exercise write a program to enter the two number and check the following 
"""1) both numbers are equal
2)num 1 is less to num 1 
3)num 1 is greater than num 2
"""
a=int(input("enter num1 :"))
b=int(input("enter num2 :"))

print("both are same") if a==b else print("a is greater than b") if a>b else print("a is smaller than b")