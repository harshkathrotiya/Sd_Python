# 1 wpf to find maximum of three numbers.
# def is use for declare function or method
#in company first letter of the function is capital.

def Max_of_two (x,y):
    if x>y:
        return x
    else :
        return y
    
def Max_of_three(x_Max,y,z):
    return Max_of_two(x_Max,Max_of_two(y,z))

result=Max_of_three(4, 89, -5)
print(result)
