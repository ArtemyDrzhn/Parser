import openpyxl


def export(comment):
    wb = openpyxl.Workbook()
    wb.create_sheet(title='Первый лист', index=0)

    sheet = wb['Первый лист']
    for i in comment:
        sheet.append(i)

    wb.save('ex.xlsx')