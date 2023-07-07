from string import punctuation

def getText(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def getTopWords(text, topn=5):
    words = text.lower().split()
    for i in range(len(words)):
        words[i] = words[i].strip(punctuation)
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    top_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:topn]
    return top_words

filepath = 'hamlet.txt'
text = getText(filepath)
top_words = getTopWords(text)
print('请输入词频最高的 top - N :')
for word, count in top_words:
    print('{} occurs {} times.'.format(word, count))
