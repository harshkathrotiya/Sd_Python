import tkinter as tk 

root=tk.Tk()
f=tk.Frame(root,width=700,height=500)
f.propagate(0)
f.pack()
lbl=tk.Label(f,text="click one or more item")
lbl.place(x=50,y=50)
lb=tk.Listbox(f,height=8,selectmode=tk.MULTIPLE)
lb.place(x=50,y=100)
listitem=["Gujarat","tamilnadu","kerala","karnataka","maharashtra"]
def on_select():
    # lst=[]
    indexes=[]
    indexes=lb.curselection()
    print(indexes)
    if indexes:
        for i in indexes:
            selected=lb.get(indexes[i])
            t.insert("1.0",selected)
        

for i in listitem:
    lb.insert(tk.END, i)
lb.bind('<<listboxselect>>', on_select)
t=tk.Text(f,width=40,height=6,wrap=tk.WORD)
t.place(x=300,y=100)
root.title("listbox")
bt=tk.Button(f,text="click",command=on_select)
bt.place(x=340,y=330)
root.mainloop() 



