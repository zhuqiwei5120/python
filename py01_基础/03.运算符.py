#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'

'''
Python中支持的运算符：
1.算术运算符
    + - * / % // **
    不支持自增++和自减--
2.比较运算符
    > < >= <= == !=或<> 
3.赋值运算符
    = += -= *= /+ %= **=
4.逻辑运算符
    and  or  not
5.条件运算符，也称三目运算符
    语法：条件为真时的结果 if 条件 else 条件为假时的结果  
6.位运算符
    与& 或| 非~  异或^ 左移<<  右移>>
7.成员运算符
    in 
    not in
8.身份运算符
    is 
    is not
    
'''

# 1.算术运算符
print(3 + 5)
print(3 * 5)
print(30 * '-')  # 乘法可以用于字符串
print(5 % 3)
print(5 / 3)  # 除法，有小数
print(5 // 3)  # 除法，取整
print(2 ** 3)  # 幂
print(pow(2, 3))
i = 5
i = i + 1
print(i)
print('*' * 80)

# 2.比较运算符
j = 5
print(j > 2)
print(10 > j > 1)  # 支持此写法
print('abc' > 'acd')  # 可以用于字符串的比较，比较的是字符串的Unicode编码

# 3.赋值运算符
a = 10
a += 5  # 等价于a= a+5
print(a)

# 4.逻辑运算符
print(True and False)
print(5 > 2 or 4 < 1)
print(not 5 > 2)

x = 0  # 0 表示False，非0表示True
y = 8
print(x and y)  # 如果ｘ为True，则返回y；否则返回x
print(x or y)  # 如果x为True，则返回x；否则返回y
print(not x)  # 如果x为True，则返回False，否则返回True

# 5.条件运算符，也称三目运算符
print('aaa' if 5 < 2 else 'bbb')

# 6.位运算符
a = 5  # 00000101
b = 8  # 00001000
print(a & b)  # 两位都是1才为1，否则为0
print(a | b)  # 只要有一位为1，则为1，否则为0
print(~a)  # 如果为1，则为0，如果为0，则为1
print(a ^ b)  # 如果两位相同，则为0，不同为1
print(b >> 2)  # 二进制的所有位都向右移2位

# 7.成员运算符
c = [3, 5, 12, 15, 7, 2]
d = 5
print(d not in c)

# 8.身份运算符
m = [1, 3, 5, 7]
n = [1, 3, 5, 7]
x = n
print(m is n)
print(x is n)

'''
    is 和 == 的区别
    is 判断两个变量是否引用同一个对象
    == 判断两个变量的值是否相等
'''
print(m == n)
