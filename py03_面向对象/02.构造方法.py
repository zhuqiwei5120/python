#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'


class Student:

    # 构造方法（函数），不支持重载
    def __init__(self, name, age):
        print('创建对象，执行构造方法。。。')
        self.name = name
        self.age = age

    # 实例方法
    def show(self):
        print('姓名：%s，年龄：%d' % (self.name, self.age))


stu1 = Student('tom', 18)
print(stu1.name, stu1.age)
stu1.show()
