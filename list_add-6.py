#计算列表数字的和
#input: [1,2,3,4] output: 10
def sum_list(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum
print(sum_list([1,2,3,4]))

#简单粗暴的是直接把列表命名，开始以为要自己输入列表
list1 = [1,2,3,4]
list2 = [17,5,3,5]
print(sum(list1))
print(sum(list2))
print(f"sum of {list1}",sum_list(list1))
