
import pyperclip
text = pyperclip.paste() #从剪贴板中获取文本
lines = text.split('\r\n') #将文本分割成行
for i in enumerate(lines): #遍历每一行
    lines[i[0]] = str(i[0]+1) + '.\t' + i[1] #在每一行前面加上序号
text = 'Good Student List:\r\n' + '\r\n'.join(lines) #将列表重新组合成文本
pyperclip.copy(text) #将文本复制到剪贴板
