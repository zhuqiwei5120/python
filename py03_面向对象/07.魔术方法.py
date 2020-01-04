#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'


# 定义一个类
class Person(object):

    def __init__(self, name, age):
        print('__init__')
        self.name = name
        self.age = age

    # 将对象转换为字符串时调用，类似于java中的toString()
    def __str__(self):
        return 'Person [name=%s, age=%d]' % (self.name, self.age)

    # 在对象使用len()函数时调用
    def __len__(self):
        return len(self.name)

    # 在对象使用repr()函数时调用
    def __repr__(self):
        return 'hello person'

    # 将对象转换为bool类型时调用
    def __bool__(self):
        return self.age > 18

    # 在对象进行大于比较时调用
    def __gt__(self, other):  # self表示当前对象，other表示要比较的对象
        return self.age > other.age


p1 = Person('唐伯虎', 20)
p2 = Person('秋香', 18)

print(p1)

print(len(p1))

print(repr(p1))

print(bool(p1))

if p1:
    print(p1.name, '已成年')
else:
    print(p1.name, '未成年')

print(p1 > p2)
