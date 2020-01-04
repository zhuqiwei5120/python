#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'

# 查看函数的帮助信息
help(print)
help(abs)

# 数学运算
print(abs(-5))
print(max(12, 6, -5, 120, 74))
print(pow(2, 4))
# print(abs('hello'))  # 如果参数不对，会报TypeError错误
print('-' * 80)

# 类型转换
print(int('123'))
print(float('12.5'))
print(str(123))
print(bool(5))
print('-' * 80)

# 判断数据类型
a = 12.5
print(isinstance(a, str))
# print(isinstance(a, int) or isinstance(a, float))
print(isinstance(a, (int, float)))
