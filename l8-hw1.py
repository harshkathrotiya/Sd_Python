# l8-hw2 wpp to calculate number of lines in a file
myfile=open("demo.txt","r")
str= " "
i=0
while str:
    str=myfile.readline()
    i+=1
print("lines :",i-1)
myfile.close()


