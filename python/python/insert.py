import MySQLdb as db2

def insert_row(emp_id,first_name,age,sex,income):
    db1=db2.connect(host="localhost",user="root",password="",db="employeedb")
    cursor=db1.cursor() 
    sql="insert into employee(EMP_ID,NAME,AGE,SEX,INCOME) VALUES('%d','%s','%d','%s','%d')"
    args=(emp_id,first_name,age,sex,income)
    try:
        cursor.execute(sql % args)
        db1.commit()
        print("row inserted")
    except:
        db1.rollback()
    finally:
        cursor.close()
        db1.close()

n=int(input("enter num of rows"))
for i in range(n):
    eno=int(input("enter e id"))
    ename=input("enter e name")
    eage=int(input("enter e age"))
    esex=input("enter e sex")
    eincome=int(input("enter e income"))
    insert_row(eno,ename,eage,esex,eincome)
    
    
                                              