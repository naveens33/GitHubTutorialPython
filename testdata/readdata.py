from pathlib import Path

import xlrd

def getdata():
    wb=xlrd.open_workbook(str(Path(__file__).parent)+r'\PayeeDetails.xlsx')
    sheet=wb.sheet_by_name('PayeeDetails')
    data=[]
    for i in range(1,sheet.nrows):
        li=[]
        for j in range(0,sheet.ncols):
            li.append(sheet.cell_value(i,j))
        data.append(li)

    return data
