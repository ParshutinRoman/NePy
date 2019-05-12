import json
from collections import Counter
from pprint import pprint

file = ('newsafr.json')

with open(file, 'rb') as f:
    data = f.read()
    data = json.loads(data)
    text = data['rss']['channel']['items']
    all_words = []
    for news in text:
        words = news['description']
        words = words.split(' ')
        all_words += words
    words_short = []
    for word in all_words:
        if len(word) > 6:
            words_short.append(word)
    count = Counter(words_short)
    print('топ 10 самых часто встречающихся слов длиннее 6 символов:', count.most_common(10))



