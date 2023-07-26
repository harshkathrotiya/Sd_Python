# 2file handling program
myfile=open("data.txt","r")

str1=myfile.read()
str2=myfile.read(10)
str3=myfile.read(5)

print("output of the first read :")
print(str1)
print("output of the second read :")
print(str2)
print("output of the third read :")
print(str3)
myfile.close()