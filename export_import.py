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

    return data_set


# Нужно разбить на три класса - плохой, средний, положительный
# 0-положительно 1 - отрицательно
def corpus_write(data_set, path0, path1):
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
        normal = open(path0 + str(n) + '.txt', 'w', encoding='utf-8')
        normal.writelines(lst_normal[:185])
        del lst_normal[:185]

    for b in range(367):
        bad = open(path1 + str(b) + '.txt', 'w', encoding='utf-8')
        bad.writelines(lst_bad[:55])
        del lst_bad[:55]


def export_test():
    with open('data//labeled.csv', 'r', encoding='utf-8') as file_dataset:
        comments = file_dataset.readlines()

    data_set = []
    for c in comments:
        c = c.replace('"', '')
        c = c.replace('"', '')
        c = c.replace('.0', '')
        c = c.replace('\n', '')
        if c == ',1' or c == ',0':
            c = c[1]
        data_set.append(c)

    need = []
    for data in range(0, len(data_set), 2):
        lst = [data_set[data], int(data_set[data + 1])]
        need.append(lst)
    return need
