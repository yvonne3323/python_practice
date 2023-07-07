
def getText(filepath):
    f = open(filepath, 'r', encoding='utf-8')
    text = f.read()
    f.close()
    return text

import re 
def wordFreq(filepath,text,topn):
    words = re.findall(r'[a-zA-Z]+',text.strip())
    lower_words = [word.lower() for word in words] # 将单词转为小写字母
    counts = {}
    for i in range(len(words)):
        word = words[i]
        lower_word = lower_words[i]
        if word != lower_word: # 如果单词中含有大写字母
            counts[word] = counts.get(word,0) + 1 # 统计大写字母出现的频次
        counts[lower_word] = counts.get(lower_word,0) + 1 # 统计小写字母出现的频次
    items = list(counts.items())
    items.sort(key=lambda x:x[1],reverse=True)
    f = open(filepath[:-4]+'_词频.txt', 'w')
    for i in range(topn):
        word,count = items[i]
        f.write('{}\t{}\n'.format(word,count)) # 修改输出格式
    f.close()

text = getText('hamlet.txt')
wordFreq('hamlet.txt',text,5)
