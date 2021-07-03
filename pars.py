from nltk.stem.snowball import SnowballStemmer
from nltk import pos_tag
import requests
from bs4 import BeautifulSoup


def pars_html(url, headers):
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

    return full


def lower_pos_tag(words):
    """
    :param words: список слов
    :return: все лексемы, преобразованные к нижнему регистру
    """
    lower_words = []
    for i in words:
        lower_words.append(i.lower())
    pos_words = pos_tag(lower_words, lang='rus')
    return pos_words


def clean(words):
    """
    :param words: список слов
    :return: существительные, прилагательные, глаголы и наречия
    """
    stemmer = SnowballStemmer("russian")
    cleaned_words = []
    for i in words:
        if i[1] in ['S', 'A', 'V', 'ADV']:
            cleaned_words.append(stemmer.stem(i[0]))
    return cleaned_words
