#  2 wpf to multiply all the numbers of a list

def Multiply(numbers):
    total=1
    for i in numbers:
        total*=i
    return total
result=Multiply([1,2,3,4,5,6])
print(result)
