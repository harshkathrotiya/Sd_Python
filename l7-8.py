# 8
#wpp to create and print list where the values  are the aquares of numbers between 1 and 30

def Square_values():
    l=list()
    for i in range(1,31):
        l.append(i**2)
    return l
print(Square_values())
