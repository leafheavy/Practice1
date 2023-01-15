# row = 1
# while row <= 7:
#     n = 1
#     while n <= 2 * row - 1:
#         print("*", end=" ")
#         if n == 2 * row - 1:
#             print()
#             pass
#         n += 1
#     row += 1

# xuefen=int(input("请输入您的学分："))
# if xuefen>10:
#     grade=int(input("请输入您的成绩："))
#     if grade>=80:
#         print('您可以升班了 恭喜你')
#         pass
#     else:
#         print('很遗憾，您的成绩不达标')
#         pass
#     pass
# else:
#     print("不会吧 不会吧，还有人不及格吗？(●'◡'●)")

# import random
# win = 0
# x = 0
# while True:
#     if win == 3:
#         print("你已经胜利3次,一共玩了%d次"%x)
#         break
#     else:
#         y = float (input("请出拳【石头为0,剪刀为1,布为2】:"))
#         z = random.randint(0,2)
#         print("电脑出拳%d"%z)
#         if y > 2:
#             print("输入错误,请重新输入")
#         elif (y == 1.5):
#             print("牛逼啊,你赢了!!!")
#             win += 1
#             x+=1
#             pass
#         elif (y==0 and z==1) or (y==1 and z==2) or (y==2 and z==0):
#             print("你赢了!")
#             win+=1
#             x+=1
#             pass
#         elif y == z:
#             print("平局!")
#             x+=1
#             pass
#         else:
#             print("你输了")
#             x+=1
#             pass

# strMsg='hello world'
# #slice [start:end:step] 左闭右开start<=value<end 范围# print(strMsg) #输出完整的数据# print(strMsg[o])
# print(strMsg[2: 5])#2-5下标之间的数据print(strMsg[2:])_#第三个字符到最后
# print(strMsg[: 3])#1-3 strMsg[0:3]=strMsg[:3]print(strMsg[::-1])_#倒叙输出负号表示方向 从右边

# li = [1,2,3,'s']
# print(len(li))

# dictA = {'name': '小明', 'age': '20', 'height': '1.8m', 'wight': '65kg'}
# dictA.pop('age')
# print(dictA)
# print(sorted(dictA.items(), key = lambda d:d[0]))
# print(sorted(dictA.items(), key = lambda d:d[1]))


