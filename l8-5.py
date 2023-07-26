# l8-5 wpp to create a file,calculate size of the file,remove all end of line and blank
# lines from file,again calculate the size of file.
# strip method removes all endof line or blank lines from file
myfile=open("data.txt","r")
str1=" "
size=0
tsize=0
while str1:
    str1=myfile.readline()
    tsize+=len(str1)
    size+=len(str1.strip())
print("toatal size :",tsize)
print("size after removing all eol and blank lines :",size)
myfile.close()
