#求圆的面积
import math
a = float(input("请输入圆的半径：(单位:cm)"))
area = math.pi * a * a
print(f"该圆的面积为{area}cm2")

#函数版本
def area_of_cycle(a):
    return(math.pi * a * a)
r=float(input("请输入圆的半径:\n"))

print(f"圆的面积为{area_of_cycle(r)}")
#新知识点：
#round(x,n)
#n -- 数值表达式，表示从小数点位数。
print(round(80.2356, 2))  # 80.24
print(round(100.000056, 3))  # 100.0
#除非对精确度没什么要求，否则尽量避开用round()函数
#round的结果跟python版本有关
print(round(0.5)) # 0
print(round(2.675,2)) # 2.67
print(round(123.45)) # 123
print(round(123.45,0)) #123.0
print(round(123.45,-1)) #120.0
#https://www.runoob.com/w3cnote/python-round-func-note.html
