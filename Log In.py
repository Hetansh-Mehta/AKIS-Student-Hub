import gspread
import pprint
from oauth2client.service_account import ServiceAccountCredentials
import os

from Tkinter import *

scope = ["https://spreadsheets.google.com/feeds"]
creds = ServiceAccountCredentials.from_json_keyfile_name('spreadsheet.json',scope)
client = gspread.authorize(creds)

sheet = client.open('credentials').sheet1
pp = pprint.PrettyPrinter()

root = Tk()
root.resizable(width=False, height=False)

def bypass(event):
    new()

def new():
   for i in range(1,10):
       
       if (adno_input.get()) == sheet.cell(i,1).value:
           
           if (pw_input.get()) == sheet.cell(i,2).value:
               
               root.destroy()
               execfile('Main.py')
               break

       else:
           error = Label(bottomFrame, text="SORRY, WRONG PASSWORD.")
           error.config(font='Segoe', fg="white", bg="black")
           error.grid(row=4, column=0, columnspan=2)
           
           break

topFrame = Frame(root)
topFrame.pack(side=TOP)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

logo = PhotoImage(file="StudentHubLogo.gif")
logo = logo.subsample(4, 4)  # Diminish an Image

piclabel = Label(topFrame, image=logo)
piclabel.grid(row=0, column=0)

adno = Label(bottomFrame, text="Admission Number: ")
adno.config(font=('Segoe UI Light', 12))
pw = Label(bottomFrame, text="Password: ")
pw.config(font=('Segoe UI Light', 12))
adno_input = Entry(bottomFrame)
pw_input = Entry(bottomFrame, show='*')

adno.grid(row=1, column=0, sticky=E)
pw.grid(row=2, column=0, sticky=E)

adno_input.grid(row=1, column=1)
pw_input.grid(row=2, column=1)

Login = Button(bottomFrame, text="Log in", fg="black", command=new)
Login.config(font=('Segoe UI Light', 12))
Login.grid(row=3, column=0, columnspan=2)

root.bind('<Return>',bypass)


root.mainloop()
