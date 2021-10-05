from cmath import log

from nltk import FreqDist

from tokenizer import lower_pos_tag, clean, get_features


def train(data, labels):
    # Создание вокабуляра с уникальными лексемами
    all_words_bad, all_words_normal = {}, {}
    freq = {}
    for label in labels:
        frequency = FreqDist(data[label]['All_words'])
        if label == 'bad':
            for word, count in frequency.items():
                all_words_bad[word] = count / len(frequency)
            freq['bad'] = all_words_bad
        else:
            for word, count in frequency.items():
                all_words_normal[word] = count / len(frequency)
            freq['normal'] = all_words_normal
    freq_classes = 0.5

    return freq_classes, freq  # P(C) , P(O|C)


def classify(classifier, feats):
    freq_classes, freq = classifier
    print(feats)
    feats = get_features(feats)
    sum_bad, sum_normal = [], []

    for label, words in freq.items():
        for word, fr in words.items():
            for feat in feats:
                if word == feat and label == 'bad':
                    sum_bad.append(fr)
                elif word == feat and label == 'normal':
                    sum_normal.append(fr)

    if sum(sum_bad) > sum(sum_normal):
        print('bad')
    else:
        print('normal')
