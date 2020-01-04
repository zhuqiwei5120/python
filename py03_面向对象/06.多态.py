#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'


class Animal:
    def __init__(self, name):
        self.name = name

    def cry(self):
        print('动物在叫。。。。')


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def cry(self):
        print('狗在叫。。。。汪汪汪')


class Cat(Animal):
    def __init__(self, name, sex):
        super().__init__(name)
        self.sex = sex

    def cry(self):
        print('猫在叫。。。喵喵喵')


# 一个对象可以以不同的形式去呈现，就是多态
def play(animal):
    print(animal.name)
    animal.cry()


dog = Dog('旺财', 2)
cat = Cat('猫咪', '公')
play(dog)
play(cat)
