# -*- coding:utf-8 -*-

__all__ = ["add", "diff"]

def add(x,y):
    return x+y

def diff(x,y):
    return x-y

def printInfo():
    return '这是我的自定义模块'

if __name__ == '__main__':
    add(3,4)
    diff(3,4)
    printInfo()
    print("模块__name__变量=%s"%__name__)
