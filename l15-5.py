# l15-5 gui programming 1
import tkinter as t
r=t.Tk() #Tk is method of tkinter library r is object createc by Tk method ,first step of gui is create object
r.title("harsh") # title of canvas title method is use for give title
button=t.Button(r,text="mybutton",height=5,width=5,command=r.destroy) # Button is initialize button r object passed in button and text  
button.pack() # pack is use for associate button with canvas

r.mainloop()