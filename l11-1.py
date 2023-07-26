#11-1 wpf to delete entire data along with file from system
import os
def file_del():
    if os.path.exists("demo.txt"):
        os.remove("demo.txt")
        print("file deleted ")
    else:
        print("file doesn't exist")
file_del()
