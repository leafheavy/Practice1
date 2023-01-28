# class Person(object):
#      def __init__(self):
#        self.__age = "30岁"
#         pass
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self, parms):
#         self.__age = parms
#         pass
#     def get_age(self):
#         return self.__age
#     def set_age(self, age):
#         if age < 0:
#             print("输入错误")
#         else:
#             self.__age = age
#
#     age = property(get_age, set_age)
#     def __str__(self):
#         return "{}的年龄是{}".format(self.__name, self.age)

# p1 = Person()
# print(p1.age)
# p1.age = "60岁"
# print(p1.age)
# p1.get_age()
# p1.set_age()
# class Stu(Person):
#     def printInfo(self):
#         print(self.__name)
#     pass

# xiaoli = Person()
# # print(xiaoli.__name)
# print(xiaoli)

# stu = Stu()
# # print(stu.__name)
# stu.printInfo()

# class Animal:
#     def __eat(self):
#         print("吃东西")
#         pass
#     def run(self):
#         self.__eat()
#         print("跑起来")
#         pass
#
# class Bird(Animal):
#     pass
#
# b1 = Bird()
# b1.run()

# class Animal:
#     def __init__(self):
#         self.color = "RED"
#         pass
#     def __new__(cls, *args, **kwargs):
#         return super().__new__(cls, *args, **kwargs)
#     pass
#
# tiger  = Animal()


# class DataBaseClass(object):
#     __instance = None
#     def __new__(cls, *args, **kwargs):
#         if not cls.__instance:
#             cls.__instance = object.__new__(cls, *args, **kwargs)
#             return cls.__instance
#         else:
#             return cls.__instance
#     pass
#
# class DBoptSingle(DataBaseClass):
#     pass
#
# db1 =DataBaseClass()
# print(id(db1))
# db2 =DataBaseClass()
# print(id(db2))
# db3 =DataBaseClass()
# print(id(db3))
# print("程序运行中......")
# print("--------------------------")
# try:
#     li = [1, 2, 3]
#     print(li[10])
#     pass
# except:
#     print("跳过错误代码，程序继续运行........")
#     pass
# print("--------------------------")
# print("hhhhh")

class Stu(object):
    __slots__ = ("name", "age", "grade")
    def __str__(self):
        return "{}的年龄是{}".format(self.name, self.age)
    pass
class SubStu(Stu):
    __slots__ = ()
    pass

ln = SubStu()
# ln.gender = "woman"
ln.age = 3
print(ln.age)
# xw = Stu()
# xw.name = "小王"
# xw.age = 20
# xw.grade = 96
# print(xw)