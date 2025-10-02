helight=float(input("请输入身高/m:"))
weight=float(input("请输入体重/kg:"))
BMI=weight/(helight*helight)
print("BMI的输出值：",BMI)
if BMI<18.5:
    print("过轻")
elif BMI<24.9:
    print("正常")
elif BMI<27.9:
    print("过重")
elif BMI<30:
    print("肥胖")
elif BMI<35:
    print(" severely obese")
elif BMI<40:
    print(" morbidly obese")
else:
    print(" severely morbidly obese")