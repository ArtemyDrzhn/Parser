import openpyxl


def export(wb, comment, title, index):

    wb.create_sheet(title=str(index), index=index)

    sheet = wb[str(index)]
    for i in comment:
        sheet.append(i)
    wb.save('data.xlsx')