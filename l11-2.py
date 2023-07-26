#wpp to delete entire data but not file from the system.
def del_content():
    fp=open("data.txt","r+")
    fp.seek(0)
    fp.truncate()
    print("data deleted successfully")
del_content()

