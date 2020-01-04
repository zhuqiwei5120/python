#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'


class Student:
    # 定义私有属性
    __age = 18  # 以两个下划线开头，表示对象的隐藏属性，只能在类内部访问

    # 提供getter/setter方法
    def get_age(self):
        return self.__age

    def set_age(self, age):
        # 判断数据是否有效
        if 0 < age < 100:
            self.__age = age
        else:
            self.__age = 18


stu1 = Student()
# print(stu1.__age)  # 在类外部无法访问私有属性
stu1.set_age(28)
print(stu1.get_age())

# 其实Python会把私有属性转为 _类名__属性名（强烈不建议）
print(stu1._Student__age)
