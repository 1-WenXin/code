
print("手机活动正在进行中")
# print("\n手机活动正在进行中")   #\n换行符号
week=input("请输入今天是星期几(星期一)：")
time=float(input("请输入时间中时间段（0~23）："))
# if (week == "星期二" and (10 <= time < 11)) or (week == "星期三" and (time >= 10 and time<=11)):
#     print("手机活动正在进行中")
# else:
#     print("手机活动未开始")

if week == "星期二":
    if (time > 10 and time <= 11):
        print("手机活动正在进行中")
    else:
        print("手机活动未开始")
elif week == "星期三":
    if time <= 15:
        print("手机活动正在进行中")
    else:
        print("手机活动未开始")
else:
    print("手机活动未开始")