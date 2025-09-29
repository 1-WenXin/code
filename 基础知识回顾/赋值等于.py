# x=10#赋值，这里的x是变量，x是一个
# print(x)
# num=input("请你输入一个数字：")#将输入的数字赋值给num变量
# num=int(num)
# print(num+x)


# helight=input("请输入身高：")
# if helight.isdigit():
#     num=int(helight)
#     print("打印数字：",num)
# else:
#     print("输入有误。")

helight=input('请输入你的身高：')
try:
    num=float(helight)
    print("打印数字：",num)
except:
    print("输入有误")