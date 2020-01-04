#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'


# 定义函数，使用def
def calc(num1, num2):  # 必选参数，也称为位置参数，不能省略
    res = num1 + num2
    return res


# print(calc(3, 5))  # 调用函数


# 参数类型检查
def my_abs(x):
    # 可以为函数添加文档注释，也称为文档字符串doc string
    """
    计算绝对值
    :param x: 参数
    :return: 返回x的绝对值
    """
    # 对参数类型进行检查
    if not isinstance(x, (int, float)):
        raise TypeError('参数类型不正确，只能为数值类型')  # 抛出异常

    if x >= 0:
        return x
    else:
        return -x


# print(my_abs('aaa'))

# print(help(my_abs))


# 默认参数，即有默认值的参数
def my_pow(x, y=2):
    if y == 0:
        return 1
    res = x
    for i in range(y - 1):
        res *= x
    return res


# print(my_pow(5))


# 可变参数，使用*号，表示参数个数是可变的
def my_sum(x, *y):
    print(x)
    print(y)  # 接收到的实际上是一个tuple


# my_sum(3, 5, 8, 12, 4)

# 不建议下面的这种写法，建议将必选参数放在最前面
def my_sum2(*y, x):
    print(y)
    print(x)


# my_sum2(12, 4, 2, 7, x=9)  # 必选参数在后面时需要指定参数名

# 对于可变参数，可以直接传入list或tuple，只需要在参数前添加一个*
nums = [12, 4, 2, 64, 23, 9]


# my_sum(4, nums[0], nums[1], nums[2], nums[3], nums[4], nums[5])
# my_sum(4, *nums)


# 关键字参数，使用**，也表示参数个数是可变的，但传递的是带名称的参数
def f1(x, **y):
    print(x)
    print(y)  # 接收到的实际上一个dict


# f1(3, a=5, b=9, c=18)

# 对于关键字参数，可以直接传入一个dict，只需要在参数前添加**
user = {'id': 1001, 'name': 'tom', 'age': 18}


# f1(4, id=user['id'], name=user['name'], age=user['age'])
# f1(4, **user)


# 命名关键字参数，限制关键字参数的名字，使用*分隔，*号后面的参数表示命名关键字参数
def f2(x, *, name, age):
    print(x)
    print(name)
    print(age)


# f2(4, name='alice', age=20)


# 接收任意参数
def f3(*args, **kwargs):
    print(args)
    print(kwargs)


f3(1, 43, 'aaa', name='alice', age=20)
