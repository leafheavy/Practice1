# a = 1
# def func(x):
#     print("x的地址:{}".format(id(x)))
#     x = 2
#     print("x修改后的地址:{}".format(id(x)))
#     pass
#
# print("a的地址:{}".format(id(a)))
# func(a)

# li = []
# def testRenc(parms):
#     print("列表的地址为:{}".format(id(parms)))
#     parms.append(2)
#     print("列表修改之后的地址为:{}".format(id(parms)))
#     pass
#
# print("li的地址为:{}".format(id(li)))
# testRenc(li)

# def computer(x, y):
#     return x + y
#     pass
#
# Sum = lambda x, y:x + y
# print(Sum(10,20))
# print(computer(10, 20))

# def jiecheng(n):
#     result = 1
#     for item in range(1,n+1):
#         result *= item
#         pass
#     return result
#
# print(jiecheng(5))
#
# def digui(n):
#     result = 1
#     if n == 1:
#         result = n
#     else:
#         result = n * digui(n-1)
#         pass
#     return result
#
# print(digui(5))