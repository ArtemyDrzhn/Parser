from nltk.corpus import PlaintextCorpusReader
from nltk.stem.snowball import SnowballStemmer
from nltk import RegexpTokenizer
from nltk import bigrams
from nltk import FreqDist


def lower_pos_tag(words):
    lower_words = []
    for i in words:
        lower_words.append(i.lower())
    from nltk import pos_tag
    pos_words = pos_tag(lower_words, lang='rus')
    return pos_words


def clean(words):
    stemmer = SnowballStemmer("russian")
    cleaned_words = []
    for i in words:
        if i[1] in ['S', 'A', 'V', 'ADV']:
            cleaned_words.append(stemmer.stem(i[0]))
    return cleaned_words


corpus_root = 'corpus_root'  # Путь к корпусу


def process(label):
    # Wordmatrix - список документов с лексемами
    # All words - список всех слов
    data = {'Word_matrix': [], 'All_words': []}
    # Промежуточный список для удаления гапаксов
    templist_allwords = []
    # Определение пути к папке с определенным лейблом
    corpus = PlaintextCorpusReader(corpus_root + '\\' + label, '.*', encoding='utf-8')
    # Получение списка имен файлов в корпусе
    names = corpus.fileids()
    # Создание токенайзера

    tokenizer = RegexpTokenizer(r'\w+|[^\w\s]+')
    for i in range(len(names)):  # Обработка корпуса
        bag_words = tokenizer.tokenize(corpus.raw(names[i]))
        lower_words = lower_pos_tag(bag_words)
        cleaned_words = clean(lower_words)
        final_words = list(bigrams(cleaned_words)) + cleaned_words
        data['Word_matrix'].append(final_words)
        templist_allwords.extend(cleaned_words)
    # Определение гапаксов

    temp_list_freq = FreqDist(templist_allwords)
    hapaxes = temp_list_freq.hapaxes()
    # Фильтрация от гапаксов
    for word in templist_allwords:
        if word not in hapaxes:
            data['All_words'].append(word)
    return {label: data}
