# 9-7 wpp to replace character i in place of j in your text file and display the output.

def jreplace_i():
    fp=open("demo.txt","r")
    str=fp.read()
    count=0
    for i in str:
        if i=='j' or i=='J':
            print("i",end="")
        else:
            print(i,end="")
    fp.close()
jreplace_i()

