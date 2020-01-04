#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'


# 定义一个类，使用class关键字
class Student:
    # pass

    # 类属性：直接在类中定义的属性，可以通过类或实例对象来访问
    hobby = '吃饭'

    # 实例方法：将self作为第一个参数的方法
    def say_hi(self):  # self表示当前类的实例，类似于java中的this
        print('Hi:' + self.name)

    def say_hello(self, username='无名氏'):
        print('Hello:' + username)

    # 类方法：使用@classmethod修饰的方法，将cls作为第一个参数
    @classmethod
    def show(cls, msg):  # cls表示当前类
        print(msg, cls.hobby)

    # 静态方法：使用@staticmethod修饰的方法，没有任何必选参数，不需要将cls作为第一个参数
    @staticmethod
    def show2(msg):
        print(msg, Student.hobby)


# 创建类的对象
stu1 = Student()  # 创建Student类的一个实例
stu2 = Student()
print(stu1, type(stu1))
print(stu2, type(stu2))

a = 3
print(a, type(a))
b = int(5)  # 创建int类的一个实例
c = str('hello')  # 创建str类的一个实例
print(b, type(b))

# 为对象绑定属性
stu1.name = 'tom'  # 实例属性，通过实例对象添加的属性
stu1.age = 20
stu2.name = 'alice'
stu2.sex = 'female'
stu2.height = 180.5
print(stu1.name, stu1.age)
print(stu2.name, stu2.sex, stu2.height)

# 访问实例方法
stu1.say_hi()  # 调用方法时无需传递self，由解析器调用时将对象作为self自动传入
stu2.say_hi()
stu1.say_hello('张三')
stu2.say_hello()

# 访问类属性
print(Student.hobby)
stu1.hobby = '睡觉'  # 为stu1添加了一个实例属性，并不会改变类属性hobby的值
print(stu1.hobby)
print(stu2.hobby)  # 如果当前实例没有hobby属性，则会向上查找类属性hobby

# 访问类方法
Student.show('hello')  # 调用方法时无需传递cls
stu1.show('Hello')
Student.show2('您好')
stu2.show2('你好')
