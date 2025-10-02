file=open(r"D:\python_test\basic\file",'a+')
wen=input("时间的差错，不应该归功于是谁")
file.write(wen + "\n")
file.close()
file=open(r"D:\python_test\basic\file",'a+')
while True:
    wen=input("请输入要保存的内容（输入'quit'退出）：")
    if wen == 'quit':
        break
    file.write(wen + "\n")
    print("内容已保存")
file.close()
print("文件已关闭")
