from tokenizer import process

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/81.0.4044.122 Safari/537.36",
}

urls = ['https://vk.com/wall-29534144_15621640', 'https://vk.com/wall-29534144_15621274',
        'https://vk.com/wall-29534144_15620797', 'https://vk.com/wall-29534144_15620545',
        'https://vk.com/wall-29534144_15619450', 'https://vk.com/wall-29534144_15618993',
        'https://vk.com/wall-29534144_15618210', 'https://vk.com/wall-29534144_15617506',
        'https://vk.com/wall-29534144_15616183', 'https://vk.com/wall-29534144_15615722'
        ]


if __name__ == '__main__':
    data = {}
    labels = ['neutral', 'bad', 'good']
    result = map(process, labels)
    for i in result:
        data.update(i)
    print(data)