#有一个文本文件 student.txt ，其中包含了学生的学号，格式如下
#154772 154778 154784 154793 156273...
#假设现在老师要随机点几位学生回答问题
#编写一个函数
#每次调用从中抽取一位学生
#在主程序中对其连续调用，并可以控制是否需要继续抽取。
#假设每次抽取的学生可以重复。

import random

def random_student():
    with open('student.txt', 'r') as f:
        student_list = f.read().split()
    return random.choice(student_list)

# 主程序中连续调用该函数
while True:
    student = random_student()
    print("抽到的学生是：", student)
    if input("是否继续抽取？(y/n)") == "n":
        break

