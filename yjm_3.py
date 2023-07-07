#某心理测试题全部由单选题组成
#每个题目有3个选项，不同选项得分不同
#（但每题分数都是在10分﹣99分之间）
#答案和分数保存在一个文件 answer.txt 中，格式为：
#1A10B20C30
#2A20B10C30
#3A30B10C20
#其中前面的数字为题号。从键盘输入某位考生答案，例如： ABC
#编程计算并输出该考生的成绩。

# 1. 读取答案
# 2. 读取考生答案
# 3. 比较答案，计算分数
# 4. 输出分数

# 1. 读取答案
# 1.1 打开文件
# 1.2 读取文件内容
# 1.3 关闭文件
# 1.4 将答案保存到字典中

# 2. 读取考生答案
# 2.1 从键盘输入考生答案
# 2.2 将考生答案保存到列表中

# 3. 比较答案，计算分数
# 3.1 遍历考生答案列表
# 3.2 从字典中取出对应的答案
# 3.3 比较考生答案和标准答案
# 3.4 计算分数

# 4. 输出分数

# # 1. 读取答案
# # 1.1 打开文件
# f = open('answer.txt', 'r')
# # 1.2 读取文件内容
# answer_lines = f.readlines()
# # 1.3 关闭文件
# f.close()
# # 1.4 将答案保存到字典中
# answer_dict = {}
# for line in answer_lines:
#     items = line.split()
#     answer_dict[items[0]] = items[1:]

# # 2. 读取考生答案
# # 2.1 从键盘输入考生答案
# student_answer = input("请输入考生答案：")
# # 2.2 将考生答案保存到列表中
# student_answer_list = []
# for i in student_answer:
#     student_answer_list.append(i)

# # 3. 比较答案，计算分数
# # 3.1 遍历考生答案列表
# score = 0
# for i, ans in enumerate(student_answer_list):
#     # 3.2 从字典中取出对应的答案
#     # 3.3 比较考生答案和标准答案//有问题

#     # if ans == answer_dict[str(i+1)][0]:
#     #     score += int(answer_dict[str(i+1)][1])
#     # elif ans == answer_dict[str(i+1)][2]:
#     #     score += int(answer_dict[str(i+1)][3])
#     # else:
#     #     score += int(answer_dict[str(i+1)][5])
    
# # 4. 输出分数
# print("考生得分为：", score)

# #

# import re

# def calculate_score(answer_file, student_answer):
#     with open(answer_file, 'r') as f:
#         answer_lines = f.readlines()
#     answer_dict = {}
#     for line in answer_lines:
#         items = line.split()
#         answer_dict[items[0]] = items[1:]
    
#     # 使用正则表达式将考生答案拆分为单独的答案项
#     student_answer_list = re.findall(r'\w', student_answer)
    
#     score = 0
#     for i, ans in enumerate(student_answer_list):
#         if ans == answer_dict[str(i+1)][0]:
#             score += int(answer_dict[str(i+1)][1])
#         elif ans == answer_dict[str(i+1)][2]:
#             score += int(answer_dict[str(i+1)][3])
#         else:
#             score += int(answer_dict[str(i+1)][5])
    
#     return score

# # 主程序中调用 calculate_score 函数
# answer_file = input("请输入标准答案文件名：")
# student_answer = input("请输入考生答案：")
# total_score = calculate_score(answer_file, student_answer)
# print("考生得分为：", total_score)

# import re

# def calculate_score(answer_file, student_answer):
#     with open(answer_file, 'r') as f:
#         answer_lines = f.readlines()
#     answer_dict = {}
#     for line in answer_lines:
#         items = line.split()
#         answer_dict[int(items[0])] = items[1:]
    
#     # 使用正则表达式将考生答案拆分为单独的答案项
#     student_answer_list = re.findall(r'\w', student_answer)
    
#     score = 0
#     for i, ans in enumerate(student_answer_list):
#         if ans == answer_dict[i+1][0]:
#             score += int(answer_dict[i+1][1])
#         elif ans == answer_dict[i+1][2]:
#             score += int(answer_dict[i+1][3])
#         else:
#             score += int(answer_dict[i+1][5])
    
#     return score

# # 主程序中调用 calculate_score 函数
# answer_file = input("请输入标准答案文件名：")
# student_answer = input("请输入考生答案：")
# total_score = calculate_score(answer_file, student_answer)
# print("考生得分为：", total_score)

import re

def calculate_score(answer_file, student_answer):
    with open(answer_file, 'r') as f:
        answer_lines = f.readlines()
    answer_dict = {}
    for line in answer_lines:
        items = line.split()
        answer_dict[int(items[0])] = [items[1], int(items[2]), int(items[3]), int(items[4]), int(items[5])]
    
    # 使用正则表达式将考生答案拆分为单独的答案项
    student_answer_list = re.findall(r'\w', student_answer)
    
    score = 0
    for i, ans in enumerate(student_answer_list):
        if ans == answer_dict[i+1][0]:
            score += answer_dict[i+1][1]
        elif ans == answer_dict[i+1][2]:
            score += answer_dict[i+1][3]
        else:
            score += answer_dict[i+1][5]
    
    return score

# 主程序中调用 calculate_score 函数
answer_file = input("请输入标准答案文件名：")
student_answer = input("请输入考生答案：")
total_score = calculate_score(answer_file, student_answer)
print("考生得分为：", total_score)

