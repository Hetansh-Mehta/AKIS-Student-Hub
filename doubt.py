import gspread
from oauth2client.service_account import ServiceAccountCredentials

from Tkinter import *

scope = ["https://spreadsheets.google.com/feeds"]
creds = ServiceAccountCredentials.from_json_keyfile_name('spreadsheet.json',scope)
client = gspread.authorize(creds)
sheet = client.open('credentials').sheet1

root = Tk()

Frame = Frame(root)
Frame.pack()

def bypass(event):
    leave()
    
def leave():

    done = Label(Frame, text="Question submitted!")
    done.config(font='Segoe', fg="white", bg="black")
    done.grid(row=4, column=0, columnspan=2)

    sheet.update_cell(10,2,d_input.get())

    q = Label(Frame, text=sheet.cell(10,2).value)
    q.config(font='Segoe', fg="black")
    q.grid(row=5, column=0, columnspan=2)


    a = Label(Frame, text=sheet.cell(10,3).value)
    a.config(font='Segoe', fg="black")
    a.grid(row=6, column=0, columnspan=2)
    

t = Label(Frame, text="Teacher: ")
t.config(font=('Segoe UI Light', 12))
d = Label(Frame, text="Doubt: ")
d.config(font=('Segoe UI Light', 12))
t_input = Entry(Frame)
d_input = Entry(Frame)


t.grid(row=1, column=0, sticky=E)
d.grid(row=2, column=0, sticky=E)


t_input.grid(row=1, column=1)
d_input.grid(row=2, column=1)

Submit = Button(Frame, text="Enter", fg="black", command=leave)
Submit.config(font=('Segoe UI Light', 12))
Submit.grid(row=3, column=0, columnspan=2)

root.bind('<Return>',bypass)

q = Label(Frame, text=sheet.cell(10,2).value)
q.config(font='Segoe', fg="black")
q.grid(row=5, column=0, columnspan=2)

a = Label(Frame, text=sheet.cell(10,3).value)
a.config(font='Segoe', fg="black")
a.grid(row=6, column=0, columnspan=2)




root.mainloop()
