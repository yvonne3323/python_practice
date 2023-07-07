f = open('f.txt', 'w')
f.writelines(['Python programming.'])
f.close()

f = open('f.txt', 'rb')
f.seek(10, 1)#指针向后移动10个字节
print(f.tell())#打印指针位置
f.close()
