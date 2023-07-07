#编写一个函数 compare (file1,file2)
#比较两个文本文件内容是否相同
#如果内容相同返回 True 
#否则返回 False 
#在主程序中输入两个要比较的两文件名，然后调用以上函数，
#文件内容相同则输出" No difference !"
#否则，输出从第几个字符开始不相同。

# def compare(file1,file2):
#     f1 = open(file1,'r')
#     f2 = open(file2,'r')
#     count = 0
#     while True:
#         count += 1
#         line1 = f1.readline()
#         line2 = f2.readline()
#         if line1 != line2:
#             print("第%d行第%d个字符不同" %(count,len(line1)))
#         if not line1:
#             print("No difference !")
#             break
#     f1.close()
#     f2.close()

# file1 = input("请输入第一个文件名：")
# file2 = input("请输入第二个文件名：")
# compare(file1,file2)

def compare(file1, file2):
    # 打开两个文件
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        # 逐行读取文件内容
        for line1, line2 in zip(f1, f2):
            # 如果两个文件内容不同，输出不同的位置并返回 False
            if line1 != line2:
                diff_index = 0
                for i in range(min(len(line1), len(line2))):
                    if line1[i] != line2[i]:
                        diff_index = i
                        break
                print("从第{}个字符开始不相同。".format(diff_index))
                return False
        # 如果两个文件内容相同，返回 True
        return True

file1 = input("请输入第一个文件名：")
file2 = input("请输入第二个文件名：")
if compare(file1, file2):
    print("No difference !")
    