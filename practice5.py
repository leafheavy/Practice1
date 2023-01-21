# class Animal:
#     def __init__(self, name):
#         self.name = name
#         print("这是构造初始化方法")
#         pass
#     def __del__(self):
#         print("释放资源,这是析构方法")
#     pass
#
# cat = Animal("小猫")
# del cat
# print(cat.name)
# # input("程序等待中......")
# # print("-"*40)
# # dog = Animal("柯基")

# class Animal:
#     def eat(self):
#         print("大口大口吃饭")
#         pass
#     def drink(self):
#         print("痛快地喝水")
#         pass
#
# class Cat(Animal):
#     def sleep(self):
#         print("安安静静的睡觉")
#         pass
#
# class Dog(Animal):
#     def run(self):
#         print("迅速地奔跑")
#         pass
#
# dahuang = Dog()
# dahuang.sleep()


# class shenxian:
#     def fly(self):
#         print("飞")
#         pass
# class Monkey:
#     def chitao(self):
#         print("吃桃")
#         pass
# class Monkey_King(shenxian, Monkey):
#     def kungfu(self):
#         print("武艺高强")
#         pass
#
# sw = Monkey_King()
# sw.fly()
# sw.kungfu()
# sw.chitao()

# class Stu:
#     name = "黎明"
#     def __init__(self,age):
#         self.age = age
#         pass
#     pass
# lm = Stu(20)
# print("{}的岁数是{}".format(lm.name, lm.age))
# print('-'*50)
# print("{}的岁数是{}".format(Stu.name, lm.age))
# xm = Stu(18)
# print("小明的岁数是{}".format(xm.age))

# class People:
#     country = 'China'
#     @classmethod
#     def get_country(cls):
#         return cls.country
#         pass
#     pass
#     @classmethod
#     def change_country(cls, country):
#         cls.country = country
#         return cls.country
#
#
# print(People.get_country())
# xm = People()
# print("xm的国籍是{}".format(xm.get_country()))
# peter = People.change_country("UK")
# print("peter的国籍是{}".format(xm.get_country()))
# print("xm的国籍是{}".format(xm.get_country()))

# import time
# class TimeSet:
#     # def __init__(self,hour, min, second):
#     #     self.hour = hour
#     #     self.min = min
#     #     self.second = second
#     @staticmethod
#     def showTime():
#         return time.strftime("%H:%M:%S", time.localtime())
#         pass
#     @staticmethod
#     def add(x,y):
#         return x*y
#
#
# # print(TimeSet.showTime())
# # t = TimeSet(2, 10, 15)
# # print(t.showTime())
#
# sum = TimeSet()
# print(sum.add(5,7))

class Animal:
    def say_who(self):
        print("我是动物")
        pass

class Cat(Animal):
    def say_who(self):
        print("我是猫科动物")
    pass

class Dog(Animal):
    def say_who(self):
        print("我是犬科动物")
    pass

def commonInvoke(obj):
    obj.say_who()

# juanjuan = Cat()
# juanjuan.say_who()
# dahuang = Dog()
# dahuang.say_who()

listObj = [Dog(),Cat()]
for item in listObj:
    commonInvoke(item)