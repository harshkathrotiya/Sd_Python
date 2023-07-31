import tkinter as tk 
# import PIL
# from PIL import Image,ImageTk
root=tk.Tk()
c=tk.Canvas(root,bg="#9898F5",height=700,width=600)
c.pack()
f1=tk.PhotoImage(file='my.gif')
f2=tk.PhotoImage(file='back.png')
id=c.create_image(200,200,image=f1)
id=c.create_image(300, 300,image=f2,activeimage=f1)
root.mainloop()
