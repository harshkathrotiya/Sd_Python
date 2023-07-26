# 4
#   wpf to calculate factorial of a number the function
# excepts the number as an argument.

def factorial(number):
    if number==0:
        return 1
    else:
        return number*factorial(number-1)
n=int(input("enter any number :"))
result=factorial(n)
print("factorial is",result)
