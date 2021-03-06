from Tkinter import *
import gspread

from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds"]
creds = ServiceAccountCredentials.from_json_keyfile_name('spreadsheet.json',scope)
client = gspread.authorize(creds)

sheet = client.open('Database').sheet1
root = Tk()

Line1 = Label(root, text="TIMETABLE", bg="red", fg="white")
Line1.grid(row=5,column=11)

DAYS = Label(root, text="DAY", fg="black")
Sun = Label(root, text="   Sunday", bg="white", fg="black", height=4,width=15)
Mon = Label(root, text="   Monday", bg="white", fg="black", height=4,width=15)
Tue = Label(root, text="  Tuesday", bg="white", fg="black", height=4,width=15)
Wed = Label(root, text="Wednesday", bg="white", fg="black", height=4,width=15)
Thu = Label(root, text=" Thursday", bg="white", fg="black", height=4,width=15)

DAYS.grid(row=2, sticky=E)
Sun.grid(row=3, sticky=E)
Mon.grid(row=4, sticky=E)
Tue.grid(row=5, sticky=E)
Wed.grid(row=6, sticky=E)
Thu.grid(row=7, sticky=E)

Day1 = Label(root, text="1", fg="black", height=4,width=15)
Day2 = Label(root, text="2", fg="black", height=4,width=15)
Day3 = Label(root, text="3", fg="black", height=4,width=15)
Day4 = Label(root, text="4", fg="black", height=4,width=15)
Day5 = Label(root, text="5", fg="black", height=4,width=15)
Day6 = Label(root, text="6", fg="black", height=4,width=15)
Day7 = Label(root, text="7", fg="black", height=4,width=15)
Day8 = Label(root, text="8", fg="black", height=4,width=15)

Day1.grid(row=2,column=2, sticky=E)
Day2.grid(row=2,column=3, sticky=E)
Day3.grid(row=2,column=4, sticky=E)
Day4.grid(row=2,column=5, sticky=E)
Day5.grid(row=2,column=6, sticky=E)
Day6.grid(row=2,column=7, sticky=E)
Day7.grid(row=2,column=8, sticky=E)
Day8.grid(row=2,column=9, sticky=E)

Sun1= Label(root, text=sheet.cell(2,2).value,bg="white", fg="black", height=4,width=15)
Sun2= Label(root, text=sheet.cell(2,3).value,bg="white", fg="black", height=4,width=15)
Sun3= Label(root, text=sheet.cell(2,4).value,bg="white", fg="black", height=4,width=15)
Sun4= Label(root, text=sheet.cell(2,5).value,bg="white", fg="black", height=4,width=15)
Sun5= Label(root, text=sheet.cell(2,6).value,bg="white", fg="black", height=4,width=15)
Sun6= Label(root, text=sheet.cell(2,7).value,bg="white", fg="black", height=4,width=15)
Sun7= Label(root, text=sheet.cell(2,8).value,bg="white", fg="black", height=4,width=15)
Sun8= Label(root, text=sheet.cell(2,9).value,bg="white", fg="black", height=4,width=15)

Sun1.grid(row=3,column=2, sticky=E) 
Sun2.grid(row=3,column=3, sticky=E)
Sun3.grid(row=3,column=4, sticky=E)
Sun4.grid(row=3,column=5, sticky=E)
Sun5.grid(row=3,column=6, sticky=E)
Sun6.grid(row=3,column=7, sticky=E)
Sun7.grid(row=3,column=8, sticky=E)
Sun8.grid(row=3,column=9, sticky=E)


Mon1= Label(root, text=sheet.cell(3,2).value,bg="black", fg="white", height=4,width=15)
Mon2= Label(root, text=sheet.cell(3,3).value,bg="black", fg="white", height=4,width=15)
Mon3= Label(root, text=sheet.cell(3,4).value,bg="black", fg="white", height=4,width=15)
Mon4= Label(root, text=sheet.cell(3,5).value,bg="black", fg="white", height=4,width=15)
Mon5= Label(root, text=sheet.cell(3,6).value,bg="black", fg="white", height=4,width=15)
Mon6= Label(root, text=sheet.cell(3,7).value,bg="black", fg="white", height=4,width=15)
Mon7= Label(root, text=sheet.cell(3,8).value,bg="black", fg="white", height=4,width=15)
Mon8= Label(root, text=sheet.cell(3,9).value,bg="black", fg="white", height=4,width=15)

Mon1.grid(row=4,column=2, sticky=E)
Mon2.grid(row=4,column=3, sticky=E)
Mon3.grid(row=4,column=4, sticky=E)
Mon4.grid(row=4,column=5, sticky=E)
Mon5.grid(row=4,column=6, sticky=E)
Mon6.grid(row=4,column=7, sticky=E)
Mon7.grid(row=4,column=8, sticky=E)
Mon8.grid(row=4,column=9, sticky=E)


Tue1= Label(root, text=sheet.cell(4,2).value,bg="white", fg="black", height=4,width=15)
Tue2= Label(root, text=sheet.cell(4,3).value,bg="white", fg="black", height=4,width=15)
Tue3= Label(root, text=sheet.cell(4,4).value,bg="white", fg="black", height=4,width=15)
Tue4= Label(root, text=sheet.cell(4,5).value,bg="white", fg="black", height=4,width=15)
Tue5= Label(root, text=sheet.cell(4,6).value,bg="white", fg="black", height=4,width=15)
Tue6= Label(root, text=sheet.cell(4,7).value,bg="white", fg="black", height=4,width=15)
Tue7= Label(root, text=sheet.cell(4,8).value,bg="white", fg="black", height=4,width=15)
Tue8= Label(root, text=sheet.cell(4,9).value,bg="white", fg="black", height=4,width=15)

Tue1.grid(row=5,column=2, sticky=E)
Tue2.grid(row=5,column=3, sticky=E)
Tue3.grid(row=5,column=4, sticky=E)
Tue4.grid(row=5,column=5, sticky=E)
Tue5.grid(row=5,column=6, sticky=E)
Tue6.grid(row=5,column=7, sticky=E)
Tue7.grid(row=5,column=8, sticky=E)
Tue8.grid(row=5,column=9, sticky=E)

Wed1= Label(root, text=sheet.cell(5,2).value,bg="black", fg="white", height=4,width=15)
Wed2= Label(root, text=sheet.cell(5,3).value,bg="black", fg="white", height=4,width=15)
Wed3= Label(root, text=sheet.cell(5,4).value,bg="black", fg="white", height=4,width=15)
Wed4= Label(root, text=sheet.cell(5,5).value,bg="black", fg="white", height=4,width=15)
Wed5= Label(root, text=sheet.cell(5,6).value,bg="black", fg="white", height=4,width=15)
Wed6= Label(root, text=sheet.cell(5,7).value,bg="black", fg="white", height=4,width=15)
Wed7= Label(root, text=sheet.cell(5,8).value,bg="black", fg="white", height=4,width=15)
Wed8= Label(root, text=sheet.cell(5,9).value,bg="black", fg="white", height=4,width=15)

Wed1.grid(row=6,column=2, sticky=E)
Wed2.grid(row=6,column=3, sticky=E)
Wed3.grid(row=6,column=4, sticky=E)
Wed4.grid(row=6,column=5, sticky=E)
Wed5.grid(row=6,column=6, sticky=E)
Wed6.grid(row=6,column=7, sticky=E)
Wed7.grid(row=6,column=8, sticky=E)
Wed8.grid(row=6,column=9, sticky=E)

Thu1= Label(root, text=sheet.cell(6,2).value,bg="white", fg="black", height=4,width=15)
Thu2= Label(root, text=sheet.cell(6,3).value,bg="white", fg="black", height=4,width=15)
Thu3= Label(root, text=sheet.cell(6,4).value,bg="white", fg="black", height=4,width=15)
Thu4= Label(root, text=sheet.cell(6,5).value,bg="white", fg="black", height=4,width=15)
Thu5= Label(root, text=sheet.cell(6,6).value,bg="white", fg="black", height=4,width=15)
Thu6= Label(root, text=sheet.cell(6,7).value,bg="white", fg="black", height=4,width=15)
Thu7= Label(root, text=sheet.cell(6,8).value,bg="white", fg="black", height=4,width=15)
Thu8= Label(root, text=sheet.cell(6,9).value,bg="white", fg="black", height=4,width=15)

Thu1.grid(row=7,column=2, sticky=E)
Thu2.grid(row=7,column=3, sticky=E)
Thu3.grid(row=7,column=4, sticky=E)
Thu4.grid(row=7,column=5, sticky=E)
Thu5.grid(row=7,column=6, sticky=E)
Thu6.grid(row=7,column=7, sticky=E)
Thu7.grid(row=7,column=8, sticky=E)
Thu8.grid(row=7,column=9, sticky=E)

root.mainloop()
