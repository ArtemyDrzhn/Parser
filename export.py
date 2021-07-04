import openpyxl


def export(comment, name):
    wb = openpyxl.Workbook()
    wb.create_sheet(title='Первый лист', index=0)

    sheet = wb['Первый лист']
    sheet.append([name])
    for i in comment:
        sheet.append(i)
    name_xlsx = name.replace('https://vk.com/', '') + '.xlsx'
    wb.save(name_xlsx)
