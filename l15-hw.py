import tkinter as tk    
root = tk.Tk()
#root.geometry("100×100")
root.title("My buttons")
button1 = tk.Button(root, text="Button 1",activebackground="pink", width=15)
button1.grid(row=0, column=0)

button2 = tk.Button(root, text="Button 2", width=15,activebackground="pink")
button2.grid(row=0, column=1)

button3 = tk.Button(root, text="Button 3", width=15,activebackground="pink")
button3.grid(row=0, column=2)

button4 = tk.Button(root, text="Button 4", width=15,activebackground="pink")
button4.grid(row=1, column=0)

button5 = tk.Button(root, text="Button 5", width=15,activebackground="pink")
button5.grid(row=1, column=1)

button6 = tk.Button(root, text="Button 6", width=15,activebackground="pink")
button6.grid(row=1, column=2)

button7 = tk.Button(root, text="Button 7", width=15,activebackground="pink")
button7.grid(row=2, column=0)

button8 = tk.Button(root, text="Button 8", width=15,activebackground="pink")
button8.grid(row=2, column=1)

button9 = tk.Button(root, text="Button 9", width=15,activebackground="pink")
button9.grid(row=2, column=2)

root.mainloop()
