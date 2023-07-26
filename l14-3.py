#14-3 write a program to check the given value is in=teger or not if the value is not integer throw a exception and
# print value is not integer
# my
# def read_int():
#     try:
#         a=int(input("enter any number :"))
#         print("no is :",a)
#     except ValueError :
#         print("not int")
# read_int()

# mam
def read_int():
    while True:
        a=input("enter num :")
        try:
            return int(a)
        except ValueError:
            print("enter integer :")
b=read_int()
print(b)