#1+2+...+10的和
sum = 0
for i in range(1,11):
    sum += i
print(sum)

#1+3+5+...+99的和
sum = 0
for i in range(1,100,2):
    sum += i
print(sum)

#优化
sum = 0
for i in range(1,100):
    if i % 2 == 1:
        sum += i
print(sum)
