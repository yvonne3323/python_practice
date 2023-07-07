def getText(filepath):
    f = open(filepath, 'r', encoding='utf-8')
    text = f.read()
    f.close()
    return text

import re 
from string import punctuation

def wordFreq(filepath,text,topn):
    words = re.findall(r'\b\w+\b',text.strip()) # 只匹配由多个字母组成的单词
    counts_lower = {}
    counts_upper = {}
    for word in words:
        if word not in punctuation:
            if word.islower():
                counts_lower[word] = counts_lower.get(word,0) + 1
            elif word.isupper():
                counts_upper[word] = counts_upper.get(word,0) + 1
    items_lower = list(counts_lower.items())
    items_upper = list(counts_upper.items())
    items_lower.sort(key=lambda x:x[1],reverse=True)
    items_upper.sort(key=lambda x:x[1],reverse=True)
    f = open(filepath[:-4]+'_词频4.txt', 'w')
    f.write('小写单词:\n')
    for i in range(min(topn,len(items_lower))):
        word,count = items_lower[i]
        f.write('{}\t{}\n'.format(word,count)) # 修改输出格式
    f.write('\n大写单词:\n')
    for i in range(min(topn,len(items_upper))):
        word,count = items_upper[i]
        f.write('{}\t{}\n'.format(word,count)) # 修改输出格式
    f.close()

text = getText('hamlet.txt')
wordFreq('hamlet.txt',text,5)
