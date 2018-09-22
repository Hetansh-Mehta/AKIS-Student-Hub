import gspread

import random
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds"]
creds = ServiceAccountCredentials.from_json_keyfile_name('spreadsheet.json',scope)
client = gspread.authorize(creds)

sheet = client.open('Database').sheet1

z=2
b=8
while z<=6 and b<=12:
    L1 = []
    i = 2
    while len(L1)<8:
        print ""
        a=random.randint(4,11)
        value = sheet.cell(27,a).value
        try:
            L1.index(value)
        except ValueError:
            L1.append(value)
            sheet.update_cell(z,i,value)
            i+=1
            print L1
    L=[]
    i=2

    while len(L)<8:

        a=random.randint(4,11)
        value = sheet.cell(27,a).value
        try:
            L.index(value)
        except ValueError:
            if value==sheet.cell(z,i).value:
                continue
            else:
                L.append(value)
                sheet.update_cell(b,i,value)
                i+=1
            print L
    z+=1
    b+=1

print 'done'
