#编写函数，实现读取文件的功能，返回文件的内容(函数只有在调用之后才会执行)
def getText(filepath):
    f = open(filepath, 'r', encoding='utf-8')
    text = f.read()
    f.close()
    return text

#编写函数对读取的text文件进行分词，并统计词频
import jieba
def wordFreq(filepath,text,topn):
    words = jieba.lcut(text.strip())
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        counts[word] = counts.get(word,0) + 1
    items = list(counts.items())
    items.sort(key=lambda x:x[1],reverse=True)
    f = open(filepath[:-4]+'_词频.txt', 'w')
    for i in range(topn):
        word,count = items[i]
        f.write('{}\t{}\n'.format(word,count))
    f.close()

#运行
text = getText('三国演义.txt')
wordFreq('三国演义.txt',text,10)



#制作词云
import wordcloud
f = open('stopwords.txt', 'r', encoding='utf-8')
stopwords = f.read()
wcloud = wordcloud.WordCloud(font_path='msyh.ttc',stopwords=stopwords,background_color='white',width=1000,height=800,max_words=100)
wcloud.generate(getText('三国演义.txt'))
wcloud.to_file('三国演义词云.png')
f.close()
