#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'


# 空函数，表示以后再实现
def empty():
    pass  # 使用pass


# 函数的返回值，返回多个值
def f1():
    name = 'tom'
    age = 20
    sex = 'male'
    return name, age, sex


# print(f1())  # 返回值实际上是一个tuple
a, b, c = f1()


# print(a, b, c)


# 函数的返回值，返回一个函数，即将函数作为返回值
def f2(x):
    print(111)
    z = 6

    def f3(y):
        print(x * y + z)  # 内部函数使用了外部函数的参数或局部变量，称为闭包

    return f3


# fn = f2(3)
# fn(5)


# 递归函数：一个函数在内部调用自身，这个函数就是递归函数
# 计算x的y次方，如计算2的5次方
def calc(x, y):
    # 常规方式
    # if y == 0:
    #     return 1
    # i = 1
    # res = x
    # while i < y:
    #     res *= x
    #     i += 1
    # return res

    # 递归方式
    # 2*2*2*2*2=2*(2*2*2*2)=2*(2*(2*2*2))=
    if y == 0:
        return 1
    else:
        return x * calc(x, y - 1)  # 不停的调用自己，递归太深可能会抛出栈溢出异常


print(calc(2, 99999999999999))
