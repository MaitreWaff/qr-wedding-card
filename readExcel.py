import openpyxl

from openpyxl import Workbook, load_workbook

# Load in your workbook

book = load_workbook('invites_vendredi09.xlsx')

sheet = book.active

# print(sheet)
# print(sheet['A2'].value)

# sheet['A2'].value = 'WAWA'

# book.save('menu.xlsx')


rows = sheet.rows

headers = [cell.value for cell in next(rows)]

all_rows = []

# ['item', 'price']
# [cell_1, cell_2]


for row in rows:
    data = {}
    for title, cell in zip(headers, row):
        data[title] = cell.value
    
    # print(data)
    all_rows.append(data)

print(all_rows)


