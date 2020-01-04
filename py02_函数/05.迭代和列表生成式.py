#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'

# 导入模块
import collections

'''
迭代：也称为遍历，循环获取每一个元素
'''

for i in ['tom', 'jack', 'alice']:
    print(i, end=' ')
print()

for i in ('tom', 'jack', 'alice'):
    print(i, end=' ')
print()

for i in {'name': 'tom', 'age': 18, 'sex': 'male'}.keys():
    print(i, end=' ')
print()

for k, v in {'name': 'tom', 'age': 18, 'sex': 'male'}.items():
    print(k, v)

for i in 'hello':
    print(i)

# 判断对象是否是可迭代的
print(isinstance('hello', collections.Iterable))

# 获取索引和值
# 方式1：自己获取索引
names = ['tom', 'jack', 'alice']
for i in range(len(names)):
    print(i, names[i])

# 方式2：使用enumerate()函数，转换为索引-元素对
print(enumerate(names))
print(isinstance(enumerate(names), collections.Iterable))
for k, v in enumerate(names):
    print(k, v)

print('-' * 80)

'''
列表生成式：用来创建list的生成式
'''
# 生成[0,99]的list
# nums = range(0, 100)
nums = list(range(0, 100))  # 转换为list
# print(nums, type(nums))

# print(isinstance(range(0, 100), collections.Iterable))

# for i in range(0, 100):
#     print(i)

# 生成一个包含[1,100]之间所有3的倍数的list
# 方式1
# lst = []
# for i in range(1, 101):
#     if i % 3 == 0:
#         lst.append(i)

# 方式2
lst = [i for i in range(1, 101) if i % 3 == 0]  # 等价于a = list(range(1, 101))
print(lst)


