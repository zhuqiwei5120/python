#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'

'''
高阶函数：一个函数接收另一个函数作为参数，这种函数称为高阶函数
'''

nums = [12, -4, 3, -23, 65, 1, -234, 22]


# 定义一个函数，用来检查数字是否大于5
def f1(x):
    if x > 5:
        return True
    return False


# 自定义高阶函数，用来过滤列表中的元素
def fn(fun, lst):
    """
    将列表中所有符合条件的元素筛选出来，返回一个新列表
    :param fun: 条件函数
    :param lst: 要进行筛选的列表
    :return: 返回新列表
    """
    new_list = []
    for i in lst:
        if fun(i):
            new_list.append(i)
    return new_list


nums1 = fn(f1, nums)
print(nums1)


def f2(x):
    return x % 2 == 0


print(fn(f2, nums))

# 内置高阶函数 filter()，用于过滤序列
nums2 = filter(f1, nums)
print(list(nums2))


# 内置高阶函数 map()，用于处理序列
def f3(x):
    return x * x


nums3 = map(f3, nums)
print(list(nums3))


# 内置高阶函数 sorted()，用于排序
print(sorted(nums))
print(sorted(nums,key=abs))
