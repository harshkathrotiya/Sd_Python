# 10 wpp to print characters at odd position for the given string

st=input("enter the string :")

for i in range(len(st)):
    if i%2==0:
        print(st[i])