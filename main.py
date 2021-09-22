from itertools import starmap

from nltk.probability import FreqDist
from collections import OrderedDict
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import GridSearchCV
from sklearn.utils import shuffle
import numpy as np
from scipy.sparse import csr_matrix

from export_import import export_test, corpus_write
from tokenizer import process


def vectorize(corpus_root):
    data = {}
    labels = ['bad', 'normal']
    result = starmap(process, [(labels[0], corpus_root), (labels[1], corpus_root)])
    for i in result:
        data.update(i)

    # Создание помеченный данных со структурой:
    # [([список слов отзыва], метка_класса)]
    labels = ['bad', 'normal']
    labeled_data = []
    for label in labels:
        for document in data[label]['Word_matrix']:
            labeled_data.append((document, label))

    # Создание вокабуляра с уникальными лексемами
    all_words = []
    for label in labels:
        frequency = FreqDist(data[label]['All_words'])
        common_words = frequency.most_common(10000)
        words = [i[0] for i in common_words]
        all_words.extend(words)
    # Извлечение уникальных лексем
    unique_words = list(OrderedDict.fromkeys(all_words))

    # Частотное кодирование для классификаторов scikit-learn
    # Разреженная матрица для признаков
    matrix_vec = csr_matrix((len(labeled_data), len(unique_words)), dtype=np.int8).toarray()
    # Массив для меток классов
    target = np.zeros(len(labeled_data), 'str')
    for index_doc, document in enumerate(labeled_data):
        for index_word, word in enumerate(unique_words):
            # Подсчет кол-ва вхождения слова в отзыв
            matrix_vec[index_doc, index_word] = document[0].count(word)
        target[index_doc] = document[1]
    # Перемешиваем датасет
    X, Y = shuffle(matrix_vec, target)
    return X, Y


if __name__ == '__main__':
    corpus_root = 'corpus'
    X, Y = vectorize(corpus_root)
    corpus_root = 'corpus_test'
    X_test, Y_test = vectorize(corpus_root)

    parameter = [1, 0, 0.1, 0.01, 0.001, 0.0001]
    param_grid = {'alpha': parameter}
    grid_search = GridSearchCV(MultinomialNB(), param_grid, cv=5)
    grid_search.fit(X, Y)
    Alpha, best_score = grid_search.best_params_, grid_search.best_score_
