#create a menubase program to perform the following operations on array 
# 1.create,2.view,3.updatebyindex,updateyvalue,4.removebyindex,removeduplicate values
# pop append remove 
# view create 
import array as arr

def create_arr():
    global a
    l=[]
    n=int(input("how many elenes you want to insert "))
    for i in range(0,n):
        data=int(input("enter the element :"))
        l.append(data)
    a=arr.array("i",l)

def view_arr():

    length=len(a)
    for i in range(0,length):
        print(a[i],end= " ")
    print("\n")
def upd_by_index():
    
    ind=int(input("which index you prefer to insert"))
    
    if ind<len(a):
        val=int(input("enter the value you should insert :"))
    else:
        print("index not found re enter")
    a.insert(ind,val)
def update_by_val():
    val=int(input("ente the value to update"))
    a.append(val)
def rem_by_index():
    ind=int(input("enter the index for remove element :"))
    if ind<len(a):
        a.pop(ind)
    else:
        print("enter valid index")
def rem_by_duplicate():
    
    for i in range(0,len(a)-1):
        
            for j in range(i+1,len(a)-1):
                if a[i]==a[j]:
                    print(a[i])
                    a.pop(i)
    print("values removed successfully")
  
while True:
    print("1.create")
    print("2.view")
    print("3.updatebyindex")
    print("4updatebyvalue")
    print("5.removebyindex")
    print("6.removebyduplicate")
    print("7.close")
    cho=int(input("  please enter your choice  ** :"))
    if(cho==1):
        create_arr()
    elif cho==2:
        view_arr()
    elif cho==3:
        upd_by_index()
    elif cho==4:
        update_by_val()
    elif cho==5:
        rem_by_index()
    elif cho==6:
        rem_by_duplicate()
    elif cho==7:
        break
    else:
        print("plz enter valid entry")

























