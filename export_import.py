def export():
    with open('data//dataset.txt', 'r', encoding='utf-8') as file_dataset:
        comments = file_dataset.readlines()

    data_set = []
    for comment in comments:
        lst = []
        comment = comment.replace('\n', '')

        if comment.find('__label__NORMAL') == 0:
            comment = comment.replace('__label__NORMAL', '')
            lst.append(comment)
            lst.append(0)
        elif comment.find('__label__INSULT') == 0:
            comment = comment.replace('__label__INSULT', '')
            comment = comment.replace(',__label__THREAT', '')
            comment = comment.replace(',__label__OBSCENITY', '')
            comment = comment.replace(',__label__OBSCENITY,__label__THREAT', '')
            lst.append(comment)
            lst.append(1)
        elif comment.find('__label__THREAT') == 0:
            comment = comment.replace('__label__THREAT', '')
            lst.append(comment)
            lst.append(1)
        elif comment.find('__label__OBSCENITY') == 0:
            comment = comment.replace('__label__OBSCENITY', '')
            comment = comment.replace(',__label__THREAT', '')
            lst.append(comment)
            lst.append(1)
        data_set.append(lst)

    # with open('data//labeled.txt', 'r', encoding='utf-8') as file_labeled:
    #     comments = file_labeled.readlines()
    #     del comments[0]
    #
    #     # Чистка от лишнего
    #     lst = []
    #     for comment in comments:
    #         comment = comment.replace('"', '')
    #         comment = comment.replace('",', '')
    #         comment = comment.replace('.0', '')
    #         comment = comment.replace('\n', '')
    #         lst.append(comment)
    #
    #     lst_variable = []
    #     for comment in lst:
    #         if lst.index(comment) % 2 == 0:
    #             # print(comment)
    #             lst_variable.append(comment)
    #         else:
    #             comment = comment.replace(',', '')
    #             comment = int(comment)
    #             lst_variable.append(comment)
    #         data_set.append(lst_variable)
    return data_set


# Нужно разбить на три класса - плохой, средний, положительный
# 0-положительно 1 - отрицательно
def corpus_write(data_set):
    """
    Создание корпуса данных
    :param data_set: список списков (коммент, лейбл)
    :return:
    """
    lst_normal = []
    lst_bad = []

    for i in data_set:
        if i[1] == 0:
            lst_normal.append(i[0] + '\n')
        else:
            lst_bad.append(i[0] + '\n')

    for n in range(1101):
        normal = open('corpus/normal//' + str(n) + '.txt', 'w', encoding='utf-8')
        normal.writelines(lst_normal[:185])
        del lst_normal[:185]

    for b in range(367):
        bad = open('corpus/bad//' + str(b) + '.txt', 'w', encoding='utf-8')
        bad.writelines(lst_bad[:55])
        del lst_bad[:55]
