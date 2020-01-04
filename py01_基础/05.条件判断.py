#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'

age = 10
if age > 18:  # 冒号不能省略
    print('成年')
else:
    print('未成年')
print(111)

score = 85
if score >= 90:
    print('优秀')
elif score >= 70:
    print('良好')
elif score >= 60:
    print('及格')
else:
    print('什么玩意')

# 简写的条件，当判断条件为：零、空字符串、None、空list等，表示为False，否则为True
nums = []
if 'aa':
    print('嘿嘿')
