python=float(input("请输入你的python成绩:"))
english=float(input("请输入你的英语成绩:"))
c=float(input("请输入你的c语言成绩:"))
cross=float(abs(python-english))
print("python与english成绩差值：",cross)
evrage=(python+english+c)/3
print("平均成绩：",evrage)
