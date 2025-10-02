#
# total = 99
# for i in range(1,100):
#     if i%7 == 0:
#         continue
#     else:
#         string = str(i)
#         if string.endswith("7"):
#             continue
#     total-=1
# print("total:",total)

for i in range(1,100):
    if i%7 == 0 or i%10 == 7:
        continue
    print("逢七拍桌子",i)
