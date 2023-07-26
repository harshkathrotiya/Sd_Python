#15  -1write a method to check the file exist or not and write the content on file if file doesn't exist throw
#a exception to display can't find file.

try:
    fp=open("myfile.txt","w")
    fp.write("this is exception handling")
except IOError:
    print("can not found file")
else:
    print("content writted successfully")
    fp.close()
