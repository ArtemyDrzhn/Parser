import requests
from bs4 import BeautifulSoup


def pars(url, headers):
    titles = []
    full = []

    r = requests.get(url, headers=headers)  # отправка http запроса
    soup = BeautifulSoup(r.text, 'html.parser')  # создание html парсера
    comments = soup.find_all('div', {'class': 'wall_reply_text'})

    comments_clean = []
    for comment in comments:  # очистка от лишней html разметки
        comments_clean.append(comment.find_all(text=True))

    for i in comments_clean:
        full.append([' '.join(i)])  # делаем из всего список списков для удобства экспорта

    titles.append(url.replace('https://vk.com/', ''))

    return full, titles
