from export_import import export, corpus_write
from tokenizer import process
from train import train, classify

if __name__ == '__main__':
    # data_set = export()
    # corpus_write(data_set, 'corpus//normal//', 'corpus//bad//')

    data = {}
    labels = ['bad', 'normal']
    result = map(process, labels)
    for i in result:
        data.update(i)

    model = train(data, labels)
    print()
    classify(model, 'Эменем, соси бибу')
