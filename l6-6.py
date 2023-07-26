# 6 wpp to print diamond pattern with star symbol

n=int(input("enter num :"))
for i in range(n):
    print((" "*(n-i))+("* "*(i)))
for i in range(n):
    print((" "*i)+("* "*(n-i)))
    