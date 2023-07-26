# l15-2
def temp_convert(var):
    try:
        print(int(var))
    except ValueError:
        print("the argument is not number ")
    else :
        print("hello")
# print(temp_convert(4.78))
temp_convert(4.56)
