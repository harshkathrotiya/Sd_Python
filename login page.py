# ds list tuple dictionary string
# conditinal statements,loops,object oriented exception handling gui database.
# 1 august

import tkinter
from tkinter import messagebox

window=tkinter.Tk()
window.title("Login page using python")
window.geometry('750x750')
window.configure(bg='#9288F8')
frame=tkinter.Frame(bg='#9288F8')
login_label=tkinter.Label(frame,text="login page using python",bg='#E8FFCE',fg='#3E001F',font=("Arial",30)).grid(row=1,column=1,columnspan=2,sticky="news",pady=40)
username_label=tkinter.Label(frame,text="Username",bg="#7C73C0",fg="#000000",font=("Arial",16,'bold')).grid(row=2,column=1)
password_label=tkinter.Label(frame,text="Password",bg="#7C73C0",fg="#000000",font=("Arial",16,'bold')).grid(row=3,column=1)
username_entry=tkinter.Entry(frame,font=('Arial',16,))
password_entry=tkinter.Entry(frame,font=('Arial',16),show="*")
def login():
    username="harsh"
    password="harsh"
    
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login successful",message="you successfully logged in")
    else:
        messagebox.showinfo(title="error",message="invalid id or password")
login_button=tkinter.Button(frame,text="login",bg='#DC143C',fg='#FFFFFF',font=("Arial",16),command=login).grid(row=4,column=2)
username_entry.grid(row=2,column=2)
password_entry.grid(row=3,column=2)
frame.pack()
window.mainloop()
