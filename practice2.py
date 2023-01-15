# def printInfo(name, height, weight, habbit, pro):#函数定义
#     print('%s的身高是%f' %(name, height))
#     print('%s的体重是%f' %(name, weight))
#     print('%s的爱好是%s' %(name, habbit))
#     print('%s的专业是%s' %(name, pro))
# printInfo('peter', 170, 120, 'football', 'math')
# printInfo('Li Hua', 175, 130, 'basketball', 'computer science')#函数调用

# def Sum(a,b):
#     sum = a+b
#     print(sum)
# Sum(2,3)

# def Sum1(a = 20, b = 30):
#     print("默认参数使用=%d"%(a + b))
# Sum1(40)

# def getComputer(*args):
#     print(args)
#
# getComputer(1,2,3,4,5,6,78,9)

# def keyFunc(**kwargs):
#     print(kwargs)
# keyFunc(**{'number':'12', 'name':'peter'})
# keyFunc(name='joey', age='20')

# def Sum(a,b):
#     sum = a + b
#     return sum
#     pass
# print(Sum(10,30))

# def sum(*args):
#     sum = 0
#     for item in args:
#         sum += item
#     return sum
# print(sum(1,2,3,4,5))

# def find(a):
#     b = []
#     i = 0
#     for item in a:
#         if i % 2 == 0:
#             b.append(item)
#         else:
#             pass
#         i += 1
#     return b
# a = [1,2,3,4,5,6,7,8,9]
# print(find(a))