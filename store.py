import Tkinter as tk
master = tk.Tk()
X1 = "AKIS STORE \n "
msg = tk.Message(master, text = X1)
msg.config(font=('times', 20, 'italic'), fg = 'white' , bg='red')
msg.pack()
#tk.mainloop()

photo1 = tk.PhotoImage(file="store.gif")
photo1 = photo1.subsample(5,5)
label1 = tk.Label(master, image=photo1)
label1.pack()

def school_sl():
    
    v = tk.IntVar()

    tk.Label(master, 
    text="""School Uniform""",font=('times', 18, 'italic'), fg='yellow' , bg = "magenta" ,
    justify = tk.LEFT,
    padx = 20).pack()
    tk.Radiobutton(master, 
              text="White Shirt",
              font=('times', 14),  fg = 'blue',
              padx = 20, 
              variable=v, 
              value=1).pack(anchor=tk.W)
    tk.Radiobutton(master, 
              text="House Tie", font=('times', 14), fg = 'blue',
              padx = 20, 
              variable=v, 
              value=2).pack(anchor=tk.W)
    tk.Radiobutton(master, 
              text="Grey Pant", font=('times', 14), fg = 'blue',
              padx = 20, 
              variable=v, 
              value=3).pack(anchor=tk.W)
    tk.Radiobutton(master, 
              text="House TShirt", font=('times', 14), fg = 'blue',
              padx = 20, 
              variable=v, 
              value=4).pack(anchor=tk.W)
    top = tk.Frame(master)
    top.pack()
    L1 = tk.Label(top, text="Quantity" , font=('times', 12), fg='cyan' , bg='black')
    L1.pack(side = tk.LEFT)
    E1 = tk.Entry(top, bd =5)
    E1.pack(side = tk.LEFT)
    top1 = tk.Frame(master)
    top1.pack()
    L2 = tk.Label(top1, text="Size" , font=('times', 12), fg='cyan' , bg='black')
    L2.pack(side = tk.LEFT)
    E2 = tk.Entry(top1, bd =5)
    E2.pack(side = tk.LEFT)
    top2 = tk.Frame(master)
    top2.pack()
    L3 = tk.Label(top2, text="House Name",font=('times', 12), fg='cyan' , bg='black')
    L3.pack(side = tk.LEFT)
    E3 = tk.Entry(top2, bd =5)
    E3.pack(side = tk.LEFT)
    

def sta_sl():
    

    b = tk.IntVar()

    tk.Label(master, 
    text="""Stationary""", font=('times', 18, 'italic'), fg='yellow' , bg = "magenta" , 
    justify = tk.LEFT,
    padx = 20).pack()
    tk.Radiobutton(master, 
              text="Notebooks", font=('times', 14), fg = 'blue',
              padx = 20, 
              variable=b, 
              value=1).pack(anchor=tk.W)
    tk.Radiobutton(master, 
              text="Textbooks", font=('times', 14), fg = 'blue',
              padx = 20, 
              variable=b, 
              value=2).pack(anchor=tk.W)
    tk.Radiobutton(master, 
              text="Pens", font=('times', 14), fg = 'blue',
              padx = 20, 
              variable=b, 
              value=3).pack(anchor=tk.W)
    tk.Radiobutton(master, 
              text="Pencils", font=('times', 14), fg = 'blue',
              padx = 20, 
              variable=b, 
              value=4).pack(anchor=tk.W)
    top = tk.Frame(master)
    top.pack()
    L1 = tk.Label(top, text="Quantity", font=('times', 12), fg='cyan' , bg='black')
    L1.pack( side = tk.LEFT)
    E1 = tk.Entry(top, bd =5)
    E1.pack(side = tk.RIGHT)
    

frame = tk.Frame(master)
frame.pack()

button = tk.Button(frame, 
                   text="Garments", font=('times', 18), 
                   fg="red",
                   command=school_sl)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Stationary", font=('times', 18), fg="red" ,
                   command=sta_sl)
slogan.pack(side=tk.LEFT)

slogan1 = tk.Button(frame,
                   text="Submit", font=('times', 18), fg="red",
                   command=quit)
slogan1.pack(side=tk.LEFT)


tk.mainloop()

