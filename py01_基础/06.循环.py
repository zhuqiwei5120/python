#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'

# ----while循环
# 计算1到100的和
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)

# ----for...in循环
names = ['tom', 'jack', 'alice', 'mike']
for name in names:
    print(name, end=',')
print()

# 使用range()函数生成一个序列
for i in range(1, 100, 2):  # 生成一个[1,100)的整数序列，步长为2
    print(i, end=',')
print()

# 计算1到100的和
sum = 0
for i in range(1, 101):
    if sum > 50:
        break
    sum += i
print(sum)

'''
练习：
1.使用循环输出list中的每个元素的索引和元素
2.输出list中除第一个元素以外的其他元素
'''
nums = [11, 4, 3, 23, 64, 2, 236, 8]
for i in range(len(nums)):
    print(i, nums[i])

for n in nums[1:]:
    if n % 2 == 1:
        continue
    print(n, end=',')
