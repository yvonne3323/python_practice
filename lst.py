lst=[['李玉', '男', '26'], [],[],[]]
'''用format加lst一个小明，男，26，加到lst列表中'''
lst1=["[['李玉', '男', '26'], [{}],[{}]]".format('小明','男','26')]
name=input("请输入你要删除信息的员工姓名：")
for i in lst1:
    if i [0]==name:
        lst1.remove(i)
        print("删除后的列表为：{}".format(lst1))
        break
    else:
        print("列表中不存在该员工姓名！")
    