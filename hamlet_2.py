
def getText(filepath):#英文文本文件hamlet.txt的读取
    f = open(filepath, 'r', encoding='utf-8')
    text = f.read()
    f.close()
    return text


import re 
def wordFreq(filepath,text,topn):#英文文本文件的单词抽取
    words = re.findall(r'[a-zA-Z]+',text.strip())
    words = [word.lower() for word in words] # 将单词转为小写字母
    counts = {}
    for word in words:
        counts[word] = counts.get(word,0) + 1
    items = list(counts.items())
    items.sort(key=lambda x:x[1],reverse=True)
    f = open(filepath[:-4]+'_词频.txt', 'w')
    for i in range(topn):
        word,count = items[i]
        f.write('{}\t{}\n'.format(word,count))
    f.close()

#英文文本文件中出现频次最高的前5个单词的抽取
#并降序输出
text = getText('hamlet.txt')
wordFreq('hamlet.txt',text,5)