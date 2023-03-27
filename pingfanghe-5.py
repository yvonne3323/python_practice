#求前n个数字的平方和
N = int(input("请输入一个数:\n"))
sum = 0
for i in range(1,N+1):
    sum = sum + i*i
print(sum)


#求前n个数字的平方和(递归)
def sum_of_squares(n):
    if n == 1:
        return 1
    else:
        return n*n + sum_of_squares(n-1)
print(sum_of_squares(5))
    