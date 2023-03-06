#数字金字塔

#1.纯金字塔(已提供行数)
for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end="")
    for k in range(1,2*i):
        print("*",end="")
    print()
#并不是要把右边的空格也考虑到程序里面,*号结束就换行

#2.纯金字塔(未提供行数)
n=int(input("请输入行数:"))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,2*i):
        print("*",end="")
    print()

#3.数字金字塔(未提供行数)
#  1
# 121
#12321
m=int(input("请输入行数:"))
for i in range(1,m+1):
    for j in range(1,m-i+1):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end="")
    for l in range(i-1,0,-1):
        print(l,end="")
    print()
    