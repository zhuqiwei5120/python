#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'


# 定义一个Person类，父类（超类、基类）
class Person(object):  # 如果省略了父类，则默认父类为object
    def __init__(self, name):
        self.name = name

    def run(self):
        print('person:' + self.name + '正在奔跑。。。')


# 定义一个Student类，子类
class Student(Person):  # 继承自Person
    def __init__(self, name, email):
        # 调用父类的构造方法
        # Person.__init__(name)  # 方式1：直接指定父类的构造方法
        super().__init__(name)  # 方式2：使用super，推荐
        self.email = email

    # 定义子类特有的方法
    def study(self):
        print('student:' + self.name + '正在学习。。。')

    def show(self):
        print('姓名：%s，邮箱：%s' % (self.name, self.email))

    # 重写父类的方法
    def run(self):
        # super().run()  # 调用父类的方法
        print('student:' + self.name + '正在奔跑。。。。')


stu = Student('tom', 'tom@sina.com')
stu.run()  # 调用子类重写后的方法
stu.study()
stu.show()

# 判断一个对象是否是指定类的实例，即判断对象的类型
print(isinstance(stu, Student))
print(isinstance(stu, Person))

# 判断一个类是否是指定类的子类
print(issubclass(Student, Person))
print(issubclass(Student, object))


# object类是所有类的根类，默认所有类都继承自object
print(stu.__doc__)
print(stu.__dict__)
