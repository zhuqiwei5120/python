#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'

'''
读写模式：
    r  读模式
    w  写模式（覆盖）
    a  追加模式
    r+ 读写模式
    b  二进制模式
'''

# ----读取文件
try:
    f = open('itany.txt', mode='r', encoding='utf-8')  # 打开一个文件，返回一个对象，这个对象就代表着当前打开的文件
    print(f.read())  # 一次性读取所有内容
except FileNotFoundError as e:
    print('文件找不到：', e)
finally:
    if f:
        f.close()  # 文件操作后一定要关闭

print('-' * 80)

# 简写，使用with...as语句，会自动调用close()
with open('itany.txt', mode='r', encoding='utf-8') as f:
    # print(f.read())
    # print(f.read(3))  # 每次读取3个字符
    # print(f.read(3))
    # print(f.readline().strip())  # 每次读取一行
    # print(f.readline())
    lines = f.readlines()  # 一次性读取所有行，返回list
    # print(lines)
    for line in lines:
        print(line.strip())

print('-' * 80)

# ----写文件
with open('itany.txt', mode='a', encoding='utf-8') as f:
    f.write('xxx\n')
    f.write('yyy')

print('-' * 80)

# ----读写二进制文件
with open('baidu.png', mode='rb') as f:
    with open('itany.png', mode='wb') as out:
        out.write(f.read())
        print('拷贝成功')
