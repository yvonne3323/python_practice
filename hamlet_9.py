from string import punctuation

def getText(filepath):#读取文件
    openfile = open(filepath, 'r')
    text = openfile.read()
    openfile.close()
    return text

def getword(text, topn=5):#获取词频最高的前5个单词
    word = text.lower().split()#将单词转为小写字母,并分割
    for i in range(len(word)):
        word[i] = word[i].strip(punctuation)#去除标点符号
    word_count = {}#设置字典，统计词频
    for word in word:
        word_count[word] = word_count.get(word, 0) + 1
    top_word = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:topn]
    return top_word

filepath = 'hamlet.txt'
text = getText(filepath)
top_word = getword(text)
print('请输入词频最高的 top - N :')
for word, count in top_word:
    print('{} occurs {} times.'.format(word, count))
