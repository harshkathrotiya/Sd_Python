# 9 wpp to execute a string containing a python code
m='print("hello how are you")'
s="""
def multiply(x,y):
    return x*y
x=int(input("enter num :"))
y=int(input("enter num :"))
print("result is:",multiply(x,y))
"""
exec(m)
exec(s)
