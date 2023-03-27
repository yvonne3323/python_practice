#求数字的阶乘
num = int(input("请输入一个数"))
sum = 1
while(num > 1):
    sum = sum * num
    num = num -1
print(f"sum = {sum}")

#二版
#求数字的阶乘
num = int(input("请输入一个数"))
sum = 1
for i in range(1,num+1):
    sum = sum * i
print("sum = %d" % sum)
#三版(函数)
def factorial(num):
    sum = 1
    for i in range(1,num+1):
        sum = sum * i
    return sum
print("5的阶乘为:",factorial(5))

#递归
def factorial2(num):
    if num == 1:
        return 1
    else:
        return num * factorial2(num-1)
print("5的阶乘为:",factorial2(5))
