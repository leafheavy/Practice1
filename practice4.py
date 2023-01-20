# class Person:
#     name = "peter"
#     age = 20
#     def eat(self):
#         print("大口大口吃饭")
#         pass
#     def run(self):
#         print("慢跑")
#         pass
#
# peter = Person()
# peter.run()

# class People:
#     def __init__(self, name, age, sex, food):
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.food = food
#         print("--------init函数执行---------")
#         pass
#     def __str__(self):
#         return "{}的{}{}喜欢吃{}".format(self.age, self.sex, self.name, self.food)
#         pass
#     def __new__(cls, *args, **kwargs):
#         print("-------new函数的执行--------")
#         return object.__new__(cls)
#         pass
#
# # xq = People()
# # xq.name = "小倩"
# # xq.sex = "女生"
# # xq.age = "20岁"
# # xq.eat()
# # print(xq.age, xq.name, xq.sex)
# # xl = People()
# # xl.name = "小李"
# # xl.age = "18岁"
# # print(xl.age, xl.name, xl.sex)
#
# zp = People("张鹏", "20岁", "男性", "香蕉")
# print(zp)