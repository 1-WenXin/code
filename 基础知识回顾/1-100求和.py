num = 0 #初始化num值，并且num不能从1来初始化，最后的结果会多一个值
for i in range(101):#in 左边必须是迭代变量（i），右边是可迭代对象（例如列表、字符串、range()）
    num += i #累加
print("打印1-100求和",num)

# num = 0
# for 1 in 101: #in 左边必须是迭代变量（i），右边是可迭代对象（例如列表、字符串、range()）
#     num += 1 #这里只实现了num自加1，没有实现num的累加
# print("打印1-100求和",num)

# num = 0
# for i in range(1, 101):
#     num += i
#     print(f"第 {i} 次循环: num = {num}")   # f-string 打印当前状态
