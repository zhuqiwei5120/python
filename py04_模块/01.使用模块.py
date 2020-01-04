#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'

# 方式1
# import py04_模块.mymodule
# print(py04_模块.mymodule.a)  # 调用模块中的变量
# print(py04_模块.mymodule.plus(3, 5))

# import py04_模块.mymodule as m
# print(m.plus(3, 5))

# 方式2
# from py04_模块 import mymodule
# print(mymodule.b)
# print(mymodule.minus(8, 2))

from py04_模块.mymodule import b, plus, Calculator

# from py04_模块.mymodule import *  # 不建议

# print(b)
# print(plus(2, 5))
# print(Calculator.sum(3, 12, 5))
