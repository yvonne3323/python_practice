items_menu = ['banana', 9.8, 'orange', 6.5, 'apple', 12.6, 'peach', 10.5, 'watermelon', 6.2, 'cherry tomato',5.2]
#整个字符串宽度为25
print("="*25)
#rjust右对齐，左边空格填充 自身占一个，所以是24
print("Fruits","Price".rjust(24-len("Fruits")))
print("-"*25)
i = 0
#循环 步长为2 开头均为水果
for i in range(0,len(items_menu),2):
    print(f"{items_menu[i].title()}",f"{items_menu[i+1]}".rjust(24-len(f"{items_menu[i]}")))
print("="*25)#结束