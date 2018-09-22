from Tkinter import *

root=Tk()

Frame1 = Frame(root)
Frame1.pack()

cal = PhotoImage(file="calendar.gif")

calendar = Label(Frame1, image=cal)
calendar.grid(row=0, column=0)

root.mainloop()

