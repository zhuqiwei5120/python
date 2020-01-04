#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'

# 将字符串转换数值
a = '25'
b = int(a)
print(type(a), type(b))
c = '12.5'
d = float(c)
print(type(c), type(d))
# 将数值转换为字符串
print('hello ' + str(25))  # 数值类型不能直接和字符中进行拼接，需要进行类型转换

# 字符串常用方法
string = '  hello world '
print(string.islower())
print(string.isupper())
print(string.capitalize())
print(string.index('llo'))
print(string)
print(string.strip())  # 类似于java中的trim
print(len(string))  # 调用len()函数获取长度

# 切片：用来获取指定索引范围的内容
name = 'tom cruise'
print(name[0])
print(name[4], name[len(name) - 1], name[-1])
print(name[1:5])  # 获取索引为[1,5)的字符
print(name[:5])  # 表示从头获取
print(name[2:])  # 表示获取到末尾
print(name[1:8:2])  # 索引为[1,8)的字符，每两个取一个
print(name[::2])  # 所有字符，每两个取一个

# 格式化字符串，在字符串中指定占位符
# 方式1：使用%运算符，%s表示任意字符，%d表示整数，%f表示浮点数
name = 'tomaaaa'
age = 20
height = 180.5
print('大家好，我叫' + name + '，年龄：' + str(age) + '，身高：' + str(height))
print('大家好，我叫%2.4s，年龄：%d，身高：%.2f' % (name, age, height))  # 2.4s表示字符串长度为2-4位，.2f表示保留两位小数
print('当前时间：%d年-%02d月-%d日' % (2018, 5, 14))  # 指定月份为两位，不足两位则补0

# 方式2：使用format()方法，使用{}表示占位符
print('大家好，我叫{0}，年龄：{1}，身高：{2:.2f}'.format(name, age, height))
print('大家好，我叫{name}，年龄：{age}，身高：{height}'.format(age=age, name=name, height=height))

# 方式3：在字符串前面添加一个f，使用{变量名}来嵌入变量
print(f'大家好，我叫{name}，年龄：{age}，身高：{height}')