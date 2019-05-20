
import os
import xml.etree.ElementTree as ET
from collections import Counter

file_name = "newsafr.xml"
parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse(file_name, parser=parser)
print(tree)
root = tree.getroot()
news = tree.findall("channel/item/description")
all_words = []
for new in news:
    words = new.text
    words = words.lower().split(' ')
    all_words += words
long_words = []
for word in all_words:
    if len(word) > 6:
        long_words.append(word)
count = Counter(long_words)

print('топ 10 самых часто встречающихся слов длиннее 6 символов:', count.most_common(10))