#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'

# 在模块中定义变量
a = 10
b = 20


# 在模块中定义函数
def plus(x, y):
    """
    加法
    :param x: 
    :param y: 
    :return: 
    """
    return x + y


def minus(x, y):
    """
    减法
    :param x:
    :param y:
    :return:
    """
    return x - y


# 在模块中定义类
class Calculator:

    @classmethod
    def sum(cls, *nums):
        res = 0
        for n in nums:
            res += n
        return res


'''
__name__属性是模块的内置属性，每个模块中都有该属性
当该.py文件是主执行文件，直接被执行时，其值为__main__
当该.py文件是被调用，导入执行时，其值为模块名
'''
# print(__name__)

# 程序入门，类似于Java中的main()方法，只在当直接调用该文件时才会执行，用来执行测试
if __name__ == '__main__':
    print(Calculator.sum(1, 2, 3))
