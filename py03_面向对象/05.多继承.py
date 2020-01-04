#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'


class A:
    def a(self):
        print('a')


class B:
    def b(self):
        print('b')


class C(A, B):  # 继承多个父类，以逗号隔开
    def c(self):
        print('c')


c = C()
c.a()
c.b()
c.c()

# 类的特殊属性 __bases__ 可以用来获取当前类的所有父类
print(C.__bases__)
