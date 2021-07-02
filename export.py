import openpyxl


def export(comment, titles):
    wb = openpyxl.Workbook()
    index = 0  # индекс для книги ёксиля
    for title in titles:
        wb.create_sheet(title=title, index=index)

        sheet = wb[title]
        for i in comment:
            sheet.append(i)
        index += 1
    wb.save('ex.xlsx')