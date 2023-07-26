# 9-5 wpp to count upper case characters in a text file
def count_upper():
    fp=open("demo.txt","r")
    str=fp.read()
    count=0
    for i in str:
        if i.isupper():
            count+=1
    if count:
        print("total upper characters is :",count)
    else:
        print("no upper words")
    fp.close()
count_upper()