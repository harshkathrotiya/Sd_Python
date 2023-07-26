class Employee:
    # def __init__(self,emp_id,emp_name,emp_desg):
    #     self.emp_id=emp_id
    #     self.emp_name=emp_name
    #     self.emp_desg=emp_desg
    #     self.l=[emp_id,",",emp_name,",",emp_desg,"\n"]
    def __init__(self):
        pass
    # def writedata(self):
    #     self.fp=open("newfile.txt","a")
    #     self.fp.writelines(self.l)
    #     self.fp.write("\n")
    #     self.fp.close()
    def display(self):
        self.fp=open("newfile.txt","r")
        while True:
            self.rec=self.fp.readline()
            if not self.rec:
                break
            self.rec1=self.rec.split(",")
            print("Employee id :",int(self.rec1[0]))
            print("Employee name :",self.rec1[1])
            print("Employee designation:",self.rec1[2])
    def search(self):
        self.fp=open("newfile.txt","r")
        while True:
            self.rec=self.fp.readline()
            if not self.rec:
                break
            self.rec1=self.rec.split(",")
            if self.rec1[2]=="manager\n":
                print("Employee id :",int(self.rec1[0]))
                print("Employee name :",self.rec1[1])
                print("Employee designation:",self.rec1[2])
        
        self.fp.close()   
# n=int(input("enter no of records"))
# for i in range(0,n):
    # emp_id=input("enter emp  id")
    # emp_name=input("enter emp  name")
    # emp_desg=input("enter emp  desg")
    # #obj.writedata()
    # obj=Employee(emp_id,emp_name,emp_desg)
obj=Employee()
# obj.display()ss
obj.search()
#ch=int(input("enter your choice"))