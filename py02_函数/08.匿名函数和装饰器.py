#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'

'''
匿名函数：没有名字的函数，使用lambda关键字
'''

nums = [12, 4, 32, 5, 23, 7]

# def fn(x):
#     return x * 2 + 1


nums_new = list(map(lambda x: x * 2 + 1, nums))
print(nums_new)

# 将匿名函数赋给变量（不建议）
a = lambda x: x + 1
print(a(2))

print('-' * 80)

'''
装饰器：在代码运行期间动态增加功能，称为装饰器Decoration，类似于AOP
'''


# 定义一个装饰器，为函数添加打印日志的功能
def log(fn):
    def wrapper(*args, **kwargs):
        print('开始执行%s()函数。。。' % fn.__name__)
        res = fn(*args, **kwargs)
        print('执行%s()函数结束。。。' % fn.__name__)
        return res

    return wrapper  # 返回装饰函数


@log
def even(lst):
    for i in lst:
        if i % 2 == 0:
            print(i)


@log
def calc(num1, num2):
    res = num1 + num2
    return res


even([12, 34, 2, 5, 34, 21])

print(calc(3, 5))
