from Tkinter import *
import os

root = Tk()

def tt():
    
    os.system('ttable.py')    

def uniform():

    os.system('store.py')
        
def date():

    os.system('dates.py')
    
def ask():

    os.system('doubt.py')

    
timetable = PhotoImage(file="timetable.gif")
timetable = timetable.subsample(2, 2)

store = PhotoImage(file="store.gif")
store = store.subsample(2, 2)

chat = PhotoImage(file="chat.gif")
chat = chat.subsample(2, 2)

cal = PhotoImage(file="download.gif")
cal = cal.subsample(2, 2)

timetable1 = Button(root, image=timetable, command=tt)
timetable1.grid(row=0, column=0)

store1 = Button(root, image=store, command=uniform)
store1.grid(row=0, column=1)

chat1 = Button(root, image=chat, command=ask)
chat1.grid(row=1, column=1)

cal1 = Button(root, image=cal, command=date)
cal1.grid(row=1, column=0)

root.mainloop()
