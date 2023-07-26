# 4 wpf that except a string and count the number of upper and lower case letters.
def String_count(s):
    d={"UPPER":0,"Lower":0}
    for i in s:
        if i.isupper():
            d["UPPER"]+=1
        else:
            d["Lower"]+=1
    return d
st=input("enter the string :")
result=String_count(st)
print(result)

