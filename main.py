import requests
from bs4 import BeautifulSoup
import openpyxl

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
}

url = 'https://vk.com/wall-29534144_15599462'


r = requests.get(url, headers=headers)          # отправка http запроса
soup = BeautifulSoup(r.text, 'html.parser')     # создание html парсера
comments = soup.find_all('div', {'class': 'wall_reply_text'})

comments_clean = []
for comment in comments:    # очистка от лишней html разметки
    comments_clean.append(comment.find_all(text=True))

full = []
for i in comments_clean:
    full.append([' '.join(i)])


# TODO запись в эксель вотдельный файл
wb = openpyxl.Workbook()
wb.create_sheet(title='Первый лист', index=0)

sheet = wb['Первый лист']
for i in full:
    sheet.append(i)

wb.save('.xlsx')
print(full)
