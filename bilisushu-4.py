#求区间里的素数(包括末尾数字)
print("请输入起始数字和结束数字：") #需要换行
start_num =int (input())
end_num = int(input())
for i in range(start_num,end_num+1):
    for j in range(2,i): #注意：/ float
        if i % j == 0:
            break
    else:
        print(i) #else位置很重要

#在python中 else不仅与if 相联用 还可与while for 相连用
#else 代表循环正常结束

#求区间里的素数(函数版)
def is_prime(num):
    for j in range(2,num):
        if num % j == 0:
            return False
    else:
        return True

def print_prime(start_num,end_num):
    for i in range(start_num,end_num+1):
        if is_prime(i):
            print(i)

print("请输入起始数字和结束数字：") #需要换行
start_num =int (input())
end_num = int(input())
print_prime(start_num,end_num)


#求区间里的素数(优化版)
def is_prime2(num):
    for j in range(2,int(num**0.5)+1):#主要优化点
        if num % j == 0:
            return False
    else:
        return True
    
print("请输入起始数字和结束数字：") #需要换行
start_num =int (input())
end_num = int(input())
for i in range(start_num,end_num+1):
    if is_prime(i):
        print(i)

