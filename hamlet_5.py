
def getText(filepath):
    f = open(filepath, 'r', encoding='utf-8')
    text = f.read()
    f.close()
    return text

import re 
from string import punctuation

def wordFreq(filepath,text,topn):
    words = re.findall(r'[a-zA-Z]+',text.strip())
    words = [word.lower() for word in words if word not in punctuation] # 去除标点符号
    counts = {}
    for word in words:
        counts[word] = counts.get(word,0) + 1
    items = list(counts.items())
    items.sort(key=lambda x:x[1],reverse=True)
    f = open(filepath[:-4]+'_词频1.txt', 'w')
    for i in range(topn):
        word,count = items[i]
        f.write('{}\t{}\n'.format(word,count)) # 修改输出格式
    f.close()

text = getText('hamlet.txt')
wordFreq('hamlet.txt',text,5)
