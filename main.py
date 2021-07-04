import requests
from bs4 import BeautifulSoup

from export import export

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
}

url = 'https://vk.com/wall-59443849_5825'


r = requests.get(url, headers=headers)          # отправка http запроса
soup = BeautifulSoup(r.text, 'html.parser')     # создание html парсера
comments = soup.find_all('div', {'class': 'wall_reply_text'})

comments_clean = []
for comment in comments:    # очистка от лишней html разметки
    comments_clean.append(comment.find_all(text=True))

full = []
for i in comments_clean:
    full.append([' '.join(i)])


export(full)
