# hw add menu insert creage db,create table,insert data,updatedata,deletedata
import tkinter as t
from tkinter import filedialog
# global tr
import MySQLdb as db2
# import mysql.connector as db2

root = t.Tk()

root.title('menu demonstration')
menubar = t.Menu(root)
# def newFile():
#     f=open("Untitled - Notepad","a")


def open_file():
  fname = filedialog.askopenfilename(parent=root, title="select a file")
  if fname != None:
    f = open(fname, "r")
    c = f.read()
    global tr
    tr = t.Text(root, width=80, height=20)
    tr.pack()
    tr.insert(1.0, c)
    f.close()


def save_file():
  fname = filedialog.asksaveasfilename(parent=root, defaulttextension=".txt")
  if fname != " ":
    with open(fname, "w") as f:
      content = tr.get(1, t.END)
      f.write(content)
      f.close()


def insert_row():
  n = int(input("enter num of rows :"))
  for i in range(n):
    eno = int(input("enter e id :"))
    ename = input("enter e name :")
    eage = int(input("enter e age :"))
    esex = input("enter e sex :")
    eincome = int(input("enter e income :"))
  db1 = db2.connect(host="localhost",
                    user="root",
                    password="",
                    db="employeedb")
  cursor = db1.cursor()
  sql = "insert into employee(EMP_ID,NAME,AGE,SEX,INCOME) VALUES('%d','%s','%d','%s','%d')"
  args = (eno, ename, eage, esex, eincome)
  try:
    cursor.execute(sql % args)
    db1.commit()
    print("row inserted")
  except:
    db1.rollback()
  finally:
    cursor.close()
    db1.close()


def create_db():
  db1 = db2.connect(host="localhost", user="root", password="")
  name = input("enter name of your db :")
  cursor = db1.cursor()
  sql = "create database if not exists {name}".format(name=name)
  cursor.execute(sql)
  print("db created")
  cursor.close()
  db1.close()


def create_table():
  db1 = db2.connect(host="localhost",user="root",password="",db="harsh")
  
  cursor = db1.cursor()
  qry = "CREATE TABLE customers (id INT AUTO_INCREMENT, name VARCHAR(50), address VARCHAR(70))) "
  cursor.execute(qry)
  print("table created")
  cursor.close()
  db1.close()


#adding file menu and commands
file = t.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file)
file.add_command(label="New file", command=None)
file.add_command(label="Open", command=open_file)
file.add_command(label="save", command=save_file)
file.add_separator()
file.add_command(label="Exit", command=root.destroy)

#adding edit menu and commands
edit = t.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit)
edit.add_command(label="cut", command=None)
edit.add_command(label="copy", command=None)
edit.add_command(label="paste", command=None)
edit.add_command(label="Select all", command=None)
edit.add_separator()
edit.add_command(label="Find", command=None)

#addng help menu and commands

helps = t.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helps)
helps.add_command(label="community", command=None)
helps.add_command(label="contact us", command=None)
helps.add_command(label="Demo", command=None)
helps.add_command(label="About Tk", command=None)

insert = t.Menu(menubar, tearoff=0)
menubar.add_cascade(label="db", menu=insert)
insert.add_command(label="insert", command=insert_row)
insert.add_command(label="createdb", command=create_db)
insert.add_command(label="createtable", command=create_table)
root.config(menu=menubar)
root.mainloop()
