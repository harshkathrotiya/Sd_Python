# 4 liip in read
myfile=open("data.txt","r")
str=" "
while str:
    str=myfile.readline()
    print(str,end='')
#here either while or either for used.
for str in myfile:
    print(str,end="")
myfile.close()
