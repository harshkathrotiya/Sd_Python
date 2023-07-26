import pickle
def insert():
    fp=open("employee.dat","ab")
    emp_no=int(input("Enter employee no"))
    emp_name=input("enter employee name")
    emp_desg=input("enter employee designation")
    emp_sal=float(input("enter employee salary"))
    emp_dob=input("enter employee date of birth")
    emp_doj=input("enter employee date of joining")
    record=[emp_no,emp_name,emp_desg,emp_sal,emp_dob,emp_doj]
    pickle.dump(record,fp)
    fp.close()
    
def view():
    fp=open("employee.dat","rb")
    while True:
        try:
            rec=pickle.load(fp)
            print("Employee id :",rec[0])
            print("Employee name :",rec[1])
            print("Employee designation:",rec[2])
            print("Employee salary :",rec[3])
            print("Employee date of birth :",rec[4])
            print("Employee date of joining :",rec[5])
        except EOFError:
            pass
    fp.close()
def search_desg(designation):
    fp=open("employee.dat","rb")
    while True:
        try:
            rec=pickle.load(fp)
            if rec[2]==designation:
                print("Employee id :",rec[0])
                print("Employee name :",rec[1])
                print("Employee designation:",rec[2])
                print("Employee salary :",rec[3])
                print("Employee date of birth :",rec[4])
                print("Employee date of joining :",rec[5])
            
        except EOFError:
            pass
    fp.close()
                

def runmenu():
    while True:
        print("1: Insert \n 2: View  \n 3: Search by designation")
        choice=int(input("enter your choice"))
        if choice==1:
            insert()
            ch=input("enter your choice Y/N")  
            if ch in 'Nn':
                break
        elif choice==2:
            view()
        elif choice==3:
            des=input("enter designation to search")
            search_desg(des)
        else:
            break
runmenu()
    