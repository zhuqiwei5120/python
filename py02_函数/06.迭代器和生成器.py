#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'

'''
迭代器iterator：用来访问集合元素的一种方式，可以记住迭代的位置
'''

nums = [3, 8, 12, 54, 2, 7]
it = iter(nums)  # 调用iter()函数创建迭代器
print(type(it))

print(next(it))  # 调用next()函数获取迭代器的下一个元素
print(next(it))  # 只能往前不能后退

# 使用for...in循环遍历迭代器
for i in it:
    print(i)

'''
生成器generator：在循环过程中依次计算获取值的对象（节省空间、效率高）
创建生成器的方式：
    方式1：把一个列表生成式的[]改成()
    方式2：在函数中使用yield关键字，此时该函数就变成一个生成器函数
'''
# 方式1：把一个列表生成式的[]改成()
generator = (i for i in range(1, 100))
print(type(generator))  # generator类型

# 获取生成器的下一个值
print(next(generator))  # 获取时才生成值，类似于Oracle中sequence
print(next(generator))
print(next(generator))

# 使用for...in循环遍历生成器
for i in generator:
    print(i)

print('-' * 80)


# 方式2：在函数中使用yield关键字，此时该函数就变成一个生成器函数
def gen():
    print('one')
    yield 13
    print('two')
    yield 8
    print('three')
    yield 25
    print('four')
    yield 38


# 生成器函数与普通函数的执行流程不一样：
# 普通函数是顺序执行，执行到最后一行或遇到return时结束
# 生成器函数是在每次调用next()时执行，遇到yield语句就返回，下一次调用next()时会从上次返回的yield语句处继续执行
g = gen()  # generator类型
print(type(g))
print(next(g))
print(next(g))

# 使用for...in循环遍历生成器
for i in g:
    print(i)
