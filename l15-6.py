# l15-6 gui  
import tkinter as t
r=t.Tk()#init
r.title("my frame")
t.Label(r,bg= "red",foreground="pink",text="first name").grid(row=0)
t.Label(r,text="last name",foreground="pink",bg= "gray51").grid(row=1)
e1=t.Entry(r)
e2=t.Entry(r)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
r.mainloop()
