#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'

'''
   数据类型：整型、浮点型、字符串、布尔、空值等
'''
# 整型int
a = 3454566666666666666
print(a)
print(type(a))

# 浮点型float
b = 12.5
print(b, type(b))

# 字符串str，定义字符串可以使用单引号或双引号（推荐用单引号）
c = 'ccc'
d = "ddd"
print(c, type(c))

print('张三说："今晚吃鸡吗？"')

# 字符串有多行时可以使用三对单引号，表示多行内容
e = '''
welcome 
    to
        itany    
'''
print(e)
print(type(e))

# 布尔bool，取值：True、False
f = True
print(f, type(f))

g = 5 < 3
print(g)

print(5 + False)  # True表示1，False表示0

# 空值 NoneType
h = None
print(h, type(h))
