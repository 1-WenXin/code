# num = int(input("请输入一个数字："))
# if num%3==2 and num%5==3 and num%7==2:
#     print("符合三三数之剩二，五五数之剩三，七七数之剩二",num)
# else:
#     print("不符合")

# none = True
# num = 0
# while none:
#     num +=1
#     if num%3==2 and num%5==3 and num%7==2:
#         print("符合三三数之剩二，五五数之剩三，七七数之剩二",num)
#         none = False
#     else:
#         print("不符合")



# num = 0
# while True: #判断为真条件
#     num +=1 #num自加一
#     if num%3==2 and num%5==3 and num%7==2: #判断田间是否符合
#         print("符合三三数之剩二，五五数之剩三，七七数之剩二",num)
#         break #跳出循环
#     else:
#         print("不符合")



for i in range(1,1001):
    if i%3==2 and i%5==3 and i%7==2:
        print("符合三三数之剩二，五五数之剩三，七七数之剩二",i)


# none = False
# #由于 none 初始值就是 False，while 循环的条件 while none 一开始就为假，所以循环体根本不会执行，程序不会做任何查找工作。
# num = 0
# while none:
#     num +=1
#     if num%3==2 and num%5==3 and num%7==2:
#         print("符合三三数之剩二，五五数之剩三，七七数之剩二",num)
#         none = False
#     else:
#         print("不符合")
