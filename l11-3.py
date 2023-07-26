#wpp to delete data as per user requirement from the file
def user_delete():
    with open("data.txt","r") as fp:
        data=fp.readlines()
    with open("data.txt","w") as fp:
        for i in data:
            if i.strip("\n")!="age:19":
                fp.write(i)
            else:
                print("data not match")
user_delete()