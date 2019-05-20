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
    long_words = []
    for word in all_words:
        if len(word) > 6:
            long_words.append(word.lower())
    count = Counter(long_words)
    print('топ 10 самых часто встречающихся слов длиннее 6 символов:', count.most_common(10))



