# wpp to divide twonumber if divisor is zerp throw zerodivision error
def div(num1,num2):
    try:
        print(num1/num2)
    except ZeroDivisionError:
        print("it can't divide by zero")
div(3,0)